#.  Gussing game !!

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
