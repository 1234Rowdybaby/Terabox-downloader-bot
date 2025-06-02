import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("Error: BOT_TOKEN environment variable not set")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to TeraBox Downloader Bot!\nSend me a TeraBox link, and I will try to get the download link."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send a valid TeraBox file link, and I'll respond with a downloadable link."
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if "terabox.com" not in text:
        await update.message.reply_text("Please send a valid TeraBox link.")
        return

    # Placeholder for real TeraBox API processing
    download_link = f"Simulated direct download link for:\n{text}"

    await update.message.reply_text(download_link)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_link))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
