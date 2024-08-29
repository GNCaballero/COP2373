import random


def responses():
    #Open/create 8ball_responses.txt
    with open("8ball_responses.txt", "w") as file:
        #Write provided responses
        file.write("Yes, of course!\nWithout a doubt, yes.\nYou can count on it.\nFor sure!\nAsk me later!\nI'm not sure.\nI can't tell you right now.\nI'll tell you after my nap.\nNo way!\nI don't think so.\nWithout a doubt, no.\nThe answer is clearly NO!")
    #Read 8ball_responses.txt
    with open("8ball_responses.txt","r") as file:
        #Turn the file into a string
        response_raw = file.read()
        #Split the file by line
        response_list = response_raw.split("\n")
    return response_list

def questions(response_list):
    #Infinitely repeating
    while 0 == 0:
        # Prompt user
        question = input("Ask a yes or no quesion (or type QUIT to end)")
        # Check if user wants to quit
        if question.upper() == "QUIT":
            quit()
        #Display a random response
        else:
            rand = random.randrange(0, len(response_list))
            print(response_list[rand])

response_list = responses()
questions(response_list)