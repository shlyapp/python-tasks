sales = dict()

data = input()

while data != '':
    customer, purchase, count = data.split()
    if customer not in sales:
        sales[customer] = {purchase: int(count)}
    else:
        sales[customer][purchase] = sales[customer].get(
            purchase, 0) + int(count)
    data = input()

for customer, purchases in sorted(sales.items()):
    print(customer + ':')
    for purchase, count in sorted(sales[customer].items()):
        print(purchase, count)
