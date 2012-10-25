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
        self._FPS = 15
        self._green_snake_coordinate = [(5,15), (6,15)]
	self._blue_snake_coordinate = [(5,45), (6,45)]
	self._yellow_snake_coordinate = [(45,45), (46,45)]
	self._cyan_snake_coordinate = [(45,15), (46,15)]
        self._move_dict = None
        self._direction = None
        self._cellsize = 10
	#self._field_height = 300
	#self._field_width = 400 
        self._white = (255,255,255)
        self._black = (0,0,0)
        self._green = (0,255,0)
        self._red = (255,0,0)
	self._blue = (0,0,255)
	self._yellow = (255,255,0)
	self._cyan = (0,255,255)
        self._bgcolor = self._black
        self._image_list = None
        self._score = None
        self._basic_font = None
        self._green_apple = (randrange(1,39), randrange(1,29))
	self._blue_apple = (randrange(1,39), randrange(31,59))
	self._yellow_apple = (randrange(41,79), randrange(31,59))
	self._cyan_apple = (randrange(41,79), randrange(1,29))
	self._green_field = [(5,5),(5,295),(395,295),(395,5)]
	self._blue_field = [(5,305),(5,595),(395,595),(395,305)]
	self._yellow_field = [(405,305),(405,595),(795,595),(795,305)]
	self._cyan_field = [(405,5),(405,295),(795,295),(795,5)]
        super(Main, self).__init__()
        
    def on_init(self):
        pygame.init() 
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Medusa')
        self._running = True

        self._basic_font = pygame.font.Font('freesansbold.ttf',18)
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
       # self._score = len(self._snake_coordinate)
        

        #Make all images pygame.Surface object and make them transparent
        for i in range (len(self._image_list) -1):
            self._image_list[i] = pygame.image.load(self._image_list[i]).convert()
            self._image_list[i].set_colorkey((255,255,255))
        
    def on_loop(self):
        if self.state == 7:
            self._snake_move(self._green_snake_coordinate, self._green_apple)
	    self._snake_move(self._blue_snake_coordinate, self._blue_apple)
	    self._snake_move(self._yellow_snake_coordinate, self._yellow_apple)
	    self._snake_move(self._cyan_snake_coordinate, self._cyan_apple)            
            
    def _snake_move(self, snake_coordinate, apple_color):
	if self._green_snake_coordinate[0][0] < 0 or self._green_snake_coordinate[0][0] >= 39 or self._green_snake_coordinate[0][1] >= 29 or self._green_snake_coordinate[0][1] < 0:
            self.game_over()
            return
	if self._blue_snake_coordinate[0][0] < 0 or self._blue_snake_coordinate[0][0] >= 39 or self._blue_snake_coordinate[0][1] <= 31 or self._blue_snake_coordinate[0][1] >= 59:
            self.game_over()
            return
	if self._cyan_snake_coordinate[0][0] <= 41 or self._cyan_snake_coordinate[0][0] >= 79 or self._cyan_snake_coordinate[0][1] >= 29 or self._cyan_snake_coordinate[0][1] < 0:
            self.game_over()
            return
	if self._yellow_snake_coordinate[0][0] <= 41 or self._yellow_snake_coordinate[0][0] >= 79  or self._yellow_snake_coordinate[0][1] >= 59 or self._yellow_snake_coordinate[0][1] <= 31 :
            self.game_over()
            return

        for snake_body in snake_coordinate[1:]:
            if (snake_coordinate[0][0], snake_coordinate[0][1]) == snake_body:
                 self.game_over()
                 return

        if snake_coordinate[0][0]  == apple_color[0] and snake_coordinate[0][1] == apple_color[1]:
	     if apple_color == self._green_apple:
             	self._green_apple = (randrange(1,39), randrange(1,29))
	     elif apple_color == self._blue_apple:
		self._blue_apple = (randrange(1,39), randrange(31,59))
	     elif apple_color == self._yellow_apple:
		self._yellow_apple = (randrange(41,79), randrange(31,59))
	     elif apple_color == self._cyan_apple:
		self._cyan_apple = (randrange(41,79),randrange(1,29))
        else:
             snake_coordinate.pop()
           

        if self.direction == self.UP :
             snake_coordinate.insert(0, (snake_coordinate[0][0], snake_coordinate[0][1] - 1) )
        elif self.direction == self.DOWN:
             snake_coordinate.insert(0, (snake_coordinate[0][0], snake_coordinate[0][1] + 1) )
        elif self.direction == self.LEFT:
             snake_coordinate.insert(0, (snake_coordinate[0][0] -1, snake_coordinate[0][1] ) )
        elif self.direction == self.RIGHT:
             snake_coordinate.insert(0, (snake_coordinate[0][0] +1, snake_coordinate[0][1] ) )
    
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
        elif self.state == 9:
            self.display_highscore()
        elif self.state == 10:
            self.option_enter(self._FPS)
        elif self.state == 11:
            self.game_over()
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
	self._draw_fields()
        self.draw_snake(self._green_snake_coordinate, self._green)
	self.draw_snake(self._blue_snake_coordinate, self._blue)
	self.draw_snake(self._yellow_snake_coordinate, self._yellow)
	self.draw_snake(self._cyan_snake_coordinate, self._cyan)
        self.draw_apple(self._green_apple)
	self.draw_apple(self._blue_apple)
	self.draw_apple(self._yellow_apple)
	self.draw_apple(self._cyan_apple)
        self.draw_score(len(self._green_snake_coordinate)+len(self._blue_snake_coordinate)+len(self._yellow_snake_coordinate)+len(self._cyan_snake_coordinate)-8)
        pygame.display.flip()




    def game_over(self):
        self._score = (len(self._green_snake_coordinate)+len(self._blue_snake_coordinate)+len(self._yellow_snake_coordinate)+len(self._cyan_snake_coordinate)-8)
       
        self.create_highscore(self._score)
