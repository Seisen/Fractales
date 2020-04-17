import math
import random as rd
import pygame as pg
class Main():
    running=True
    nombres_point=0
    clock = pg.time.Clock()
    screen=pg.display.set_mode((1000,1000))
    x=0
    y=0
    basex=[]#listex used for the screen
    basey=[]#listey used for the screen
    basex2=[]#listex used for calculating new points
    basey2=[]#listey used for calculating new points
    cpt=0
    cst_zoom=1.05
    liste_couleur=[(153, 0, 153),(0, 0, 128),(0, 0, 255),(0, 255, 0 ),(255, 255, 255)]
    def __init__(self):
        pg.init()#starting pygame
        self.set_points()
        self.f()
        
    def f(self):#main function
        while self.running:
            self.clock.tick(30)#frame per sec
            self.screen.fill((0,0,0))#color of the background
            for event in pg.event.get():
        
                if event.type == pg.QUIT:#event quit by clocking on the cross
                    self.running=False
                    pg.quit()
            self.zoom()
            self.cst_zoom+=0.05#itering the cst zoom
            for i in range (0,len(self.basex)):#drawing points with pixels
                   self.screen.set_at((int(self.basex2[i]), int(self.basey2[i])),((3 * self.basex[i]) % 256, (1 * self.basex[i]) % 256, (10 * self.basey[i]) % 256))
            pg.display.flip()
        
    def set_points(self):#fill liste y and list x
        self.basex.clear()
        self.basey.clear()
        while len(self.basex)<self.nombres_point:
                r=rd.randint(0,100)
                if r<2 :
                    self.f1()
                elif r<17 :
                    self.f2()
                elif r<30 :
                    self.f3()
                else :
                    self.f4()
                
                if self.x<1000/self.cst_zoom and self.x>0 and self.y<1000/self.cst_zoom and self.y>0:
                    self.basex+=[self.x]
                    self.basey+=[self.y]
    
    def set_point(self):#calculate a new point
        r=rd.randint(0,100)
        if r<2 :
            self.f1()
        elif r<17 :
            self.f2()
        elif r<30 :
            self.f3()
        else :
            self.f4()
        

    def f1(self):
        self.x=50
        self.y=0.27*self.y

    def f2(self):
        self.x=(-0.19*self.x+0.263*self.y+57)
        self.y=(0.246*self.x+0.224*self.y-8.28)

    def f3(self):
        self.x=(0.17*self.x-0.215*self.y+40.8)
        self.y=(0.222*self.x+0.176*self.y+20.539)

    def f4(self):
        self.x=(0.781*self.x+0.034*self.y+10.75)
        self.y=(-0.032*self.x+0.739*self.y+62.17)

    def zoom(self):# if the points are not in the screen calculate a new one and delete the other
        self.basex2.clear()
        self.basey2.clear()
        for i in range(0,len(self.basex)):
            self.basex2+=[self.basex[i]*self.cst_zoom]
            self.basey2+=[self.basey[i]*self.cst_zoom]
            if self.basex2[i]>1000/self.cst_zoom or self.basex2[i]<0 or self.basey2[i]>1000/self.cst_zoom or self.basey2[i]<0:
                self.set_point()
                trouvé=False
                while not trouvé:
                    self.set_point()
                    if self.x<1000/self.cst_zoom and self.x>0 and self.y<1000/self.cst_zoom and self.y>0:
                        self.basex[i]=self.x
                        self.basey[i]=self.y
                        trouvé=True
        self.basex2.clear()
        self.basey2.clear()
        for i in range(0,len(self.basex)):
            self.basex2+=[self.basex[i]*self.cst_zoom]
            self.basey2+=[self.basey[i]*self.cst_zoom]

try :
    Main.nombres_point=int(input("Nombre de points = "))
except ValueError:
    print("Entrez un Nombre")

Main()
