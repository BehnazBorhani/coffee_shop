from Menu import menu

orders = []

def add_order():
    name = input("نام محصول موردنظر: ").strip().lower()

    if name not in menu:
        print(" این محصول در منوی کافه وجود ندارد.")
        return

    try:
        qty = int(input("تعداد: "))
        if qty <= 0:
            print(" تعداد باید عددی مثبت باشد.")
            return
    except ValueError:
        print(" تعداد باید عدد باشد.")
        return

    orders.append({"name": name, "price": menu[name], "qty": qty})
    print(f" {qty} عدد {name} به سفارش اضافه شد.")

def show_orders():
    if not orders:
        print(" هنوز هیچ سفارشی ثبت نشده است.")
        return

    print("\n===== سفارش‌های ثبت‌شده =====")
    for i, o in enumerate(orders, start=1):
        print(f"{i}. {o['name']} | قیمت واحد: {o['price']:,} | تعداد: {o['qty']}")
    print("==============================")