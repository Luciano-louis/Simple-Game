import pygame 
import random 

pygame.init() 

#screen width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

#Image links 

player = pygame.image.load("jet.png")
enemy1 = pygame.image.load("missile.png")
enemy2 = pygame.image.load("missile.png")
enemy3 = pygame.image.load("missile.png")
enemy4 = pygame.image.load("missile.png")
enemy5 = pygame.image.load("missile.png")
enemy6 = pygame.image.load("missile.png")
enemy7 = pygame.image.load("missile.png")
enemy8 = pygame.image.load("missile.png")
enemy9 = pygame.image.load("missile.png")
enemy10 = pygame.image.load("missile.png")
enemy11 = pygame.image.load("missile.png")
enemy12 = pygame.image.load("missile.png")
enemy13 = pygame.image.load("missile.png")
enemy14 = pygame.image.load("missile.png")
enemy15 = pygame.image.load("missile.png")
enemy16 = pygame.image.load("missile.png")
enemy17 = pygame.image.load("missile.png")
enemy18 = pygame.image.load("missile.png")
enemy19 = pygame.image.load("missile.png")
enemy20 = pygame.image.load("missile.png")
prize = pygame.image.load("beer.png")

#boundary detection

image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
enemy4_height = enemy4.get_height()
enemy4_width = enemy4.get_width()
enemy5_height = enemy5.get_height()
enemy5_width = enemy5.get_width()
enemy6_height = enemy6.get_height()
enemy6_width = enemy6.get_width()
enemy7_height = enemy7.get_height()
enemy7_width = enemy7.get_width()
enemy8_height = enemy8.get_height()
enemy8_width = enemy8.get_width()
enemy9_height = enemy9.get_height()
enemy9_width = enemy9.get_width()
enemy10_height = enemy10.get_height()
enemy10_width = enemy10.get_width()
enemy11_height = enemy11.get_height()
enemy11_width = enemy11.get_width()
enemy12_height = enemy12.get_height()
enemy12_width = enemy12.get_width()
enemy13_height = enemy13.get_height()
enemy13_width = enemy13.get_width()
enemy14_height = enemy14.get_height()
enemy14_width = enemy14.get_width()
enemy15_height = enemy15.get_height()
enemy15_width = enemy15.get_width()
enemy16_height = enemy16.get_height()
enemy16_width = enemy16.get_width()
enemy17_height = enemy17.get_height()
enemy17_width = enemy17.get_width()
enemy18_height = enemy18.get_height()
enemy18_width = enemy18.get_width()
enemy19_height = enemy19.get_height()
enemy19_width = enemy19.get_width()
enemy20_height = enemy20.get_height()
enemy20_width = enemy20.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

#player and enemy positions

playerXPosition = 10
playerYPosition = 300

prizeXPosition = 990
prizeYPosition = 300

#enemy start position

enemy1XPosition =  screen_width+200
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition =  screen_width+400
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width+600
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)
enemy4XPosition =  screen_width+800
enemy4YPosition =  random.randint(0, screen_height - enemy4_height)
enemy5XPosition =  screen_width+1000
enemy5YPosition =  random.randint(0, screen_height - enemy5_height)
enemy6XPosition =  screen_width+1200
enemy6YPosition =  random.randint(0, screen_height - enemy6_height)
enemy7XPosition =  screen_width+1400
enemy7YPosition =  random.randint(0, screen_height - enemy7_height)
enemy8XPosition =  screen_width+1600
enemy8YPosition =  random.randint(0, screen_height - enemy8_height)
enemy9XPosition =  screen_width+1800
enemy9YPosition =  random.randint(0, screen_height - enemy9_height)
enemy10XPosition =  screen_width+2000
enemy10YPosition =  random.randint(0, screen_height - enemy10_height)
enemy11XPosition =  screen_width+2200
enemy11YPosition =  random.randint(0, screen_height - enemy11_height)
enemy12XPosition =  screen_width+2400
enemy12YPosition =  random.randint(0, screen_height - enemy12_height)
enemy13XPosition =  screen_width+2600
enemy13YPosition =  random.randint(0, screen_height - enemy13_height)
enemy14XPosition =  screen_width+2800
enemy14YPosition =  random.randint(0, screen_height - enemy14_height)
enemy15XPosition =  screen_width+3000
enemy15YPosition =  random.randint(0, screen_height - enemy15_height)
enemy16XPosition =  screen_width+3200
enemy16YPosition =  random.randint(0, screen_height - enemy16_height)
enemy17XPosition =  screen_width+3400
enemy17YPosition =  random.randint(0, screen_height - enemy17_height)
enemy18XPosition =  screen_width+3600
enemy18YPosition =  random.randint(0, screen_height - enemy18_height)
enemy19XPosition =  screen_width+3800
enemy19YPosition =  random.randint(0, screen_height - enemy19_height)
enemy20XPosition =  screen_width+4000
enemy20YPosition =  random.randint(0, screen_height - enemy20_height)



#Direction checks 

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

