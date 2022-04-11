import time
from tkinter.constants import S, W
from typing import Text
import graphics as gr
import random 
# import simpleaudio as sa



'''My First function used to create my first circle at different scales'''
def compound_init(x, y, scale):
    firstCirle = gr.Circle(gr.Point(x,y), 100 * scale)

    #screen = gr.GraphWin('My Rectangle', 1000, 1000)

    # rectangle = gr.Rectangle(gr.Point(300, 500), gr.Point(0, 400))
    # rectangle.draw(screen)
    # screen.getMouse()
    # rectangle.undraw()

    circleList = [firstCirle]
    return circleList


'''This is used to call my compound test'''
def compound_test():
    # screen = gr.GraphWin('My Rectangle', 1000, 1000)
    # rectangle = gr.Rectangle(gr.Point(300, 500), gr.Point(0, 400))
    # rectangle.draw(screen)
    # screen.getMouse()
    # rectangle.undraw()

    
    screen = gr.GraphWin('My Circle Pattern', 1000, 1000)

    screenRec = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 1000))
    screenRec.setWidth(10)
    screenRec.setOutline('grey')
    screenRec.setFill('black')
    screenRec.draw(screen)
    myWord = gr.Text(gr.Point(500,300), 'Credits')
    mySecondWord = gr.Text(gr.Point(500,400), 'A Production By')
    myThirdWord = gr.Text(gr.Point(500,500), 'Bryan Thiam')
    myFourthWord = gr.Text(gr.Point(500,600), 'New York')
    myFifthWord = gr.Text(gr.Point(500,700), 'Breazy Productions LLC')
    wordList = [myWord,  mySecondWord, myThirdWord, myFourthWord, myFifthWord]

    myImage = gr.Image(gr.Point(200, 400), "bender.jpg")
    mySecondImage = gr.Image(gr.Point(800, 400), "bender.jpg")

    

    imageList = [myImage, mySecondImage]


    for Word in wordList:

        Word.setFace('times roman')
        Word.setStyle('bold')
        Word.setSize(36)
        Word.setTextColor('yellow')
        Word.draw(screen)

    for image in imageList:
        image.draw(screen)

    time.sleep(2)


    for Word in wordList:
        Word.undraw()

    for image in imageList:
        image.undraw()

    
    screenRec.undraw()



    q = compound_init(100, 100, 0.5)
    z = compound_init(100, 100, 1)
    S = compound_init(100, 100, 2)
    r = compound_init(100, 100, 3)
    b = compound_init(100, 100, 4)
    g = compound_init(100, 100, 5)

    # myColor = ['red']
    # yourColor = ['blue']

    for compound in q:
        compound.setFill('purple')
        compound.setOutline('purple')
        compound.setWidth(20)
        compound.draw(screen)


    for compound in z:
        compound.setOutline('blue')
        compound.setWidth(100)
        compound.draw(screen)
        

    for compound in S:
        compound.setOutline('green')
        compound.setWidth(100)
        compound.draw(screen)

    for compound in r:
        compound.setOutline('yellow')
        compound.setWidth(120)
        compound.draw(screen)

    for compound in b:
        compound.setOutline('orange')
        compound.setWidth(140)
        compound.draw(screen)


    for compound in g:
        compound.setOutline('red')
        compound.setWidth(80)
        compound.draw(screen)

        screen.setBackground('sky blue')

        ''''First Building'''
        rectangle = gr.Rectangle(gr.Point(100, 800), gr.Point(250, 400))
        rectangle.move(746, 75)
        rectangle.setFill('grey')
        rectangle.setOutline('brown')
        rectangle.setWidth(8)
        rectangle.draw(screen)


        '''Draws my Second Building'''
        secondBuilding = gr.Rectangle(gr.Point(100, 800), gr.Point(250, 400))
        secondBuilding.move(570, 75)
        secondBuilding.setFill('grey')
        secondBuilding.setOutline('brown')
        secondBuilding.setWidth(8)
        secondBuilding.draw(screen)


        '''Draws my Third Building'''
        thirdBuilding = gr.Rectangle(gr.Point(100, 800), gr.Point(250, 400))
        thirdBuilding.move(394, 75)
        thirdBuilding.setFill('grey')
        thirdBuilding.setOutline('brown')
        thirdBuilding.setWidth(8)
        thirdBuilding.draw(screen)

        '''The following codes are used to create my windows inside my building'''

        windowOne = gr.Rectangle(gr.Point(225, 50), gr.Point(100, 10))
        windowOne.move(759.5, 500)
        windowOne.setFill('tan')
        windowOne.setOutline('tan')
        windowOne.setWidth(2)
        windowOne.draw(screen)

        windowTwo = gr.Rectangle(gr.Point(225, 50), gr.Point(100, 10))
        windowTwo.move(583.5, 500)
        windowTwo.setFill('tan')
        windowTwo.setOutline('tan')
        windowTwo.setWidth(2)
        windowTwo.draw(screen)

        windowThree = gr.Rectangle(gr.Point(225, 50), gr.Point(100, 10))
        windowThree.move(407.5, 500)
        windowThree.setFill('tan')
        windowThree.setOutline('tan')
        windowThree.setWidth(2)
        windowThree.draw(screen)

        windowOneTwo = gr.Rectangle(gr.Point(225, 50), gr.Point(100, 10))
        windowOneTwo.move(759.5, 640)
        windowOneTwo.setFill('tan')
        windowOneTwo.setOutline('tan')
        windowOneTwo.setWidth(2)
        windowOneTwo.draw(screen)

        windowTwoTwo = gr.Rectangle(gr.Point(225, 50), gr.Point(100, 10))
        windowTwoTwo.move(583.5, 640)
        windowTwoTwo.setFill('tan')
        windowTwoTwo.setOutline('tan')
        windowTwoTwo.setWidth(2)
        windowTwoTwo.draw(screen)

        windowThreeTwo = gr.Rectangle(gr.Point(225, 50), gr.Point(100, 10))
        windowThreeTwo.move(407.5, 640)
        windowThreeTwo.setFill('tan')
        windowThreeTwo.setOutline('tan')
        windowThreeTwo.setWidth(2)
        windowThreeTwo.draw(screen)

        windowOneThree = gr.Rectangle(gr.Point(225, 50), gr.Point(100, 10))
        windowOneThree.move(759.5, 780)
        windowOneThree.setFill('tan')
        windowOneThree.setOutline('tan')
        windowOneThree.setWidth(2)
        windowOneThree.draw(screen)

        windowTwoThree = gr.Rectangle(gr.Point(225, 50), gr.Point(100, 10))
        windowTwoThree.move(583.5, 780)
        windowTwoThree.setFill('tan')
        windowTwoThree.setOutline('tan')
        windowTwoThree.setWidth(2)
        windowTwoThree.draw(screen)

        windowThreeThree = gr.Rectangle(gr.Point(225, 50), gr.Point(100, 10))
        windowThreeThree.move(407.5, 780)
        windowThreeThree.setFill('tan')
        windowThreeThree.setOutline('tan')
        windowThreeThree.setWidth(2)
        windowThreeThree.draw(screen)

        windowList = [windowOne, windowTwo, windowThree, windowOneTwo, windowTwoTwo, windowThreeTwo, windowOneThree, windowTwoThree, windowThreeThree]
        buildingList = [rectangle, secondBuilding, thirdBuilding]
        
        '''Creates the eye of ender'''
        oval = gr.Oval(gr.Point(300, 300), gr.Point(480, 400))
        oval.move(500, -300)
        oval.setFill('yellow')
        oval.setOutline('yellow')
        oval.setWidth(12)
        oval.draw(screen)

        # line = gr.Line(gr.Point(1,3), gr.Point(7, 4))
        # line.move(500, -300)
        # # line.setOutline('grey')
        # # line.setwidth(20)
        # line.draw(screen)


        '''Creates the retina of the eye of ender'''
        secondOval = gr.Oval(gr.Point(400, 300), gr.Point(380, 400))
        secondOval.move(500, -300)
        secondOval.setFill('black')
        secondOval.setOutline('black')
        secondOval.draw(screen)

        eyeList = [oval]
        retinaList = [secondOval]



        '''Creates an animation for my windows and my buildings'''

        for animation in range(1000):
            for window in buildingList:
                window.move(0, -6)
                # window.move(random.randint(0, 1), random.randint(-7, 0))
                for window in windowList:
                    window.move(0, -2)
                    # window.move(random.randint(0, 1), random.randint(-7, 0))

            '''Creates an animation for my ender's eye'''
            for window in eyeList:
                window.move(0.5, 0)
            for window in retinaList:
                window.move(0.5, 0)
            if screen.checkMouse() is not None:
                break

    






        screen.getMouse()

        '''Undraws all my shapes after screen is clicked'''
        rectangle.undraw()
        secondBuilding.undraw()
        thirdBuilding.undraw()
        windowOne.undraw()
        windowThree.undraw()
        windowOneTwo.undraw()
        windowTwoTwo.undraw()
        windowThreeTwo.undraw()
        windowOneThree.undraw()
        windowTwoThree.undraw()
        windowThreeThree.undraw()
        oval.undraw()
        secondOval.undraw()
        # windowTwo.undraw()
        screen.close()

# def rectangle():
#     h=600
#     w=600

#     screen = gr.GraphWin('My Rectangle', 1000, 1000)

#     rectangle = gr.Rectangle(gr.Point(300, 500), gr.Point(0, 400))

#     rectangle.setFill('grey')

#     rectangle.setOutline('brown')

#     rectangle.setWidth(8)

#     rectangle.draw(screen)

#     screen.getMouse()

#     rectangle.undraw()


    # rectangle = gr.Rectangle(gr.Point(700, 500), gr.Point(0, 400)







# if __name__ == '__main__':
#     rectangle()
compound_test()


