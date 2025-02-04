print("Welcome to the secret auction program.")

auction = {}  # Empty dictionary to store bids

# First bidder
name = input("What is your name? ")
bid = int(input("What is your bid? $"))
auction[name] = bid

# Check for more bidders
more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()

while more_bidders == "yes":
    name = input ("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction[name] = bid  # Add new bid to dictionary
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()

# Find highest bidder
highest_bidder = max(auction, key=auction.get)
highest_bid = auction[highest_bidder]

print(f"The winner of the auction is {highest_bidder} with a bid of ${highest_bid}.")
