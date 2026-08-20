# Electricity Bill Calculator.

import time as t
print('         -------- Electricity Bill Calculator ---------')
cust = str(input('\n• Customer Name : '))
ID = str(input('\n• Meter Number / Customer ID : '))
units = float(input('\n• Enter Units Consumed : '))

if units <= 100:
	print('\n• According to ₹5 per unit your bill is ','₹',units*5)
elif units > 100 and units <=200:
	print('\n• According to ₹10 per unit your bill is','₹',(units -100)*10)	
elif units >200:
	print('\n• According to ₹15 per unit your bill is ₹',(units - 200)*15)
else:
	print('Enter valid Units Comsumed !')

if units <= 100:
	amount= ((units * 5))
elif units >100 and units <= 200:
	amount = (((units-100)*10))
elif units > 200:
	amount = (((units - 200)*15))
t.sleep(1)
print('\n             - - - - - - - PAYMENT METHOD - - - - - - - - ')	
print('\n 1. Cash \n 2. UPI \n 3. Card ')
choose = int(input(' • Choose payment method : '))
pay = float(input('\n• PAY BILL : '))
while pay != amount:
	pay = float(input('\n• PAY BILL : '))
t.sleep(1)
print('                       !! PAYMENT RECIVIES !! ')
print('\n                            : RECIPETS :')	
print('\n• Coustomer Name :',cust)
print('\n• Coustomer ID : ',ID)
print('\n• Unit Comsume : ',units)
print('\n• Total electric Bill : ₹',amount)
print('\n• Payment status : PAID ')
if choose == 1:
	print('\n• payment Method : Cash')
elif choose == 2:
	print('\n• payment Method : UPI')
elif choose == 3:
	print('\n• payment Method : Card')
	
print('\n             Thank You for Paying Your Electricity Bill!')
