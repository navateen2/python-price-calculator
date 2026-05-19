def calculate_total_tax(price, quantity, percentageTax=0):
    total = price * quantity
    total += total * percentageTax / 100
    return total
def calculate_total_discount(price, quantity, percentageDiscount):
    total = price * quantity
    total -= total * percentageDiscount / 100
    return total

def main():
    price = 100
    quantity = 2

    
    total = calculate_total_tax(price, quantity,5)
    total = calculate_total_discount(price, quantity,20)

    
    print(f"Total amount: {total}")


main()
