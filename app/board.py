import numpy as np

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
    width = response["width"]
    height = response["height"]
    board = np.zeros((width, height))
    add_to_board(board, response, SNAKES)
    add_to_board(board, response, FOOD)
    return board


def in_bounds(position, board):
    x, y = position
    # check if the position is out of bounds
    width = len(board[0])
    height = len(board)
    if board[x][y] == -1:
        return False
    if x > width-1 or x < 0:
        return False
    if y > height-1 or y < 0:
        return False
    return True


def neighbours(position, board):
    x, y = position
    neighbours = [(x-1, y), (x, y+1), (x, y-1), (x+1, y)]
    return [pos for pos in neighbours if in_bounds(pos, board)]


if __name__ == '__main__':
    import json
    with open('sample.json') as infile:
        response = json.load(infile)
    board = get_board(response)
    print(neighbours((0, 2), board))
