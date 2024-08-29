def ticket_counter():
    total = 20
    tickets = 0
    buyers = 0

    #Loop ends when tickets run out
    while total >= 0:
        tickets = input("How many tickets would you like to purchase?")
        #Confirm that the selection is allowed
        if tickets <= total and tickets <= 4:
            #Subtract from the total 
            total = total - tickets
            buyers += 1
        #Display when selection is incorrect
        else:
            print("You cannot purchase that amount of tickets. Confirm that you are not trying to buy more than 4 or the remaining tickets")
        print("There are "+total+" tickets remaining.")