from telegram_bot import build_app

def main():
    app = build_app()
    print("✅ StockPKM est lancé")
    app.run_polling()

if __name__ == "__main__":
    main()
