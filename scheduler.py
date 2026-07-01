from apscheduler.schedulers.background import BackgroundScheduler
from checker import check_products

scheduler = BackgroundScheduler()

def scheduled_check():
    print("🔍 Vérification automatique...")
    results = check_products()
    print(f"{len(results)} produit(s) vérifié(s).")

def start_scheduler():
    scheduler.add_job(
        scheduled_check,
        "interval",
        minutes=1,
        id="stock_check",
        replace_existing=True,
    )
    scheduler.start()
