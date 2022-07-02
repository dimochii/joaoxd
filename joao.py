'''
import pygame
pygame.init()
dis=pygame.display.set_mode((600,600))
pygame.display.update()
pygame.display.set_caption('A historia de joao :)')


joao = pygame.image.load('joao.jpg').convert_alpha()




while True:
    dis.blit(joao,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        pygame.dispaly.update()
 
'''
# import pygame module in this program
import pygame
import random


#randomly chooses a movement for an impostor
def moveImpostor(impostors):
    for i in impostors:
        #randomly moves x
        if random.randint(0,1) == 1:
            if random.randint(0,1) == 1:
                i[1][0] += 50
            else:
                i[1][0] -= 50
        #randomly moves y
        if random.randint(0,1) == 1:
            if random.randint(0,1) == 1:
                i[1][1] += 50
            else:
                i[1][1] -= 50
    return impostors

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()


  
# define the RGB value
# for white colour
white = (0, 0, 0)
  
# assigning values to X and Y variable
X = 1920
Y = 1080

joaoX = 0
joaoY = 0

#(color,(x,y))
joaoBullets = []

#imposters
imposters = []


# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y ))
  
# set the pygame window name
pygame.display.set_caption('A historia do joao :)')
  
# create a surface object, image is drawn on it.
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background,(1920,1080))
joao = pygame.image.load('joao.jpg')
clock = pygame.time.Clock()
currentTime = 0
for i in range(5):
    #criar o impostor
    impostor = pygame.image.load('impostor.png')
    impostor = pygame.transform.scale(impostor,(128,128))
    #adiciono-o a lista
    x = random.randrange(0,1920)
    y = random.randrange(0,1080)
    if random.randint(0,2) == 1:
        impostor = pygame.transform.flip(impostor,True,False)
    imposters.append((impostor,[x,y]))
#fora do ciclo for
# infinite loop
while True :
  
    # completely fill the surface object
    # with white colour
    display_surface.fill(white)
    dt = clock.tick()
    currentTime += dt

    if currentTime > 200:
        imposters = moveImpostor(imposters)
        currentTime = 0
  
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(background, (0,0))
    for i in imposters:
        display_surface.blit(i[0],(i[1][0],i[1][1]))
    display_surface.blit(joao, (joaoX, joaoY))
  
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
  
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT :
  
            # deactivates the pygame library
            pygame.quit()
  
            # quit the program.
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                joaoX += 100
            if event.key == pygame.K_a:
                if joaoX - 100 >= 0:
                    joaoX -= 100
            if event.key == pygame.K_s:
                joaoY += 100
            if event.key == pygame.K_w:
                joaoY -= 100
            if event.key == pygame.K_SPACE:
                print("space")
  
        # Draws the surface object to the screen.  
        pygame.display.update() 

