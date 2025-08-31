from os import system

print("""





                        



                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
""")
print("Welcome to the secret auction program!")

auction_active = True

auction_bids:dict = {}

while auction_active:

    bidder_name = str(input("What is your name? "))
    bid_amount = int(input("What is your bid?: $"))

    auction_bids[bidder_name] = bid_amount

    other_bidders = input("Are there more bidder? Yes or No ").lower()

    if other_bidders == "no":
        auction_active = False

    system("cls")


def highest_bidder(auction_bids):
    highest_bid = 0
    name_highest_bidder = ""

    for key in auction_bids:
        if auction_bids[key] > highest_bid:
            highest_bid = auction_bids[key]
            name_highest_bidder = key

    print(f"Highest bidder is {name_highest_bidder} with a bid of: {highest_bid}")

highest_bidder(auction_bids)