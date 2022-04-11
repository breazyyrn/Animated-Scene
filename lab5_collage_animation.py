import time
import random

import graphics as gr

def main():
    '''Below I made two different variables for Height and width'''
    h=600
    w=600
    '''Screen made in order to draw my oval'''
    screen = gr.GraphWin('My Oval', width=w, height=h)
    '''Screen made in order to draw my rectangle'''
    screen = gr.GraphWin('My Rectangle', width=w, height=h)
    '''Screen made in order to draw my circle'''
    screen = gr.GraphWin('My Circle', width=w, height=h)

    '''Variable used to create my oval at two different center points'''
    oval = gr.Oval(gr.Point(300,300), gr.Point(480, 400))
    '''Variable used to create my rectangle at two different center points'''
    rectangle = gr.Rectangle(gr.Point(300,500), gr.Point(0,400))
    '''Variable used to create my circle at a center point and its radius'''
    circle = gr.Circle(gr.Point(200,200), 110)

    '''Fills in my oval with a color'''
    oval.setFill('blue')
    oval.setOutline(gr.color_rgb(255, 0, 0))
    oval.setWidth(5)
    '''Fills in my rectangle with a color'''
    rectangle.setFill('purple')
    rectangle.setOutline(gr.color_rgb(0, 255, 0))
    rectangle.setWidth(5)
    '''Fills in my circle with a color'''
    circle.setFill('yellow')
    circle.setOutline(gr.color_rgb(0, 0, 255))
    circle.setWidth(5)
    # circle.setOutline(gr.color('yellow')

    '''Made a variable to organize all my shape in a list 
    in order to be able to draw all of them using 
    one line of code'''
    shape_list = [oval, rectangle, circle]
    for shape in shape_list:
        shape.draw(screen)


    for animation in range(1000):
            for movingShapes in shape_list:
                time.sleep(0.125)
                movingShapes.move(random.randint(-10, 10), random.randint(-10, 10))
                movingShapes.setFill(gr.color_rgb(random.randint(2, 255), random.randint(2, 255), random.randint(2,255)))
                for movingShapes in shape_list:
                    time.sleep(0.125)
                    movingShapes.move(random.randint(-10, 10), random.randint(-10, 10))
                    movingShapes.setFill(gr.color_rgb(random.randint(2, 255), random.randint(2, 255), random.randint(2,255)))
            if screen.checkMouse() is not None:
                break



    # oval.draw(screen)
    # rectangle.draw(screen)
    # circle.draw(screen)

    screen.getMouse()

    oval.undraw()
    rectangle.undraw()
    circle.undraw()

if __name__ == '__main__':
    main()