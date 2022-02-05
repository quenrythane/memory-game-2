import random


# user write how how much card want?
def ask_user_how_much_card(int):
    how_much_card = 0
    while not(0 < how_much_card <= 100):  # użytkownik może wybrać od 1 do 100 kart. Jeśli wybierze inaczej, pętla będzie go dalej odpytywać
        try:
            how_much_card = int  # int(input('with how much card do you want to play?: '))
        except TypeError:
            print('Sorry, but the number must be between 1 and 100 and be integer \n')

    # inform player with number of card he will plays with
    if how_much_card % 2 != 0:
        how_much_card -= 1
        print("The number of cards couldn't be odd. I'll fix it for you and set this number to", how_much_card)
    print(f"You'll be playing with {how_much_card} cards")
    return how_much_card


# prepare shuffled cards
def prepare_shuffled_cards(how_much_card):
    list_of_cards = [n for n in range(1, int(how_much_card/2)+1)] * 2
    random.shuffle(list_of_cards)
    return list_of_cards


# count number of rows and columns (square shape)
def count_number_of_rows_and_columns(how_much_card):
    x = how_much_card ** (1/2)
    if x != int(x):
        number_of_rows_and_columns = int(x) + 1
    else:
        number_of_rows_and_columns = x
    return number_of_rows_and_columns


"""
dotąd działa    dotąd działa    dotąd działa    dotąd działa    
dotąd działa    dotąd działa    dotąd działa    dotąd działa    
dotąd działa    dotąd działa    dotąd działa    dotąd działa    
"""

# szykuje plansze
def making_empty_board(number_of_rows_and_columns):
    empty_board = []
    [empty_board.append([]) for x in range(number_of_rows_and_columns)]
    return empty_board


def fill_board(number_of_rows_and_columns, empty_board, list_of_cards):
    board = empty_board
    for i, card in enumerate(list_of_cards):
        board[i // number_of_rows_and_columns].append(card)

    # tutaj sprawdzam czy ostatni z wierszy jest pusty i jeśli tak, to go usuwam (po co ma śmiecić?)
    board.pop() if board[-1] == [] else board

    return board


def making_user_board(number_of_rows_and_columns, list_of_cards):
    global user_board
    user_board = []
    [user_board.append([]) for x in range(number_of_rows_and_columns)]
    for i, card in enumerate(list_of_cards):
        user_board[i // number_of_rows_and_columns].append('X')
    return user_board


"""
pracuje nad tym     pracuje nad tym     pracuje nad tym     pracuje nad tym     pracuje nad tym     
pracuje nad tym     pracuje nad tym     pracuje nad tym     pracuje nad tym     pracuje nad tym     
pracuje nad tym     pracuje nad tym     pracuje nad tym     pracuje nad tym     pracuje nad tym     
"""


# rozkłada karty na planszy
def deals_the_cards_on_board(number_of_rows_and_columns, list_of_cards):
    for i, card in enumerate(list_of_cards):
        board[i // number_of_rows_and_columns].append(card)


# wyświetla plansze w konsoli
def show_the_board(board_name):
    [print(board[i]) for i in range(len(board_name))]



