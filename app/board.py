import numpy as np

BOARD_SIZE = 22
SNAKES = 'snakes'
FOOD = 'food'


def add_to_board(board, response, datatype):
    val = 0
    if datatype == SNAKES:
        val = -1
        data = []
        for snake in response[SNAKES]['data']:
            data.extend(snake['body']['data'])
    elif datatype == FOOD:
        val = 1
        data = response[FOOD]['data']

    for item in data:
        x = item['x']
        y = item['y']
        board[x][y] = val
    return board


def get_board(response):
    board = np.zeros((BOARD_SIZE, BOARD_SIZE))
    add_to_board(board, response, SNAKES)
    add_to_board(board, response, FOOD)
    return board


if __name__ == '__main__':
    import json
    with open('sample.json') as infile:
        response = json.load(infile)
    print(get_board(response))
