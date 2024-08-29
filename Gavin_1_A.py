from logging import exception

total = 20
tickets = 0

def ticket_counter(total):
    #There are zero buyers initially
    buyers = 0
    #Loop ends when tickets run out
    while total > 0:
        try:
            tickets = int(input("How many tickets would you like to purchase?"))
            #Confirm that the selection is allowed
            if tickets <= total and tickets <= 4:
                # Subtract from the total
                total = total - tickets
                buyers += 1
            # Display when selection is incorrect
            else:
                print("You cannot purchase that amount of tickets. Confirm that you are not trying to buy more than 4 or the remaining tickets")
            #Display remaining tickets
            print("There are "+str(total)+" tickets remaining.")
        except ValueError:
            #Confirm input is an int
            print("Please input an integer")
    print ("All tickets sold")
    return buyers
buyers = ticket_counter(total)
#Display amount of buyers
print("There have been "+str(buyers)+" individual buyers")