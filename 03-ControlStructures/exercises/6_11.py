n_price = 150.00
d_price = 140.00
discount = (n_price - d_price) / n_price * 100
if discount >= 10:
    print(f'Current product price: {d_price}')
    print(f'Previous product price: {n_price}')
    print("Buy the product!!")
    print(f'Product price reduced by {discount}%')
else:
    print("Product isn't discounted or the price is reduced by less than 10%")