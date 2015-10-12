# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 08:27:54 2015

http://www.fantasypros.com/nfl/projections/



@author: jdomini6
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
import pandas as pd


def getQBProjections(week="season"):
    if week=="season":
        week = "draft"
    r = urlopen("http://www.fantasypros.com/nfl/projections/qb.php?week=" + week).read()
    soup = BeautifulSoup(r, "lxml")
    rows = soup.find_all("tr", class_="mpb-available")
    
    rows_list = []
    for row in rows:
        #print row
        
        cells = row.find_all("td")
        #print cells[0].find("small").contents
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        if len(cells[0].find_all('small')) == 1:
            dict1["Team"] = str(cells[0].find("small").contents[0])
        else:
            dict1["Team"] = "None"
        dict1["Position"] = "QB"
        dict1["PATT"] = cells[1].string
        dict1["PCMP"] = cells[2].string
        dict1["PYD"] = cells[3].string
        dict1["PTD"] = cells[4].string
        dict1["PINT"] = cells[5].string
        dict1["RUATT"] = cells[6].string
        dict1["RUYD"] = cells[7].string
        dict1["RUTD"] = cells[8].string
        dict1["FL"] = cells[9].string
    
        rows_list.append(dict1)
    return rows_list
    
    
def getRBProjections(week="season"):
    if week=="season":
        week = "draft"
    r = urlopen("http://www.fantasypros.com/nfl/projections/rb.php?week=" + week).read()
    soup = BeautifulSoup(r, "lxml")
    rows = soup.find_all("tr", class_="mpb-available")
    
    rows_list = []
    for row in rows:
        #print row
        
        cells = row.find_all("td")
        #print cells[0].find("small").contents
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        if len(cells[0].find_all('small')) == 1:
            dict1["Team"] = str(cells[0].find("small").contents[0])
        else:
            dict1["Team"] = "None"
        dict1["Position"] = "RB"
        dict1["RUATT"] = cells[1].string
        dict1["RUYD"] = cells[2].string
        dict1["RUTD"] = cells[3].string
        dict1["REREC"] = cells[4].string
        dict1["REYD"] = cells[5].string
        dict1["RETD"] = cells[6].string
        dict1["FL"] = cells[7].string
    
        rows_list.append(dict1)
    return rows_list
    
    
def getWRProjections(week="season"):
    if week=="season":
        week = "draft"
    r = urlopen("http://www.fantasypros.com/nfl/projections/wr.php?week=" + week).read()
    soup = BeautifulSoup(r, "lxml")
    rows = soup.find_all("tr", class_="mpb-available")
    
    rows_list = []
    for row in rows:
        #print row
        
        cells = row.find_all("td")
        #print cells[0].find("small").contents
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        if len(cells[0].find_all('small')) == 1:
            dict1["Team"] = str(cells[0].find("small").contents[0])
        else:
            dict1["Team"] = "None"
        dict1["Position"] = "WR"
        dict1["RUATT"] = cells[1].string
        dict1["RUYD"] = cells[2].string
        dict1["RUTD"] = cells[3].string
        dict1["REREC"] = cells[4].string
        dict1["REYD"] = cells[5].string
        dict1["RETD"] = cells[6].string
        dict1["FL"] = cells[7].string
    
        rows_list.append(dict1)
    return rows_list    
    
def getTEProjections(week="season"):
    if week=="season":
        week = "draft"
    r = urlopen("http://www.fantasypros.com/nfl/projections/te.php?week=" + week).read()
    soup = BeautifulSoup(r, "lxml")
    rows = soup.find_all("tr", class_="mpb-available")
    
    rows_list = []
    for row in rows:
        #print row
        
        cells = row.find_all("td")
        #print cells[0].find("small").contents
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        if len(cells[0].find_all('small')) == 1:
            dict1["Team"] = str(cells[0].find("small").contents[0])
        else:
            dict1["Team"] = "None"
        dict1["Position"] = "TE"
        dict1["REREC"] = cells[1].string
        dict1["REYD"] = cells[2].string
        dict1["RETD"] = cells[3].string
        dict1["FL"] = cells[4].string
    
        rows_list.append(dict1)
    return rows_list
    
    
def getKProjections(week="season"):
    if week=="season":
        week = "draft"
    r = urlopen("http://www.fantasypros.com/nfl/projections/k.php?week=" + week).read()
    soup = BeautifulSoup(r, "lxml")
    rows = soup.find_all("tr", class_="mpb-available")
    
    rows_list = []
    for row in rows:
        #print row
        
        cells = row.find_all("td")
        #print cells[0].find("small").contents
        dict1 = {}
        dict1["Name"] = cells[0].find("a").string
        if len(cells[0].find_all('small')) == 1:
            dict1["Team"] = str(cells[0].find("small").contents[0])
        else:
            dict1["Team"] = "None"
        dict1["Position"] = "K"
        dict1["FG"] = cells[1].string
        dict1["FGA"] = cells[2].string
        dict1["XPT"] = cells[3].string
    
        rows_list.append(dict1)
    return rows_list
    
def getAllProjections(week="season"):
    preds = []
    preds = preds + getQBProjections(week)  
    preds = preds + getRBProjections(week)
    preds = preds + getWRProjections(week)
    preds = preds + getTEProjections(week)
    preds = preds + getKProjections(week)
    df = pd.DataFrame(preds)
    df = df.fillna(0)
    df["source"] = "FantasyPros"
    return df       
    
preds = getAllProjections()