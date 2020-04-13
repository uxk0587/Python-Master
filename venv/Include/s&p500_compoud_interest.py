"""

author: Jack Lee
time: 2020/2/25 21:34

"""


def compin_for_the_first_4_year(interest, addmoney, year):
	total = addmoney
	for i in range(year):
		total = total * (1 + interest)
		print("the {} year of the total money is : {}".format(i + 1, total))
		total += addmoney
	return total


def compin_for_the_last_4_year(money_begin, interest, addmoney, year):
	total = money_begin
	for i in range(year):
		total = total * (1 + interest)
		print("the %s year of the total money is %s" % (i + 5, total))
		total += addmoney
	return total - addmoney


def top_coin(now_price, total_count, interest, year):
	total = total_count * now_price
	for i in range(8):
		total = total * (1 + interest)
		print("the {} year of the total top_coin money is {}".format(i + 1, total))
	return total


if __name__ == '__main__':
	money_begin = compin_for_the_first_4_year(0.15, 50000, 4)
	final_money_in_eight_year = compin_for_the_last_4_year(money_begin, 0.15, 100000, 4)
	print("8 year later you will got : %f" % final_money_in_eight_year)
	print("-----------------------------------")
	top_coin(0.01, 30000000, 0.28, 8)


