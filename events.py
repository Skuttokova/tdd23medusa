import pygame,sys
from pygame.locals import *

class Event(object):
    def __init__(self):
        self.state = 1
    def on_event(self,event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.key == pygame.K_s and self.state == 1:
                self.state = 2
            elif event.key == pygame.K_DOWN:
                if self.state > 1 and self.state < 6:
                    self.state += 1
            elif event.key == pygame.K_UP:
                if self.state > 2  and self.state < 7:
                    self.state -= 1
            elif event.key == pygame.K_RETURN:
                if self.state == 2:
                    self.state = 7
                elif self.state == 5:
                    self.state = 8
        
                elif self.state == 6:
                    self._running = False

