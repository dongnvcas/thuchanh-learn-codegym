from turtle import *
from datetime import datetime
from math import sin, cos, pi

def drawClock():
    # disable the tracer while we are updating the clock, to avoid flicker.
    tracer(False)
    # Only clear before drawing each clock face, not before each hand.
    # We want to be able to see all the hands at once.
    clear()
    now = datetime.now()
    # Provide the position as a value from 0..1 instead of 0..60.
    # The logic is simpler this way.
    drawHand(now.hour / 12, 4, 60)
    drawHand(now.minute / 60, 3, 80)
    drawHand(now.second / 60, 1, 80)
    # restore the tracer so that all the drawing is shown on screen.
    tracer(True)
    # Set up the next drawing.
    # We want to know how long until the *next* second, *after drawing*
    # So, we need to call `datetime.now` again, and not use the old value
    # The `datetime` object tells us how many microseconds have passed
    # since the beginning of the second. We divide by 1000 to convert that
    # to milliseconds.
    until_next_second = 1000 - int(datetime.now().microsecond / 1000)
    ontimer(drawClock, until_next_second)

def drawHand(hand, thickness, length):
    pensize(thickness)
    # The sin and cos functions require a value in radians, not degrees.
    goto(sin(2 * pi * hand) * length, cos(2 * pi * hand) * length)
    # It's okay if we retrace the line without lifting the pen.
    goto(0, 0)
    # We don't really need to "restore" any turtle state afterward,
    # because the next call will just change it again anyway.

color("black")
hideturtle()
title("Clock")
speed(0)
drawClock()
done()

