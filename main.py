import os
import requests
import time


TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send_telegram_message(html_message: str) -> dict:
    """Send an HTML-formatted message to a Telegram chat."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": html_message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False,
    }

    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


def build_html_message() -> str:
    """Build a sample HTML-formatted Telegram message."""
    now = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())

    return (
        "🔔 <b>Notification Alert</b>\n"
        "\n"
        f"🕐 <i>Timestamp:</i> <code>{now}</code>\n"
        "\n"
        "📋 <b>Details:</b>\n"
        "  • Status: <b>✅ Healthy</b>\n"
        "  • Environment: <code>production</code>\n"
        "  • Deployed via: <a href='https://railway.app'>Railway</a>\n"
        "\n"
        "<blockquote>Everything is running smoothly.</blockquote>"
    )


def main():
    print("Sending Telegram notification...")

    message = build_html_message()
    result = send_telegram_message(message)

    if result.get("ok"):
        msg_id = result["result"]["message_id"]
        print(f"✅ Message sent successfully (message_id={msg_id})")
    else:
        print(f"❌ Failed to send message: {result}")
        raise RuntimeError("Telegram API returned ok=false")


if __name__ == "__main__":
    main()
