 # Student Result Management System.

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
