'''
The menu for the game
'''

# necesary imports
import pygame, sys, math, random

class NewFile:
    '''A game file that can be loaded.'''
    
    def __init__(self, position, name, num):
        '''Creates the file.'''
        
        self.num = num
                
        # create the image and rect
        self.image = pygame.image.load("images/menu/file buttons/file button.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        
        # creates font
        font = pygame.font.Font(None, 23)
        self.name = font.render(name, 1, (255, 255, 255))
        
        # sounds
        self.mouse_over_sound = pygame.mixer.Sound("sounds/menu/mouse over.wav")
        self.mouse_over_sound.set_volume(1.00) 
        self.select_sound = pygame.mixer.Sound("sounds/menu/select.wav")
        self.select_sound.set_volume(1.00) 
        self.mouse_over = False
    
    def update(self, screen):
        '''Updates the button'''
        
        # displays the button
        screen.blit(self.image, self.rect)
        self.rect.left = self.rect.left + 40
        self.rect.top = self.rect.top + 3
        screen.blit(self.name, self.rect)
        self.rect.left = self.rect.left - 40
        self.rect.top = self.rect.top - 3
        
        # determines whether the button is clicked on or not
        pressed = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if x > self.rect.left and x < self.rect.right and y > self.rect.top and y < self.rect.bottom:
            self.image = pygame.image.load("images/menu/file buttons/shaded file button.png")
            self.image.set_colorkey((255, 255, 255))
            if not self.mouse_over:
                self.mouse_over = True
                self.mouse_over_sound.play(0)
            if pressed == (1, 0, 0):
                self.select_sound.play(0)
                if self.num == 6:
                    return []
                else:
                    file = open("files//" + str(self.num) + ".txt", 'r')
                    lines = file.read().split('\n')
                    progress = int(lines[0])
                    room = [int(lines[1]), int(lines[2])]
                    position = [int(lines[3]), int(lines[4])]
                    health = int(lines[5])
                    health_fraction = int(lines[6])
                    max_health = int(lines[7])
                    if lines[8] != '':
                        collected_heart_pieces = lines[8].split(' ')
                        collected_heart_pieces = []
                        for i in collected_heart_pieces:
                            self.collected_heart_pieces.append(int(i))
                    else:
                        collected_heart_pieces = []
                    navi_lines = lines[9].split(' end_line ')
                    return [progress,
                            room,
                            position,
                            health,
                            health_fraction,
                            max_health,
                            collected_heart_pieces,
                            navi_lines]
        else:
            self.image = pygame.image.load("images/menu/file buttons/file button.png")
            self.image.set_colorkey((255, 255, 255))
            self.mouse_over = False
        
        # if not returns false
        return False
        

def main_menu(screen):
    '''The main menu.'''
    
    # create clock
    clock = pygame.time.Clock()
    
    # the three file
    files = []
    x = 50
    y = 150
    for i in ['1', '2', '3', '4', '5']:
        file = NewFile([x, y], "Slot " + i, int(i))
        files.append(file)
        y = y + 50
    file = NewFile([x, y], "New File", 6)
    files.append(file)
        
    background = pygame.image.load("images/menu/file buttons/background.jpg")
    background = pygame.transform.scale(background, [800, 600])
    
    # the black fog
    front = pygame.Surface([800, 600])
    front.set_alpha(0)
    time = 0
    start = False
    return_list = []
    
    # event loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # sets a time delay
        clock.tick(50)
        
        # erases screen
        screen.blit(background, [0, 0])
        
        # cycles through the buttons
        if not start:
            for file in files:
                list = file.update(screen)
                if list != False:
                    start = True
                    return_list = list
        else:
            for file in files:
                
                # displays the button
                screen.blit(file.image, file.rect)
                file.rect.left = file.rect.left + 40
                file.rect.top = file.rect.top + 3
                screen.blit(file.name, file.rect)
                file.rect.left = file.rect.left - 40
                file.rect.top = file.rect.top - 3

        # makes the front more opaque
        if start:
            time = time + 2
            front.set_alpha(time)
            if time >= 255:
                return return_list
                
        # displays the front
        screen.blit(front, [0, 0])
            
        
        # displays changes
        pygame.display.flip()