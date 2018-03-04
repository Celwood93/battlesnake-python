import board
import numpy as np
import bfs

def decideMove(me, snakes, food, options):
	currX = me["body"]["data"][0]['x']
	currY = me["body"]["data"][0]['y']

	move = 'up'
	checkX = None
	checkY = None
	for i in food['data']:
		smallestX = abs(i['x'] - currX)
		if checkX == None or smallestX > checkX:
			smallestX = i['x']
		smallestY = abs(i['y'] - currY)
		if checkY == None or smallestY > checkY:
			smallestY = i['y']
	directionX = currX - smallestX
	directionY = currY - smallestY

	if abs(directionX) > abs(directionY):
		if directionX < 0:
			move = 'right'
		elif directionX > 0:
			move = 'left'
	else:
		if directionY < 0:
			move = 'down'
		elif directionY > 0:
			move = 'up'
	i = 0
	while not checkKill(me, move):
		move = options[i]
		i = i +1
		i = i%4
	return move

def checkKill(me, move):
	currX = me["body"]["data"][0]['x']
	currY = me["body"]["data"][0]['y']
	lastX =  me["body"]["data"][1]['x']
	lastY =  me["body"]["data"][1]['y']
	currDir = 'up'

	dirX = lastX - currX
	dirY = lastY - currY

	if(dirX < 0 ):
		currDir  = "right"
	elif(dirX > 0):
		currDir = "left"
	else:
		if(dirY < 0):
			currDir = "down"
		elif(dirY > 0):
			currDir = "up"
	if currDir == "left" and move == "right":
		return False
	if currDir == "right" and move == "left":
		return False
	if currDir == "down" and move == "up":
		return False
	if currDir == "up" and move == "down":
		return False
	return True

def decideMoveGood(data):
	graph = board.get_board(data)
	currX = data['you']["body"]["data"][0]['x']
	currY = data['you']["body"]["data"][0]['y']
	startP = (currX, currY)

	checkX = None
	checkY = None
	for i in data['food']['data']:
		smallestX = abs(i['x'] - currX)
		if checkX == None or smallestX > checkX:
			smallestX = i['x']
		smallestY = abs(i['y'] - currY)
		if checkY == None or smallestY > checkY:
			smallestY = i['y']
	goalF = (checkX, checkY)

	path = bfs.breadth_first_search(graph, startP, goalF)
	return directionToGo(path, startP)


def directionToGo(path, startP):
	goto = path[0]
	if path[0] == startP:
		goto = path[1]

	dirX = goto[0] - startP[0]
	dirY = goto[1] - startP[1]
	currDir = ""
	if(dirX < 0 ):
		currDir  = "right"
	elif(dirX > 0):
		currDir = "left"
	else:
		if(dirY < 0):
			currDir = "down"
		else:
			currDir = "up"
	return currDir