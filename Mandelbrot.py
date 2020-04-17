import pygame

MAX_ITERATION = 0
XMIN, XMAX, YMIN, YMAX = -1.25, 1.25, -1.25, +1.25
LARGEUR, HAUTEUR = 1000, 1000
pas=int(input("Entrez une taille de pixel 1,2,3,4,5  : "))
vitesse=int(input("entrez le pas ditération : "))
pygame.init()
screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            loop = False
    MAX_ITERATION += vitesse
    for y in range(0,HAUTEUR,pas):
        for x in range(0,LARGEUR,pas):
            
            xn = (x * (XMAX - XMIN) / LARGEUR + XMIN)
            yn = (y * (YMIN - YMAX) / HAUTEUR + YMAX)
            cx = 0.285
            cy = 0.01
            n = 0
            while (xn * xn + yn * yn) < 4 and n < MAX_ITERATION: 
            
                tmp_x = xn
                tmp_y = yn
                xn = tmp_x * tmp_x - tmp_y * tmp_y + cx
                yn = 2 * tmp_x * tmp_y + cy
                n = n + 1
            if n == MAX_ITERATION:
                for i in range(pas):
                    screen.set_at((x+i, y+i), (0, 0, 0)) 
            else:
                for i in range(pas):
                    screen.set_at((x+i, y+i), ((3 * n) % 256, (1 * n) % 256, (10 * n) % 256))
            
    pygame.display.flip() 
      
pygame.quit()
