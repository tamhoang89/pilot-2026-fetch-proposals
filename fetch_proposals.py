#!/usr/bin/env python3
"""
Catalyst Proposal Fetcher
==========================
Crawl proposals của 1 campaign trên Project Catalyst, parse thành markdown
chuẩn. KHÔNG tự commit git - việc đó do GitHub Actions (hoặc bạn) làm sau
khi script chạy xong. Script chỉ có nhiệm vụ: fetch -> ghi file.

Cấu trúc thư mục kỳ vọng (repo root):
    fetch_proposals/
        fetch_proposals.py   <- file này
    pilot_2026_snapshots/
        index.json            <- map proposal_id -> tên file hiện tại
        <ten-du-an>.json       <- snapshot JSON gốc (để so sánh lần sau)
        <ten-du-an>.md         <- bản markdown đã format

Cách dùng:
    pip install requests --break-system-packages
    python3 fetch_proposals/fetch_proposals.py
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import requests

# ============ CẤU HÌNH ============
CAMPAIGN_ID = "6c4b4dd9-0000-5575-a5d3-d2ef6765893d"
BASE_URL = "https://app.projectcatalyst.io/v1"
# Repo root = thư mục cha của thư mục chứa script này (fetch_proposals/../)
REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = REPO_ROOT / "pilot_2026_snapshots"
INDEX_FILE = STATE_DIR / "index.json"
# ===================================


def fetch_proposal_list(campaign_id: str, page_size: int = 50) -> list[dict]:
    """Lấy toàn bộ danh sách proposal trong 1 campaign (tự động phân trang)."""
    proposals = []
    page = 1
    while True:
        resp = requests.get(
            f"{BASE_URL}/campaigns/{campaign_id}/proposals",
            params={"page": page, "pageSize": page_size, "sort": "submitted", "dir": "desc"},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        proposals.extend(data["items"])
        if page * page_size >= data["total"]:
            break
        page += 1
    return proposals


def fetch_proposal_detail(proposal_id: str) -> dict:
    """Lấy chi tiết đầy đủ 1 proposal, bao gồm formData + campaign schema."""
    resp = requests.get(f"{BASE_URL}/proposals/{proposal_id}", timeout=30)
    resp.raise_for_status()
    return resp.json()


def build_field_title_map(campaign: dict) -> dict[str, str]:
    """Map field key (vd 'team') -> câu hỏi gốc (title) từ schema của campaign."""
    props = campaign["submissionForm"]["schema"]["properties"]
    return {key: val.get("title", key) for key, val in props.items()}


def build_field_option_labels(campaign: dict) -> dict[str, dict[str, str]]:
    """Với field kiểu multi-select (vd integrations), map giá trị -> nhãn hiển thị."""
    props = campaign["submissionForm"]["schema"]["properties"]
    result = {}
    for key, val in props.items():
        one_of = val.get("items", {}).get("oneOf")
        if one_of:
            result[key] = {opt["const"]: opt["title"] for opt in one_of}
    return result


def clean_title(title: str) -> str:
    """Bỏ cụm 'Learn more about X [here](url).' thừa trong câu hỏi."""
    title = re.sub(r"\s*Learn more about [^\[]*\[here\]\([^)]*\)\.?", "", title)
    title = re.sub(r"\s*\[here\]\([^)]*\)\.?", "", title)
    return title.strip()


def format_value(value, option_labels: dict[str, str] | None) -> str:
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if isinstance(value, list):
        if option_labels:
            value = [option_labels.get(v, v) for v in value]
        return "\n".join(f"- {v}" for v in value)
    if value is None or value == "":
        return "*(không có dữ liệu)*"
    return str(value)


def slugify(title: str) -> str:
    """Chuyển tên dự án thành tên file an toàn: chữ thường, dấu gạch dưới."""
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)  # bỏ ký tự đặc biệt
    s = re.sub(r"[\s]+", "_", s.strip())
    return s[:80]  # giới hạn độ dài


def render_markdown(detail: dict, title_map: dict, option_labels_map: dict) -> str:
    fd = detail.get("formData", {})
    lines = [
        f"# {detail['title']}",
        "",
        f"> {detail.get('tagline', '')}",
        "",
        "## Proposal Metadata",
        "",
        f"- **Status:** {detail.get('state')}",
        f"- **Revision:** {detail['headRevision']['number']}",
        f"- **Proposer:** `{detail.get('proposer')}`",
        f"- **Funding requested:** ₳{detail.get('requestedAmount', 0):,}",
    ]
    finalization = detail.get("latestFinalization")
    if finalization:
        finalized_at = datetime.fromtimestamp(
            finalization["finalizedAt"] / 1000, tz=timezone.utc
        )
        lines.append(f"- **Last finalized:** {finalized_at.isoformat()}")
    lines.append("")

    skip_fields = {"m1Evidence", "m2Target"}  # nội dung tĩnh, giống nhau mọi proposal

    for key, value in fd.items():
        if key in skip_fields:
            continue
        question = clean_title(title_map.get(key, key))
        lines.append(f"### {question}")
        lines.append("")
        lines.append(format_value(value, option_labels_map.get(key)))
        lines.append("")

    return "\n".join(lines)


def load_index() -> dict:
    if INDEX_FILE.exists():
        return json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    return {}


def save_index(index: dict):
    INDEX_FILE.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


def load_previous_snapshot(json_path: Path) -> dict | None:
    if json_path.exists():
        return json.loads(json_path.read_text(encoding="utf-8"))
    return None


def main():
    STATE_DIR.mkdir(exist_ok=True)
    index = load_index()  # proposal_id -> slug hiện tại

    proposals = fetch_proposal_list(CAMPAIGN_ID)
    print(f"Tìm thấy {len(proposals)} proposal trong campaign.")

    changed_summaries = []

    for p in proposals:
        pid = p["id"]
        title = p["title"]
        new_slug = slugify(title)
        old_slug = index.get(pid)

        # Nếu tên dự án đổi (hiếm), đổi tên file cũ theo tên mới
        if old_slug and old_slug != new_slug:
            old_json = STATE_DIR / f"{old_slug}.json"
            old_md = STATE_DIR / f"{old_slug}.md"
            if old_json.exists():
                old_json.rename(STATE_DIR / f"{new_slug}.json")
            if old_md.exists():
                old_md.rename(STATE_DIR / f"{new_slug}.md")
            print(f"[ĐỔI TÊN] {old_slug} -> {new_slug}")

        json_path = STATE_DIR / f"{new_slug}.json"
        md_path = STATE_DIR / f"{new_slug}.md"

        prev = load_previous_snapshot(json_path)
        prev_rev = prev["headRevision"]["number"] if prev else None

        detail = fetch_proposal_detail(pid)
        new_rev = detail["headRevision"]["number"]

        index[pid] = new_slug

        if prev_rev == new_rev:
            continue  # không có gì thay đổi

        title_map = build_field_title_map(detail["campaign"])
        option_labels_map = build_field_option_labels(detail["campaign"])

        json_path.write_text(
            json.dumps(detail, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        md_path.write_text(
            render_markdown(detail, title_map, option_labels_map), encoding="utf-8"
        )

        status = (
            f"[MỚI] {title} (revision {new_rev})"
            if prev_rev is None
            else f"[CẬP NHẬT] {title}: revision {prev_rev} -> {new_rev}"
        )
        print(status)
        changed_summaries.append(status)

    save_index(index)

    if changed_summaries:
        print(f"\n{len(changed_summaries)} proposal thay đổi. Đã ghi vào {STATE_DIR}")

    else:
        print("Không có proposal nào thay đổi.")


if __name__ == "__main__":
    main()
