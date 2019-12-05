'''
__________________________________________________________________
Created By: George Shea                                    ßeta
Date Created: 28/11/2019
Version: 1.0
Version Update:

Use:
this program will be a snake ai that plays game perfectly
__________________________________________________________________
'''

from graphics import *
import random
import time

def main():
    print("program has booted up")
    print("please press terminal to avoid typing random nonsense")
    # this is simple game boot up here is the screen
    window = GraphWin( "Snake Game", 500,500)
    window.setCoords(0.0, 0.0, 500, 500)
    window.setBackground('black')


    #
    #
    #
    dx1 = 460
    dy1 = 460
    dx2 = 480
    dy2 = 480

    snake = Rectangle(Point(dx1, dy1), Point(dx2, dy2)).draw(window)
    snake.setFill('green')

    # gives snake the original movement
    direction1 = 0
    direction2 = -20

    # tell you score
    score = Text(Point(10,490), "0").draw(window)
    score.setTextColor('white')
    #
    # this is apple
    #
    apple = Rectangle(Point(240, 240), Point(260, 260)).draw(window)
    apple.setFill('red')
    apple.setOutline('black')

    # this servers to problems
    # 1 just nice for the user to confirm that they are ready
    # 2 the game would run while unable to be interacted with
    text = Text(Point(250,250),"Press To Play").draw(window)
    text.setTextColor('white')
    window.getMouse()
    text.undraw()
    windowOpen = True
    scoreNumb = 0
    while windowOpen == True:

        # gets key input from user w,s,a,d
        move = window.checkKey()

        # this puts the program to sleep so
        # the snake does instianitly kill itself
        time.sleep(.1)

        # resposnible for contunied movement
        snake.move(direction1,direction2)


        if move == 'w':
            # switched direction
            direction1 = 0
            direction2 = 20
        elif move == 's':
            # switched direction
            direction1 = 0
            direction2 = -20
        elif move == 'a':
            # switched direction
            direction1 = -20
            direction2 = 0
        elif move == 'd':
            # switched direction
            direction1 = 20
            direction2 = 0

        # responsible for killing the snake if you hit the borders of screen
        # the noise is so i can see if it hit a wall
        snakeP2 = snake.getP2()
        snakeP2 = str(snakeP2)
        snakeP2 = snakeP2.replace("(", "")
        snakeP2 = snakeP2.replace("Point", "")
        snakeP2 = snakeP2.replace(")", "")
        snakeP2a, snakeP2b = snakeP2.split(",")
        snakeP2a = float(snakeP2a)
        snakeP2b = float(snakeP2b)
        # a is left right wa
        # kill box
        if snakeP2a > 500.0 or snakeP2b < 0 or snakeP2b > 500 or snakeP2a < 0:
            print("program closed down")
            print(snakeP2a, snakeP2b)
            quit()


        # gets snakes location to see if it is near an apple
        snakeP1 = snake.getP1()

        appleP1 = apple.getP1()
        appleP1 = str(appleP1)
        snakeP1 = str(snakeP1)
        # if it hits an apple it will eat it
        if snakeP1 == appleP1:
            # numbers divisable by 20 so apple is not impossible to eat

            # mutiples of 20 could not get random just choice it like that
            appleChoice = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480]
            appleX = random.choice(appleChoice)
            appleY = random.choice(appleChoice)

            scoreNumb = scoreNumb + 1
            scoreNumb = str(scoreNumb)
            score.undraw()
            score = Text(Point(10, 490), scoreNumb).draw(window)
            score.setTextColor('white')

            scoreNumb = int(scoreNumb)

            apple.undraw()
            apple = Rectangle(Point(appleX,appleY), Point(appleX+20,appleY+20)).draw(window)
            apple.setFill('red')

main()
