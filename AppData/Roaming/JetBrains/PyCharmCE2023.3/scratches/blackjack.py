import random

def deal_cards():
    card_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_value)
    return card

def compare(my_score, their_score):
    if my_score == their_score:
        print(f"It is a draw. \nYour scores: {my_score}")
        return True
    elif their_score == 0:
        print(f"You lose. Blackjack for them. \nYour score: {my_score}. \nTheir score: {their_score}.")
        return True
    elif my_score > 21:
        print(f"You went over. You lose.\nYour score: {my_score}. \nTheir score: {their_score}.")
        return True
    elif their_score > 21:
        print(f"They went over. You win! \nYour score: {my_score}. \nTheir score: {their_score}.")
        return True
    elif my_score > their_score:
        print(f"You have the greater score. You win! \nYour score: {my_score}. \nTheir score: {their_score}.")
        return True
    elif my_score < their_score:
        print(f"They have the greater score. You lose. \nYour score: {my_score}. \nTheir score: {their_score}.")
        return True
    return False

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

game_over = False
my_cards = []
their_cards = []

for _ in range(2):
    my_cards.append(deal_cards())
    their_cards.append(deal_cards())

while not game_over:
    my_score = calc_score(my_cards)
    their_score = calc_score(their_cards)
    print(f"\nYour cards: {my_cards}.\nCurrent score: {my_score}.")
    print(f"Their first card: {their_cards[0]}.")

    if my_score == 0 or their_score > 21 or my_score > 21 or their_score == 0:
        game_over = True
    else:
        should_deal = input("Type 'y' for another card, 'n' to pass: ")
        if should_deal == 'y':
            my_cards.append(deal_cards())
        else:
            game_over = True

    my_score = calc_score(my_cards)
    their_score = calc_score(their_cards)

while their_score != 0 and their_score < 17:
    their_cards.append(deal_cards())
    their_score = calc_score(their_cards)

game_over = compare(my_score, their_score)
