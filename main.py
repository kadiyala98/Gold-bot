import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

BOT_RUNNING = False
app_web = Flask(__name__)
@app_web.route('/')
def home():
    return "Gold Bot Running"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_RUNNING
    BOT_RUNNING = True
    await update.message.reply_text("✅ GOLD BOT STARTED\nLondon Breakout + EMA20\n09:00-13:30 UTC\n0.01 lot | SL $3 TP $6")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_RUNNING
    BOT_RUNNING = False
    await update.message.reply_text("🛑 Bot STOPPED")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💰 Status: {'RUNNING 🟢' if BOT_RUNNING else 'STOPPED 🔴'}\nTime: {datetime.now().strftime('%H:%M')} UTC")

def run_telegram():
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("balance", balance))
    print("Bot starting...")
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_telegram, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)
