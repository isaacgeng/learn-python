# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:23:39 2017

@author: 耿浩
Get all the names of the csv files under the same directory, loop through the files into pandas dataframe\
append all the files into one dataframe and save it into stata dta file
"""
import os
import pandas as pd

#==============================================================================
# def eachFile(filepath):
#     pathDir =  os.listdir(filepath)
#     for compny in pathDir:
#         compny = os.path.join('%s%s' % (filepath, allDir))
# #        print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
#         return compny
# 
# Share_detail_2015 = pd.DataFrame()
# for compny in cmpys:
#     path ='C:\\Documents and Settings\\Foo\\My Documents\\pydata-book\\pydata-book-master`\\ch02\\names\\yob%d.txt' % year
#     frame = pd.read_csv(path, names=columns)
#     Share_detail_2015 = pd.concat(cmpys, frame, ignore_index=True)
#==============================================================================
os.chdir("C:\\Users\\耿浩\\Downloads\\Share_detail_2015")
Path_dir = os.listdir()
Share_detail_2015 = pd.DataFrame()
for compy in Path_dir:
    frame = pd.read_csv(compy, header=0,encoding="gbk",index_col=0)
    Share_detail_2015 = Share_detail_2015.append(frame)
change_column = {'发起人': 'Starter', '认缴出资额（万元）': 'money_raise','认\
                 缴出资时间':'money_time','认缴出资方式':'money_method',"实缴出资\
                 额（万元）":"money_raise_real","出资时间":"money_time_real\
                 ","出资方式":"money_method_real"}
Share_detail_2015 = Share_detail_2015.rename(columns=change_column)
Share_detail_2015.to_csv("Share_detail_2015.csv")

