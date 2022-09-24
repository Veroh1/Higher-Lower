#Imports
import random
from game_data import data
from art import logo
from art import vs
from replit import clear


#Functions

def format_data(account):
    """Takes the account data and returns a printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def picker():
    """Returns a random choice from game data."""
    pick = random.choice(data)
    return pick

def check_answer(guess, account_a,account_b):
    """Use if statement to check if user is correct"""
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    if a_follower_count > b_follower_count:
        return guess == "a"
    else: 
        return guess == "b"
    
#Function to run the main game data

def higher_lower():
    
    score = 0
    game_should_continue = True
    account_b = picker()
    
    while game_should_continue:
        account_a = account_b
        account_b = picker()
        while account_a == account_b:
            account_b = picker()
        
        print(logo)
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")
    
        guess = input("who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess, account_a, account_b)
        if is_correct:
            score += 1
            clear()
            print(f"You're right! Current score: {score}")   
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False
        
        
        
#main loop to reset game
while input("Do you want to play Higher Lower?: ").lower() == "y":
    higher_lower()


