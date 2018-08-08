'''
Contains all the animations for the
story parts of this game
'''

# necesary imports
import pygame, sys, math, random

# my modules
import objects

def beginning(screen):
    '''The first story part.'''
    
    # create clock
    clock = pygame.time.Clock()
    
    # creates font
    font = pygame.font.Font(None, 23)
    
    # variables
    new_tree = 0
    time = 0
    
    # the trees and the road and the fence
    paths = []
    trees = []
    for y in range(-100, 700, 93):
        path = objects.ground([0, y], "images/ground/dirt road/ver path.png", (255, 255, 255))
        path.rect.centerx = 400
        paths.append(path)
    for y in range(800, -150, -90):
        x = random.randint(510, 600)
        tree = objects.swamp_tree([x, y + 50])
        trees.insert(0, tree)
        x = random.randint(150, 200)
        tree = objects.swamp_tree([x, y + 50])
        trees.insert(0, tree)
        x = random.randint(630, 750)
        tree = objects.swamp_tree([x, y])
        trees.insert(0, tree)
        x = random.randint(-20, 120)
        tree = objects.swamp_tree([x, y])
        trees.insert(0, tree)
        
    # the words
    lines = ["Insert story part here,",
    "keep putting more text here,",
    "keep it comming",
    "over half way there",
    "still need more.  He is almost there",
    "Final note....."]
    
    # link walking up images
    images = [] 
    size = 1.5
    for i in range(1, 12):
        image = pygame.image.load("images/link/walk_up/" + str(i) + ".png")
        image.set_colorkey((125, 41, 130))
        image = pygame.transform.rotozoom(image, 0, size)
        images.append(image)
    image = 0
    delay = 0
        
    # the black fog
    fog = pygame.Surface([800, 600])
    fog.set_alpha(200)
    
    # selects the a song to play
    '''pygame.mixer.music.load("music/Princess Zelda Theme.mp3")
    pygame.mixer.music.set_volume(0.20)
    pygame.mixer.music.play(1)'''
    
    # event loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # sets a time delay
        clock.tick(15)
        time = time + 1
        
        # decides when to make a new tree
        new_tree = new_tree + 1
        
        # erases screen
        screen.fill((80, 192, 144))
            
        # displays objects
        for object in paths:
            object.rect.top = object.rect.top + 3
            screen.blit(object.image, object.rect)
            if object.rect.bottom >= 700:
                object.rect.top = -100
        for object in trees:
            object.rect.top = object.rect.top + 3
            screen.blit(object.image, object.rect)
            if object.rect.bottom >= 700:
                trees.remove(object)
                
        # creates new tree
        if new_tree == 10:
            x = random.randint(630, 750)
            tree = objects.swamp_tree([x, -100])
            trees.insert(0, tree)
        if new_tree == 15:
            x = random.randint(-20, 120)
            tree = objects.swamp_tree([x, -100])
            trees.insert(0, tree)
        if new_tree == 20:
            x = random.randint(510, 600)
            tree = objects.swamp_tree([x, -100])
            trees.insert(0, tree)
        if new_tree >= 25:
            x = random.randint(150, 200)
            tree = objects.swamp_tree([x, -100])
            trees.insert(0, tree)
            new_tree = 0
        
        # cycles through link images
        delay = delay + 1
        if delay > 0:
            delay = 0
            image = image + 1
            if image > 10:
                image = 0
        
        # displays link
        rect = images[image].get_rect()
        rect.center = [400, 600]
        rect.top = rect.top - time * 1.7
        screen.blit(images[image], rect)
        
        # makes everything darker
        screen.blit(fog, [0, 0])
        
        if time < 350:
            text = font.render(lines[0][0:time], 1, (255, 255, 255))
            screen.blit(text, [50, 50])
            if time >= 60:
                text = font.render(lines[1][0:time - 60], 1, (255, 255, 255))
                screen.blit(text, [50, 80])
            if time >= 120:
                text = font.render(lines[2][0:time - 120], 1, (255, 255, 255))
                screen.blit(text, [50, 110])
            if time >= 160:
                text = font.render(lines[3][0:time - 160], 1, (255, 255, 255))
                screen.blit(text, [50, 140])
            if time >= 200:
                text = font.render(lines[4][0:time - 200], 1, (255, 255, 255))
                screen.blit(text, [50, 170])
            if time >= 290:
                text = font.render(lines[5][0:time - 290], 1, (255, 255, 255))
                screen.blit(text, [50, 200])
        else:
            fog.set_alpha(200 + time - 350)
            if time >= 405:
                done = True
        
        # displays changes
        pygame.display.flip()