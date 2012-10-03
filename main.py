import pygame, sys
import events
from random import randrange
from pygame.locals import *
class Main(events.Event):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._set_image = None
        self._credit_screen = None
        self._set_start_text = None
        self.visible = False
        self.menu_clock = pygame.time.Clock()
        self.size = self.width, self.height = 800, 600
        self._start_screen = None
        self._menu_screen = None
        self._pts_random = None
        self._rand_nr = None
        self._FPS = 135
        self._snake_coordinate = [(250,250), (260,250)]
        self._move_dict = None
        self._direction = None
        self._cellsize = 10
        self._black = (0,0,0)
        self._green = (0,255,0)
        self._red = (255,0,0)
        self._bgcolor = self._black
        self._image_list = None
        #self._apple = (500,300)
        self._apple = (randrange(10,780), randrange(10,580))
        super(Main, self).__init__()
        
    def on_init(self):
        pygame.init() 
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Medusa')
        self._running = True

        self._set_image = pygame.image.load("start2.png").convert()
        self._start_screen = pygame.transform.scale(self._set_image, (800, 600 ))
        self._set_image = pygame.image.load("meny.png").convert()
        self._menu_screen = pygame.transform.scale(self._set_image, (800, 600 ))
        self._set_image = pygame.image.load("creditScreen.png").convert()
        self._credit_screen = pygame.transform.scale(self._set_image,(800,600))
        self._pts_random = ["pts.png","pts2.png","pts3.png"]
        self._image_list = ["Play.png", "Options.png", "Highscore.png", "Credits.png", "Quit.png", "PlaySelected.png",
                            "OptionsSelected.png", "HighscoreSelected.png", "CreditsSelected.png", "QuitSelected.png",
                            "playBackground.png", "meny.png", "start2.png"]

        

        #Make all images pygame.Surface object and make them transparent
        for i in range (len(self._image_list) -1):
            self._image_list[i] = pygame.image.load(self._image_list[i]).convert()
            self._image_list[i].set_colorkey((255,255,255))
        
    def on_loop(self):
        if self.state == 7:
            print "snake coord 0 0",self._snake_coordinate[0][0] 
            print "self_apple", self._apple
            print "self.apple 0",self._apple[0]
            if self._snake_coordinate[0][0] == -1 or self._snake_coordinate[0][0] == 800 or self._snake_coordinate[0][1] == -1 or self._snake_coordinate[0][1] == 800:
                return
       

            if self._snake_coordinate[0][0]  == self._apple[0] and self._snake_coordinate[0][1]   == self._apple[1]:
                self._apple = (randrange(10,780), randrange(10,580))
            else:
                self._snake_coordinate.pop()
           

            if self.direction == self.UP :
                self._snake_coordinate.insert(0, (self._snake_coordinate[0][0], self._snake_coordinate[0][1] - 1) )
            elif self.direction == self.DOWN:
                self._snake_coordinate.insert(0, (self._snake_coordinate[0][0], self._snake_coordinate[0][1] + 1) )
            elif self.direction == self.LEFT:
                self._snake_coordinate.insert(0, (self._snake_coordinate[0][0] -1, self._snake_coordinate[0][1] ) )
            elif self.direction == self.RIGHT:
                self._snake_coordinate.insert(0, (self._snake_coordinate[0][0] +1, self._snake_coordinate[0][1] ) )

############DETTA FUNKAR EJ          
            for snake_body in self._snake_coordinate[1:]:
                if (self._snake_coordinate[0][0], self._snake_coordinate[0][1] == snake_body):
                    return
#######################################                            
            
            

            
                    

    def game_rules(self):
        if self._snake_coordinate[0][0] == -1 or self._snake_coordinate[0][0] == self.width or self._snake_coordinate[0][1] == self.height:
            return
    
    def on_render(self):
        
        if self.state == 1:
            self.state_startup()
            
        elif self.state == 2:
            self.state_play_selected()
        elif self.state == 3:
            self.state_option_selected()
        elif self.state == 4:
            self.state_highscore_selected()
        elif self.state == 5:
            self.state_credit_selected()
        elif self.state == 6:
            self.state_quit_selected()
        elif self.state == 7:
            self.state_play_game()
        elif self.state == 8:
            self.show_credits()
        self.menu_clock.tick(self._FPS)
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
        
    def state_startup(self):
        self.menu_clock.tick(5)
        self._rand_nr = randrange(3)
        self._set_start_text = pygame.image.load(self._pts_random[self._rand_nr]).convert()
        
        self._set_start_text.set_colorkey((255,255,255))
        if self.visible == True:
            self._display_surf.blit(self._start_screen,(0,0))
            self._display_surf.blit(self._set_start_text,(215,500))
            self.visible = False
        else:
            self._display_surf.blit(self._start_screen,(0,0))
            self.visible = True
        

    #Write all menu item on the background, play will be selected
    def state_play_selected(self):
        self._display_surf.blit(self._menu_screen,(0,0))
        self._display_surf.blit(self._image_list[5],(210,250))
        self._display_surf.blit(self._image_list[1],(210,300))
        self._display_surf.blit(self._image_list[2],(210,350))
        self._display_surf.blit(self._image_list[3],(210,400))
        self._display_surf.blit(self._image_list[4],(210,450))

        #Make play red and Option shown as selected
    def state_option_selected(self):
                
        self._display_surf.blit(self._image_list[0],(210,250))
        self._display_surf.blit(self._image_list[6],(210,300))
        self._display_surf.blit(self._image_list[2],(210,350))

    def state_highscore_selected(self):
                
        self._display_surf.blit(self._image_list[1],(210,300))
        self._display_surf.blit(self._image_list[7],(210,350))
        self._display_surf.blit(self._image_list[3],(210,400))

    def state_credit_selected(self):
        
        self._display_surf.blit(self._image_list[2],(210,350))
        self._display_surf.blit(self._image_list[8],(210,400))
        self._display_surf.blit(self._image_list[4],(210,450))
        
    def state_quit_selected(self):
        
        self._display_surf.blit(self._image_list[3],(210,400))
        self._display_surf.blit(self._image_list[9],(210,450))

    def state_play_game(self):
        self._display_surf.fill(self._bgcolor)
        self.draw_snake()
        self.draw_apple(self._apple)
        pygame.display.flip()

    def show_credits(self):
        self._display_surf.blit(self._credit_screen,(0,0))


        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
                      
            self.on_loop()
            self.on_render()
        self.on_cleanup()

        
    def draw_snake(self):
        for coord in self._snake_coordinate:
            
            x = coord[0] # * self._cellsize
            y = coord[1] # * self._cellsize
            print "x,y",x,y
            self._coord_rect = pygame.Rect(x,y, self._cellsize, self._cellsize)
            pygame.draw.rect(self._display_surf, self._green, self._coord_rect)


    def draw_apple(self,apple):
        
        x = apple[0] 
        y = apple[1] 

        self._apple_rect = pygame.Rect(x,y,self._cellsize,self._cellsize)
        pygame.draw.rect(self._display_surf,self._red,self._apple_rect)
     

if __name__ == "__main__":
    theMain = Main()
    theMain.on_execute()
