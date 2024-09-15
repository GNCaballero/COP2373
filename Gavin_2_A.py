spam_likely = []

#Create list of Spam-likely words
def spam_words():
    #Open/create spam_words.txt
    with open("spam_words.txt",'w') as file:
        file.write("Free\nWin\nCongratulations\nUrgent\nLimited time\nAct now\nOffer\nDeal\nGuaranteed\nRisk-free\nClick here\nOrder now\n100% free\nExclusive\nBonus\nPrize\nGift\nWinner\nClaim\nInstant\nMoney-back\nCash\nCredit\nEarn\nBuy now\nApply now\nCheap\nMiracle\nInvestment\nDiscount")
    #Read spam_words.txt
    with open("spam_words.txt","r") as file:
        #Turn the file into a string
        spam_raw = file.read().lower()
        #Split the file by line
        spam_list = spam_raw.split("\n")
    return spam_list

#Score User's input
def spam_checker(spam_list):
    spam_score=0
    user_txt = input("Enter text to check likelihood of it being spam:")
    #Loop goes through each word in the spam likely
    for word in spam_list:
        #Check for words in the spam words
        if word in user_txt.lower():
            spam_score += 1
            #Save the words that are spam likely
            spam_likely.append(word)
    return spam_score

spam_list = spam_words()
spam_score = spam_checker(spam_list)
#
if spam_score > 4:
    spam = "likely"
else: spam = "not likely"
print("This message is "+spam+" spam. It has a spam score of "+str(spam_score)+". The words or phrases that are spam-likely are as follows:\n"+str(spam_likely))