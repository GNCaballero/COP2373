import random

class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

def redraw(my_deck, save_point):
    #prompt for user input
    my_deck.cards_in_play_list = save_point.copy()
    valid_numbers = {'1','2','3','4','5'}
    num_discard = 0
    previous_num = []
    previous_num.clear()
    discard = input(f"\nIf you want to discard any cards, please type their corresponding number. Alternatively, if you want a brand new hand, just type 'new'. Additionally, if you want to keep your hand, type 'keep':\n")
    if discard.lower() == 'new':
        num_discard = 5
    elif any(char.isdigit() for char in discard):
        if any(char in valid_numbers for char in discard):
            for char in discard:
                if char.isdigit():
                    if char in valid_numbers:
                        num = int(char) - 1 
                        for previous in previous_num:
                            if num == previous:
                                print("No duplicate numbers")
                                return redraw(my_deck, save_point)
                            if num > previous:
                                num -= 1
                        card = my_deck.cards_in_play_list.pop(num)  
                        my_deck.discards_list.append(card)
                        previous_num.append(num)  
                        num_discard += 1
                    else:
                        print("Invalid Number. Try Again")
                        return redraw(my_deck, save_point)
    elif discard.lower() == 'keep':
        print("Keeping hand")
    else:
        print("Invalid Input. Try Again.")
        return redraw(my_deck, save_point)
    
    return num_discard
    

def play():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9','10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades' ]
    my_deck = Deck(52)
    #initial hand
    for i in range(5):
        d = my_deck.deal()
        r = d % 13
        s = d // 13
        print(i+1,'. ',ranks[r], 'of', suits[s])
    print()
    
    save_point = my_deck.cards_in_play_list
    num_discard = redraw(my_deck, save_point)
    kept_cards = my_deck.cards_in_play_list[:5 - num_discard]
    print("Final Hand:")
    #print new values
    for i in range(5-num_discard):
        d = kept_cards[i]
        r = d % 13
        s = d // 13
        print(i+1,'. ',ranks[r], 'of', suits[s])
    
    for i in range(num_discard):
        d = my_deck.deal()
        r = d % 13
        s = d // 13
        print(i + 1 + (5 - num_discard), '. ', ranks[r], 'of', suits[s])
    print()

play()