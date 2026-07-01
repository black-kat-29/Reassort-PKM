from logger import log

def log("Produit ajouté"):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("stockpkm.log", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")
