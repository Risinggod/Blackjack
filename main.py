import random
cards=[2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "D", "K", "A"]*4
random.shuffle(cards)
player1=[]
dealer=[]

def drawr(user):
    user.append(cards.pop())
def cardcounter(user):
    count=0
    for a in user:
        if a=="j" or a=="D" or a=="K":
            count+=10
        elif a=="A":
            count+=11
        else:
            count+=a
    return count

#filling up the list and than counting them together
drawr(player1)
drawr(player1)
drawr(dealer)

#the loop for the game
while True:
    print("your cards sir:", player1)
    print("dealers card is:", dealer)
    cardcounter(player1)
    cardcounter(dealer)
    ferst_question=input("do you whant wann mor card")
    if ferst_question=="yes":
        drawr(player1) and print("your new cards", player1)
        drawr(dealer) and print(("dealers cards", dealer))
        if cardcounter(player1)>21 or cardcounter(dealer)>21:
            print("game is over:","",  "dealer got:",dealer,  cardcounter(dealer),"",  "you got:",player1, cardcounter(player1) )
            break
        continue
    if ferst_question=="no":
        print(player1)
        print(cardcounter(player1))
        break
    if cardcounter(player1)>21:
        break




















