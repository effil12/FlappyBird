import sys
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 750))

backgroundImage = pygame.image.load("background.jpg")

birdImage = pygame.image.load("bird1.png")
birdX = 50
birdY = 300
birdYChange = 0

obstacleWidth = 70
obstacleHeight = random.randint(150, 450)
obstacleXChange = -2
obstacleX = 500
obstacleGap = 150

score = 0
scoreList = []

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)

def gameOverScreen ():
    maxScore = max(scoreList)
    display1 = game_over_font1.render(f"GAME OVER", True, (200,35,35))
    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maxScore}", True, (255, 255, 255))
    
    screen.blit(display1, (50, 300))
    screen.blit(display2, (50, 400))

    print("in game over")

    if score == maxScore:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!!", True, (200,35,35))
        screen.blit(display3, (80, 100))

    pygame.display.update()

startFont = pygame.font.Font('freesansbold.ttf', 32)
def startScreen ():
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 255, 255))
    screen.blit(display, (20, 200))
    pygame.display.update()

def fpsCounter ():
    fpsText = str(int(clock.get_fps()))
    fpsDisplay = pygame.font.Font("freesansbold.ttf", 25).render("FPS: " + fpsText , 1, (255, 255, 255))
    screen.blit(fpsDisplay,(10, 50))

def scoreDisplay ():
    scoreDisplay = pygame.font.Font("freesansbold.ttf", 32).render(f"Score: {score}", True, (255, 255, 255))
    
    screen.blit(scoreDisplay, (10, 10))

def collisionDetection ():
    # birds width is 64 pixels
    if obstacleX >= 50 and obstacleX <= 114:
        if birdY <= obstacleHeight or birdY >= (obstacleHeight + 150) - 64 :
            return True
    else:
        return False

def displayObstacle (height):
    bottomObstacleHeight = 635 - height - obstacleGap
    obstacleTopColor = (211, 253, 117)
    obstacleBottomColor = (50, 50, 50)
    
    # top obstacle
    pygame.draw.rect(screen, obstacleTopColor, (obstacleX, 0, obstacleWidth, height))
    # bottom obstacle
    pygame.draw.rect(screen, obstacleBottomColor, (obstacleX, height + obstacleGap, obstacleWidth, bottomObstacleHeight))

def displayBird (x, y):
    screen.blit(birdImage, (x, y)) 

clock = pygame.time.Clock()

running = True
waiting = True
print("RUNNING!")
collisionHappened = False

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    screen.blit(backgroundImage, (0, 0))

    while waiting:
        if collisionHappened:
            gameOverScreen()
        else:
            startScreen()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    birdY = 300
                    birdYChange = -5
                    obstacleX = 500
                    waiting = False
            if event.type == pygame.QUIT:
                running = False 
                waiting = False
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("clicked Space down")
                birdYChange = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                birdYChange = 3

    birdY = birdY + birdYChange

    if birdY <= 0:
        birdY= 0
    elif birdY >= 571:
        birdY = 571

    obstacleX = obstacleX + obstacleXChange
    if obstacleX <= -10:
        score += 1 
        obstacleX = 500
        obstacleHeight = random.randint(100, 450)
  
    collision = collisionDetection()
    collisionHappened = collision

    if collision:
        scoreList.append(score)
        waiting = True
    
    else:
        fpsCounter()
        scoreDisplay()
        displayObstacle(obstacleHeight)
        displayBird(birdX, birdY)
    
    # update display after each iteration
    pygame.display.update()

print("Game closeed")
pygame.quit()

