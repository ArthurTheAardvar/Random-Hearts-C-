import pygame
pygame.init()
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)

screen = pygame.display.set_mode((700, 1000))

pygame.display.set_caption("Lunar Lander Simulation")

doExit = False
clock = pygame.time.Clock()

#CONSTANTS


kup = False
kright = False
kleft = False

xPos = 100
yPos = 350

xVel = 0
yVel = -10/60

isOnGround = False
RocketOn = False
crashed = False

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render('Vertical velocity: ', False, (0,200, 200))
text2 = font.render(str(int(yVel)), 1, (0, 200, 200))
text3 = font.render('You Crashed', False, (200, 50, 50))
text4 = font.render('Vertical velocity: ', False, (200, 20, 20))
text5 = font.render(str(int(yVel)), 1, (200, 20, 20))
text6 = font.render('Height: ', False, (20,20,200))
text7 = font.render(str(int(yPos)), 1, (20, 20, 200))



while not doExit:

    clock.tick(60)
    kup = False
    kright = False
    kleft = False
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            doExit = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                kleft = True

            elif event.key == pygame.K_UP:
                kup = True

            elif event.key == pygame.K_RIGHT:
                kright = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                kleft = False

            elif event.key == pygame.K_UP:
                kup = False

            elif event.key == pygame.K_RIGHT:
                kright = False

#input-------------------------------------------------------
        if kleft==True:
            xVel = 1/60
            

        if kup == True:
            yVel = 1.62/60
            isOnGround = False
            RocketOn = True
        
        if kright==True:
            xVel = 1/60

        else:
            yVel += 1.62/60
            RocketOn = False

#physics------------------------------------------------------------

        if isOnGround == True and abs(yVel) >.5:
            xPos = 350
            yPos = 0
            xVel = 0
            yVel = 0
            isOnGround = False

        elif isOnGround == True and abs(yVel) <=.5:
            crashed = False
        print("yVel is", yVel)

        xPos += xVel
        yPos += yVel


        text2 = font.render(str("%.2f" %(yVel*-1)), 1, (0,200,200))
        text5 = font.render(str("%.2f" %(yVel*-1)), 1, (200,20,20))

        text6 = font.render('Height:', False, (20,20,200))
        text7 = font.render(str(int(1000-yPos)), 1, (20,20,200))
        
#render---------------------------------------------------------
        screen.fill ((0,0,0))
        if crashed == True:
            screen.blit(text3, (200,500))
            pygame.display.flip()
            pygame.time.wait(1000)
        if abs(yVel) < .5:
            screen.blit(text1,(10,10))
            screen.blit(text2,(250,10))
        else:
            screen.blit(text4(20,10))
            screen.blit(text5,(250,10))

        screen.blit(text6,(10,60))
        screen.blit(text7,(150,60))

        pygame.draw.rect(screen, (250, 250, 250), (xPos, yPos, 40, 40))
        print(xPos,yPos)
              
        pygame.display.flip()
#end game loop###################################

pygame.quit()



            
