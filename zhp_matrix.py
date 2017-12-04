# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:36:59 2017

@author: 耿浩
deal with zhp's matrix
"""
import pandas as pd
import os
import numpy as np

os.chdir(r"C:\Users\耿浩\Desktop")
zhp_org =pd.read_excel("zhp.xlsx")

def generate_response_matrix(dishi):    
    group_test = zhp_org[zhp_org["地市"]==dishi]
    print(dishi)
    pre_matrix = group_test.drop(group_test.columns[0:2],axis=1)
    pre_matrix = pre_matrix.dropna(axis=1,how="all")
    pre_matrix = pre_matrix.dropna(axis=0,how="all")
    matrix = pre_matrix.values
    a = np.empty(np.array(matrix.shape)+1)*np.NaN
    for i,j in np.ndindex(a.shape):
        if i<j and j<a.shape[0]:
            a[i,j] = matrix[i,j-i-1]
        else:
            pass
    if a.ndim>1:
        b = np.transpose(a)
        na = np.isnan(a)
        nb = np.isnan(b)
        a[na] = 0
        b[nb] = 0
        a += b
        na &= nb
        a[na] = np.nan
    else:
        pass
    index = group_test.index.values
#    a = np.concatenate((a,np.array([index]).T),axis=1)
    meet_sheet = pd.DataFrame(a)
    print(meet_sheet)
    meet_sheet.set_index(index,drop=True,inplace=True)
    meet_sheet["地市"] = dishi
    meet_sheet["公司"] = group_test["公司"]
    print(meet_sheet.columns)
#    meet_sheet.drop(meet_sheet.columns[-2],axis=1,inplace=True)
#    meet_sheet.set_index(meet_sheet)
    print(meet_sheet)
    return meet_sheet

lst = list(zhp_org["地市"].unique())
#initial = generate_response_matrix(lst[0])
initial = pd.DataFrame(index=None)
for dishi in lst:
    meet_sheet = generate_response_matrix(dishi)
    meet_sheet = pd.merge(zhp_org,meet_sheet,how='inner',on=['地市','公司'])
    initial = pd.concat([initial,meet_sheet],axis=0)
zhp_org=pd.merge(zhp_org,initial,how='inner',on=["公司","地市"])
        
#initial = generate_response_matrix("白银市")
#meet_sheet = generate_response_matrix("阿拉尔市")
#initial = pd.merge(zhp_org,initial,how='inner',on=['公司','地市'],left_index=True,right_index=True)
#meet_sheet = pd.merge(zhp_org,meet_sheet,how='inner',on=[r'公司',r'地市'],left_index=True)
#
#initial = pd.concat([initial,meet_sheet],axis=0) 