#Rock Paper Scissors
# 1=Rock, 2=Scissors, 3=Paper
a= str(input('Your Choice (Rock, Paper, Scissors) '))
b=a.upper()
import random
import string
n= random.randint(1,3)
if b=='ROCK' and n==1:
    print ('My choice was Rock and we Tied')
elif b=='ROCK' and n==2:
    print ('My Choice was Scissors and You Won')
elif b=='ROCK' and n==3:
    print ('My choice was Paper and You Lost')
elif a.upper()=='SCISSORS' and n==1:
    print ('My choice was Rock and You Lost')
elif a.upper()=='SCISSORS' and n==2:
    print ('My choice was Scissors and we Tied')
elif a.upper()=='SCISSORS' and n==3:
    print ('My choice was Paper and You Won')
elif a.upper()=='PAPER' and n==1:
    print ('My choice was Rock and You Won')
elif a.upper()=='PAPER' and n==2:
    print ('My choice was Scissors and You Lost')
elif a.upper()=='PAPER' and n==3:
    print ('My choice was also Paper and we Tied')
else:
    print ('Select the right option')