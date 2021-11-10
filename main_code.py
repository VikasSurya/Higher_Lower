import random
from art import logo,vs

from game_data import data

def format_data(account):
  account_name = account["name"]
  account_des = account["description"]
  account_con = account["country"]
  return(f"{account_name}, {account_des}, from {account_con}.")

def answer_check(user_guess, a_account_follower, b_account_follower):
  if a_account_follower>b_account_follower:
    return guess == "a"
    
  else:
    return guess == "b"

print(logo)
score = 0
game_is_continue = True
account_b = random.choice(data)
while game_is_continue:
  account_a = account_b
  account_b = random.choice(data)
  if account_a==account_b:
    account_b = random.choice(data)

  print(f"compare A : {format_data(account_a)}")
  print(vs)
  print(f"compare B : {format_data(account_b)}")

  guess = input("for A press 'A' and for B Press 'B'  :").lower()

  a_account_follower = account_a["follower_count"]
  b_account_follower = account_b["follower_count"]

  is_correct = answer_check(guess, a_account_follower, a_account_follower)

  if is_correct:
    score = score+1
    print(f"you are right,your current score is {score}")
  else:
    game_is_continue = False
    print(f"you are wrong, your final score is {score}")
