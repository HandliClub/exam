import pygame
import math

###Граф окно с заданными размерами
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
'''

###Граф окно с заданными размерами###Заливка окна цветом
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])
pygame.display.flip()
'''
###Граф окно с заданными размерами###Красный круг
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])
pygame.draw.circle(screen,[255,0,0],[100,100],30,0)
pygame.display.flip()
'''
###Граф окно с заданными размерами###Окр, прям, линия
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])
pygame.draw.circle(
    screen,[255,0,0],[100,100],30,1)

pygame.draw.rect(
    screen,[0,255,0],[100,100,50,50],0)

plotPoints = [[0,0],[30,30],[60,0],[90,30],[120,0]]

pygame.draw.lines(
    screen,[0,0,255], False, plotPoints, 2)

pygame.display.flip()
'''
###Граф окно с заданными размерами###Точка, синусоида
"""
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])

for x in range(0, 300):
    y = int(math.sin(x/300.0*4*math.pi)*150 + 150)
    screen.set_at([x,y],[0,0,0])

pygame.display.flip()
"""
###Граф окно с заданными размерами###Линия, синусоида
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])
plotPoint = []

for x in range(0, 300):
    y = int(math.sin(x/300.0*4*math.pi)*150 + 150)
    plotPoint.append([x,y])

pygame.draw.lines(
    screen,[0,0,0], False, plotPoint, 1)

pygame.display.flip()
'''
###Граф окно с заданными размерами###Текст
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])

fontObj = pygame.font.Font('9688.ttf',20)

text = fontObj.render('Handli',True,(255,255,0),(0,0,255))

screen.blit(text,[70,100])

pygame.display.flip()
'''
####Граф окно с заданными размерами###Загрузка внешнего изображения
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])

my_ball = pygame.image.load("Ball.png")

screen.blit(my_ball,[50,50])

pygame.display.flip()
'''
####Граф окно с заданными размерами###Загрузка спрайта###Использование встроенных классов
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

img_file = "Ball.png"
location = [10,10]
ball = MyBallClass(img_file, location)
screen.blit(ball.image,ball.rect)

pygame.display.flip()
'''

####Граф окно с заданными размерами###Загрузка спрайта###Использование встроенных классов
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed





            
img_file = "Ball.png"
location = [10,10]
speed = [2,2]
ball = MyBallClass(img_file, location, speed)

while True:
    pygame.time.delay(20)

    screen.fill([255,255,255])

    ball.move()

    screen.blit(ball.image,ball.rect)

    pygame.display.flip()
'''
###
'''
pygame.init()
screen = pygame.display.set_mode([300,300])
screen.fill([255,255,255])

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 300:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 300:
            self.speed[1] = -self.speed[1]



            
img_file = "Ball.png"
location = [10,10]
speed = [2,2]
ball = MyBallClass(img_file, location, speed)

while True:
    pygame.time.delay(20)

    screen.fill([255,255,255])

    ball.move()

    screen.blit(ball.image,ball.rect)

    pygame.display.flip()
'''







