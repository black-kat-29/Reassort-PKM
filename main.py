from storage import load_state, save_state
import json
import time

def load_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    while True:
        products = load_products()
        state = load_state()

        # Les modules Amazon/Fnac seront appelés ici.

        save_state(state)
        time.sleep(60)

if __name__ == "__main__":
    main()
