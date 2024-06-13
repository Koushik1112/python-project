import random
def guess(j):
    num=random.randint(1,51)
    i=j
    while(i<=j):
        x=int(input("guess the number :"))
        if x<num:
            print("your guess is too low")
            i-=1
            print("left u have",i,"chances")
        elif x>num:
            print("your guess is to high")
            i-=1
            print("left u have",i,"chances")
        elif x==num:
            print("your guess is correct")
            print("left u have",i,"chances")
            break
        if i==0:
            print("loose game")
            break 
opinion=input("choose your level hard or easy :")
if opinion=="hard":
    guess(5)
elif opinion=="easy":
    guess(10)
       
    
