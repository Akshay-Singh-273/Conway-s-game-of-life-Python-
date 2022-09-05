#conway's game of life

import cv2
import numpy as np
import random

simD = int(input("Enter dimentions of simulation window (larger window can slow down generation cycle)"))

img = np.zeros((simD,simD,3),np.uint8)
cv2.namedWindow('C_GOL')
cv2.imshow('C_GOL',img)

randm = simD*90

while randm > -1:
    img[random.randint(0,simD-1)][random.randint(0,simD-1)] = [255,255,255]
    randm -= 1

#img[200:300,225:275] = [255,255,255]
#img[200:300,205:295] = [255,255,255]
#img[100:250,150:200] = [255,255,255]
#print(img[250][250][0])

def fkShitUp():
    row = -1
    #print("executed!")
    while row < simD-1:
        row += 1
        col = -1
        #print("row:",row)
        while col < simD-1: 
            col += 1
            #print("col:",col)
            counter = 0
            if img[row][col][0] == 0:
                r = row - 2
                while r <= row:
                    r += 1
                    c = col - 2
                    #print("r:",r)
                    while c <= col:
                        c += 1
                        #print("c:",c)
                        if ((r == row) and (c == col) or (r > simD-1) or (c > simD-1)):
                            #print("passed!")
                            continue
                        if img[r][c][0] == 255:
                            #print("live Cell")
                            counter += 1
                        #else:
                            #print("dead Cell")
                if counter == 3:
                    img[row][col] = [255,255,255]
            else:
                r = row - 2
                while r <= row + 1:
                    r += 1
                    c = col - 2
                    while c <= col + 1:
                        c += 1
                        if ((r == row and c == col) or (r > simD-1) or (c > simD-1)):
                            continue
                        else:
                            if img[r][c][0] == 255:
                                counter += 1
                                #print("dead Cell")
                if counter == 2 or counter == 3:
                    continue
                else:
                    img[row][col] = [0,0,0]

while True:
    cv2.imshow('C_GOL',img)
    cv2.waitKey(1)
    fkShitUp()

cv2.waitKey(0)
cv2.destroyWindow('C_GOL')
