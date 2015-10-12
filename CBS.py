# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:05:03 2015

@author: jdomini6
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
import pandas as pd

def getQBProjections(week="season"):
    
    r = urlopen("http://www.cbssports.com/fantasy/football/stats/weeklyprojections/QB/" + week + "/avg/ppr?&print_rows=9999").read()
    soup = BeautifulSoup(r, "lxml")
    #Pull out the header row
    soup.select("#special")[0].decompose() 
    rows = soup.find_all("tr", class_=["row1", "row2"])
    
    rows_list = []
    for row in rows:
        #print row
        cells = row.find_all("td")
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        dict1["Team"] = cells[0].contents[1][2:]
        dict1["Position"] = "QB"
        dict1["PATT"] = cells[1].string
        dict1["PCMP"] = cells[2].string
        dict1["PYD"] = cells[3].string
        dict1["PTD"] = cells[4].string
        dict1["PINT"] = cells[5].string
        #dict1["PCMPPCT"] = cells[6].string
        dict1["RUYATT"] = cells[7].string
        dict1["RUATT"] = cells[8].string
        dict1["RUYD"] = cells[9].string
        #dict1["RUAVG"] = cells[10].string
        dict1["RUTD"] = cells[11].string
        dict1["FL"] = cells[12].string
    
        rows_list.append(dict1)
    return rows_list
    
    
def getRBProjections(week="season"):
    r = urlopen("http://www.cbssports.com/fantasy/football/stats/weeklyprojections/RB/" + week + "/avg/ppr?&print_rows=9999").read()
    soup = BeautifulSoup(r)
    #Pull out the header row
    soup.select("#special")[0].decompose() 
    rows = soup.find_all("tr", class_=["row1", "row2"])
    
    rows_list = []
    for row in rows:
        #print row
        cells = row.find_all("td")
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        dict1["Team"] = cells[0].contents[1][2:]
        dict1["Position"] = "RB"
        dict1["RUATT"] = cells[1].string
        dict1["RUYD"] = cells[2].string
        #dict1["RUAVG"] = cells[3].string
        dict1["RUTD"] = cells[4].string
        dict1["REREC"] = cells[5].string
        dict1["REYD"] = cells[6].string
        #dict1["REAVG"] = cells[7].string
        dict1["RETD"] = cells[8].string
        dict1["FL"] = cells[9].string
        rows_list.append(dict1)
    return rows_list
    
    
def getWRProjections(week="season"):
    r = urlopen("http://www.cbssports.com/fantasy/football/stats/weeklyprojections/WR/" + week + "/avg/ppr?&print_rows=9999").read()
    soup = BeautifulSoup(r)
    #Pull out the header row
    soup.select("#special")[0].decompose() 
    rows = soup.find_all("tr", class_=["row1", "row2"])
    
    rows_list = []
    for row in rows:
        #print row
        cells = row.find_all("td")
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        dict1["Team"] = cells[0].contents[1][2:]
        dict1["Position"] = "WR"
        dict1["REREC"] = cells[1].string
        dict1["REYD"] = cells[2].string
        #dict1["REAVG"] = cells[3].string
        dict1["RETD"] = cells[4].string
        dict1["FL"] = cells[5].string
        rows_list.append(dict1)
    return rows_list
    
def getTEProjections(week="season"):
    r = urlopen("http://www.cbssports.com/fantasy/football/stats/weeklyprojections/TE/" + week + "/avg/ppr?&print_rows=9999").read()
    soup = BeautifulSoup(r)
    #Pull out the header row
    soup.select("#special")[0].decompose() 
    rows = soup.find_all("tr", class_=["row1", "row2"])
    
    rows_list = []
    for row in rows:
        #print row
        cells = row.find_all("td")
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        dict1["Team"] = cells[0].contents[1][2:]
        dict1["Position"] = "TE"
        dict1["REREC"] = cells[1].string
        dict1["REYD"] = cells[2].string
        #dict1["REAVG"] = cells[3].string
        dict1["RETD"] = cells[4].string
        dict1["FL"] = cells[5].string
        rows_list.append(dict1)
    return rows_list
    
def getKProjections(week="season"):
    r = urlopen("http://www.cbssports.com/fantasy/football/stats/weeklyprojections/K/" + week + "/avg/ppr?&print_rows=9999").read()
    soup = BeautifulSoup(r)
    #Pull out the header row
    #soup.select("#special")[0].decompose() 
    rows = soup.find_all("tr", class_=["row1", "row2"])
    #print rows
    rows_list = []
    for row in rows:
        #print row
        cells = row.find_all("td")
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        dict1["Team"] = cells[0].contents[1][2:]
        dict1["Position"] = "K"
        dict1["FG"] = cells[1].string
        dict1["FGA"] = cells[2].string
        dict1["XP"] = cells[3].string
        rows_list.append(dict1)
    return rows_list
    
def getDEFProjections(week="season"):
    r = urlopen("http://www.cbssports.com/fantasy/football/stats/weeklyprojections/DST/" + week + "/avg/ppr?&print_rows=9999").read()
    soup = BeautifulSoup(r)
    #Pull out the header row
    #soup.select("#special")[0].decompose() 
    rows = soup.find_all("tr", class_=["row1", "row2"])
    #print rows
    rows_list = []
    for row in rows:
        
        cells = row.find_all("td")
        #print cells
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        dict1["Team"] = cells[0].contents[1][2:]
        dict1["Position"] = "DEF"
        dict1["DINT"] = cells[1].string
        dict1["DDFR"] = cells[2].string
        dict1["DFF"] = cells[3].string
        dict1["DSACK"] = cells[4].string
        dict1["DDTD"] = cells[5].string
        dict1["DSTY"] = cells[6].string
        dict1["DPA"] = cells[7].string
        dict1["DTYDA"] = cells[8].string
        rows_list.append(dict1)
    return rows_list
      
def getAllProjections(week="season"):
    preds = []
    preds = preds + getQBProjections(week)  
    preds = preds + getRBProjections(week)
    preds = preds + getWRProjections(week)
    preds = preds + getTEProjections(week)
    preds = preds + getKProjections(week)
    preds = preds + getDEFProjections(week)
    df = pd.DataFrame(preds)
    df = df.fillna(0)
    df["source"] = "CBS"
    return df
    