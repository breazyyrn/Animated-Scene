from tkinter.constants import S
import graphics as gr 
import random 
import time

def snowman_init(x, y, scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a snowman.
    Minimally, this is just three equal sized circles stack on top of each other
    with two smaller circles for the eyes

    Parameters:
    -----------
    x: int. x coordinate for the top circle center.
    y: int. y coordinate for the top circle center.
    scale: float. Scaled size of the snowman.

    Returns:
    -----------
    list with 5 Zelle Circle objects in it.
    '''
    firstCirle = gr.Circle(gr.Point(x,y), 100 * scale)
    secondCircle = gr.Circle(gr.Point(x,y - (200 * scale)), scale *100)
    thirdCircle = gr.Circle(gr.Point(x, y - (scale * 400)), 100 * scale)
    fourthCircle = gr.Circle(gr.Point(x - (scale * 50), y - (scale * 400)), 10 * scale)
    fifthCircle = gr.Circle(gr.Point(x + (scale * 50), y - (scale * 400)), 10 * scale)
    circleList = [firstCirle, secondCircle, thirdCircle, fourthCircle, fifthCircle]
    return circleList



def snowman_test():
    '''Main function that calls my init function in order to draw my snowman'''

    screen = gr.GraphWin('snowman', 700, 700)

    newList = snowman_init(350, 550, 1)
    for snowman in newList:
        snowman.setOutline('black')
        snowman.setWidth(1)
        snowman.draw(screen)

    # snowman_animate(newList, 2, screen)

    for animation in range(1000):
        snowman_animate(newList, animation, screen)
    
    screen.update()
    screen.getMouse()
    screen.close()


def snowman_animate(shapes, frame, screen):

        if frame % 2 == 0:
            for movingShapes in shapes:
                movingShapes.move(10, -5)

        elif frame % 2 == 1:
            for movingShapes in shapes:
                movingShapes.move(-10, -5)

        time.sleep(0.125)
        screen.update()

        


    # '''Move the snowman at the current iteration of the animation (frame).

    # Parameters:
    # -----------
    # shapes: list with the 5 Zelle Circle objects in it that make up the snowman
    # frame: int. Current iteration of the animation
    # screen: GraphWin. Screen/canvas that the snowman is on.
    #     NOTE: The `screen` is not needed for lab.
    # '''








    # '''Move the snowman at the current iteration of the animation (frame).

    # Parameters:
    # -----------
    # shapes: list with the 5 Zelle Circle objects in it that make up the snowman
    # frame: int. Current iteration of the animation
    # screen: GraphWin. Screen/canvas that the snowman is on.
    #     NOTE: The `screen` is not needed for lab.
    # '''


snowman_test()


