import art


print(art.logo)

is_new_people = True
auction_dict = {}

while is_new_people:
    name = input("What is your name? ")
    bid = int(input("What's your bit?: $"))

    auction_dict[name] = bid

    is_bidders = input("Are there any other bidders? Type 'yes' or 'no'")

    if is_bidders == 'no':
       is_new_people = False
    #elif is_bidders == 'yes':
        # should add clear function



def find_highest_bigger(auction_dict):
    highest_bid = 0
    winner = ''
    for bidder, bid in auction_dict.items():
        if (bid > highest_bid):
            highest_bid = bid
            winner = bidder

    print(f"The winner is {winner} with a bid of {highest_bid}$")


find_highest_bigger(auction_dict)

    
