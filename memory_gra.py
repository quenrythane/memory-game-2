import memory


x = 23  # int(input('with how much card do you want to play?: '))
how_much_card = memory.ask_user_how_much_card(x)
list_of_cards = memory.prepare_shuffled_cards(how_much_card)
print('list_of_cards: ', list_of_cards)

number_of_rows_and_columns = memory.count_number_of_rows_and_columns(how_much_card)
print(f'number_of_rows_and_columns: {number_of_rows_and_columns}x{number_of_rows_and_columns}')

empty_board = memory.making_empty_board(number_of_rows_and_columns)
print('empty_board: ', empty_board)


game_board = memory.fill_board(number_of_rows_and_columns, empty_board, list_of_cards, False)
player_board = memory.fill_board(number_of_rows_and_columns, empty_board, list_of_cards, True)
print('game_board: ', game_board)
print('player_board: ', player_board)
