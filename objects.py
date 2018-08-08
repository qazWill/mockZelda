'''
Contains all the classes of the
objects that will be used in the game.
'''

# nesccesary imports
import pygame, sys, math, random

class ground:
    '''Ground that can have any image.'''
    
    def __init__(self, position, image, colorkey=None):
        '''Creates the ground.'''
        
        self.image = pygame.image.load(image).convert()
        if colorkey != None:
            self.image.set_colorkey(colorkey, pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.blit_before = True
        self.type = "ground"
        
    def action(self, screen, link, navi, text_window, sounds):
        '''The ground doesn't have an action to perform.'''
        
        pass
        

class tree:
    '''A tree.'''
    
    def __init__(self, position):
        '''Creates the tree.'''
        
        self.image = pygame.image.load("images/objects/tree.png").convert()
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.blit_before = True
        self.type = "normal"
        
    def action(self, screen, link, navi, text_window, sounds):
        '''Prevents link from moving through the tree.'''
        
        # checks to see when to blit the tree
        if link.rect.centery < self.rect.centery:
            self.blit_before = False
        else:
            self.blit_before = True
        
        # prevents link from moving through the tree
        if link.rolling:
            c = 5
        else:
            c = 3
        if link.rect.centery < self.rect.bottom and link.rect.centery > self.rect.top and link.rect.left < self.rect.right and link.rect.right > self.rect.left:
            if link.moving:
                if link.rect.right < self.rect.centerx:
                    link.rect.left = link.rect.left - c
                if link.rect.left > self.rect.centerx:
                    link.rect.left = link.rect.left + c
                if link.rect.top < self.rect.centery:
                    link.rect.top = link.rect.top - c
                if link.rect.bottom > self.rect.centery:
                    link.rect.top = link.rect.top + c
                
class swamp_tree:
    '''Another type of tree.'''
    
    def __init__(self, position):
        '''Creates the tree.'''
        
        self.image = pygame.image.load("images/objects/swamp tree.png").convert()
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.blit_before = True
        self.type = "normal"
        
    def action(self, screen, link, navi, text_window, sounds):
        '''Prevents link from moving through the tree.'''
        
        # checks to see when to blit the tree
        if link.rect.centery < self.rect.centery:
            self.blit_before = False
        else:
            self.blit_before = True
        
        if link.rolling:
            c = 5
        else:
            c = 3
        if link.rect.centery < self.rect.bottom and link.rect.centery > self.rect.top and link.rect.left < self.rect.right and link.rect.right > self.rect.left:
            if link.moving:
                if link.rect.right < self.rect.centerx:
                    link.rect.left = link.rect.left - c
                if link.rect.left > self.rect.centerx:
                    link.rect.left = link.rect.left + c
                if link.rect.top < self.rect.centery:
                    link.rect.top = link.rect.top - c
                if link.rect.bottom > self.rect.centery:
                    link.rect.top = link.rect.top + c
                
class bush:
    '''A small bush.'''
    
    def __init__(self, position):
        '''Creates the bush.'''
        
        self.image = pygame.image.load("images/objects/bush.png").convert()
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.blit_before = True
        self.type = "normal"
        
    def action(self, screen, link, navi, text_window, sounds):
        '''Prevents link from moving through the tree.'''
        
        # checks to see when to blit the tree
        if link.rect.centery < self.rect.centery:
            self.blit_before = False
        else:
            self.blit_before = True
        
        # prevents link from moving through the bush
        if link.rolling:
            c = 5
        else:
            c = 3
        if link.rect.centery < self.rect.bottom and link.rect.bottom - 5 > self.rect.top and link.rect.left < self.rect.right and link.rect.right > self.rect.left:
            if link.moving:
                if link.rect.right < self.rect.centerx:
                    link.rect.left = link.rect.left - c
                if link.rect.left > self.rect.centerx:
                    link.rect.left = link.rect.left + c
                if link.rect.bottom < self.rect.centery:
                    link.rect.top = link.rect.top - c
                if link.rect.bottom > self.rect.centery:
                    link.rect.top = link.rect.top + c
                
class fence:
    '''A fence.'''
    
    def __init__(self, position, align="bottom"):
        '''Creates the bush.'''
        
        if align == "bottom":
            self.image = pygame.image.load("images/objects/hor fence.png").convert()
        elif align == "right":
            self.image = pygame.image.load("images/objects/ver fence.png").convert()
        else:
            self.image = pygame.image.load("images/objects/ver fence.png").convert()
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.blit_before = True
        self.type = "normal"
        
    def action(self, screen, link, navi, text_window, sounds):
        '''Prevents link from moving through the tree.'''
        
        # checks to see when to blit the tree
        if link.rect.centery < self.rect.centery:
            self.blit_before = False
        else:
            self.blit_before = True
     
        # prevents link from moving through the fence
        if link.rolling:
            c = 5
        else:
            c = 3
        if link.rect.centery < self.rect.bottom and link.rect.bottom - 5 > self.rect.top and link.rect.left < self.rect.right and link.rect.right > self.rect.left:
            if link.moving:
                if link.rect.right < self.rect.centerx:
                    link.rect.left = link.rect.left - c
                if link.rect.left > self.rect.centerx:
                    link.rect.left = link.rect.left + c
                if link.rect.bottom < self.rect.centery:
                    link.rect.top = link.rect.top - c
                if link.rect.bottom > self.rect.centery:
                    link.rect.top = link.rect.top + c
                
class heart_piece:
    '''Gives Link an extra heart'''
    
    def __init__(self, position, id):
        '''Creates the heart piece.'''
        
        self.image = pygame.image.load("images/objects/heart piece.png").convert()
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.id = id
        self.blit_before = False
        self.type = "normal"
        
    def action(self, screen, link, navi, text_window, sounds):
        '''Checks to see if link has collected the heart piece'''
        
        # gives link the heart piece
        if link.rect.top < self.rect.bottom and link.rect.bottom > self.rect.top and link.rect.left < self.rect.right and link.rect.right > self.rect.left:
            link.max_health = link.max_health + 1
            link.add_health()
            link.add_health()
            link.add_health()
            link.add_health()
            text_window.out = True
            text_window.lines.append("Navi:")
            text_window.lines.append("Good Job.  You found a heart piece.")
            navi.out = True
            navi.position[0] = link.rect.left - 20
            navi.position[1] = link.rect.top - 20
            navi.rect.left, navi.rect.top = navi.position
            sounds.navi_out.play()
            return "heart piece"
                
class sign:
    '''A sign that can be read.'''
    
    def __init__(self, position, lines):
        '''Creates the sign.'''
        
        self.image = pygame.image.load("images/objects/sign.png").convert()
        self.image.set_colorkey((255, 255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.blit_before = True
        self.lines = lines
        self.type = "normal"
        
    def action(self, screen, link, navi, text_window, sounds):
        '''Prevents link from moving through the tree.'''
        
        # checks to see when to blit the tree
        if link.rect.centery < self.rect.centery:
            self.blit_before = False
        else:
            self.blit_before = True
        
        # prevents link from moving through the sign
        if link.rolling:
            c = 5
        else:
            c = 3
        if link.rect.centery < self.rect.bottom and link.rect.bottom - 5 > self.rect.top and link.rect.left < self.rect.right and link.rect.right > self.rect.left:
            if link.moving:
                if link.rect.right < self.rect.centerx:
                    link.rect.left = link.rect.left - c
                if link.rect.left > self.rect.centerx:
                    link.rect.left = link.rect.left + c
                if link.rect.bottom < self.rect.centery:
                    link.rect.top = link.rect.top - c
                if link.rect.bottom > self.rect.centery:
                    link.rect.top = link.rect.top + c
                
        # checks to see if link is in range of reading the sign
        if link.rect.bottom > self.rect.bottom and link.rect.bottom < self.rect.bottom + 50 and link.rect.left < self.rect.right and link.rect.right > self.rect.left:
            
            # link is near a sign
            link.near_sign = True
                
            # returns a list of what keys are pressed
            pressed = pygame.key.get_pressed()
                          
            # allows link to read the sign
            if pressed[pygame.K_SPACE] and not text_window.out:
                text_window.out = True
                link.reading = True
                for line in self.lines:
                    text_window.lines.append(line)
                    
class thief:
    '''The guy who runs away in the beginning.'''
    
    def __init__(self, position):
        '''Creates the thief.'''
        
        self.images = [] 
        for i in [1, 2, 3]:
            image = pygame.image.load("images/objects/thief/" + str(i) + ".png")
            image.set_colorkey((255, 255, 255, 255), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, 1.5) 
            image.convert()
            self.images.append(image)
        self.image_num = 0
        self.delay = 0
        self.image = self.images[self.image_num]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.blit_before = True
        self.type = "normal"
        
    def action(self, screen, link, navi, text_window, sounds):
        '''Moves the thief'''
        
        self.rect.left = self.rect.left + 1
        
        # cycles through her images
        self.delay = self.delay + 1
        if self.delay > 4:
            self.delay = 0
            self.image_num = self.image_num + 1
            if self.image_num > 2:
                self.image_num = 0
        
        # changes her image        
        self.image = self.images[self.image_num]
        old_rect = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_rect
        
class dark_nut:
    '''The evil tough knights.'''
    
    def __init__(self, position):
        '''Creates the dark nut.'''
        
        size = 1.75
        
        self.images = [] 
        self.walk_right = []
        self.walk_left = []
        self.walk_up = []
        self.walk_down = []
        for i in range(0, 3):
            image = pygame.image.load("images/objects/dark_nut/right/" + str(i) + ".png")
            image.set_colorkey((163, 73, 164), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size) 
            image.convert()
            self.walk_right.append(image)
            image = pygame.transform.flip(image, 1, 0) 
            self.walk_left.append(image)
        for i in range(0, 4):
            image = pygame.image.load("images/objects/dark_nut/up/" + str(i) + ".png")
            image.set_colorkey((163, 73, 164), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size) 
            image.convert()
            self.walk_up.append(image)
        for i in range(0, 4):
            image = pygame.image.load("images/objects/dark_nut/down/" + str(i) + ".png")
            image.set_colorkey((163, 73, 164), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size) 
            image.convert()
            self.walk_down.append(image)
        self.slice_right = []
        self.slice_left = []
        self.slice_up = []
        self.slice_down = []
        for i in range(0, 6):
            image = pygame.image.load("images/objects/dark_nut/slice_down/" + str(i) + ".png")
            image.set_colorkey((163, 73, 164), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size) 
            image.convert()
            self.slice_down.append(image)
        for i in range(0, 6):
            image = pygame.image.load("images/objects/dark_nut/slice_up/" + str(i) + ".png")
            image.set_colorkey((163, 73, 164), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size) 
            image.convert()
            self.slice_up.append(image)
        for i in range(0, 6):
            image = pygame.image.load("images/objects/dark_nut/slice_right/" + str(i) + ".png")
            image.set_colorkey((163, 73, 164), pygame.RLEACCEL)
            image = pygame.transform.rotozoom(image, 0, size) 
            image.convert()
            self.slice_right.append(image)
            image = pygame.transform.flip(image, 1, 0)
            self.slice_left.append(image)
        self.images = self.walk_right
        self.image_num = 0
        self.delay = 0
        self.max_delay = 10
        self.image = self.images[self.image_num]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.blit_before = True
        self.type = "normal"
        self.hit = False
        
    def action(self, screen, link, navi, text_window, sounds):
        
        # moves him towards link
        if self.images != self.slice_down and self.images != self.slice_right and self.images != self.slice_left and self.images != self.slice_up or self.image_num == 0 and self.delay == 0:
            difx = self.rect.centerx - link.rect.centerx
            dify = self.rect.centery - link.rect.centery
            if difx < 0:
                difx = -difx
            if dify < 0:
                dify = -dify
            if difx >= dify:
                if difx > 50:
                    if link.rect.bottom < self.rect.bottom:
                        if self.delay % 2 == 0:
                            self.rect.top = self.rect.top - 1
                    if link.rect.bottom > self.rect.bottom:
                        if self.delay % 2 == 0:
                            self.rect.top = self.rect.top + 1
                    if link.rect.centerx < self.rect.centerx:
                        if self.images != self.walk_left:
                            self.images = self.walk_left
                            self.max_delay = 10
                            self.image_num = 0
                        self.rect.left = self.rect.left - 1
                    else:
                        if self.images != self.walk_right:
                            self.images = self.walk_right
                            self.image_num = 0
                            self.max_delay = 10
                        self.rect.left = self.rect.left + 1
                else:
                    if self.images == self.walk_right:
                        #self.delay = -20
                        self.images = self.slice_right
                        self.max_delay = 5
                        self.image_num = 0
                        self.rect.left = self.rect.left + 5
                    if self.images == self.walk_left:
                        #self.delay = -20
                        self.images = self.slice_left
                        self.max_delay = 5
                        self.image_num = 0
                        self.rect.left = self.rect.left - 5
            else:
                if dify > 50:
                    if link.rect.bottom < self.rect.bottom:
                        if self.images != self.walk_up:
                            self.images = self.walk_up
                            self.image_num = 0
                            self.max_delay = 10
                        self.rect.top = self.rect.top - 1
                    else:
                        if self.images != self.walk_down:
                            self.images = self.walk_down
                            self.image_num = 0
                            self.max_delay = 10
                        self.rect.top = self.rect.top + 1
                    if link.rect.centerx < self.rect.centerx:
                        if self.delay % 2 == 0:
                            self.rect.left = self.rect.left - 1
                    if link.rect.centerx > self.rect.centerx:
                        if self.delay % 2 == 0:
                            self.rect.left = self.rect.left + 1     
                else:
                    if self.images == self.walk_up:
                        self.images = self.slice_up
                        #self.delay = -20
                        self.max_delay = 5
                        self.image_num = 0
                        self.rect.top = self.rect.top - 5
                    if self.images == self.walk_down:
                        #self.delay = -20
                        self.images = self.slice_down
                        self.max_delay = 5
                        self.image_num = 0
                        self.rect.top = self.rect.top + 5
        
        # cycles through her images
        self.delay = self.delay + 1
        if self.delay > self.max_delay:
            if self.max_delay == 5 and self.image_num == 0:
                sounds.slice.play()
            self.delay = 0
            self.image_num = self.image_num + 1
            if self.image_num >= len(self.images):
                self.image_num = 0
                self.hit = False
        
        # changes her image        
        self.image = self.images[self.image_num]
        old_rect = self.rect
        self.rect = self.image.get_rect()
        self.rect.center = old_rect.center
        if self.images == self.slice_down:
            self.rect.right, self.rect.top = old_rect.right, old_rect.top
            if link.rect.right > self.rect.left and link.rect.left < self.rect.right and link.rect.bottom > self.rect.top and link.rect.top < self.rect.bottom + 10 and not self.hit and self.image_num >= 4:
                link.sub_health()
                sounds.link_hurt.play()
                #link.rect.top = self.rect.bottom + 20
                self.hit = True
        if self.images == self.slice_left:
            self.rect.right = old_rect.right
            if link.rect.right > self.rect.left - 10 and link.rect.left < self.rect.right and link.rect.bottom > self.rect.top and link.rect.top < self.rect.bottom and not self.hit and self.image_num >= 4:
                link.sub_health()
                sounds.link_hurt.play()
                #link.rect.right = self.rect.left - 20
                self.hit = True
        if self.images == self.slice_right:
            self.rect.left = old_rect.left
            if link.rect.right > self.rect.left and link.rect.left < self.rect.right + 10 and link.rect.bottom > self.rect.top and link.rect.top < self.rect.bottom and not self.hit and self.image_num >= 4:
                link.sub_health()
                sounds.link_hurt.play()
                #link.rect.left = self.rect.right + 20
                self.hit = True
        if self.images == self.slice_up:
            self.rect.left, self.rect.bottom = old_rect.left, old_rect.bottom
            if link.rect.right > self.rect.left and link.rect.left < self.rect.right and link.rect.bottom > self.rect.top - 10 and link.rect.top < self.rect.bottom and not self.hit and self.image_num >= 4:
                link.sub_health()
                sounds.link_hurt.play()
                #link.rect.bottom = self.rect.top - 20
                self.hit = True
            
class cloud:
    
    def __init__(self, wind):
        
        self.image = pygame.image.load("images/objects/cloud/" + str(random.randint(0, 2)) + ".png").convert()
        self.image = pygame.transform.flip(self.image, random.choice([0, 1]), random.choice([0, 1]))
        self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.image.set_alpha(50)
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(-200, 800), random.randint(-200, 600)]
        self.wind = wind
        self.delay = [0, 0]
        self.blit_before = False
        self.type = "normal"
        
    def action(self, screen, link, navi, text_window, sounds):
        self.delay[0] = self.delay[0] + self.wind[0]
        self.delay[1] = self.delay[1] + self.wind[1]
        if self.delay[0] > 100:
            self.delay[0] = 0
            self.rect.left = self.rect.left + 1
        if self.delay[1] > 100:
            self.delay[1] = 0
            self.rect.top = self.rect.top + 1
                
                