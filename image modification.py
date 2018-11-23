# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:57:35 2018

@author: AMaquthu
"""

import exifread
import calendar
import os

def main():
    f = open('IMG_0803.CR2', 'rb')
    
    tags = exifread.process_file(f)
    DateTime = tags['Image DateTime']
    print("The EXIF Data :: ",DateTime)
    f.close()
    data= str(DateTime)
    dateAndTime = data.split()
    dirName = dateAndTime[0]
    dirr = dirName.split(":")
    year,month,day = str(dirr[0]),int(dirr[1]),str(dirr[2])
    
    monthStr = calendar.month_name[month] 
    directory = "{} {} {}".format(day,monthStr,year)
     

    print("File created : ",directory)
    createFolder('./{}/'.format(directory))
    os.rename("./IMG_0803.png","./{}/IMG_0803.png".format(directory))
    
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

if __name__ == "__main__":
    main()



