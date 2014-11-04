
def calculate_discount(item_cost, relative_discount, absolute_discount):
	if relative_discount < 0:
		relative_discount = 0

	if absolute_discount < 0:
		absolute_discount = 0
		
	if item_cost < 0:
		return 0
	else:
		relative_discount_amount = item_cost * (float(relative_discount)/100)
		after_relative_discount = item_cost - relative_discount_amount
		discounted_total = after_relative_discount - absolute_discount

		if discounted_total < 0:
			return 0
		else:
			return discounted_total

def main():
	discounted_total = calculate_discount(200,10,30)
	print discounted_total

if __name__ == '__main__':
	main()