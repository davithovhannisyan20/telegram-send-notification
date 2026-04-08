# Telegram Notifier — Railway Deployment

Send HTML-formatted Telegram messages from a Python script, deployed on Railway.

## Files

```
telegram-notifier/
├── main.py           # Main script
├── requirements.txt  # Python deps
├── railway.toml      # Railway config
└── README.md
```

## 1. Create a Telegram Bot

1. Open Telegram and message [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the prompts
3. Copy the **bot token** (format: `123456:ABC-DEF...`)
4. Get your **chat ID**:
   - Message your bot once
   - Visit: `https://api.telegram.org/bot<TOKEN>/getUpdates`
   - Find `"chat":{"id": YOUR_CHAT_ID}` in the response

## 2. Run Locally

```bash
pip install -r requirements.txt

export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"

python main.py
```

## 3. Deploy to Railway

### Option A — Railway CLI

```bash
npm install -g @railway/cli
railway login
railway init        # create new project
railway up          # deploy
```

Then set env vars:
```bash
railway variables set TELEGRAM_BOT_TOKEN=your_token
railway variables set TELEGRAM_CHAT_ID=your_chat_id
```

### Option B — Railway Dashboard

1. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
2. Connect your repo containing these files
3. In **Variables**, add:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
4. Railway auto-detects Python and deploys

## HTML Formatting Tags (Telegram supports)

| Tag | Effect |
|-----|--------|
| `<b>text</b>` | **Bold** |
| `<i>text</i>` | *Italic* |
| `<code>text</code>` | `Monospace` |
| `<pre>text</pre>` | Code block |
| `<a href="url">text</a>` | Hyperlink |
| `<blockquote>text</blockquote>` | Quote block |
| `<u>text</u>` | Underline |
| `<s>text</s>` | Strikethrough |

## Customizing the Message

Edit `build_html_message()` in `main.py` to build your own notification. Example:

```python
def build_html_message() -> str:
    return (
        "🚨 <b>Deploy Complete</b>\n"
        "Version: <code>v1.4.2</code>\n"
        "Status: <b>✅ Success</b>"
    )
```

## Running on a Schedule (Railway Cron)

In `railway.toml`, replace the deploy section with:

```toml
[deploy]
cronSchedule = "0 9 * * *"   # Every day at 9 AM UTC
startCommand = "python main.py"
```
