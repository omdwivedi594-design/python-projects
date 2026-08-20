#.  Railway Reservation System.

print('         ---------- Railway Reservation System -----------')
Des = str(input('\n• Where You Want To Go : '))
print('\n                        -: Choose Class :- ')
print('\n 1. Binessess Class \n 2. AC Class \n 3. Economic Class  ') 
choose = int(input('\n• Choose Class You Want : '))
if choose == 1:
	print('\n• Binessess Class Booking Successfully')
elif choose == 2:
	print('\n• AC Class Booking Successfully')
elif choose == 3:
	print('\n• Economic Class Booking Successfully')
Num = int(input('\n• Number of Passengers : '))
if Num > 3 :
	print('\n• 10% Discount are Applied ')
total= (150*Num)
print('\n• Your Total Bill of Ticket : ',total)
print('\n• After applied Discount :',total - 25)
pay = int(input('• Pay Bill : '))
while pay != total:
	pay = int(input('• Pay Bill : '))
print('\n         Payment Successful Recived ')
print('\n• Do You Want to Cancel the Ticket ')
tri = str(input('• Yes/No : '))
if tri == 'Yes' or tri == 'yes':
	print('\n• Your Ticket has been Cancel !!')
elif tri == 'No' or tri == 'no':
	print('\n• Sure Sir !')
