import os
def bit_winner(bidder_details):
    highest_bit=0
    winner=''
    for bidder_name in bidder_details:
        bidding_price=bidder_details[bidder_name]
        if bidding_price>highest_bit:
            highest_bit=bidding_price
            winner=bidder_name
    print(f"The Winner is {winner} with a bid of {highest_bit}")

bidder_data={}
# print(type(data))
exit=False
while(not exit):
    name=input("Enter the name: ")
    bid_price=int(input("Enter the bit_value: "))
    bidder_data[name]=bid_price
    add=input("Are there any bidders?,type 'yes' or 'no' ").lower()
    if(add=='yes'):
        exit=False
        os.system('cls')
    else:
        exit=True
        bit_winner(bidder_data)




