# Q.1 Check input number is divisible by 35 , 5 and 7.

for num in range(10):
    num = int(input('Enter your no..'))
    if num % 35 == 0:
        print ('this number is divisible by 35 , 7 and 5' )
    elif num % 5==0:
        print('this no. is divisible by 5')
    elif num % 7==0:
        print('this no. is divisible by 7')
    else :
        print ('this no. is not divisible by 35 ,5 and 7')
#_____________________________________________ 
# Q.2 Check student exam status.

marks1 = float(input('Enter your english marks :'))
marks2 = float(input('Enter your maths marks :'))
marks3 = float(input('Enter your I.P marks : '))

avg_marks = (marks1 + marks2 + marks3)/3
total = (marks1 + marks2 + marks3)
if total > 75:
    print('PASS \ngrace marks A+')
elif total< 75:
    print('Fail')
print(f'Average marks is {avg_marks}')
#_____________________________________________

# Q.3 Give bonus according to sallery and experience.

sal = int(input('Enter your salary : '))
exp = int(input('Enter your experience : '))
if sal < 30000:
    print('You get 5% bonus !!')
elif sal > 30000 and sal <50000:
    print(' You get 10% bonus !!')
elif sal > 50000:
    print('You get 20% bonus !!')
if exp > 10:
    print('You get 5% bonus extra')
else:
    print(' ~ invalid detail ~')
    
#_____________________________________________ 
# Q.4 Write a Any table using loops.

table = 1
while table < 11:
    print('2 ×',table,'=',table*2)
    table = 1 + table
  
#_____________________________________________

# Q.5 Banking Management System.

balance = 500
user = int(input(' • Enter your password : '))
pas = int(input(' • Login account : '))
while user != pas:
    print('\n    Wrong password')
    user = int(input(' • Enter your password : '))
    pas = int(input(' • Login account : '))
print('\n                        Login Successful ')

while balance >0 :
   print('\n 1. Deposite Money \n 2. See balance \n 3. Withdraw \n 4. Exit ')
   choice = int(input('\n Enter your Choice : ')) 
   if choice == 1:
       dep = float(input(' • Enter Amount : '))
       if dep > 0:
           balance = (balance + dep)
           print(' ',dep,'₹ has been deposite !! ')
   elif choice == 2:
            print(' Your Remain balance is :', balance,'₹')
       
   elif choice == 3:
        draw = float(input('Enter Amount : '))
        
        if draw < balance :
            balance = balance - draw
            print(' ',draw,'₹ has been withdraw !!')
            print('Your Remain balance is', balance,'₹')
    
   elif choice == 4:
        print ('\n                       Thanks For Using !!')
        break
        
#_____________________________________________
        
# Q.6 Resturant Billing System.

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

#_____________________________________________
#Q.7 Electricity Bill Calculator.

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
#_____________________________________________
# Q.8 Car Rental System.
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
#_____________________________________________
# Q.9 Gussing game !!

import random as rd
print("-: Welcome the Gussing number game :-")
print ('  -: guss number between 1 - 100 :-')
chioes= (rd.randint(1,100))
attempts=0
while True:
  guess=int(input("~enter your no :-"))
  attempts= attempts+1
  if guess>chioes:
    print(" 😂little short!! Try again ")
  elif guess<chioes:
    print("😂little higher Try again")    
  elif guess==chioes:
    break
print(f" Congratulations 🎉 👏 You won! in 💀{attempts} attempts")
#_____________________________________________
# Q.10  🏫 Student Result Management System.

import time

name = str(input('Enter your name : '))
roll = int(input('Enter your Roll no : '))

marks1 = float(input('Enter your english marks :'))
while marks1<0 or marks1>100 :
    print('Invalid number, please try again')
    marks1 = float(input('Enter your english marks :'))
   
marks2 = float(input('Enter your Maths marks :'))
while marks2<0 or marks2>100 :
    print('Invalid number, please try again')
    marks2 = float(input('Enter your Maths marks :'))
  
