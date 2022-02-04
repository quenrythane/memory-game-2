import random

# user write how how much card want?
how_much_card = 0
while not(0 < how_much_card <= 100):
    try:
        how_much_card = 20  # int(input('with how much card do you want to play?: '))
    except TypeError:
        print('Sorry, but the number must be between 1 and 100 and be integer \n')

# inform player with number of card he will plays with
if how_much_card % 2 != 0:
    how_much_card -= 1
    print("The number of cards couldn't be odd. I'll fix it for you and set this number to", how_much_card)
print(f"You'll be playing with {how_much_card} cards")


# count number of rows and columns (square shape)
x = how_much_card ** (1/2)
if x != int(x):
    number_of_rows_and_columns = int(x) + 1
else:
    number_of_rows_and_columns = x
print('number_of_rows_and_columns: ', number_of_rows_and_columns)

""""""
# prepare shuffled cards
list_of_cards = [n for n in range(1, int(how_much_card/2)+1)] * 2
random.shuffle(list_of_cards)


# szykuje plansze
def making_board(number_of_rows_and_columns):
    global board
    board = []
    for x in range(number_of_rows_and_columns):
        board.append([])
    return board


# rozkłada karty na planszy
def deals_the_cards_on_board(number_of_rows_and_columns, list_of_cards):
    for i, card in enumerate(list_of_cards):
        board[i // number_of_rows_and_columns].append(card)


def inside_the_board():
    [print(board[i]) for i in range(len(board))]

def show_the_board():
    [print('x') for i in range(len(board))]



making_board(number_of_rows_and_columns)
deals_the_cards_on_board(number_of_rows_and_columns, list_of_cards)
inside_the_board()
show_the_board()



