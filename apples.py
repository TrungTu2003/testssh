def tong_tien_phai_tt(input_kg,APPLE):
	return APPLE * input_kg

def tien_thua(Tien_Tao,input_money):
	if input_money < Tien_Tao:
		return -1
	return input_money - Tien_Tao
def tien_thieu(Tien_Tao,input_money):
	return input_money - Tien_Tao

def so_to(total):
	To_500 = int(total/500)
	total = int(total%500)
	if To_500 != 0:
		print("So to 500:" + str(To_500))

	To_200 = int(total/200)
	total = int(total%200)
	if To_200 != 0:
		print("So to 200:" +str(To_200))

	To_100 = int(total/100)
	total = int(total%100)
	if To_100 != 0:
		print("So to 100:" +str(To_100))

	To_50 = int(total/50)
	total = int(total%50)
	if To_50 != 0:
		print("So to 50:" +str(To_50))

	To_20 = int(total/20)
	total = int(total%20)
	if To_20 != 0:
		print("So to 20:" +str(To_20))

	To_10 = int(total/10)
	total = int(total%10)
	if To_10 != 0:
		print("So to 10:" +str(To_10))

	To_5 = int(total/5)
	total = int(total%5)
	if To_5 != 0:
		print("So to 5:" + str(To_5))

	To_2 = int(total/2)
	total =int(total%2)
	if To_2 != 0:
		print("So to 2:" + str(To_2))

	To_1 = total
	if To_1 != 0:
		print("So to 1:" + str(To_1))

def main():
	APPLE = 20 #k VND
	input_kg = float(input("Can nang cua tao:"))
	input_money = float(input("Tien khach tra:"))

	Tien_Tao = tong_tien_phai_tt(APPLE,input_kg)
	Tien_Thua = tien_thua(Tien_Tao,input_money)
	Tien_Thieu = tien_thieu(Tien_Tao,input_money) 

	print("Tien Phai Thanh Toan:" + str(int(Tien_Tao)))
	if Tien_Thua == -1:
		print("Ban thieu so tien la:" + str(int(Tien_Thieu)))
	else:
		print("Tien Thua Cua Khach:" + str(int(Tien_Thua))) 
		so_to(Tien_Thua)

main()
