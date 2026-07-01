from product_manager import load_products
from stats import increment_checks

def check_products():
    increment_checks()  
    
    products = load_products()

    results = []

    for product in products:
        if product["site"] == "amazon":
            results.append({
                "site": "Amazon",
                "name": product["asin"],
                "status": "⏳ Vérification bientôt disponible"
            })

        elif product["site"] == "fnac":
            results.append({
                "site": "Fnac",
                "name": product["url"],
                "status": "⏳ Vérification bientôt disponible"
            })

    return results
