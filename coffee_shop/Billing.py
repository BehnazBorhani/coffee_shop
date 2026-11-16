from Order import orders

def calculate_total():
    total = 0
    for o in orders:
        total += o["price"] * o["qty"]
    return total

def calculate_discount(total):
    if total > 1_000_000:
        return total * 0.10
    return 0

def print_invoice():
    if not orders:
        print("سفارشی برای صدور فاکتور وجود ندارد.")
        return

    print("\n========= فاکتور =========")
    for o in orders:
        line_total = o["price"] * o["qty"]
        print(f"{o['name']} × {o['qty']} = {line_total:,} تومان")

    total = calculate_total()
    discount = calculate_discount(total)
    final = total - discount

    print("-" * 30)
    print(f"مبلغ کل:         {total:,} تومان")
    print(f"تخفیف:           {discount:,} تومان")
    print(f"مبلغ قابل پرداخت: {final:,} تومان")
    print("==========================")