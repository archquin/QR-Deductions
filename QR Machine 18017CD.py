#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:01:00 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:23:50 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 03:53:09 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:43:19 2020

@author: fadewell
"""

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
ijk = 0
KiJ=JiK = 0
c = 0
dimensions = 0
#Fs = []
while ensemble <1 :
    white = '-2'   ######## white <---->Green, Cream           1
    Yellow = '-5'   ####-2,-3,-4,----> Yellow==k @ k = 0 ======> 4 White
    Blue = '-6'      ##### -3,-4,-5 ---->Blue == j @ j = -1
    Somon = '5'    ##### 1,3,4,5 -----> Somon = k @ k = 0
    Pink = '-5'      ###### 2,3,4 ----> Pink = ij @ ij = 0
    Green= '-2'      ##### 1,-1,-2,-3 ----> Green = j @ j = 2
    black = '-2' ##### -2,-3,-4 -----> black == i == ij@ ij = 0
    Tree = '1'  #### i 3x
    Cream = '2'  ######## 3,4,5-------> is white too 2
    print('How many mines?')
    b = input()
    b = int(b)
    Tree = str(int(b))  
    while dimensions < 1:
       
      #  Somon = str(-int(Green))
    #    Blue = str( int(Green)+1 )     ##### -3,-4,-5 ---->Blue == j @ j = -1
        qqrrr22 = qrcode.make(Cream)
        qqrrr22.save('r000partEnQtities000r.png')
        iiim0g0mgg111 = cv2.imread("r000partEnQtities000r.png")
        gggrreeeeyy0 = cv2.cvtColor(iiim0g0mgg111, cv2.COLOR_XYZ2RGB)
        cream, bbox, straight_qrcode = detector.detectAndDecode(iiim0g0mgg111)
     #   print('how many mines?')
      #  b = input()
      #  b = int(b)
      #  black = str(-int(b))  
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
            Mines = int(Tree)          
            while i < Tree:

                j = 2
                
                qqrrr22 = qrcode.make(black)
                qqrrr22.save('r000partEntities000r.png')
                iiim00mgg111 = cv2.imread("r000partEntities000r.png")
                ggrreeeeyy0 = cv2.cvtColor(iiim00mgg111, cv2.COLOR_HSV2RGB)
                Black, bbox, straight_qrcode = detector.detectAndDecode(iiim00mgg111)
                i = 0
                ij = 0
                print('which y has ')
                OfY = input()
                OfY = int(OfY)
                   #    b = input()
                    #    b = int(b)
                print('which x has ')
                OfX = input()
                OfX = int(OfX)
                print('what value?')
                a = input()
                a = int(a)
                while i < j :
               #     i = ij
           
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
                    x = 0
                 
                   
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
                        
                        y = 0
                        x += 1
                       
              #          print('a: from 1 to 4')
                       #
                     #   i=ij#############################################
                        while ij < jk:
                            y+=1
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
                            z = 0
                            while  k  < Somon :###### X KiJ X
                                z+=1
                                
                                 ### -2
                                qqr2 = qrcode.make(Blue)
                                qqr2.save('0partEntities.png')
                                iimg11 = cv2.imread("0partEntities.png")
                                ggreyy = cv2.cvtColor(iimg11, cv2.COLOR_BGR2LAB)
                                blue, bbox, straight_qrcode = detector.detectAndDecode(iimg11)
                                w = 0
                              #  j = 5
                                if OfX == x and OfY == y:
                                    j = -1
                                while j < k:
                                    Nn=0  
                                    w +=1
                                    k = 4
                                    if OfX == x:
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
                                        Nn+=1
                                        white = int(white) ### white == jk , -6
                                        jk = 2
                                      #  KiJ = 0
                                        
                                        while ik < jk:
                                            

                                            
                                           
                                            white = int(white)
                                            if ik != white:
                                                white+= 1
                                                
                                      #          z = -ik+1
                                                
                                                
                                                
                                            
                                          #      if ik == jk:and OfY == y
                                               #     jk -=1
                                                  #  ik = jk
                                        
                                            if  ik == white:
                                                white = White
                                                ik = 3
                                                
                                                if (OfX == x and OfY == y and OfX == z and OfY == w and a != 'M'):
                                                    print('Corner coordinates')
                                                    if Nn == 1:
                                                        print(x+1,'x',y+1,'y')
                                                        FS=[x+1,y+1]
                                                      #  Fs.append(FS)
                                                    elif Nn==2:
                                                        print(x+1,'x',y-1,'y')
                                                        FS=[x+1,y-1]
                                                      #  Fs.append(FS)
                                                    elif Nn==3:
                                                        print(x-1,'x',y-1,'y')
                                                        FS=[x-1,y-1]
                                                      #  Fs.append(FS)
                                                    elif Nn==4:
                                                        print(x-1,'x',y+1,'y')   
                                                        FS=[x-1,y+1]
                                                     #   Fs.append(FS)
                                                    qr6 = qrcode.make(FS)
                                                    qr6.save('White.png')
                                                    aWhite = cv2.imread("White.png")
                                                    cWhite = cv2.cvtColor(aWhite, cv2.COLOR_BGR2RGB)
                                                    data, bbox, straight_qrcode = detector.detectAndDecode(aWhite)
                                                    plt.imshow(cWhite)
                                                    plt.show()
                                    #        plt.imshow(greyyyy)
                                     #       plt.show()
                                         #   
                                        #    KiJ+=1
                                      #  ik  = i
                                      #  print(OfX,OfY,x,y,z,w)
                                   #     plt.imshow(greyyy)
                              #          plt.show()
                                     #   Nn+=1
                                        Yellow = int(Yellow)
                                        
                                        if  k != Yellow:
                                            Yellow +=1
                                          #  k -=1
                                            
                                            
                                            
                                        #    print(x,'x')
                                            
                                        #    
                                          #  plt.show()
                                            
                                            #
                                            
                                    #    print(w,'w')
                                        if k == Yellow :
                                            col = [x,w]
                                            qr6 = qrcode.make(col)
                                            qr6.save('Yellow.png')
                                            aYellow = cv2.imread("Yellow.png")
                                            cYellow = cv2.cvtColor(aYellow, cv2.COLOR_BGR2GRAY)
                                            data, bbox, straight_qrcode = detector.detectAndDecode(aYellow)
                                            Yellow = yellow
                                      #      print(Yellow)
                                            k = int(somon)
                                            if (OfX == z and OfY == y and OfX == x) and (OfY == w+1 or OfY == w-1) and a != 'M':
                                                
                                               # FS=[x,w]
                                                #Fs.append(FS)
                                                print('Same column (X coordinates)')
                                                print(x,'x',w,'y')
                                                plt.imshow(cYellow)
                                                plt.show()
                                   
                                          
                            
                                    Blue = int(Blue)
                              #      print(i,j,k)
                          #          print('HERE')
                                    if j != Blue:  #### blue -2
                                       # j -= 1
                                        Blue +=1
                                   #  
                                       
                                    if j == Blue:
                                        Blue = blue
                                        row =[z,y]
                                        j = int(Cream)
                                        jk = j
                                        qr6 = qrcode.make(row)
                                        qr6.save('Blue.png')
                                        aBlue = cv2.imread("Blue.png")
                                        cBlue = cv2.cvtColor(aBlue, cv2.COLOR_BGR2HSV)
                                        data, bbox, straight_qrcode = detector.detectAndDecode(aBlue)
                                     #   print(z,'x',w,'y')
                                        if ( OfX == x and OfY == y ) and (OfX == z+1 or  OfX == z-1) and a != 'M' :
                                            print('Same row (Y coordinates)')
                                            print(z,'x',y,'y')
                                          #  FS=[z,y]
                                           # Fs.append(FS)
                                            plt.imshow(cBlue)
                                            plt.show()
                                    
                                    
                                    k = ki
                                    
                       
                          #      JiK += 1
                          
                                
                                if k != i:
                                   i -= 1
                                   if ( OfX == x and OfY == y and a != '¬M' and  a =='M' ):
                               
                                       #print(i+1,x)
                                       #print(z,y)
                                       if b == int(b) and b > 0:
                                           b -= 1
                                           if b == 0:
                                               print(' Enter Value, M , ¬M')
                                               c = input()
                                               c = str(c)
                                               if c != '¬M' and c!='M':
                                                   c = int(c)
                                                   print('which y has ')
                                                   OfY = input()
                                                   OfY = int(OfY)
                                                   print('which x has ')
                                                   OfX = input()
                                                   OfX = int(OfX)
                                                   x  = OfX -1  
                                                   print(y)
                                 #      cx = x+1
                                #      cy = y+1
                                 #      c = [cx,cy]
                                 #      a = c
                               
                                       print(c,'c',b,'b')
                                    
                                           
                                   
                                if k == i:
                                   Somon -=1
                                   if a != '¬M'or a!='M':
                                      Somon = k
                                   if Somon!= i:
                                      # print(w)
                                       i = int(somon)
                                       z = 0
                                  #     print(x,'x',y,'y')
                                 #      print('True')
                                   
                                   if ( OfX == x and OfY == y and (a != '¬M' and a!='M') ) :
                                      # FS=[x,y]
                                     #  Fs.append(FS)
                                       c = a
                                       plt.imshow(ggreyy)
                                       plt.show()
                                       print(' Enter Value, M , ¬M')
                                       a = input()
                                       a = str(a)
                                       if a != '¬M' and a!='M':
                                           a = int(a)
                                           print('which y has ')
                                           OfY = input()
                                           OfY = int(OfY)
                                           print('which x has ')
                                           OfX = input()
                                           OfX = int(OfX)
                                           x  = OfX -1
                                           Green = green
                                       if a == 0:
                                           a= 'M'

                                
                                
                                
                            Somon = somon
                           
                            
                           
                            
                            
                            i = ij   
                            Pink = int(Pink)
                            if ij != Pink:
                               Pink+=1
                               
                            #   print('False')
                               
                               qr6 = qrcode.make(OfY)
                               qr6.save('Pink.png')
                               aPink= cv2.imread("Pink.png")
                               cPink = cv2.cvtColor(aPink, cv2.COLOR_BGR2Luv)
                               data, bbox, straight_qrcode = detector.detectAndDecode(aPink)
                               if ( OfX == x and ( OfY == y or OfY == y+1)) :
                                  print(y,'y') 
                                  plt.imshow(cPink)
                                  plt.show()
                                  
                            
                            if ij == Pink: 
                          #      print('here')
                                ij = 101
                                
                            
                            
                            
                                   
                 
                        Pink = pink
                        
                  
                  
                        
                        if ji!=j:
                            print(x,'x')
                            qr6 = qrcode.make(OfX)
                            qr6.save('Green.png')
                            aGreen = cv2.imread("Green.png")
                            cGreen = cv2.cvtColor(aGreen, cv2.COLOR_BGR2HLS)
                            data, bbox, straight_qrcode = detector.detectAndDecode(aGreen)
                            if OfX == x or OfX == x+1:
                                plt.imshow(cGreen)
                                plt.show()
                                
                                    #k = int(green)
                            Green = int(Green)
                            Green +=1
               #         if a == 0:
                #                print('How many mines would then be?')
                 #               b = input()
                  #              b = int(b)
                   #             black = str(-int(b))
                
                        if ji==j:
                            j = kj
                            j -=1
                            kj = j
                           # 
                         #   
                        
                        ij = ijk
                        i = int(black)
                    #j = ij
                    Green = int(green)
                 #   plt.imshow(ggrreeeyy0)
                   # plt.show() 
                    
                        
                    print('a',a)
                    
                    if ij != i:####black
                        qr6 = qrcode.make(KiJ)
                        qr6.save('IceBlueWhite.png')
                        anWhite = cv2.imread("IceBlueWhite.png")
                        ccWhite = cv2.cvtColor(anWhite, cv2.COLOR_RGB2XYZ)
                        data, bbox, straight_qrcode = detector.detectAndDecode(anWhite)
                        plt.imshow(ccWhite)
                        if a == '¬M':
                            plt.imshow(ggrreeeyy0)
                            plt.show() 
                            if ij != i:
                                ij= i
                            
                          #  ij-= 1
                        if a == 'M':
                            plt.imshow(ggrreeeyy0)
                            plt.show() 
                         #   if b == '¬M':
                                #print(x,y) 
                            print(' Enter Value, M , ¬M')
                            c = input()
                            if c != 'M' and c != '¬M':
                                b = int(c)
                            if c == 'M' or c == '¬M':
                                ij= 101
                                i = ij
                                print(c,'c',i,'i',j,'j')
                                black = Black
                            
                    
                    if ij == i and a == '¬M':
                        ij= 101
                        i = ij
                        black = Black
               
                            
                        
                    
                
                print(i,'i',ij,'ij',ijk,'ijk')
                
                  
               # Tree -= 1
                if jik != i:
                    i = ikj     
                    i += 1
                    ikj = i
                    
                    print('Mines',Mines)
                    plt.imshow(ggrreeeeyy0)
                    plt.show() 
                   # if jik == i:
                       # i = -Tree
                if jik ==i:
                    i = int(Tree)
                    Mines -= 1
                   # Tree-=1
                ### I  
            Tree = tree
  

            print('QR Cream QR')
            
            plt.imshow(gggrreeeeyy0)
            plt.show()   
            yaw -= 1

        dimensions += 1

    ensemble += 1
