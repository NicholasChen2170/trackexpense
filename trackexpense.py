products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	money = []
	money.append(name)
	money.append(price)
	products.append(money)
print(products)