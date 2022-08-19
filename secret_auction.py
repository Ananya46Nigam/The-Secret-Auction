# Ananya Nigam

from turtle import clear
from art import logo
import os
print(logo)

bidding_dict=dict()

is_bidder=True

while is_bidder:
    name=input("What is your Name ?\n").strip()
    amount=int(input("How much rupees would you like to bid ?\nRs.").strip())
    bidding_dict[name]=amount
    decision=input("Type yes if there more bidders else type no.\n").strip().lower()
    if decision=="no":
        is_bidder=False
        cls = lambda: os.system('cls')
        cls()
        max=0
        
        for key in bidding_dict:
            if bidding_dict[key]>max:
                max=bidding_dict[key]
                final_bidder=""+key
        print("***** The results are out !! *****")        
        print(f"Hurray!! The highest bid amount is : Rs.{max} of {final_bidder} !!")  
        
           
    else:
        cls = lambda: os.system('cls')
        cls()       
        
# print(bidding_dict)
  

      
    
        
        

