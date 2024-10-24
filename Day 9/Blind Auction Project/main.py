# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo

print(logo)
should_continue = True
dict = {}
while should_continue:
    name = input("Enter your name")
    price = input("Enter your price:$")
    dict[name] = price

    restart = input("Are there any other bidders in the auction type 'yes' or 'no:").lower()
    if restart == "yes":
        print("\n" * 20)
    else:
        should_continue = False
        winner = ""
        highest_bid = 0
        for bidder in dict:
            bid_amount = int(dict[bidder])
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"the winner is {winner}, with a highest bid of {highest_bid}")


