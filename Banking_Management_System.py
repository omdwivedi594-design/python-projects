#  Banking Management System.

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