marks3 = float(input('Enter your Science marks :'))
while marks3<0 or marks3>100 :
    print('Invalid number, please try again')
    marks3 = float(input('Enter your Science marks :'))
    
marks4 = float(input('Enter your G.K marks :'))
while marks4<0 or marks4>100 :
    print('Invalid number, please try again')
    marks4 = float(input('Enter your G.K marks :'))
    
marks5 = float(input('Enter your Hindi marks :'))
while marks5<0 or marks5>100 :
    print('Invalid number, please try again')
    marks5 = float(input('Enter your Hindi marks :'))

total_marks = (marks1 + marks2 + marks3 + marks4 + marks5)
percen = (total_marks /500)*100 
avg_marks =  (total_marks /500)*100 


print('Do you Want to see your Result : (Y / N)')
choose = (input('Enter your choose : '))
if choose == 'n' or choose == 'N' :
   print('Thanks for visiting')
elif choose == 'y' or choose == 'Y':
      time.sleep(1)
    

print('              ________________Result__________________')
print()
print(' • NAME     :',name)
print(' • Roll no. :', roll)
print()
print(' • English :', marks1)
print(' • Maths   :', marks2)
print(' • Science :', marks3)
print(' • G.K     :', marks4)
print(' • Hindi   :', marks5)
print()
print(' • Total Marks =', total_marks,'/500')
print(' • Total percentage =', percen,'%')
print(' • Average =', percen)
print()
 

if percen >=90 and percen <=100:
   print(' • Grade = A+')
elif percen >=80 and percen <=89:
   print(' • Grade = A')
elif percen >=70 and  percen <=79:
   print(' • Grade = B')
elif percen >= 60 and percen <=69:
   print(' • Grade = C')
elif percen >=50 and percen <=59:
  print(' • Garde = D')
  

if percen >50:
   print(' • Result = PASS ')
else:
   print(' • Result = FAIL ')
   
#_____________________________________________
#Q.11 Railway Reservation System.

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
#_____________________________________________
# Q.12  Quiz Competition System ⭐⭐⭐⭐⭐

print('     ----------------- WELCOME TO QUIZ GAME ------------------')
st = input('\n • ARE YOU READY (Y/N) : ')
if st == 'no' or st == 'No' :
	print('\n                  { Abe to Khel kyu rha hai } ')
elif st == 'yes' or st == 'Yes':
	print()
	
	correct = 0 
	Q = print('\n Q.1 who is the father of nation ??')
	Op = print('\n 1. keshav                 2. Om \n 3. Raju                   4. Mahatma Gandhi')
	ans = int(input('\n• Choose correct Option : '))
	if ans == 1:
		print('\n                        - WRONG ANSWER -\n                Correct Answer : MAHATMA GANDHI ')
	elif ans == 2:
		print('\n                        - WRONG ANSWER -\n                Correct Answer : MAHATMA GANDHI ')
	elif ans == 3:
		print('\n                        - WRONG ANSWER -\n                Correct Answer : MAHATMA GANDHI ')
	elif ans == 4:
		correct +=1
		print('\n                      !! Correct Answer !!')
	Qs = print('\n Q.2 Which Animal Store water for a month ??')
	ops = print('\n 1. keshav                 2. Cat \n 3. Dog                    4. Camel ')
	anw = int(input('\n• Choose correct Option : '))
	if anw == 1:
		print('\n                        - WRONG ANSWER -\n                Correct Answer : CAMEL ')
	elif anw == 2:
		('\n                        - WRONG ANSWER -\n                Correct Answer : CAMEL ')
	elif anw == 3:
		print('\n                        - WRONG ANSWER -\n                Correct Answer : CAMEL ')
	elif anw == 4:
		correct +=1
		print('\n                      !! Correct Answer !!')
	
	print(f'\n•      -- YOUR CORRECT ANSWER : {correct} OUT OF 2 QUESTION -- ')
#_____________________________________________
#Q.13 








