import pygame
import random
import math
'''
screen = pygame .display.set_mode([1024,768])
pygame.display.set_caption("Текущее разрешение: 1024 на 768")
pygame.time.delay (2000)

 

screen = pygame .display.set_mode ([800, 600])
pygame.display.set_caption("Текущее разрешение: 800 на 600")
pygame.time.delay (2000)

screen = pygame .display.set_mode ([640,480])
pygame.display.set_caption("Текущее разрешение: 640 на 480")
pygame.time.delay (2000)

 

screen = pygame.display.set_mode([1024,768], pygame.FULLSCREEN)
pygame.time.delay (2000)

screen = pygame.display.set_mode ([800, 600], pygame.FULLSCREEN)
pygame.time.delay (2000)

screen = pygame.display.set_mode ([640,420], pygame.FULLSCREEN)
pygame.time.delay (2000)

pygame.quit ()
'''
'''
screen = pygame.display.set_mode ([640, 480])
pygame.display.set_caption ("Заливка объекта")


screen.fill ([200,200,200])

pygame.display.flip() 


pygame.time.delay(1000)

screen.fill([255,255,255], [220,50, 200,50])
pygame.display.flip() 
pygame.time.delay (1000)

screen.fill([0,0,255], [220,100, 200,50])
pygame.display.flip() 
pygame.time.delay (1000)

screen.fill([255,0,20], [220,150, 200,50])
pygame.display.flip() 
pygame.time.delay (3000)

screen.fill([255,255,255])


screen.fill([255,0,0], [250,50,70,70])
screen.fill([0,255,0], [320,50,70,70])
screen.fill([0,0,255], [250,120,70,70])
screen.fill([0,255,255], [320,120,70,70])


pygame.display.flip() 


pygame.time.delay(3000)

pygame.quit()
'''

'''
pygame.init()
screen = pygame.display.set_mode ([640, 480])
pygame.display.set_caption ("Цветный точкии")

  

for i in range (10000): 
    x = random.randint (0,639) 
    y = random.randint (0,479) 
    R = random.randint (0,254) 
    G = random.randint (0,254) 
    B = random.randint (0,254) 


    screen.set_at([x,y],[R,G,B])
    pygame.display.flip()


pygame.time.delay(3000)
 

pygame.quit()
'''

def f_graph(x1):
    y1 = math.cos(x1) 
    return (y1)

a = -10 
b = 10 

grModeX = 800 
grModeY = 600 
pygame.init()
screen = pygame.display.set_mode ( [grModeX, grModeY] , pygame.FULLSCREEN)

sx = grModeX/(b - a) 
h = 1/sx 
xmid = grModeX // 2 
ymid = grModeY // 2

x = a
maxF = f_graph(x)
minF = maxF
while x <= b:
    y = f_graph(x)
    if y < minF:
        minF = y 
    if y > maxF:
        maxF = y 
    x = x + h

sy = grModeY/(maxF - minF) 

# рисуем ось X
pygame.draw. line (screen, [255,255,255], [0, ymid] , [grModeX, ymid])

# рисуем ось Y
pygame.draw. line (screen, [255,255,255], [xmid, 0], [xmid, grModeY])


x = a
#y = f_graph(x)

while x <= b:
    y = f_graph(x)
    screen.set_at([xmid + round(sx*x), ymid-round (sy*y)], [255,255,255])
    x = x + h
    pygame.time.delay(50)
    pygame.display.flip ()

pygame.time.delay (2000)

pygame.quit()





