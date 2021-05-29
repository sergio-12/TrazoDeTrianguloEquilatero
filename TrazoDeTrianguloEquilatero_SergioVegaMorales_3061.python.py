import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from PIL import Image
from math import ceil

plt.imshow(Image.open('fondo.png'))

def BASE(steps1, xinc1, yinc1, x1r, y1r):
    for i in range (0, int(steps1)):
        plt.gca().add_patch(Rectangle((x1r, y1r), 1, 1, linewidth=1, edgecolor='r', facecolor='none'))
        plt.ylim(0, 30)
        x1r=(x1r+xinc1); y1r=(y1r+yinc1)
        print ("("+str(round(x1r))+", "+str(round(y1r))+")")

def base(x1, y1, x2r, p1, dx1, dy1):
    while (x1<x2r):
        plt.gca().add_patch(Rectangle((x1, y1), 1, 1, linewidth=1, edgecolor='r', facecolor='none'))
        plt.ylim(0, 30)
        x1+=1;  
        if (p1<0):
            p1=p1+2*dy1
        else:
            p1=p1+(2*dy1)-(2*dx1)
            y1+=1

        print ("("+str(round(x1))+", "+str(round(y1))+")")

def DDA(x1, y1, x2, y2):
    x1r=x1; y1r=y1
    altura=round((x2+1)/2)
    x3=x1+altura
    y3=y1+altura
    dx=abs(x3-x1)
    dy=abs(y3-y1)
    
    if(dx>dy):
        steps=dx
    else:
        steps=dy
    xinc=float(dx/steps)    
    yinc=float(dy/steps)    
    xinc=round(xinc, 1)
    yinc=round(yinc, 1)
    x2=(x2+x1)-1
    dx1=abs(x2-x1)
    dy1=abs(y2-y1)
    
    if(dx1>dy1):
        steps1=dx1
    else:
        steps1=dy1
    xinc1=float(dx1/steps1)    
    yinc1=float(dy1/steps1)    
    xinc1=round(xinc1, 1)
    yinc1=round(yinc1, 1)
    

    for i in range (0, int(steps)):
        plt.gca().add_patch(Rectangle((x1, y1), 1, 1, linewidth=1, edgecolor='pink', facecolor='green'))
        plt.gca().add_patch(Rectangle((x2, y2), 1, 1, linewidth=1, edgecolor='pink', facecolor='green'))
        plt.ylim(0, 30)
        x1=(x1+xinc); y1=(y1+yinc)
        x2=(x2-xinc); y2=(y2+yinc)
        print ("("+str(round(x1))+", "+str(round(y1))+")")
        print ("("+str(round(x2))+", "+str(round(y2))+")")

    BASE(steps1, xinc1, yinc1, x1r, y1r)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Digital Differential Analyzer')
    plt.show()

def Bresenham(x1, y1, x2, y2):
    x2r=x2+x1
    altura=round((x2+1)/2)
    x3=x1+altura
    y3=y1+altura
    x=x1; y=y1; xr=x1; yr=y1
    x2=(x2+x1)-1
    dx1=abs(x2-x1)
    dy1=abs(y2-y1)
    print("dx1: "+str(dx1)+", dy1: "+str(dy1))
    p1=2*dy1-dx1

    dx=abs(x3-x1)
    dy=abs(y3-y1)
    p=2*dy-dx

    if (x2%4!=0) or (x2==5) or (x2>=9):
        x3-=1
    
    while (x<=x3):
        plt.gca().add_patch(Rectangle((x, y), 1, 1, linewidth=1, edgecolor='red', facecolor='yellow'))
        plt.gca().add_patch(Rectangle((x2, y2), 1, 1, linewidth=1, edgecolor='red', facecolor='yellow'))
        plt.ylim(0, 30)
        x+=1; x2-=1; 
        if (p<0):
            p=p+2*dy
        else:
            p=p+(2*dy)-(2*dx)
            y+=1; y2+=1

        print ("("+str(round(x))+", "+str(round(y))+")")
        print ("("+str(round(x2))+", "+str(round(y2))+")")    

    base(x1, y1, x2r, p1, dx1, dy1)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bresenhams')
    plt.show()

if __name__=='__main__':
    tipo=int(input("Ingrese el valor del algoritmo a usar:\n1. Algoritmo DDA\n2. Algoritmo Bresenham\n"))
    x1=int(input("Ingrese el valor de x1: "))    
    y1=int(input("Ingresa el valor de y1: ")) 
    x2=int(input("Ingresa el tamaño de la base (solo se aceptan numeros impares): ")) 
    y2=y1
    if (x1<0):
        x1=x1*-1   

    if (tipo==1):
        DDA(x1, y1, x2, y2)
    elif (tipo==2):
        Bresenham(x1, y1, x2, y2)
    else: print ("OPCION NO VALIDA")