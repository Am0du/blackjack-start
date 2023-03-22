from art import logo
import random
from replit import clear

def give_card(deck):
    """Generates a card"""
    random_num = random.randint(0,len(deck) -1)
    draw = deck[random_num]
    return draw

def scores(u_score):
    """add total score and checks for ace"""
    score = sum(u_score)
    ace = 0
    for i in range(len(u_score)):
        if u_score[i] == 11:
            ace = u_score[i]
        
    if score >= 21 and ace == 11:
        return score - 10
        
    return score

def check_blackjack(user_, comp_, user_name):
    """Checks if there's an BlackJack"""
    if sum(user_) <= 21 and sum(comp_) <= 21:
       return ""
        
    elif sum(comp_) == 21:
        return f"computer's card = {comp_}: Total: {sum(comp_)}\n BLACKJACK, Computer wins"
     
    elif sum(user_) == 21:
        return f"{user_name}'s card = {user_}: Total: {sum(user_)}\n BLACKJACK {user_name} wins"
       
            
def blackjack():
    """Hold the game """
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
    
    user = []
    comp = []
    user_name = input("What's Your name: ")
    for i in range(2):
        user.append(give_card(cards))
        comp.append(give_card(cards))
        
    #Checks if there's an ace that can win the game
    blackjack_result = check_blackjack(user, comp, user_name)

    
    if blackjack_result == "":
        another_card = True
    else:
        print(blackjack_result )
        another_card = False
        rerun = input("Type 'y' to restart game: ")
        if rerun == 'y':
            clear()
            blackjack()
        else:
            clear()
            print(f"Goodbye {user_name}")

    
    #Loops to add more card, calculate the sum and check if user hand is higher than 21
    while another_card is True:
        user_score = scores(user)
        comp_score = scores(comp)
        print(f"{user_name}'s card = {user}::::::::TOTAL = {user_score}\n Computer's card = [{comp[0]}]")

        if user_score > 21:
            print(f"Computer's card = {comp}, Computer wins")
            another_card = False
            rerun = input("Type 'y' to restart game: ")
            if rerun == 'y':
                blackjack()
            else:
                clear()
                print(f"Goodbye {user_name}")
            
        else:
            restart = input("Type 'y' to get another card, 'n' to end: ")
            if restart == 'y' :
                another_card = True
                user.append(give_card(cards))
            else:
                another_card = False
            
    #Loop to increase computer hand 
    while comp_score <= 17:
        comp.append(give_card(cards))
        comp_score = scores(comp)

    #checks for a winner
    if comp_score > 21 or user_score > comp_score:
         print(f"{user_name} = {user}, {user_name} wins")
    elif comp_score > user_score:
        print(f"Computer's card = {comp} Computer wins")
    else: 
        print(f"Computer's card = {comp} and {user_name}'s card = {user}, Its a draw")
    
    #Restart the game
    rerun = input("Type 'y' to restart game or 'n' to end: ")
    if rerun == 'y':
        clear()
        blackjack()
    else:
        clear()
        print(logo)
        print(f"Goodbye {user_name}")
        

blackjack()