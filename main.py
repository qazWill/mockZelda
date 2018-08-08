'''
This game takes place almost seven
years after majoras mask.
'''

# necessary imports
import pygame, sys, math, random, os #, easygui

# modules that I have made
import objects, story, menu

#initializes pygame
pygame.init()

class NewLink:
    '''The main character of this game.'''
    
    def __init__(self):
        '''Creates Link.'''
        
        # determines how big link will be
        size = 1.5
        
        # walking down images
        self.walk_down = [] 
        for i in range(1, 12):
            image = pygame.image.load("images/link/walk_down/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            self.walk_down.append(image)
            
        # walking up images
        self.walk_up = [] 
        for i in range(1, 12):
            image = pygame.image.load("images/link/walk_up/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            image.convert()
            self.walk_up.append(image)
            
        # walking right and left images
        self.walk_right = [] 
        self.walk_left = []
        for i in range(1, 12):
            image = pygame.image.load("images/link/walk_right/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            image.convert()
            self.walk_right.append(image)
            image = pygame.transform.flip(image, 1, 0)
            self.walk_left.append(image)
            
        # rolling down images
        self.roll_down = [] 
        for i in range(1, 8):
            image = pygame.image.load("images/link/roll_down/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            image.convert()
            self.roll_down.append(image)
            
        # rolling up images
        self.roll_up = [] 
        for i in range(1, 8):
            image = pygame.image.load("images/link/roll_up/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            image.convert()
            self.roll_up.append(image)
            
        # rolling right and left images
        self.roll_right = [] 
        self.roll_left = []
        for i in range(1, 8):
            image = pygame.image.load("images/link/roll_right/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            image.convert()
            self.roll_right.append(image)
            image = pygame.transform.flip(image, 1, 0)
            self.roll_left.append(image)
        
        # slice down images
        self.slice_down = [] 
        for i in range(0, 8):
            image = pygame.image.load("images/link/slice_down/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            self.slice_down.append(image)
            
        # slice up images
        self.slice_up = [] 
        for i in range(0, 8):
            image = pygame.image.load("images/link/slice_up/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            image.convert()
            self.slice_up.append(image)
            
        # slicing right and left images
        self.slice_right = [] 
        self.slice_left = []
        for i in range(0, 8):
            image = pygame.image.load("images/link/slice_right/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            image.convert()
            self.slice_right.append(image)
            image = pygame.transform.flip(image, 1, 0)
            self.slice_left.append(image)
            
        # game over fall
        self.game_over = [] 
        for i in range(1, 15):
            image = pygame.image.load("images/link/game_over/" + str(i) + ".png")
            image.set_colorkey((125, 41, 130), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size)
            for i in range(0, 8):
                self.game_over.append(image)

        # image related attributes
        self.delay = 0
        self.end = 2
        self.image = 0
        self.images = self.walk_down
        self.rect = self.images[self.image].get_rect()
        self.rect.center = [400, 500]
        
        # collected items
        self.collected_heart_pieces = []
        
        # other attributes
        self.room = [0, 0]
        self.health = 3
        self.health_fraction = 0
        self.max_health = 3
        self.near_sign = False
        self.reading = False
        self.progress = 0
        self.rolling = False
        self.direction = [0, 1]
        self.moving = False
        self.items = []
        
    def move(self, sounds):
        '''Cycles through links images as well as altering his position.'''
        
        # returns a list of what keys are pressed
        pressed = pygame.key.get_pressed()
        
        # moving left, right, up, and down
        if self.rolling != True:
            self.moving = True
            if pressed[pygame.K_s]:
                if self.images == self.walk_down:
                    self.rect.top = self.rect.top + 3
                else:
                    self.direction = [0, 1]
                    self.images = self.walk_down
                    self.image = 0
                    self.delay = 0
                    self.end = 2
            elif pressed[pygame.K_w]:
                if self.images == self.walk_up:
                    self.rect.top = self.rect.top - 3
                else:
                    self.direction = [0, -1]
                    self.images = self.walk_up
                    self.image = 0
                    self.delay = 0
                    self.end = 2
            elif pressed[pygame.K_d]:
                if self.images == self.walk_right:
                    self.rect.left = self.rect.left + 3
                else:
                    self.direction = [1, 0]
                    self.images = self.walk_right
                    self.image = 0
                    self.delay = 0
                    self.end = 2
            elif pressed[pygame.K_a]:
                if self.images == self.walk_left:
                    self.rect.left = self.rect.left - 3
                else:
                    self.direction = [-1, 0]
                    self.images = self.walk_left
                    self.image = 0
                    self.delay = 0 
                    self.end = 2 
            
            # when link isn't moving
            else:
                self.moving = False
                if pressed[pygame.K_LEFT] or self.images == self.slice_down or self.images == self.slice_up or self.images == self.slice_left or self.images == self.slice_right:
                    if self.direction == [0, 1] and self.images != self.slice_down:
                        sounds.slice.play()
                        self.images = self.slice_down
                        self.image = 0
                        self.delay = 0
                        self.end = 2
                    if self.direction == [0, -1] and self.images != self.slice_up:
                        sounds.slice.play()
                        self.images = self.slice_up
                        self.image = 0
                        self.delay = 0
                        self.end = 2
                    if self.direction == [1, 0] and self.images != self.slice_right:
                        sounds.slice.play()
                        self.images = self.slice_right
                        self.image = 0
                        self.delay = 0
                        self.end = 2
                    if self.direction == [-1, 0] and self.images != self.slice_left:
                        sounds.slice.play()
                        self.images = self.slice_left
                        self.image = 0
                        self.delay = 0
                        self.end = 2
                else:
                    self.image = 0
                    self.delay = 0
                
        else:
            if self.moving == True:
                if self.direction == [0, 1]:
                    self.images = self.roll_down
                    self.rect.top = self.rect.top + 5
                elif self.direction == [0, -1]:
                    self.images = self.roll_up
                    self.rect.top = self.rect.top - 5
                elif self.direction == [1, 0]:
                    self.images = self.roll_right
                    self.rect.left = self.rect.left + 5
                elif self.direction == [-1, 0]:
                    self.images = self.roll_left
                    self.rect.left = self.rect.left - 5
                else:
                    self.rolling = False

         
        # cycles through link images
        self.delay = self.delay + 1
        if self.delay > self.end:
            self.delay = 0
            self.image = self.image + 1
            if self.image > len(self.images) - 1:
                if self.rolling:
                    self.rolling = False
                    if self.direction == [0, 1]:
                        self.images = self.walk_down
                    if self.direction == [0, -1]:
                        self.images = self.walk_up
                    if self.direction == [1, 0]:
                        self.images = self.walk_right
                    if self.direction == [-1, 0]:
                        self.images = self.walk_left
                        
                if self.images == self.slice_down or self.images == self.slice_up or self.images == self.slice_left or self.images == self.slice_right:
                    if self.direction == [0, 1]:
                        self.rect
                        self.images = self.walk_down
                    if self.direction == [0, -1]:
                        self.images = self.walk_up
                    if self.direction == [1, 0]:
                        self.images = self.walk_right
                    if self.direction == [-1, 0]:
                        self.images = self.walk_left
                
                self.image = 0
                
        image = self.images[self.image]
        rect = image.get_rect()
        if self.images == self.slice_down or self.images == self.slice_up or self.images == self.slice_left or self.images == self.slice_right:
            if self.direction == [0, 1]:
                rect.left, rect.top = self.rect.left, self.rect.top
            if self.direction == [0, -1]:
                rect.right, rect.bottom = self.rect.right, self.rect.bottom
            if self.direction == [1, 0]:
                rect.left, rect.centery = self.rect.left, self.rect.centery
            if self.direction == [-1, 0]:
                rect.right, rect.centery = self.rect.right, self.rect.centery
        else:
            rect.center = self.rect.center
            rect.bottom = self.rect.bottom
        self.rect = rect
    
    def add_health(self):
        '''Can add to links health.'''
        
        self.health = self.health + 1
        if self.health > self.max_health:
            self.health = self.max_health
            self.health_fraction = 0
            
    def sub_health(self):
        '''Can subtract from links health.'''
        
        self.health_fraction = self.health_fraction - 1
        if self.health_fraction < 0:
            self.health_fraction = 3
            self.health = self.health - 1
            
                
    def display_hearts(self, screen):
        '''Displays the hearts in the top left side of the screen.'''
        
        i = 0
        for i in range(0, int(self.health)):
            heart = pygame.image.load("images/menu/hearts/4.png").convert()
            heart.set_colorkey((111, 49, 152))
            screen.blit(heart, [i * 18 + 5, 5])  
        if self.health < self.max_health:
            heart = pygame.image.load("images/menu/hearts/" + str(int(self.health_fraction)) + ".png").convert()
            heart.set_colorkey((111, 49, 152))
            screen.blit(heart, [i * 18 + 23, 5])
            difference = self.max_health - self.health
            i = i + 1
            if self.health_fraction != 0:
                difference = difference - 1
                i = i + 1
            for not_i in range(i, int(difference) + i):
                heart = pygame.image.load("images/menu/hearts/0.png").convert()
                heart.set_colorkey((111, 49, 152))
                screen.blit(heart, [not_i * 18 + 5, 5])
                
    def change_room(self, navi):
        '''Checks to see if link has moved into a different room.'''
                
        # allows link to move into different rooms
        if self.rect.bottom < 0:
            self.room[1] = self.room[1] - 1
            self.rect.top = 600
            if navi.out:
                navi.position[1] = 640
                navi.rect.top = navi.position[1]
                navi.dust_list = []
            return True
        elif self.rect.top > 600:
            self.room[1] = self.room[1] + 1
            self.rect.bottom = 0
            if navi.out:
                navi.position[1] = -40
                navi.rect.top = navi.position[1]
                navi.dust_list = []
            return True
        elif self.rect.right < 0:
            self.room[0] = self.room[0] - 1
            self.rect.left = 800
            if navi.out:
                navi.position[0] = 840
                navi.rect.left = navi.position[1]
                navi.dust_list = []
            return True
        elif self.rect.left > 800:
            self.room[0] = self.room[0] + 1
            self.rect.right = 0
            if navi.out:
                navi.position[0] = -40
                navi.rect.left = navi.position[1]
                navi.dust_list = []
            return True
        else:
            return False
                
class NewFairy:
    '''The fairy that follows link around.'''
    
    def __init__(self):
        '''Creates Navi.'''
        
        # images
        self.images = [] 
        for i in range(1, 4):
            image = pygame.image.load("images/navi/" + str(i) + ".png").convert()
            image.set_colorkey((0, 0, 0))
            self.images.append(image)

        # image related attributes
        self.delay = 0
        self.image = 0
        self.rect = self.images[self.image].get_rect()
        self.rect.left, self.rect.top = [400, 450]
        self.position = [400, 450]
        
        # other atributes
        self.out = True
        self.dust = pygame.image.load("images/navi/dust.png").convert()
        self.dust_delay = 0
        self.fly = False
        self.dust.set_colorkey((0, 0, 0))
        self.dust_list = []
        self.angle = 0
        self.lines = ["Navi:",
        "Come on hurry up!  Don't you want to get back to Hyrule?"]
        
    def move(self, screen, link, sounds):
        '''Cycles through navi's images as well as altering her position.'''
         
        # cycles through link images
        self.delay = self.delay + 1
        if self.delay > 8:
            self.delay = 0
            self.image = self.image + 1
            if self.image > 2:
                self.image = 0
            
        # determines how long until next dust is blitted
        self.dust_delay = self.dust_delay + 1
        if self.dust_delay > 2 and self.fly:
            self.dust_delay = 0
            x = random.randint(-5, 10)
            y = random.randint(-5, 10)
            self.dust_list.append([[self.rect.left + x, self.rect.top + y], 255])
               
        # handels the dust
        for dust in self.dust_list:
            dust[1] = dust[1] - 1
            if dust[1] < 200:
                dust[1] = dust[1] - 3
            image = self.dust
            image.set_alpha(dust[1])
            screen.blit(image, dust[0])
            if dust[1] <= 1:
                self.dust_list.remove(dust)
            
        # moves navi to link
        self.fly = False
        if self.rect.bottom < link.rect.top - 5 or self.rect.top > link.rect.bottom + 5 or self.rect.left > link.rect.right + 5 or self.rect.right < link.rect.left - 5:
            self.fly = True
            angle = -math.degrees(math.atan2(self.rect.centerx - link.rect.centerx, self.rect.centery - link.rect.centery)) - 90
            x = math.cos(math.radians(angle)) * 2
            y = math.sin(math.radians(angle)) * 2
            self.position[0] = self.position[0] + x
            self.position[1] = self.position[1] + y
            self.rect.left, self.rect.top = [int(self.position[0]), int(self.position[1])]
        if self.rect.centery < link.rect.centery + 10 and self.rect.centery > link.rect.centery - 10 and self.rect.left < link.rect.right and self.rect.right > link.rect.left:
            self.out = False
            self.dust_list = []
            sounds.navi_in.play()
            
class NewButton:
    '''Buttons on the top section of screen.'''
    
    def __init__(self, position, text):
        '''Creates the button.'''
        
        # image and rect
        self.image = pygame.image.load("images/menu/buttons/top button.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.set_alpha(150)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        font = pygame.font.Font(None, 17)
        self.text = text
        self.name = font.render(text, 1, (255, 255, 255))
        
        # sounds
        self.mouse_over_sound = pygame.mixer.Sound("sounds/menu/mouse over.wav")
        self.mouse_over_sound.set_volume(1.00) 
        self.select_sound = pygame.mixer.Sound("sounds/menu/select.wav")
        self.select_sound.set_volume(1.00) 
        self.mouse_over = False
    
    def display(self, screen):
        '''Displays the button.'''
        
        # displays the button
        screen.blit(self.image, self.rect)
        self.rect.left = self.rect.left + 20      
        self.rect.top = self.rect.top + 0
        screen.blit(self.name, self.rect)
        self.rect.left = self.rect.left - 20
        self.rect.top = self.rect.top - 0
        
        # determines whether the button is clicked on or not
        pressed = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if x > self.rect.left and x < self.rect.right and y > self.rect.top and y < self.rect.bottom:
            self.image = pygame.image.load("images/menu/buttons/shaded top button.png").convert()
            self.image.set_colorkey((255, 255, 255))
            self.image.set_alpha(150)
            if not self.mouse_over:
                self.mouse_over = True
                self.mouse_over_sound.play(0)
            if pressed == (1, 0, 0):
                self.select_sound.play(0)
                return True
        else:
            self.image = pygame.image.load("images/menu/buttons/top button.png").convert()
            self.image.set_colorkey((255, 255, 255))
            self.image.set_alpha(150)
            self.mouse_over = False
        
        # if not returns false
        return False
            
class NewSounds:
    '''Contains all the sounds that will be used.'''
    
    def __init__(self):
        '''Creates the sounds.'''
        
        # the sound navi makes when she comes out of links pocket
        self.navi_out = pygame.mixer.Sound('sounds/navi/out.wav')
        self.navi_out.set_volume(1.00) 
        
        # the sound navi makes when she re-enters out of links pocket
        self.navi_in = pygame.mixer.Sound('sounds/navi/in.wav')
        self.navi_in.set_volume(1.00)   
        
        # the sound navi makes while she is floating
        self.navi_listen = pygame.mixer.Sound('sounds/navi/listen.wav')
        self.navi_listen.set_volume(1.00)    
        
        # the sound link makes when he is hurt
        self.link_hurt = pygame.mixer.Sound('sounds/link/hurt2.wav')
        self.link_hurt.set_volume(0.50)      
        
        # link slicing
        self.slice = pygame.mixer.Sound('sounds/link/slice.wav')
        self.slice.set_volume(0.50)           
            
class NewText:
    '''The small text window on the bottom of the screen.'''
    
    def __init__(self):
        '''Creates the text display window.'''
        
        # image and rect
        self.image = pygame.image.load("images/menu/text window.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.set_alpha(170)
        self.rect = self.image.get_rect()
        self.rect.top = 600
        self.rect.left = 200
        
        # other attributes
        self.out = True
        self.lines = ["Navi:",
        "Use The W, A, S, and D keys to move.  Space to read signs, talk", 
        "to people ect...  You can also talk to me with Space if no one", 
        "else is around."]
        
    def display(self, screen):
        '''Displays the text window.'''
        
        # displays the window
        screen.blit(self.image, self.rect)
        
        # creates a font
        font = pygame.font.Font(None, 20)
           
        # displays the lines of text
        x = self.rect.left + 10
        y = self.rect.top + 10
        for line in self.lines:
            if y < self.rect.top + 80:
                text = font.render(line, 1, (255, 255, 255))
                screen.blit(text, [x, y])
                y = y + 20
         
        # moves the screen out and in
        if self.lines == []:
            self.rect.top = self.rect.top + 7
            if self.rect.top > 600:
                self.out = False 
        if self.rect.top > 400 and self.lines != []:
            self.rect.bottom = self.rect.bottom - 7
                
    def next(self):
        '''Replaces previous text with different text.'''
        
        if self.lines != []:
            for i in range(0, 4):
                if self.lines != []:
                    self.lines.remove(self.lines[0])
            
        
class NewRoom:
    '''The different areas that link can travel through.'''
    
    def __init__(self, room, link):
        '''creates the map.'''
        
        # will be filled with objects later
        self.objects = []
        
        # default music that is played in room
        self.music = "music/Lost Woods.mp3"
        self.volume = 0.20
        
        # fill color
        self.background_color = [50, 243, 76]
        
        # creates the first room
        if room == [0, 0]:
            tree = objects.tree([275, -60])
            self.objects.append(tree)
            tree = objects.tree([0, -60])
            tree.rect.right = 525
            self.objects.append(tree)
            for i in range(0, 2000):
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                grass = objects.ground([x, y], "images/ground/grass.png", (255, 255, 255))
                if random.choice([True, False]):
                    grass.image = pygame.transform.flip(grass.image, 1, 0)
                self.objects.append(grass)
            for x in range(0, 300, 100):
                tree = objects.tree([x, 0])
                self.objects.append(tree)
                tree = objects.tree([x, 0])
                tree.rect.bottom = 600
                self.objects.append(tree)
            for x in range(800, 400, -100):
                tree = objects.tree([x, 0])
                self.objects.append(tree)
                tree = objects.tree([x, 0])
                tree.rect.bottom = 600
                self.objects.append(tree)
            for y in range(90, 400, 90):
                tree = objects.tree([0, y])
                self.objects.append(tree)
                tree = objects.tree([0, y])
                tree.rect.right = 800
                self.objects.append(tree)
            for x in range(100, 190, 30):
                for y in range(100, 500, 25):
                    bush = objects.bush([x, y])
                    self.objects.append(bush)
            for x in range(700, 610, -30):
                for y in range(100, 500, 25):
                    bush = objects.bush([x, y])
                    bush.rect.right = x
                    self.objects.append(bush)
            for x in range(10, 100, 30):
                for y in range(450, 500, 25):
                    bush = objects.bush([x, y])
                    self.objects.append(bush)
            for x in range(790, 700, -30):
                for y in range(450, 500, 25):
                    bush = objects.bush([x, y])
                    bush.rect.right = x
                    self.objects.append(bush)
            for y in range(0, 600, 93):
                path = objects.ground([0, y], "images/ground/dirt road/ver path.png", (255, 255, 255))
                path.rect.centerx = 400
                self.objects.append(path)
            for x in range(297, 497, 30):
                fence = objects.fence([x, 550])
                self.objects.append(fence)
                if x < 350 or x > 440:
                    fence = objects.fence([x, 40])
                    self.objects.append(fence)
            self.objects.append(objects.sign([440, 90], ["Head south to reach Clock Town.  Just north of here is the Lost",
            "Woods.  At the other side of Lost Woods is Hyrule.  There is a",
            "sign up ahead that has specific more directions. Be Careful not",
            "to get lost."]))
            
        # creates the room to left of the first room that contains a heart piece
        if room == [-1, 0]:
            tree = objects.tree([275, -60])
            self.objects.append(tree)
            tree = objects.tree([0, -60])
            tree.rect.right = 525
            self.objects.append(tree)
            for i in range(0, 2000):
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                grass = objects.ground([x, y], "images/ground/grass.png", (255, 255, 255))
                if random.choice([True, False]):
                    grass.image = pygame.transform.flip(grass.image, 1, 0)
                self.objects.append(grass)
            for x in range(800, 400, -100):
                tree = objects.tree([x, 0])
                self.objects.append(tree)
                tree = objects.tree([x, 0])
                tree.rect.bottom = 600
                self.objects.append(tree)
            for x in range(0, 300, 100):
                tree = objects.tree([x, 0])
                self.objects.append(tree)
                tree = objects.tree([x, 0])
                tree.rect.bottom = 600
                self.objects.append(tree)
            for y in range(90, 400, 90):
                tree = objects.tree([0, y])
                self.objects.append(tree)
                tree = objects.tree([0, y])
                tree.rect.right = 800
                self.objects.append(tree)
            for x in range(700, 640, -30):
                for y in range(100, 500, 25):
                    bush = objects.bush([x, y])
                    bush.rect.right = x
                    self.objects.append(bush)
            for x in range(790, 700, -30):
                for y in range(450, 500, 25):
                    bush = objects.bush([x, y])
                    bush.rect.right = x
                    self.objects.append(bush)
            for y in range(80, 520, 20):
                fence = objects.fence([500, y], "left")
                self.objects.append(fence)
            for y in range(0, 600, 93):
                path = objects.ground([0, y], "images/ground/dirt road/ver path.png", (255, 255, 255))
                path.rect.centerx = 400
                self.objects.append(path)
            for x in range(-90, 300, 93):
                path = objects.ground([x, 0], "images/ground/dirt road/hor path.png", (255, 255, 255))
                path.rect.centery = 487
                self.objects.append(path)
            path = objects.ground([x, 0], "images/ground/dirt road/center left path.png", (255, 255, 255))
            path.rect.center = [400, 487]
            self.objects.append(path)
            for x in range(297, 497, 30):
                fence = objects.fence([x, 550])
                self.objects.append(fence)
            if 1 not in link.collected_heart_pieces:
                self.objects.append(objects.heart_piece([575, 125], 1))
                
        # creates the room to right of the first room that has the correct directions sign
        if room == [1, 0]:
            for i in range(0, 2000):
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                grass = objects.ground([x, y], "images/ground/grass.png", (255, 255, 255))
                if random.choice([True, False]):
                    grass.image = pygame.transform.flip(grass.image, 1, 0)
                self.objects.append(grass)
            tree = objects.tree([275, -60])
            self.objects.append(tree)
            tree = objects.tree([0, -60])
            tree.rect.right = 525
            self.objects.append(tree)
            for x in range(297, 497, 30):
                fence = objects.fence([x, 40])
                self.objects.append(fence)            
            tree = objects.tree([-10, 350])
            self.objects.append(tree)
            tree = objects.tree([-10, 0])
            tree.rect.bottom = 600
            self.objects.append(tree)
            for y in range(350, 600, 90):
                tree = objects.tree([270, y])
                self.objects.append(tree)
            for x in range(80, 280, 100):
                tree = objects.tree([x, 300])
                self.objects.append(tree)
            for x in range(0, 90, 30):
                for y in range(450, 500, 25):
                    bush = objects.bush([x, y])
                    self.objects.append(bush)
            for x in range(90, 150, 30):
                for y in range(400, 500, 25):
                    bush = objects.bush([x, y])
                    self.objects.append(bush)
                    bush = objects.bush([x + 120, y])
                    self.objects.append(bush)
            for x in range(150, 210, 30):
                for y in range(400, 450, 25):
                    bush = objects.bush([x, y])
                    self.objects.append(bush)
            for x in range(92, 300, 30):
                fence = objects.fence([x, 550])
                self.objects.append(fence)
            if link.progress > 0:
                self.objects.append(objects.sign([165, 450], ["Directions to Hyrule:",
                "North.",
                "West.",
                "North.",
                "North.",
                "East.",
                "East.",
                "South.",
                "East."]))
                    
        # creates the normal parts of lost woods
        if room[0] >= -2 and room[0] <= 1 and room[1] <= -1 and room[1] >= -4:
            for i in range(0, 2000):
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                grass = objects.ground([x, y], "images/ground/grass.png", (255, 255, 255))
                if random.choice([True, False]):
                    grass.image = pygame.transform.flip(grass.image, 1, 0)
                self.objects.append(grass)
            tree = objects.tree([275, -60])
            self.objects.append(tree)
            tree = objects.tree([0, -60])
            tree.rect.right = 525
            self.objects.append(tree)
            for x in range(0, 300, 100):
                tree = objects.tree([x, 0])
                self.objects.append(tree)
            for x in range(800, 400, -100):
                tree = objects.tree([x, 0])
                self.objects.append(tree)
            for y in range(90, 200, 90):
                tree = objects.tree([0, y])
                self.objects.append(tree)
                tree = objects.tree([0, y])
                tree.rect.right = 800
                self.objects.append(tree)
            for x in range(0, 800, 93):
                path = objects.ground([x, 0], "images/ground/dirt road/hor path.png", (255, 255, 255))
                path.rect.centery = 305
                self.objects.append(path)
            for y in range(320, 500, 90):
                tree = objects.tree([0, y])
                self.objects.append(tree)
                tree = objects.tree([0, y])
                tree.rect.right = 800
                self.objects.append(tree)
            for x in range(0, 300, 100):
                tree = objects.tree([x, 0])
                tree.rect.bottom = 600
                self.objects.append(tree)
            for x in range(800, 400, -100):
                tree = objects.tree([x, 0])
                tree.rect.bottom = 600
                self.objects.append(tree)
            for y in range(0, 600, 93):
                path = objects.ground([0, y], "images/ground/dirt road/ver path.png", (255, 255, 255))
                path.rect.centerx = 400
                self.objects.append(path)
            path = objects.ground([0, 0], "images/ground/dirt road/center path.png", (255, 255, 255))
            path.rect.center = [400, 305]
            self.objects.append(path)
            tree = objects.tree([275, 570])
            self.objects.append(tree)
            tree = objects.tree([0, 570])
            tree.rect.right = 525
            self.objects.append(tree)
        
        # creates the first part of lost woods
        if room == [0, -1]:
            self.objects.append(objects.sign([390, 260], ["Directions to Hyrule:",
            "South.",
            "North."]))
            if link.progress == 0:
                self.objects.append(objects.thief([700, 275]))
            
        # creates a part of the incorrect path in lost woods
        if room == [0, -3]:
            for x in range(297, 497, 30):
                fence = objects.fence([x, 40])
                self.objects.append(fence)
            for y in range(270, 330, 20):
                fence = objects.fence([0, y], "left")
                fence.rect.right = 740 
                self.objects.append(fence)
                fence = objects.fence([60, y], "right")
                self.objects.append(fence)
                
        # creates a part of the incorrect path in lost woods
        if room == [-1, -1]:
            for x in range(297, 497, 30):
                fence = objects.fence([x, 40])
                self.objects.append(fence)
            for y in range(270, 330, 20):
                fence = objects.fence([60, y], "right")
                self.objects.append(fence)
                
        # creates a part of the incorrect path in lost woods
        if room == [1, -2]:
            for x in range(297, 497, 30):
                fence = objects.fence([x, 40])
                self.objects.append(fence)
            for y in range(270, 330, 20):
                fence = objects.fence([0, y], "left")
                fence.rect.right = 740 
                self.objects.append(fence)
                
        # creates a part of the incorrect path in lost woods
        if room == [1, -1]:
            for y in range(270, 330, 20):
                fence = objects.fence([0, y], "left")
                fence.rect.right = 740 
                self.objects.append(fence)
            feet = objects.ground([0, y], "images/ground/foot steps.png", (255, 255, 255))
            feet.rect.center = [400, 580]
            self.objects.append(feet)
                
        # creates a part of the incorrect path in lost woods
        if room == [-2, -2]:
            for y in range(270, 330, 20):
                fence = objects.fence([60, y], "right")
                self.objects.append(fence)
                fence = objects.fence([60, y], "left")
                fence.rect.right = 740
                self.objects.append(fence)
            for x in range(297, 497, 30):
                fence = objects.fence([x, 40])
                self.objects.append(fence)
                
        # creates a part of the incorrect path in lost woods
        if room == [-2, -3]:
            for y in range(270, 330, 20):
                fence = objects.fence([60, y], "right")
                self.objects.append(fence)
                
        # creates a part of the incorrect path in lost woods
        if room == [-2, -4]:
            for x in range(297, 497, 30):
                fence = objects.fence([x, 40])
                self.objects.append(fence)
            for y in range(270, 330, 20):
                fence = objects.fence([0, y], "left")
                fence.rect.right = 740 
                self.objects.append(fence)
                fence = objects.fence([60, y], "right")
                self.objects.append(fence)
                
        # creates a part of the incorrect path in lost woods
        if room == [-2, -1]:
            for y in range(270, 330, 20):
                fence = objects.fence([60, y], "right")
                self.objects.append(fence)
                
        # creates a part of the incorrect path in lost woods
        if room == [-2, 0]:
            for y in range(90, 400, 90):
                tree = objects.tree([0, y])
                tree.rect.right = 800
                self.objects.append(tree)
            for y in range(0, 600, 90):
                tree = objects.tree([0, y])
                self.objects.append(tree)
            tree = objects.tree([275, -60])
            self.objects.append(tree)
            tree = objects.tree([0, -60])
            tree.rect.right = 525
            self.objects.append(tree)
            for x in range(800, 400, -100):
                tree = objects.tree([x, 0])
                self.objects.append(tree)
                tree = objects.tree([x, 0])
                tree.rect.bottom = 600
                self.objects.append(tree)
            for x in range(0, 300, 100):
                tree = objects.tree([x, 0])
                self.objects.append(tree)
                if x != 0:
                    tree = objects.tree([x, 0])
                    tree.rect.bottom = 600
                    self.objects.append(tree)
            for y in range(0, 600, 93):
                path = objects.ground([0, y], "images/ground/dirt road/ver path.png", (255, 255, 255))
                path.rect.centerx = 400
                self.objects.append(path)
            for x in range(420, 700, 93):
                path = objects.ground([x, 0], "images/ground/dirt road/hor path.png", (255, 255, 255))
                path.rect.centery = 487
                self.objects.append(path)
            path = objects.ground([0, 0], "images/ground/dirt road/center right path.png", (255, 255, 255))
            path.rect.center = [405, 487]
            self.objects.append(path)
            for x in range(297, 497, 30):
                fence = objects.fence([x, 550])
                self.objects.append(fence)
            
        # creates a part of the correct path in lost woods
        if room == [-1, -4]:
            for x in range(297, 497, 30):
                fence = objects.fence([x, 40])
                self.objects.append(fence)
                
        # creates a part of the correct path in lost woods
        if room == [0, -4]:
            for x in range(297, 497, 30):
                fence = objects.fence([x, 40])
                self.objects.append(fence)
                
        # creates a part of the correct path in lost woods
        if room == [1, -4]:
            for x in range(297, 497, 30):
                fence = objects.fence([x, 40])
                self.objects.append(fence)
            for y in range(270, 330, 20):
                fence = objects.fence([0, y], "left")
                fence.rect.right = 740 
                self.objects.append(fence)
        
        # creates last part of the correct path in lost woods
        if room == [1, -3]:
            if link.progress < 2:
                for y in range(270, 330, 20):
                    fence = objects.fence([0, y], "left")
                    fence.rect.right = 740 
                    self.objects.append(fence)
                
        # exit of lost woods
        if room == [2, -3]:
            for i in range(0, 2000):
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                grass = objects.ground([x, y], "images/ground/grass.png", (255, 255, 255))
                if random.choice([True, False]):
                    grass.image = pygame.transform.flip(grass.image, 1, 0)
                self.objects.append(grass)
            for y in range(0, 600, 20):
                if y < 250 and y > 50 or y > 350:
                    fence = objects.fence([50, y], "right")
                    self.objects.append(fence)
            for y in [250, 350]:
                for x in [-5, 25]:
                    fence = objects.fence([x, y])
                    self.objects.append(fence)
            for x in range(65, 830, 30):
                fence = objects.fence([x, 50])
                self.objects.append(fence)
            for x in range(0, 800, 93):
                path = objects.ground([x, 0], "images/ground/dirt road/hor path.png", (255, 255, 255))
                path.rect.centery = 315
                self.objects.append(path)
            for y in range(315, 615, 93):
                path = objects.ground([0, y], "images/ground/dirt road/ver path.png", (255, 255, 255))
                path.rect.centerx = 410
                self.objects.append(path)
            path = objects.ground([0, 0], "images/ground/dirt road/center right path.png", (255, 255, 255))
            path.image = pygame.transform.rotate(path.image, 270)
            path.rect.center = [400, 340]
            self.objects.append(path)
            for x in [-10, 20]:
                for y in range(0, 600, 25):
                    if y < 250 or y > 350:
                        self.objects.append(objects.bush([x, y]))
            for x in range(50, 830, 30):
                for y in [0, 25]:
                    if y < 250 or y > 350:
                        self.objects.append(objects.bush([x, y]))
            sign = objects.sign([400, 260], ["Welcome.  You are now in Hyrule Field.",
            "West:  Lost Woods.",
            "East:  Hyrule Castle.",
            "South:  Kokiri Forest."])
            self.objects.append(sign)
            self.music = "music/Hylian.mp3"
            self.volume = 0.20
        if room == [3, -3]:
            for i in range(0, 2000):
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                grass = objects.ground([x, y], "images/ground/grass.png", (255, 255, 255))
                if random.choice([True, False]):
                    grass.image = pygame.transform.flip(grass.image, 1, 0)
                self.objects.append(grass)
            for x in range(-10, 720, 30):
                for y in [0, 25]:
                    if y < 250 or y > 350:
                        self.objects.append(objects.bush([x, y]))
            for x in range(5, 720, 30):
                fence = objects.fence([x, 50])
                self.objects.append(fence)
            for y in [250, 350]:
                for x in [765, 735]:
                    fence = objects.fence([x, y])
                    self.objects.append(fence)
            for y in range(0, 600, 20):
                if y < 250 and y > 50 or y > 350:
                    fence = objects.fence([720, y], "left")
                    self.objects.append(fence)
            for x in [770, 740]:
                for y in range(0, 600, 25):
                    if y < 250 or y > 350:
                        self.objects.append(objects.bush([x, y]))
            for x in range(0, 800, 93):
                path = objects.ground([x, 0], "images/ground/dirt road/hor path.png", (255, 255, 255))
                path.rect.centery = 315
                self.objects.append(path)
            self.objects.append(objects.dark_nut([700, 290]))
            self.music = "music/Enemy Attack.mp3"
            self.volume = 0.20
                
        if self.objects == []:
            for i in range(0, 2000):
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                grass = objects.ground([x, y], "images/ground/grass.png", (255, 255, 255))
                if random.choice([True, False]):
                    grass.image = pygame.transform.flip(grass.image, 1, 0)
                self.objects.append(grass)
            for i in range(0, 10):
                self.objects.append(objects.dark_nut([random.randint(0, 800), random.randint(0, 600)]))
            self.music = "music/Enemy Attack.mp3"
            self.volume = 0.20
            self.background_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            
        # reorganizes the objects so that they are displayed in order
        old_objects = self.objects
        new_objects = []
        for i in range(-100, 700):
            for object in old_objects:
                if object.type != "ground":
                    if object == 0:
                        if link.rect.centery == i:
                            new_objects.append(0)
                    else:
                        if object.rect.centery == i: 
                            new_objects.append(object)
        for object in reversed(old_objects):
            if object.type == "ground":
                new_objects.insert(0, object)
        self.objects = new_objects
        cloud = objects.cloud([5, 0])
        self.objects.append(cloud)
        
    def display_before(self, screen, link, navi, text_window, sounds):
        '''Displays all the objects.'''
        
        for object in self.objects:
            if object.blit_before:
                screen.blit(object.image, object.rect)
                if link.health + link.health_fraction > 0:
                    r = object.action(screen, link, navi, text_window, sounds)
                    if r == "heart piece":
                        self.objects.remove(object)
                        link.collected_heart_pieces.append(object.id)
            
    def display_after(self, screen, link, navi, text_window, sounds):
        '''Displays all the objects.'''
        
        for object in self.objects:
            if not object.blit_before:
                screen.blit(object.image, object.rect)
                if link.health + link.health_fraction > 0:
                    r = object.action(screen, link, navi, text_window, sounds)
                    if r == "heart piece":
                        self.objects.remove(object)
                        link.collected_heart_pieces.append(object.id)
    
def main():
    '''The main part of the program in which you play the game.'''
    
    # sets up the screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("The Legend of Zelda Return to Hyrule")
    
    # create clock
    clock = pygame.time.Clock()
    
    # creates instances of objects
    link = NewLink()
    navi = NewFairy()
    room = NewRoom(link.room, link)
    text_window = NewText()
    sounds = NewSounds()
    menu_pause = NewButton([200, 0], "Pause Game")
    menu_save = NewButton([0, 0], " Save Game")
    menu_save.rect.centerx = 400
    menu_exit = NewButton([500, 0], " Exit Game")
    menu_exit.rect.right = 600
    
    # variables
    idle_time = 0
    pause = False
    item_button = pygame.image.load("images/menu/buttons/item button.png").convert()
    item_button.set_colorkey((255, 255, 255))
    item_button.set_alpha(150)
    
    # loads settings
    list = menu.main_menu(screen)
    if len(list) > 1:
        link.progress = list[0]
        link.room = list[1]
        link.rect.left, link.rect.top = list[2]
        link.health = list[3]
        link.fraction_health = list[4]
        link.max_health = list[5]
        link.collected_heart_pieces = list[6]
        navi.lines = list[7]
        room = NewRoom(link.room, link)
        text_window.next()
        
    else:
        
        # plays the first story part
        story.beginning(screen)

    # selects the first song to play
    '''pygame.mixer.music.load(room.music)
    pygame.mixer.music.set_volume(room.volume)
    pygame.mixer.music.play(-1)'''
        
    # event loop
    done = False
    while not done:
        if not pause and link.health >= 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and text_window.out:
                        text_window.next()
                    elif event.key == pygame.K_SPACE and not text_window.out and not link.near_sign:
                        if not navi.out:
                            navi.out = True
                            navi.position[0] = link.rect.left - 20
                            navi.position[1] = link.rect.top - 20
                            navi.rect.left, navi.rect.top = navi.position
                            sounds.navi_out.play()
                        text_window.out = True
                        for line in navi.lines:
                            text_window.lines.append(line)
                    if event.key == pygame.K_LSHIFT:
                        link.rolling = True
                        link.image = 0
                        link.end = 3
                if event.type ==pygame.MOUSEMOTION:
                    idle_time = 0
                    pygame.mouse.set_visible(True)
                      
            # link is no longer near a sign and is not reading it
            link.near_sign = False
            link.reading = False
                    
            # erases screen
            screen.fill(room.background_color)
            
            # sets a time delay
            time = clock.tick(75)
                
            # displays object before link
            room.display_before(screen, link, navi, text_window, sounds)
            
            # displays link
            screen.blit(link.images[link.image], link.rect)
                
            # displays object before link
            room.display_after(screen, link, navi, text_window, sounds)
            
            # moves link and displays his health
            link.move(sounds)
            link.display_hearts(screen)
            
            # moves and displays navi
            if navi.out:
                navi.move(screen, link, sounds)
                screen.blit(navi.images[navi.image], navi.rect)
            
            # allows link to move into different rooms
            if link.change_room(navi):
                old_room = room
                room = NewRoom(link.room, link)
                if old_room.music != room.music:
                    pygame.mixer.music.load(room.music)
                    pygame.mixer.music.set_volume(room.volume)
                    pygame.mixer.music.play(-1)
                
            # displays the text window
            if text_window.out:
                text_window.display(screen)
                
            for rect in ([620, 550], [680, 550], [740, 550], [680, 500]):
                screen.blit(item_button, rect)
                
            # increment the time since last mouse motion event by 1
            idle_time = idle_time + 1
                
            # top of screen menu buttons
            if idle_time <= 200:
                if menu_save.display(screen):
                    '''file = open(file_loc, 'w')
                    collected_heart_pieces = []
                    for h in link.collected_heart_pieces:
                        collected_heart_pieces.append(str(h))'''
                if menu_exit.display(screen):
                    sys.exit()
                if menu_save.display(screen):
                    pygame.mixer.music.pause()
                    fog = pygame.Surface([800, 600])
                    fog.set_alpha(200)
                    screen.blit(fog, [0, 0])
                    pause_display = pygame.image.load("images/menu/pause2.png").convert()
                    pause_display.set_colorkey((255, 255, 255))
                    pause_rect = pause_display.get_rect()
                    pause_rect.center = [400, 300]
                    screen.blit(pause_display, pause_rect)
                    font = pygame.font.Font(None, 30)
                    pause_text = font.render("Game paused.", 1, (255, 255, 255))
                    pause_rect = pause_text.get_rect()
                    pause_rect.center = [400, 500]
                    screen.blit(pause_text, pause_rect)
                    pygame.display.flip()
                    slot = easygui.buttonbox("Which slot do you want to save to?", "Legend of Zelda Return to Hyrule", ["1", "2", "3", "4", "5"])
                    file = open("files/" + slot + ".txt", 'w')
                    file.write(str(link.progress) + "\n")
                    file.write(str(link.room[0]) + "\n")
                    file.write(str(link.room[1]) + "\n")
                    file.write(str(link.rect.left) + "\n")
                    file.write(str(link.rect.top) + "\n")
                    file.write(str(link.health) + "\n")
                    file.write(str(link.health_fraction) + "\n")
                    file.write(str(link.max_health) + "\n")
                    if link.collected_heart_pieces == []:
                        file.write("\n")
                    else:
                        for p in link.collected_heart_pieces:
                            file.write(str(p) + " ")
                        file.write("\n")
                    for line in navi.lines:
                        if navi.lines.index(line) != 0:
                            file.write(" end_line ")
                        file.write(line)
                    file.close()
                    pygame.mixer.music.unpause()
                if menu_pause.display(screen):
                    pause = True
                    pygame.mixer.music.pause()
                    fog = pygame.Surface([800, 600])
                    fog.set_alpha(200)
                    screen.blit(fog, [0, 0])
                    pause_display = pygame.image.load("images/menu/pause2.png").convert()
                    pause_display.set_colorkey((255, 255, 255))
                    pause_rect = pause_display.get_rect()
                    pause_rect.center = [400, 300]
                    screen.blit(pause_display, pause_rect)
                    font = pygame.font.Font(None, 30)
                    pause_text = font.render("Game paused.  Click anywhere to resume.", 1, (255, 255, 255))
                    pause_rect = pause_text.get_rect()
                    pause_rect.center = [400, 500]
                    screen.blit(pause_text, pause_rect)
            else:
                pygame.mouse.set_visible(False)
                
            # advances link through the story
            if link.progress == 0:
                if link.room == [0, -1]:
                    navi.lines = ["Navi:",
                    "What do you think that girl was doing?"]
                    link.progress = link.progress + 1
            if link.progress == 1:
                if link.room == [0, -1] and link.near_sign and link.reading:
                    navi.lines = ["Navi:",
                    "Did you read that sign?  That will just take us right back here!"]
                    link.progress = 2
            if link.progress <= 2:
                if link.room == [1, 0] and link.near_sign and link.reading:
                    navi.lines = ["Navi:",
                    "Thats wierd.  This sign wasn't here earlier.  Well don't just", 
                    "stand there.  Memorize those directions and let's get going."]
                    link.progress = 3
            if link.progress == 3:
                if link.room == [0, 0]:
                    navi.lines = ["Navi:",
                    "Come on Hurry.  We have the directions now lets go."]
                    link.progress = 4
            if link.progress == 4:
                if link.room == [2, -3]:
                    navi.lines = ["Navi:",
                    "Finally!  It feels good to be out of the woods."]
                    link.progress = 5     
            if link.progress == 5:
                if link.room == [2, -3] and link.near_sign and link.reading:
                    navi.lines = ["Navi:",
                    "Alright, lets keep going.  Hyrule is west of here."]
                    link.progress = 6
            if link.progress == 5 or link.progress == 6:
                if link.room == [3, -3]:
                    navi.lines = ["Navi:",
                    "What is an enemy doing right near Hyrule Castle?.  Lets go to",
                    "Kokiri Forest to get your old sword before we move along."]
                    link.progress = 7
                    
            if link.health + link.health_fraction <= 0:
                pause = True
                    
            # displays changes
            pygame.display.flip()
            
        elif pause and link.health + link.health_fraction > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause = False
                    pygame.mixer.music.unpause()
        
        else:
            pygame.mixer.music.load("music/Loud Game Over.wav")
            pygame.mixer.music.set_volume(1.00)
            pygame.mixer.music.play(1)
            for image in link.game_over:
                clock.tick(60)
                screen.fill(room.background_color)
                room.display_before(screen, link, navi, text_window, sounds)
                screen.blit(image, link.rect)
                link.display_hearts(screen)
                room.display_after(screen, link, navi, text_window, sounds)
                if navi.out:
                    navi.move(screen, link, sounds)
                    screen.blit(navi.images[navi.image], navi.rect)
                pygame.display.flip()
            for i in range(0, 230):
                clock.tick(60)
                screen.fill(room.background_color)
                room.display_before(screen, link, navi, text_window, sounds)
                screen.blit(image, link.rect)
                link.display_hearts(screen)
                room.display_after(screen, link, navi, text_window, sounds)
                if navi.out:
                    navi.move(screen, link, sounds)
                    screen.blit(navi.images[navi.image], navi.rect)
                fog = pygame.Surface([800, 600])
                fog.set_alpha(i)
                screen.blit(fog, [0, 0])
                pygame.display.flip()
            for i in range(0, 256):
                clock.tick(60)
                screen.fill(room.background_color)
                room.display_before(screen, link, navi, text_window, sounds)
                screen.blit(image, link.rect)
                link.display_hearts(screen)
                room.display_after(screen, link, navi, text_window, sounds)
                if navi.out:
                    navi.move(screen, link, sounds)
                    screen.blit(navi.images[navi.image], navi.rect)
                screen.blit(fog, [0, 0])
                pause_display = pygame.image.load("images/menu/pause2.png").convert()
                pause_display.set_colorkey((255, 255, 255))
                pause_rect = pause_display.get_rect()
                pause_rect.center = [400, 300]
                pause_display.set_alpha(i)
                screen.blit(pause_display, pause_rect)
                pygame.display.flip()
            font = pygame.font.Font(None, 30)
            pause_text = font.render("Game Over.", 1, (255, 255, 255))
            pause_tr = pause_text.get_rect()
            pause_tr.center = [400, 500]
            pause_text.set_alpha(i);
            screen.blit(pause_text, pause_tr)
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
if __name__ == "__main__":
    main()
