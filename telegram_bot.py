from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ StockPKM est en ligne.\n\n"
        "Commandes disponibles :\n"
        "/status\n"
        "/list"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Bot actif sur Railway.")

async def list_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 La liste des produits sera ajoutée à l'étape suivante.")

def build_app():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("list", list_products))

    return app
