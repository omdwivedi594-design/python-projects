#.  Quiz Competition System ⭐⭐⭐⭐⭐

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
