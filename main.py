import pygame, sys
import events
from pygame.locals import *
class Main(events.Event):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._set_image = None
        self._set_start_text = None
        self.visible = False
        self.menu_clock = pygame.time.Clock()
        self.size = self.weight, self.height = 693, 556
        super(Main, self).__init__()
        
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._set_image = pygame.image.load("back.JPG").convert()
        self._set_start_text = pygame.image.load("start").convert()
        self._set_start_text.set_colorkey((255,255,255))
    def on_loop(self):
        pass

    def on_render(self):
        
        if self.state == 1:
            self.state_one()
            
        elif self.state == 2:
            self._display_surf.blit(self._set_image,(0,0))
        
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
        
    def state_one(self):
        self.menu_clock.tick(5)
        if self.visible == True:
            self._display_surf.blit(self._set_image,(0,0))
            self._display_surf.blit(self._set_start_text,(271,500))
            self.visible = False
        else:
            self._display_surf.blit(self._set_image,(0,0))
            self.visible = True
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

        

    
if __name__ == "__main__":
    theMain = Main()
    theMain.on_execute()
