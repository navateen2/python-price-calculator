def calculate_total(price, quantity, percentageDiscount):
    total = price * quantity
    total -= total * percentageDiscount / 100
    return total

def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity,20)
    print(f"Total amount: {total}")


main()
