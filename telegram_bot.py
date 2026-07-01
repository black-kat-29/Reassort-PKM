from product_manager import add_product
from product_manager import load_products
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

    products = load_products()

    if not products:
        await update.message.reply_text("Aucun produit surveillé.")
        return

    text = "📦 Produits surveillés\n\n"

    for i, product in enumerate(products, start=1):

        if product["site"] == "amazon":
            text += f"{i}. Amazon - {product['asin']}\n"

        else:
            text += f"{i}. Fnac\n"

    await update.message.reply_text(text)
    

def build_app(app.add_handler(CommandHandler("add", add))):
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("list", list_products))

    return app

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Utilisation :\n/add <lien>"
        )
        return

    url = context.args[0]

    success, message = add_product(url)

    if success:
        await update.message.reply_text("✅ " + message)
    else:
        await update.message.reply_text("❌ " + message)
