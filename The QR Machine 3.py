#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:54:30 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:50:44 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:23:53 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:49:09 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:51:56 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 00:33:53 2020

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
    white = '-1'   ######## white <---->Green, Cream           1
    Yellow = '0'   ####-2,-3,-4,----> Yellow==k @ k = 0
    Blue = '-2'      ##### -3,-4,-5 ---->Blue == j @ j = -1
    Somon = '2'    ##### 1,3,4,5 -----> Somon = k @ k = 0
    Pink = '-1'      ###### 2,3,4 ----> Pink = ij @ ij = 0---------> Cream
    Green= '0'      ##### 1,-1,-2,-3 ----> Green = j @ j = 2
    black = '-1' ##### -2,-3,-4 -----> black == i == ij@ ij = 0
    Tree = '2'  #### i 
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
            live = i
            qr2 = qrcode.make(Tree)
            qr2.save('partEntities00.png')
            img111 = cv2.imread("partEntities00.png")
            greyyyy = cv2.cvtColor(img111, cv2.COLOR_BGR2RGB)
            tree, bbox, straight_qrcode = detector.detectAndDecode(img111)
            Tree = int(Tree)   
            ij = i                           
            while i < Tree:

                j = 2
                
                qqrrr22 = qrcode.make(black)
                qqrrr22.save('r000partEntities000r.png')
                iiim00mgg111 = cv2.imread("r000partEntities000r.png")
                ggrreeeeyy0 = cv2.cvtColor(iiim00mgg111, cv2.COLOR_HSV2RGB)
                Black, bbox, straight_qrcode = detector.detectAndDecode(iiim00mgg111)
               
                ij = 0
                while i < j :
                    i = ij
           
                    qqrr22 = qrcode.make(Green)
                    qqrr22.save('000partEntities000.png')
                    iiim0mgg111 = cv2.imread("000partEntities000.png")
                    ggrreeeyy0 = cv2.cvtColor(iiim0mgg111, cv2.COLOR_RGB2XYZ)
                    green, bbox, straight_qrcode = detector.detectAndDecode(iiim0mgg111)
                    
                    Cream = int(Cream)
                    j = Cream
                    k = 0
                    ij = i
                    ijk = ij
                    j= 2
                    soul = j
                    Green = int(Green)
                    while j > Green :## i<j
                       # ij = ijk
                     #   i = ijk
                        qr22 = qrcode.make(Pink)
                        qr22.save('00partEntities00.png')
                        iiimmgg111 = cv2.imread("00partEntities00.png")
                        ggrreeeyy = cv2.cvtColor(iiimmgg111, cv2.COLOR_BGR2HLS)
                        pink, bbox, straight_qrcode = detector.detectAndDecode(iiimmgg111)
                        
                        jk = int(Cream)
                        ###i = 0 or 
                        ij = 0
                        ik = k
                        JiK = 0
                        KiJ = 0
                    #    i=ij#############################################
                        while ij < jk:
                          #  ij = 0
                          #  i = ik
                      #      ij = i
                          #  k = 0
                             
                            qr22 = qrcode.make(Somon)
                            qr22.save('0partEntities0.png')
                            iiimg111 = cv2.imread("0partEntities0.png")
                            ggreeyy = cv2.cvtColor(iiimg111, cv2.COLOR_BGR2Luv)
                            somon, bbox, straight_qrcode = detector.detectAndDecode(iiimg111)
                            i = int(Somon)
                            k = 0
                            dark = k
                            Somon = int(Somon)
                            while  k  < Somon :###### X KiJ X
                                
                                
                                 ### -2
                                qqr2 = qrcode.make(Blue)
                                qqr2.save('0partEntities.png')
                                iimg11 = cv2.imread("0partEntities.png")
                                ggreyy = cv2.cvtColor(iimg11, cv2.COLOR_BGR2LAB)
                                blue, bbox, straight_qrcode = detector.detectAndDecode(iimg11)
                                
                                j = int(blue)
                                while j < k:
                                    
                                    
                                    
                                    qr1 = qrcode.make(Yellow)
                                    qr1.save('partEntities.png')
                                    img11 = cv2.imread("partEntities.png")
                                    greyy = cv2.cvtColor(img11, cv2.COLOR_BGR2HSV)
                                    yellow, bbox, straight_qrcode = detector.detectAndDecode(img11)
                                    
                                    k=int(Yellow)
                                    while k <  i:
                                        
                                        qr = qrcode.make(white)
                                        qr.save('partEntities0.png')
                                        img1 = cv2.imread("partEntities0.png")
                                        greyyy = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                                        White, bbox, straight_qrcode = detector.detectAndDecode(img1)
                                        ik = int(white)
                                        Nn=1    
                                        white = int(white) ### white == jk , -6
                                       # jk = int(Cream)
                                        
                                        
                                        while ik < ij:
                                   

                                            
                                            plt.imshow(greyyyy)
                                            plt.show()
                                            white = int(white)
                                            if ik != white:
                                                ik +=1
                                                if ik == white:
                                                    white = White
                                        
                                            if  ik == white:
                                                white += 1
                                                
                                            
                                         #   
                                            
                                   #     ik  = i
                                  
                                        plt.imshow(greyyy)
                                        plt.show()
                                        Yellow = int(Yellow)
                                        if  k != Yellow:
                                            k+=1
                                            if k == Yellow:
                                                Yellow = yellow
                                    
                                   
                                        if k == Yellow :
                                            Yellow += 1
                                            
                                      #      if k == Yellow:
                                       #         k-=1
                                                
                                                
                                  #      jk = k
                                        
                                #    plt.imshow(greyy)
                                #    plt.show()
                                    Blue = int(Blue)
                                    plt.imshow(greyy)
                                    plt.show()
                         
                                    if j!= Blue:
                                        j+=1
                                        if j == Blue:
                                            Blue = blue
                                            print('j',j,'Blue',Blue)
                                    if j == Blue:  #### blue -2
                                        Blue+=1
                                    
                                        
                                            
                                        print('j',j,'Blue',Blue)
                                        
                                        #Blue+=1
                                     #   jk = int(pink)
                                       # j = jk
                                        
                                    k = dark
                                    
                                plt.imshow(ggreyy)
                                plt.show()
                                if k != i:
                                   i -= 1
                                   if k == i:
                                       print('there')
                                       #plt.imshow(ggreyy)
                                       #plt.show()
                                       
                                if k == i:
                                   Somon -=1
                                   if Somon!= i:
                                   #    print('here')
                                       i = int(somon)
                                       
             
                            Somon = somon
             
                           
         
                            Pink = int(Pink)
                         #   i = ij
                            if ij != Pink:
                               ij+=1
                               if ij == Pink:
                                   Pink = pink
                           
                            if ij == Pink: 
                              #  Pink = int(pink)
                                print('ij',ij,'jk',jk)
                              #  ij += 1
                                Pink +=1
                             #   if pink == Pink:
                              #      jk = -66
                               # i = 0
                               # if i == Pink
                                #jk = -66
                            
                            
                                  
                            KiJ+=1
                            print(KiJ)
                            plt.imshow(ggreeyy)
                            plt.show()
                        Pink = pink
                        
             
                        plt.imshow(ggrreeeyy)
                        plt.show()   
              
                        Green = int(Green)
                        Green = int(Green)    
                       # if j != Green:
                         #   Green +=1
                         #   if Green == j:
                          #      j -=1
                     #   Green = int(Green) 
                      # if j != Cream:
                           # print('ij')
                            #Green += 1  
                        j = soul    
                        j-=1
                        soul = j
                           
                        #Green += 1
                        
                        print('i',i,'j',j,'k',k)
                        print('ij',ij,'jk',jk,'ik',ik)
                    ij = ijk
                    i = int(black)
                    j = ij
                    Green = green
                    #Green = int(Green)
                    plt.imshow(ggrreeeyy0)
                    plt.show() 
                    if ij == i:####black
                        ij = 101
                       # i = ij
              
                    
                    if j == ij:
                       # i = -2
                        black = int(black)
                        black += 1
                        if ij == black:
                            black = Black
                            ij-= 1
                    
               # ijk = i
                i = live
                print(i,'i',ij,'ij',ijk,'ijk')
                
                plt.imshow(ggrreeeeyy0)
                plt.show()   
                #Tree -= 1
                i += 1
                live = i
                        
            Tree = tree
  

            print('QR Cream QR')
            
            plt.imshow(gggrreeeeyy0)
            plt.show()   
            yaw -= 1

        dimensions += 1

    ensemble += 1