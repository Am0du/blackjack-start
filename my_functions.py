import random
from replit import clear
from art import logo


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


def random_bet():
    """Places a bet for the computer"""
    bet = random.randint(10, 200)
    return bet

def bet_winner(comp_score,user_name, user_score, comp_bet, user_bet, comp, user):
    """Checks for a winner"""
    result = comp_bet + user_bet
    if comp_score > 21 or user_score > comp_score:
        return f"{user_name} = {user}, {user_name} wins \n You win \n {user_name} wins {result}"
            
    elif comp_score > user_score:
        return f"Computer's card = {comp} Computer wins \n Computer wins ${result}"
    else: 
        return f"Computer's card = {comp} and {user_name}'s card = {user}, Its a draw \n {user_name} takes ${user_bet} while Computer takes ${comp_bet}"
    
    