#        self.state = 1
#        self.__init__()
###DONT WORK


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

        
    def draw_snake(self, snake_coordinate, color):
        for coord in snake_coordinate:
            
            x = coord[0]  * self._cellsize
            y = coord[1]  * self._cellsize
            self._coord_rect = pygame.Rect(x,y, self._cellsize, self._cellsize)
            pygame.draw.rect(self._display_surf, color, self._coord_rect)

    def _draw_fields(self):
        pygame.draw.lines(self._display_surf, self._green, True, self._green_field, 10)
        pygame.draw.lines(self._display_surf, self._blue, True, self._blue_field, 10)
	pygame.draw.lines(self._display_surf, self._cyan, True, self._cyan_field, 10)
	pygame.draw.lines(self._display_surf, self._yellow, True, self._yellow_field, 10)

    def draw_apple(self,apple):
        
        x = apple[0] * self._cellsize
        y = apple[1] * self._cellsize

        self._apple_rect = pygame.Rect(x,y,self._cellsize,self._cellsize)
        pygame.draw.rect(self._display_surf,self._red,self._apple_rect)

    def draw_score(self,score):
        self._score_surf = self._basic_font.render('Score: %s' %(score), True, self._white)
        self._score_rect = self._score_surf.get_rect()
        self._score_rect.topleft = (10,10)
        self._display_surf.blit(self._score_surf, self._score_rect)


    def create_highscore(self,score):
        with open('hscore.txt','a') as f:
            f.write(str(score))
            f.write('\n')
        f.close()
        return


    def display_highscore(self):
        f = open('hscore.txt','r')

        
        self._display_surf.fill(self._black)
        for index,line in enumerate(f.readlines()):
            line = line.split("\n")[0]
            self._score_surf = self._basic_font.render('%s,' %(line), True, self._white)
            self._score_rect = self._score_surf.get_rect()
            self._score_rect.left = 20 * index
            
            self._display_surf.blit(self._score_surf, self._score_rect)
        
    def write_game_over(self):

        self._score_surf = self._basic_font.render(' %s' %('Game over'), True, self._white)
        self._score_rect = self._score_surf.get_rect()
        self._score_rect.topright = (10,10)
        self._display_surf.blit(self._score_surf, self._score_rect)



    def option_enter(self,fps):

        self._display_surf.fill(self._black)

        self._text_surf = self._basic_font.render('FPS: %s' %(fps), True, self._white)
        self._text_rect = self._text_surf.get_rect()
        self._text_rect.left = 10
        self._display_surf.blit(self._text_surf, self._text_rect)



if __name__ == "__main__":
    theMain = Main()
    theMain.on_execute()
