# Enumeration 2
# Here is another similar problem that needs some more careful consideration. Add some code that iterates over the products list items and produces the following output:

# Product: table

# Product: chair

# Product: door

products = ['table', 'chair', 'door']

for index, product in enumerate(products):
    print(f"Product: {product}")