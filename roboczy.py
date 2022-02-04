cards = [8, 3, 1, 2, 4, 9, 1, 3, 7, 5, 10, 5, 6, 2, 6, 7, 10, 4, 9, 8]

board = [[], [], [], [], []]
for i, card in enumerate(cards):
    board[i // 5].append(card)

print(board)



