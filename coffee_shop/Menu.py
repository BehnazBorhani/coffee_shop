menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000
}

def show_menu():
    print("\n===== منوی کافه =====")
    for item, price in menu.items():
        print(f"{item}: {price:,} تومان")
    print("=====================")