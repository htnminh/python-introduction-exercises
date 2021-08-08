def calc(line, d):
    customer, product, quantity = tuple(line.split())
    if customer not in d:
        d[customer] = dict()
    if product not in d[customer]:
        d[customer][product] = 0
    d[customer][product] += int(quantity)
    
    
def process(filepath):
    f = open(filepath, 'r')
    
    d = dict()
    for line in f:
        calc(line, d)
    
    customers = list(d)
    customers.sort()
    
    for customer in customers:
        print(customer + ':')
        products = list(d[customer])
        products.sort()
        for product in products:
            print(product, d[customer][product])

'''
filepath = 'data1.inp'
process(filepath)
'''




    