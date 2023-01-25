############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art

# deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# ******************************************************
def restart_game():
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer == 'y':
        return True
    else:
        return False


# *****************************************************

# function for random card
def randomise_card():
    random_card = random.choice(cards)
    return random_card


# *****************************************************

# calculating scores
def score_calc(hand):
    score = 0
    ace_flag = 0
    for card in hand:
        if card != 11:
            score += card
        else:
            # what if it is an Ace
            if score < 11:
                score += card
                ace_flag += 1
            # means that score is 11 and above
            else:
                score += 1

        # if score is above 21 and there are Aces
    while (score > 21 and ace_flag > 0):
        score -= 10
        ace_flag -= 1

    return score


# *********************************************
def computer_draw(computer_hand):
    draw_flag = True
    while (draw_flag):
        rand_card_draw = randomise_card()
        computer_hand.append(rand_card_draw)

        score_computer = score_calc(computer_hand)

        # if score_computer < 17  --> computer draws a card
        if score_computer < 17:
            draw_flag = True
        else:
            draw_flag = False

    return computer_hand


# *********************************************

# final printing function
def print_final(my_hand, my_score, comp_hand, score_comp, flag):
    print(f"Your final hand: {your_hand}, final score: {score_player}")
    print(f"Computer's final hand: {computer_hand}, final score: {score_computer}")
    if flag == 1 and score_player == 21:
        print("You win with Blackjack😎")
    elif flag == 1 and score_player != 21:
        print("You lost. Opponent has Blackjack 😱")
    elif score_player > 21:
        print("You went over. You lose 😭")
    elif score_computer > 21:
        print("Opponent went over. You win 😁")
    elif score_player > score_computer:
        print("You win 😁")
    elif score_player == score_computer:
        print("It's a Draw 🙃")
    else:
        print("You lose 😤")


# -------------------------------------------------------------------------------------------------------
# let the game begin
while (restart_game()):
    # print logo
    print(art.logo)

    # draw random cards for starting the game
    rand_card1 = randomise_card()
    rand_card2 = randomise_card()
    rand_card_comp1 = randomise_card()
    rand_card_comp2 = randomise_card()
    # Creating the hands
    your_hand = [rand_card1, rand_card2]
    computer_hand = [rand_card_comp1, rand_card_comp2]

    # calculating the score
    score_player = score_calc(your_hand)
    score_computer = score_calc(computer_hand)
    # printing the beginning of the game
    print(f"Your cards:[{rand_card1},{rand_card2}], current score: {score_player}")
    print(f"Computer's first card: {rand_card_comp1}")

    # while loop to keep drawing cards for player
    blackjack = 0
    draw_flag = True
    if score_computer == 21 or score_player == 21:
        blackjack = 1
        if score_player == 21 and score_computer < 17:
            computer_hand = computer_draw(computer_hand)
            score_computer = score_calc(computer_hand)
        print_final(your_hand, score_player, computer_hand, score_computer, blackjack)
        draw_flag = False

    while draw_flag:
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw == 'y':
            # draw another card
            rand_card_draw = randomise_card()
            your_hand.append(rand_card_draw)
            score_player = score_calc(your_hand)

            print(f"Your cards:[{your_hand}], current score: {score_player}")
            print(f"Computer's first card: {rand_card_comp1}")
            # if score is > 21
            if score_player > 21:
                # exit the while loop
                draw_flag = False
            # if score is =< 21
            else:
                # re-enter the while loop
                draw_flag = True
        else:
            # exit the while loop
            draw_flag = False

    # -------------------------------------------------------------------------------------------------------
    # while loop for computer
    if blackjack == 0:
        if score_computer < 17:
            computer_hand = computer_draw(computer_hand)
            score_computer = score_calc(computer_hand)
        print_final(your_hand, score_player, computer_hand, score_computer, blackjack)
# ----------------------------------------------------------------------------------------------
# When the player doesn't want to play anymore
print("Goodbye")
