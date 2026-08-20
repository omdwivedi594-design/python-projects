 #.          Resturant Billing System.

print("           ------- Restaurant Billing System -------")
customer= str(input("\nEnter your name : "))
print("\n                          -: MAINU :-")
food =("\n 1. Panner \n 2. Chole \n 3. maggie \n 4. pasta")
print(food)
choose = int(input('\n• Choose item : '))
print("\n• Do you Want anything else (Y/N)")
chose = str(input('  : '))
while chose == 'Yes' or chose == 'yes':
    print(food)
    choose = int(input('\n• Choose item : '))
    print("\n• Do you Want anything else (Y/N)")
    chose = str(input('                                 : '))
    
qut = int(input('\n• Enter Quantity you want : ')) 
total = (100 * qut)
if total > 300:
	total = total-50
	print('\n• You get 5% discount : ',total)
else:
	print('\n• Your total amount is :',total)
print('\n            ---------Choose Payment method---------')	
print('\n 1. Cash \n 2. UPI \n 3. Card')
chi = str(input('\n• Selecte Method : '))
bill= float(input('\n• Pay bill : '))
while bill != total :
	bill= float(input('\n• Pay bill : '))
print('\n                    Payment successfully Recived        ')	
print('\n               _ _ _ _ _ _ _ Recipted _ _ _ _ _ _ _ ')
print(f'\n• Customer Name : {customer}')
if choose == 1:
	print('\n• Your Order : Panner ')
elif choose == 2:
	print('\n• Your Order : Chole ')
elif  choose == 3:
		print('\n• Your Order : Maggie ')	
elif  choose == 4:
			print('\n• Your Order : Pasta ')
else:
			print('\n• Your Order : Nothing')

if total > 300:
			print('\n• You get 5% discount')
else:
			print('\n• You did not get any discount ')
print('\n• Your Total Amount is :',total)

print('\n                         !Thanks For Order !')
