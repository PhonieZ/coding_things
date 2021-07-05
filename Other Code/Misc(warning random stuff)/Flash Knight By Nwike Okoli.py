import pygame
pygame.init()

#Start button menu
print("Welcome to Avion!")
name= input("What is your name?")#Asks user for name
print("Hi "+name+"!")#Inputs users input
print(""+name+", we live in a world full of monsters and villians!")#Narrator talks about the dangers of the world
print("The towns' owner knows this and refuses to speak the truth.")
print("It is up to you to make our world safe again!")#Narrator in trusts user to make the world right


win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Flash Knight")

walkRight = [pygame.image.load('Flash Knight By Nwike Okoli6(12).jpg'),pygame.image.load('Flash Khight By Nwike Okoli6(10).jpg')#This loads my sprite
L = [pygame.image.load('Flash Knight By Nwike Okoli6(8).jpg'),pygame.image.load('Flash Knight By Nwike Okoli6(9).jpg')]
Up = [pygame.image.load("Flash Knight By Nwike Okoli6(5).jpg"),pygame.image.load("Flash Knight By Nwike Okoli6(6).jpg")
Down = [pygame.image.load("Flash Knight By Nwike Okoli6(3).jpg"),pygame.image.load("Flash Knight By Nwike Okoli(2).jpg")
bg = pygame.image.load("Back.PNG")
char = pygame.image.load("Flash Knight By Nwike Okoli6(2).jpg")

clock = pygame.time.clock

x = 50
y = 425
width = 64
height = 64
vel = 5
walkCount = 0
left = False
right = False
1up= False
1down = False

def redrawGameWindow():
        global walkCount
        win.blit(bg (0,0)

        if walkCount + 1 >= 27:
            walkCount = 0
       if left:
            win.blit(walkLeft[walkCount//3], (x,y))
             walkCount += 1

       elif right:
                 win.blit(walkRight[walkCount//3], (x,y))
                 walkCount +=1
       else:
           win.blit(char, (x,y))




        pygame.display.update()
#mainloop
run = True
while run:
      clock.tick(27)


    for event in pygame.event.get():
        if event.type == pygame.quit
            run = False

     keys = pygame.key.get_pressed()
# Controls
     elif keys[pygame.K_LEFT]:
         x -= vel
         left = True
         right = False
     else:
         right=False
         left = False

         walkCount = 0
     if keys[pygame.K_RIGHT]:
         x += vel
         right = True
         left = False
         1down = False
         1up = False
     if keys[pygame.K_UP]:
        y -= vel
        1up = True
        1down = False
        left = False
        right = False

     if keys[pygame.K_DOWN]:
        y += vel
        1up= False
        1down = True
        left = False
        right = False
   redrawGameWindow()
pygame.quit()
