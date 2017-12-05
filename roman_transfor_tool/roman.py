#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python roman.py 2017
# 2017
# -->
# MMXVII


import sys
def numToRomanNum(Num):
   if Num < 1 or Num > 3999:
     print ('The Num must in 1-3999')
   else:
     NumDic = {
       '1':('I','IV','V','IX'),
       '2':('X','XL','L','XC'),
       '3':('C','CD','D','CM'),
       '4':('M')
       }
     items = sorted(NumDic.items())
     retstr = ''
     for item in items:
       str = ''
       (Num,modNum) = divmod(Num,10)
       if modNum != 0:
         if item[0] != '4':
           if modNum <= 3:
             while modNum > 0:
               str = str.join(['',item[1][0]])
               modNum -= 1
           elif modNum < 5:
             str = item[1][1]
           elif modNum == 5:
             str = item[1][2]
           elif modNum < 9:
             str = item[1][2]
             while modNum > 5:
               str = str.join(['',item[1][0]])
               modNum -= 1
           else:
             str = item[1][3]
         else:
           while modNum > 0:
             str = str.join(['',item[1][0]])
             modNum -= 1
         retstr = str.join(['',retstr])
     return retstr 



if __name__ == "__main__":
    a = int(sys.argv[1])
    print(a)
    print('-->')
    print(numToRomanNum(a))
