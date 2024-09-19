def excluding_vat_price(price):
	if price != None:
		return round((price * 100) / 115, 2)
	else:
		return -1
