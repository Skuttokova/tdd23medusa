import pygame,sys
from pygame.locals import *

class Event(object):
    def __init__(self):
        self.state = 1
        self.UP = 1
        self.DOWN = 2
        self.LEFT = 3
        self.RIGHT = 4
        self.direction = self.RIGHT
    def on_event(self,event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.key == pygame.K_s and self.state == 1:
                self.state = 2
            elif event.key == pygame.K_DOWN and self.state != 7:
                if self.state > 1 and self.state < 6:
                    self.state += 1
            elif event.key == pygame.K_UP and self.state != 7:
                if self.state > 2  and self.state < 7:
                    self.state -= 1
            elif event.key == pygame.K_RETURN:
                if self.state == 2:
                    self.state = 7
                elif self.state == 5:
                    self.state = 8
        
                elif self.state == 6:
                    self._running = False

            elif event.key == pygame.K_LEFT and self.direction != self.RIGHT and self.state != 1:
                self.direction = self.LEFT
                print "Left pressed"
            elif event.key == pygame.K_RIGHT and self.direction != self.LEFT:
                self.direction = self.RIGHT
                print "Right pressed"
            elif event.key == pygame.K_UP and self.direction != self.DOWN:
                self.direction = self.UP
                print "Up pressed"
            elif event.key == pygame.K_DOWN and self.direction != self.UP:
                self.direction = self.DOWN
                print "Down pressed"
