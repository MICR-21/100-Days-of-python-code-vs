import art
def find_highest_bidder(auction):
    winner = ""
    highest_bid = 0
    for bidder in auction:
        bid_amount = auction[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of the auction is {winner} with a bid of ${highest_bid}.")

print("Welcome to the secret auction program.")
print(art.logo)
auction = {}  
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if more_bidders == "no":
        continue_bidding = False
        find_highest_bidder(auction)
    elif more_bidders == "yes":    
        print("\n" * 100)
        name = input ("What is your name? ")
        bid = int(input("What is your bid? $"))
        auction[name] = bid 
        
        
        

# more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()    
# highest_bidder = max(auction, key=auction.get)
# highest_bid = auction[highest_bidder]

# print(f"The winner of the auction /is {highest_bidder} with a bid of ${highest_bid}.")
