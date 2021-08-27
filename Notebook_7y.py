# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:17:50 2021

@author: franc
"""

def GetDomain(email):
    return email.split("@")[-1]
    GetDomain("user@domain.com")
    print(GetDomain)
#"domain.com"