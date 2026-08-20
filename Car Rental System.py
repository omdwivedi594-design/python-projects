#      Car Rental System.

print('          - - - - - - - Car Rental System - - - - - - -  ')
name = str(input('\n• Name : '))
add = str(input('• Address : '))
no = int(input('• Mobil Number : '))
print('\n                       : Choose Your Car :')
print('\n 1. BMW \n 2. Audi \n 3. Mersdice \n 4. Fortuner ')
chose = int(input('\n• Select Car : '))
day = int(input('• Rental Days : '))
driver = str(input('• Do you need Driver (Yes/No) : '))
if driver == 'yes' or driver == 'Yes' or driver == 'YES':
	print('\n                     We Arrange Driver For you !! ')
elif driver == 'no' or driver == 'NO' or driver == 'No':
	print('\n                            Sure sir !!')

fuel= str(input('\n• Do You Want Extra Fuel : '))
if fuel== 'no' or fuel== 'No':
	print('\n                            Okay Sirr !!')
elif fuel == 'Yes' or fuel== 'yes':
	print('\n                         Sure Sir We added !! ')

if day >5:
	print('\n• You Get 10% Discounts !!')
elif day <5:
	print('\n• You Get 2% Discount !!')
print('\n           ____________ Choose Payment Method ___________')
print('\n 1. Cash \n 2. Card \n 3. UPI ')
ch= int(input('• Choose Payment Method : '))
total=(day*10000)
print('\n• Your Total amount to Pay :',total)
bill= int(input('• Pay Bill : '))
while bill != total:
	bill= int(input('• Pay Bill : '))
	
print('                               -- YOUR Billl --')
print('\n• Name : ',name)
print('• Addrrss : ',add)
print('• Mobil number : ',no)
if chose == 1:
	print('• Your Select Car : BMW ')
elif chose == 2:
	print('• Your Select Car : Audi ')
elif chose == 3:
	print('• Your Select Car : Merdcise')
elif chose == 4:
	print('• Your Select Car : Fortuner')	
print('• Rental Days : ',day)
if driver == 'yes' or driver == 'Yes' or driver == 'YES':
	print('• Driver Need : Yes ')
elif driver == 'no' or driver == 'NO' or driver == 'No':
	print('• Driver Need : No')

if fuel== 'no' or fuel== 'No':
	print('• Fuel Need : No ')
elif fuel == 'Yes' or fuel== 'yes':
	print('• Fuel Need : Yes ')
	

if day >5:
	print('• Any Discount : You Get 10% Discounts !!')
elif day <5:
	print('• Any Discount : You Get 2% Discount !!')
print('• Total Bill : ',total )
print('• Bill Paid or Not : PAID ')
print('\n          ----------- THANKS FOR BUY CAR ----------')
