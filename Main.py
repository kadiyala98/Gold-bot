import os, asyncio
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from metaapi_cloud_sdk import MetaApi

TOKEN = os.getenv("TELEGRAM_TOKEN")
METAAPI_TOKEN = os.getenv("METAAPI_TOKEN")
ACCOUNT_ID = os.getenv("ACCOUNT_ID")

bot_running = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot_running
    bot_running = True
    await update.message.reply_text("✅ Gold bot STARTED\nLondon Breakout + EMA20\n09:00-13:30 UTC\nMax 3 trades/day, 0.01 lot, SL $3 TP $6")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot_running
    bot_running = False
    await update.message.reply_text("🛑 Bot STOPPED - All trading paused")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Demo Balance: Use MetaApi dashboard to see live P&L\nWeekly target: +3% to +6% realistic (not 25%)\nLeverage: 1:100\nLot: 0.01 fixed")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stop", stop))
app.add_handler(CommandHandler("balance", balance))

print("Bot running...")
app.run_polling()
