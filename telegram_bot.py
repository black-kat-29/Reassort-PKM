from checker import check_products
from product_manager import remove_product
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
    

def build_app():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("list", list_products))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("remove", remove))
    app.add_handler(CommandHandler("check", check))
    app.add_handler(CommandHandler("help", help_command))
    
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

async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Utilisation :\n/remove <numéro>"
        )
        return

    try:
        index = int(context.args[0]) - 1
    except ValueError:
        await update.message.reply_text("❌ Le numéro doit être un entier.")
        return

    success, result = remove_product(index)

    if success:
        await update.message.reply_text("✅ Produit supprimé.")
    else:
        await update.message.reply_text("❌ " + result)

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("🔍 Vérification des produits...")

    results = check_products()

    if not results:
        await update.message.reply_text("Aucun produit enregistré.")
        return

    text = "📦 Résultat de la vérification\n\n"

    for product in results:
        text += (
            f"🏪 {product['site']}\n"
            f"{product['name']}\n"
            f"{product['status']}\n\n"
        )

    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "🤖 StockPKM\n\n"
        "Commandes disponibles :\n\n"
        "/start - Démarrer le bot\n"
        "/status - Vérifier que le bot fonctionne\n"
        "/list - Afficher les produits surveillés\n"
        "/add <lien> - Ajouter un produit\n"
        "/remove <numéro> - Supprimer un produit\n"
        "/check - Vérifier les produits\n"
        "/help - Afficher cette aide"
    )

    await update.message.reply_text(message)
