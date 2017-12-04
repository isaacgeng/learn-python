# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:36:46 2017

@author: 耿浩
"""
import pandas as pd

Share_detail_2015 = pd.read_csv("C://Users//耿浩//Downloads//Share_detail_2015/\
                                Share_detail_2015.csv",encoding="gbk")
Share_detail_2015['money_raise'] = Share_detail_2015['money_raise'].\
 map(lambda x: x.rstrip('万元人民币' or '万元' or '万人民币元'))
 
Share_detail_2015['money_raise_real'] = Share_detail_2015['money_raise_real'].\
map(lambda x: x.rstrip('万元人民币' or '万元' or '万人民币元'))

Share_detail_2015["money_raise_all"] = Share_detail_2015['money_raise'].\
groupby(Share_detail_2015.company_name).transform('sum')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
#Share_detail_2015.to_csv("Share_detail_2015.csv")
