import json
import os

PRODUCTS_FILE = "products.json"

def load_products():
    if not os.path.exists(PRODUCTS_FILE):
        return []

    with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_products(products):
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

import re

def add_product(url):
    products = load_products()

    if "amazon" in url:
        match = re.search(r"/dp/([A-Z0-9]{10})", url)

        if not match:
            return False, "ASIN introuvable."

        asin = match.group(1)

        for product in products:
            if product.get("asin") == asin:
                return False, "Produit déjà présent."

        products.append({
            "site": "amazon",
            "asin": asin
        })

    elif "fnac" in url:

        for product in products:
            if product.get("url") == url:
                return False, "Produit déjà présent."

        products.append({
            "site": "fnac",
            "url": url
        })

    else:
        return False, "Site non pris en charge."

    save_products(products)

    return True, "Produit ajouté."

def remove_product(index):
    products = load_products()

    if index < 0 or index >= len(products):
        return False, "Numéro invalide."

    deleted = products.pop(index)
    save_products(products)

    return True, deleted
