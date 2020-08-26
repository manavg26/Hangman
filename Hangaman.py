"""
Created on Tue Aug 25 20:37:56 2020

@author: Admin
"""


import pygame
import math
pygame.init()

#game window
HT,WTH=600,800
win=pygame.display.set_mode((WTH,HT))
pygame.display.set_caption("Hangman! :o")
STRING=input("Enter Word")
STRING= STRING.upper()
desc=input("Write Clue for Word")
#images
img=[]
for i in range(7):
    address = "C:\\Users\\Admin\\Desktop\\PythonProject\\hangman"+str(i)+".PNG"
    image = pygame.image.load(address)
    img.append(image)

#buttons spacing
RAD=20
GAP=15
alpha=[]
start_x=int((WTH-(RAD*2+GAP)*13)/2)
start_y=450
for i in range(26):
    x = start_x+GAP*2+((RAD*2+GAP)*(i%13))
    y = start_y+((RAD*2+GAP)*(i//13))
    alpha.append([x,y,chr(i+65),True])



#Font
font=pygame.font.SysFont('comicsans',40)
#hangman_image status
status=0

# game loop
SPEED=40
clk=pygame.time.Clock()
run= True

def draw():
    win.blit(img[status], (100, 100))

    #draw buttons   
    for alp in alpha:
        x,y,z,visible=alp
        if visible==True:
            pygame.draw.circle(win, (255, 255, 255), (x, y),RAD,4)
            txt=font.render(z,1,(255,255,255))
            clue=font.render(desc,1,(255,255,255))
            win.blit(txt,(round(x-txt.get_width()/2),round(y-txt.get_height()/2)))
            win.blit(clue,(round((WTH-img[status].get_width()-100)/1.3),150))
    
    pygame.display.update() 




j=0
while run:
    clk.tick(SPEED)
    if status < len(img):
        draw()
    else:
        print("Better Luck Next Time")
        run=False
    EVENT=pygame.event.get()
    for event in EVENT:
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for alp in alpha:
                x,y,z,visible=alp
                if j<len(STRING) :
                    dis=math.sqrt((x-mx)**2+(y-my)**2)
                    if dis<RAD:
                        if z==STRING[j]:
                            print(z,end=" ")
                            j=j+1
                            
                        else:
                            alp[3]=False
                            status=status+1
                            
                else:
                    
                    run=False
print(end="\n\n")
if status == 0:
    print("Strike!!!")
elif status<len(img):
    print("Good Job")
pygame.quit()

