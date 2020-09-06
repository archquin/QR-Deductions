#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:03:31 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:12:42 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 05:50:58 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:52:12 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:58:01 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:36:26 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:12:14 2020

@author: fadewell
"""

#import math
import qrcode
#import pyqrcode
#import pandas as pd
#import numpy as np
#from pandas import D
import matplotlib.pyplot as plt
import cv2 as cv2
detector = cv2.QRCodeDetector()

#import pandas as pd
#import
ensemble = 0
white = 0
ijk = 0
while ensemble <1 :
    dimensions = 0
    white = '-2'   ######## white <---->Green, Cream           1
    Yellow = '-5'   ####-2,-3,-4,----> Yellow==k @ k = 0
    Blue = '-3'      ##### -3,-4,-5 ---->Blue == j @ j = -1
    Somon = '4'    ##### 1,3,4,5 -----> Somon = k @ k = 0
    Pink = '-1'      ###### 2,3,4 ----> Pink = ij @ ij = 0
    Green= '1'      ##### 1,-1,-2,-3 ----> Green = j @ j = 2
    black = '-1' ##### -2,-3,-4 -----> black == i == ij@ ij = 0
    Tree = '1'  #### i 3x
    Cream = '2'  ######## 3,4,5-------> is white too 2
    while dimensions < 1:
        qqrrr22 = qrcode.make(Cream)
        qqrrr22.save('r000partEnQtities000r.png')
        iiim0g0mgg111 = cv2.imread("r000partEnQtities000r.png")
        gggrreeeeyy0 = cv2.cvtColor(iiim0g0mgg111, cv2.COLOR_XYZ2RGB)
        cream, bbox, straight_qrcode = detector.detectAndDecode(iiim0g0mgg111)
        
        yaw = 1
        while yaw > 0:
            
            i = 0
            ikj = i
            qr2 = qrcode.make(Tree)
            qr2.save('partEntities00.png')
            img111 = cv2.imread("partEntities00.png")
            greyyyy = cv2.cvtColor(img111, cv2.COLOR_BGR2RGB)
            tree, bbox, straight_qrcode = detector.detectAndDecode(img111)
            Tree = int(Tree)   
            jik = int(Tree)                        
            while i < Tree:

                j = 2
                
                qqrrr22 = qrcode.make(black)
                qqrrr22.save('r000partEntities000r.png')
                iiim00mgg111 = cv2.imread("r000partEntities000r.png")
                ggrreeeeyy0 = cv2.cvtColor(iiim00mgg111, cv2.COLOR_HSV2RGB)
                Black, bbox, straight_qrcode = detector.detectAndDecode(iiim00mgg111)
                i = 0
                ij = 0
                while i < j :
                    i = ij
           
                    qqrr22 = qrcode.make(Green)
                    qqrr22.save('000partEntities000.png')
                    iiim0mgg111 = cv2.imread("000partEntities000.png")
                    ggrreeeyy0 = cv2.cvtColor(iiim0mgg111, cv2.COLOR_RGB2XYZ)
                    green, bbox, straight_qrcode = detector.detectAndDecode(iiim0mgg111)
                    
                    Cream = int(Cream)
                    j = 2
                    kj = j
                    k = 0
                    ijk = ij
                    ji = int(Green)
                    Green = int(Green)
                    while j > Green :## i<j
                       # ij = ijk
                        #i = ij
                        qr22 = qrcode.make(Pink)
                        qr22.save('00partEntities00.png')
                        iiimmgg111 = cv2.imread("00partEntities00.png")
                        ggrreeeyy = cv2.cvtColor(iiimmgg111, cv2.COLOR_BGR2HLS)
                        pink, bbox, straight_qrcode = detector.detectAndDecode(iiimmgg111)
                        
                        jk = 2
                        ###i = 0 or 
                        ij = 0
                        ik = k
                        JiK = 0
                        print('a: from 1 to 4')
                        a = input()
                        a = int(a)
                     #   i=ij#############################################
                        while ij < jk:
                            
                           # b = input()
                            k = 0
                            ik = k
                            ki = k
                            qr22 = qrcode.make(Somon)
                            qr22.save('0partEntities0.png')
                            iiimg111 = cv2.imread("0partEntities0.png")
                            ggreeyy = cv2.cvtColor(iiimg111, cv2.COLOR_BGR2Luv)
                            somon, bbox, straight_qrcode = detector.detectAndDecode(iiimg111)
                            i = int(Somon)
                            
                            Somon = int(Somon)
                            while  k  < Somon :###### X KiJ X
                                
                                
                                 ### -2
                                qqr2 = qrcode.make(Blue)
                                qqr2.save('0partEntities.png')
                                iimg11 = cv2.imread("0partEntities.png")
                                ggreyy = cv2.cvtColor(iimg11, cv2.COLOR_BGR2LAB)
                                blue, bbox, straight_qrcode = detector.detectAndDecode(iimg11)
                                
                                j = -1
                                while j < k:
                                    
                                    x = 0 
                                    k=-1
                                    qr1 = qrcode.make(Yellow)
                                    qr1.save('partEntities.png')
                                    img11 = cv2.imread("partEntities.png")
                                    greyy = cv2.cvtColor(img11, cv2.COLOR_BGR2HSV)
                                    yellow, bbox, straight_qrcode = detector.detectAndDecode(img11)
                                    
                                  #  Yellow = yellow
                                    while k <  i:
                                        
                                        qr = qrcode.make(white)
                                        qr.save('partEntities0.png')
                                        img1 = cv2.imread("partEntities0.png")
                                        greyyy = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                                        White, bbox, straight_qrcode = detector.detectAndDecode(img1)
                                        ik = 0
                                        Nn=1    
                                        white = int(white) ### white == jk , -6
                                        jk = 2
                                        KiJ = 0
                                        
                                        while ik < jk:
                                   

                                            
                                           
                                            white = int(white)
                                            if ik != white:
                                                white+= 1
                                                z = -ik+1
                                                print(z)
                                                qr6 = qrcode.make(z)
                                                qr6.save('White.png')
                                                aWhite = cv2.imread("White.png")
                                                cWhite = cv2.cvtColor(aWhite, cv2.COLOR_BGR2RGB)
                                                data, bbox, straight_qrcode = detector.detectAndDecode(aWhite)
                                                plt.imshow(cWhite)
                                                plt.show()
                                          #      if ik == jk:
                                               #     jk -=1
                                                  #  ik = jk
                                        
                                            if  ik == white:
                                                white = White
                                                ik = 3
                                    #        plt.imshow(greyyyy)
                                     #       plt.show()
                                         #   
                                            KiJ+=1
                                      #  ik  = i
                                  
                                      #  plt.imshow(greyyy)
                                     #   plt.show()
                                        Yellow = int(Yellow)
                                        
                                        if  k != Yellow:
                                            Yellow +=1
                                          #  k -=1
                                            x += 1
                                            
                                            if x == a:
                                                print(x)
                                                qr6 = qrcode.make(x)
                                                qr6.save('Yellow.png')
                                                aYellow = cv2.imread("Yellow.png")
                                                cYellow = cv2.cvtColor(aYellow, cv2.COLOR_BGR2GRAY)
                                                data, bbox, straight_qrcode = detector.detectAndDecode(aYellow)
                                                plt.imshow(cYellow)
                                                plt.show()
                                                print('HERE')
                                            
                                        
                                        if k == Yellow :
                                            Yellow = yellow
                                            print(Yellow)
                                            k = 5
                                          
                                      #  jk = k############
                                        
                                #    plt.imshow(greyy)
                              #      plt.show()
                                    Blue = int(Blue)
                              #      print(i,j,k)
                                    
                                    if j != Blue:  #### blue -2
                                       # j -= 1
                                        Blue +=1
                                        y = -j-2
                                        print(y)
                                        qr6 = qrcode.make(y)
                                        qr6.save('Blue.png')
                                        aBlue = cv2.imread("Blue.png")
                                        cBlue = cv2.cvtColor(aBlue, cv2.COLOR_BGR2HSV)
                                        data, bbox, straight_qrcode = detector.detectAndDecode(aBlue)
                                        plt.imshow(cBlue)
                                      #  plt.imshow(greyy)
                                        plt.show()
                                      #  print('here',i,i,k)
                                        
                                     #   if j == Blue:
                                            
                                       
                                    if j == Blue:
                                        Blue = blue
                                        j = int(Cream)
                                        jk = j
                                        print('here',Blue)
                                    
                                    
                                    k = ki
                                    
                       
                                JiK += 1
                                print(JiK) 
                             #   plt.imshow(ggreyy)
                              #  plt.show()
                                qr6 = qrcode.make(KiJ)
                                qr6.save('Somon.png')
                                aSomon = cv2.imread("Somon.png")
                                cSomon = cv2.cvtColor(aSomon, cv2.COLOR_BGR2Lab)
                                data, bbox, straight_qrcode = detector.detectAndDecode(aSomon)
                                plt.imshow(cSomon)
                              #  plt.imshow(ggreyy)
                                plt.show()
                                if k != i:
                                    Somon += 1
                                    i-=1
                                    #if i ==k:
                                      #  Somon = -i
                                      #  print('here')
                                    
                                if k == i:
                                   print('y')
                                   Somon = -i
                                  # Somon = somon
                                 #  Somon -=1
                                   # if i!= Somon:
                                    #    i-= 1
                                   # i = int(somon)
                                    #ik = i
                                 #   JiK = Somon
                                  #  Somon = i
                                
                                
                            Somon = somon
                           
                            
                           
                            
                            
                            i = ij   
                            Pink = int(Pink)
                            if ij != Pink:
                               ij-=1
                           
                            if ij == Pink: 
                                ij = 101
                                
                            
                            
                                   
                            
                            plt.imshow(ggreeyy)
                            plt.show()
                        Pink = pink
                        
                  
                        plt.imshow(ggrreeeyy)
                        plt.show()   
                        
                        if ji!=j:
                            j = kj
                            j -=1
                            kj = j
           #                 if j == ji:
                      #          j = -Green
                     #          
                        if ji==j:
                           # Green +=1
                           j = int(Green)
                        
                        ij = ijk
                        i = int(black)
                    #j = ij
                    Green = green
                    plt.imshow(ggrreeeyy0)
                    plt.show() 
                    
                        
              
                    
                    if ij != i:####black
                     #   ij = 101
                        ij-= 1
              
                    
                    if ij == i:
                        ij= 101
                        i = ij
                        black = Black
                            
                        
                    
                
                print(i,'i',ij,'ij',ijk,'ijk')
                
                plt.imshow(ggrreeeeyy0)
                plt.show()   
               # Tree -= 1
                if jik != i:
                    i = ikj        
                    i += 1
                    ikj = i
                   # if jik == i:
                       # i = -Tree
                if jik ==i:
                    i = int(Tree)
                   # Tree-=1
                ### I  
            Tree = tree
  

            print('QR Cream QR')
            
            plt.imshow(gggrreeeeyy0)
            plt.show()   
            yaw -= 1

        dimensions += 1

    ensemble += 1