while 1:

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(enemy4, (enemy4XPosition, enemy4YPosition))
    screen.blit(enemy5, (enemy5XPosition, enemy5YPosition))
    screen.blit(enemy6, (enemy6XPosition, enemy6YPosition))
    screen.blit(enemy7, (enemy7XPosition, enemy7YPosition))
    screen.blit(enemy8, (enemy8XPosition, enemy8YPosition))
    screen.blit(enemy9, (enemy9XPosition, enemy9YPosition))
    screen.blit(enemy10, (enemy10XPosition, enemy10YPosition))
    screen.blit(enemy11, (enemy11XPosition, enemy11YPosition))
    screen.blit(enemy12, (enemy12XPosition, enemy12YPosition))
    screen.blit(enemy13, (enemy13XPosition, enemy13YPosition))
    screen.blit(enemy14, (enemy14XPosition, enemy14YPosition))
    screen.blit(enemy15, (enemy15XPosition, enemy15YPosition))
    screen.blit(enemy16, (enemy16XPosition, enemy16YPosition))
    screen.blit(enemy17, (enemy17XPosition, enemy17YPosition))
    screen.blit(enemy18, (enemy18XPosition, enemy18YPosition))
    screen.blit(enemy19, (enemy19XPosition, enemy19YPosition))
    screen.blit(enemy20, (enemy20XPosition, enemy20YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # Button checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        #event checks if the key is up
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
 
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1

    if keyDown == True:
        if playerYPosition < screen_width - image_width:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0 :
            playerXPosition -= 1

    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1
    
        # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    enemy4Box = pygame.Rect(enemy4.get_rect())
    enemy4Box.top = enemy4YPosition
    enemy4Box.left = enemy4XPosition

    enemy5Box = pygame.Rect(enemy5.get_rect())
    enemy5Box.top = enemy5YPosition
    enemy5Box.left = enemy5XPosition

    enemy6Box = pygame.Rect(enemy6.get_rect())
    enemy6Box.top = enemy6YPosition
    enemy6Box.left = enemy6XPosition

    enemy7Box = pygame.Rect(enemy7.get_rect())
    enemy7Box.top = enemy7YPosition
    enemy7Box.left = enemy7XPosition

    enemy8Box = pygame.Rect(enemy8.get_rect())
    enemy8Box.top = enemy8YPosition
    enemy8Box.left = enemy8XPosition

    enemy9Box = pygame.Rect(enemy9.get_rect())
    enemy9Box.top = enemy9YPosition
    enemy9Box.left = enemy9XPosition

    enemy10Box = pygame.Rect(enemy10.get_rect())
    enemy10Box.top = enemy10YPosition
    enemy10Box.left = enemy10XPosition

    enemy11Box = pygame.Rect(enemy11.get_rect())
    enemy11Box.top = enemy11YPosition
    enemy11Box.left = enemy11XPosition

    enemy12Box = pygame.Rect(enemy12.get_rect())
    enemy12Box.top = enemy12YPosition
    enemy12Box.left = enemy12XPosition

    enemy13Box = pygame.Rect(enemy13.get_rect())
    enemy13Box.top = enemy13YPosition
    enemy13Box.left = enemy13XPosition

    enemy14Box = pygame.Rect(enemy14.get_rect())
    enemy14Box.top = enemy14YPosition
    enemy14Box.left = enemy14XPosition

    enemy15Box = pygame.Rect(enemy15.get_rect())
    enemy15Box.top = enemy15YPosition
    enemy15Box.left = enemy15XPosition

    enemy16Box = pygame.Rect(enemy16.get_rect())
    enemy16Box.top = enemy16YPosition
    enemy16Box.left = enemy16XPosition

    enemy17Box = pygame.Rect(enemy17.get_rect())
    enemy17Box.top = enemy17YPosition
    enemy17Box.left = enemy17XPosition

    enemy18Box = pygame.Rect(enemy18.get_rect())
    enemy18Box.top = enemy18YPosition
    enemy18Box.left = enemy18XPosition

    enemy19Box = pygame.Rect(enemy19.get_rect())
    enemy19Box.top = enemy19YPosition
    enemy19Box.left = enemy19XPosition

    enemy20Box = pygame.Rect(enemy20.get_rect())
    enemy20Box.top = enemy20YPosition
    enemy20Box.left = enemy20XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # collision of the boxes:
    
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box) or playerBox.colliderect(enemy4Box) or playerBox.colliderect(enemy5Box) or playerBox.colliderect(enemy6Box) or playerBox.colliderect(enemy7Box) or playerBox.colliderect(enemy8Box) or playerBox.colliderect(enemy9Box) or playerBox.colliderect(enemy10Box) or playerBox.colliderect(enemy11Box) or playerBox.colliderect(enemy12Box) or playerBox.colliderect(enemy13Box) or playerBox.colliderect(enemy14Box) or playerBox.colliderect(enemy15Box) or playerBox.colliderect(enemy16Box) or playerBox.colliderect(enemy17Box) or playerBox.colliderect(enemy18Box) or playerBox.colliderect(enemy19Box) or playerBox.colliderect(enemy20Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quit game and exit window: 
        
        pygame.quit()
        exit(0)
        
    # If the player reaches prize
    
    if playerBox.colliderect(prizeBox):
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemy approach the player and the speed.
    
    enemy1XPosition -= 1
    enemy2XPosition -= 1
    enemy3XPosition -= 1
    enemy4XPosition -= 1
    enemy5XPosition -= 1
    enemy6XPosition -= 1
    enemy7XPosition -= 1
    enemy8XPosition -= 1
    enemy9XPosition -= 1
    enemy10XPosition -= 1
    enemy11XPosition -= 1
    enemy12XPosition -= 1
    enemy13XPosition -= 1
    enemy14XPosition -= 1
    enemy15XPosition -= 1
    enemy16XPosition -= 1
    enemy17XPosition -= 1
    enemy18XPosition -= 1
    enemy19XPosition -= 1
    enemy20XPosition -= 1
    
    
    
    
    
    # ================The game loop logic ends here. =============
