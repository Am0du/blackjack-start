from art import logo
import random
from replit import clear
from my_functions import give_card, scores, check_blackjack, random_bet, bet_winner

def rerun_game(user_name):
    """Restarts the game """
    rerun = input("Type 'y' to restart game or 'n' to end: ")
    if rerun == 'y':
        clear()
        blackjack()
    elif rerun == 'n':
        clear()
        print(logo)
        print(f"Goodbye {user_name}")
    else:
        print("Invalid option")
        rerun()

def blackjack():
    """Hold the game """
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
    
    user = []
    comp = []
    user_name = input("What's Your name: ")
    user_bet = int(input("Place a bet: $"))
    comp_bet = random_bet()
    print(f"The computer place a bet of ${comp_bet}")
    
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
            print(bet_winner(comp_score,user_name, user_score, comp_bet, user_bet, comp, user))
            another_card = False
            rerun_game(user_name)
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
    print(bet_winner(comp_score,user_name, user_score, comp_bet, user_bet, comp, user))
    
    #Restart the game
    rerun_game(user_name)

blackjack()