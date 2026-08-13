#!/usr/bin/env python3
"""
Catalyst Pilot Proposal Fetcher
==========================
Crawl proposals của 1 campaign trên Project Catalyst, parse thành markdown chuẩn.

Cách dùng:
    pip install requests --break-system-packages
    python3 fetch_proposals.py
"""

import html
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import requests

# ============ CẤU HÌNH ============
CAMPAIGN_ID = "6c4b4dd9-0000-5575-a5d3-d2ef6765893d"
BASE_URL = "https://app.projectcatalyst.io/v1"
# Repo root = thư mục chứa script này (script đặt ngay tại repo root)
REPO_ROOT = Path(__file__).resolve().parent
STATE_DIR = REPO_ROOT / "pilot_2026_snapshots"
INDEX_FILE = STATE_DIR / "index.json"

# Telegram: điền qua biến môi trường (secrets trên GitHub Actions), không hard-code ở đây
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
# GITHUB_REPOSITORY tự có sẵn khi chạy trong GitHub Actions (dạng "user/repo")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY")
TELEGRAM_FIELD_TRUNCATE = 250  # số ký tự tối đa hiển thị mỗi giá trị trước/sau
TELEGRAM_MAX_FIELDS = 8  # số field tối đa liệt kê trong 1 tin nhắn
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


def truncate(text, length: int = TELEGRAM_FIELD_TRUNCATE) -> str:
    text = str(text)
    if len(text) <= length:
        return text
    return text[:length].rstrip() + "…"


def diff_formdata(old_fd: dict, new_fd: dict, title_map: dict) -> list[tuple[str, str, str]]:
    """So sánh formData cũ và mới, trả về list (tên câu hỏi, giá trị cũ, giá trị mới)
    cho từng field có thay đổi."""
    changes = []
    all_keys = sorted(set(old_fd.keys()) | set(new_fd.keys()))
    for key in all_keys:
        old_val = old_fd.get(key)
        new_val = new_fd.get(key)
        if old_val == new_val:
            continue
        title = clean_title(title_map.get(key, key))
        old_display = "(trống)" if old_val in (None, "", []) else truncate(old_val)
        new_display = "(trống)" if new_val in (None, "", []) else truncate(new_val)
        changes.append((title, old_display, new_display))
    return changes


def build_telegram_message(
    proposal_title: str,
    old_rev,
    new_rev: int,
    changes: list[tuple[str, str, str]],
    slug: str,
) -> str:
    lines = [f"🔔 <b>{html.escape(proposal_title)}</b>"]
    if old_rev is None:
        lines.append("Proposal mới được phát hiện lần đầu.")
    else:
        lines.append(f"Revision {old_rev} → {new_rev}")
        lines.append("")
        for field_title, old_v, new_v in changes[:TELEGRAM_MAX_FIELDS]:
            lines.append(f"• <b>{html.escape(field_title)}</b>")
            lines.append(f"  Trước: {html.escape(old_v)}")
            lines.append(f"  Sau: {html.escape(new_v)}")
            lines.append("")
        if len(changes) > TELEGRAM_MAX_FIELDS:
            lines.append(f"…và {len(changes) - TELEGRAM_MAX_FIELDS} mục khác thay đổi.")

    if GITHUB_REPOSITORY:
        lines.append("")
        lines.append(
            f"🔗 Xem đầy đủ: https://github.com/{GITHUB_REPOSITORY}"
            f"/blob/main/pilot_2026_snapshots/{slug}.md"
        )

    message = "\n".join(lines)
    if len(message) > 4000:  # Telegram giới hạn 4096 ký tự / tin nhắn
        message = message[:3950] + "\n\n…(rút gọn, xem link đầy đủ ở trên)"
    return message


def send_telegram(message: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return  # chưa cấu hình Telegram -> bỏ qua lặng lẽ
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(
            url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "HTML",
                "disable_web_page_preview": True,
            },
            timeout=15,
        )
        if not resp.ok:
            print(f"[warn] Gửi Telegram thất bại: {resp.status_code} {resp.text}")
    except requests.RequestException as e:
        print(f"[warn] Lỗi khi gửi Telegram: {e}")


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

        # Tính diff theo field (nếu đã có snapshot cũ) rồi gửi Telegram
        changes = []
        if prev is not None:
            changes = diff_formdata(prev.get("formData", {}), detail.get("formData", {}), title_map)
        message = build_telegram_message(title, prev_rev, new_rev, changes, new_slug)
        send_telegram(message)

    save_index(index)

    if changed_summaries:
        print(f"\n{len(changed_summaries)} proposal thay đổi. Đã ghi vào {STATE_DIR}")

    else:
        print("Không có proposal nào thay đổi.")


if __name__ == "__main__":
    main()