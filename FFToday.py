# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:57:54 2015

@author: jdomini6
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
import pandas as pd

BASE_URL = "http://www.fftoday.com"

def getQBProjections(week="season"):
    
    if week == "season":
        r = urlopen("http://www.fftoday.com/rankings/playerproj.php?PosID=10&LeagueID=1").read()
    else: 
        r = urlopen("http://www.fftoday.com/rankings/playerwkproj.php?Season=2015&GameWeek=" + week + "&PosID=10&LeagueID=1").read()
    soup = BeautifulSoup(r, "lxml")

    rows_list = []
    
    next_page = "first"
    while next_page != "":
        rows = soup.find("tr", class_="tableclmhdr")    
        # Move to next row (this takes two sibling calls for some reason...)
        rows = rows.next_sibling
        rows = rows.next_sibling
        
        while rows is not None and rows.name == "tr":
            cells = rows.find_all("td")
            dict1 = {}
            dict1["Name"] = cells[1].find("a").string
            dict1["Team"] = cells[2].string
            dict1["Position"] = "QB"
            dict1["PATT"] = cells[5].string
            dict1["PCMP"] = cells[4].string
            dict1["PYD"] = cells[6].string
            dict1["PTD"] = cells[7].string
            dict1["PINT"] = cells[8].string
            dict1["RUATT"] = cells[9].string
            dict1["RUYD"] = cells[10].string
            dict1["RUTD"] = cells[11].string
            rows_list.append(dict1)        
            #Move to the next row (this takes two sibling calls for some reason...)
            rows = rows.next_sibling
            rows = rows.next_sibling
        if soup.find(string="Next Page") is not None:
            next_page = soup.find(string="Next Page").find_parents("a")[0]["href"]
            print "Opening " + BASE_URL + next_page
            r = urlopen(BASE_URL + next_page).read()
            soup = BeautifulSoup(r, "lxml")
        else:
            next_page = ""
    return rows_list
 
def getRBProjections(week="season"):
    
    if week == "season":
        r = urlopen("http://www.fftoday.com/rankings/playerproj.php?PosID=20&LeagueID=1").read()
    else: 
        r = urlopen("http://www.fftoday.com/rankings/playerwkproj.php?Season=2015&GameWeek=" + week + "&PosID=20&LeagueID=1").read()
    soup = BeautifulSoup(r, "lxml")
    rows_list = []
    next_page = "first"
    while next_page != "":
        rows = soup.find("tr", class_="tableclmhdr") 
        # Move to next row (this takes two sibling calls for some reason...)
        rows = rows.next_sibling
        rows = rows.next_sibling
        
        while rows is not None and rows.name == "tr":
            cells = rows.find_all("td")
    
            #print rows
            #cells = row.find_all("td")
            dict1 = {}
            dict1["Name"] = cells[1].find("a").string
            dict1["Team"] = cells[2].string
            dict1["Position"] = "RB"
            dict1["RUATT"] = cells[4].string
            dict1["RUYD"] = cells[5].string
            dict1["RUTD"] = cells[6].string
            dict1["REREC"] = cells[7].string
            dict1["REYD"] = cells[8].string
            dict1["RETD"] = cells[9].string
            #print dict1
            rows_list.append(dict1)
            
            #Move to the next row (this takes two sibling calls for some reason...)
            rows = rows.next_sibling
            rows = rows.next_sibling
        if soup.find(string="Next Page") is not None:
            next_page = soup.find(string="Next Page").find_parents("a")[0]["href"]
            print "Opening " + BASE_URL + next_page
            r = urlopen(BASE_URL + next_page).read()
            soup = BeautifulSoup(r, "lxml")
        else:
            next_page = ""
    return rows_list   
   
def getWRProjections(week="season"):
    
    if week == "season":
        r = urlopen("http://www.fftoday.com/rankings/playerproj.php?PosID=30&LeagueID=1").read()
    else: 
        r = urlopen("http://www.fftoday.com/rankings/playerwkproj.php?Season=2015&GameWeek=" + week + "&PosID=30&LeagueID=1").read()
    soup = BeautifulSoup(r, "lxml")
    rows_list = []
    next_page = "first"
    while next_page != "":
        rows = soup.find("tr", class_="tableclmhdr") 
        # Move to next row (this takes two sibling calls for some reason...)
        rows = rows.next_sibling
        rows = rows.next_sibling
        
        while rows is not None and rows.name == "tr":
            cells = rows.find_all("td")  
            dict1 = {}
            dict1["Name"] = cells[1].find("a").string
            dict1["Team"] = cells[2].string
            dict1["Position"] = "WR"
            dict1["REREC"] = cells[4].string
            dict1["REYD"] = cells[5].string
            dict1["RETD"] = cells[6].string
            #print dict1
            rows_list.append(dict1)
            
            #Move to the next row (this takes two sibling calls for some reason...)
            rows = rows.next_sibling
            rows = rows.next_sibling
        if soup.find(string="Next Page") is not None:
            next_page = soup.find(string="Next Page").find_parents("a")[0]["href"]
            print "Opening " + BASE_URL + next_page
            r = urlopen(BASE_URL + next_page).read()
            soup = BeautifulSoup(r, "lxml")
        else:
            next_page = ""
    return rows_list   

def getTEProjections(week="season"):
    
    if week == "season":
        r = urlopen("http://www.fftoday.com/rankings/playerproj.php?PosID=40&LeagueID=1").read()
    else: 
        r = urlopen("http://www.fftoday.com/rankings/playerwkproj.php?Season=2015&GameWeek=" + week + "&PosID=40&LeagueID=1").read()
    soup = BeautifulSoup(r, "lxml")
    rows_list = []
    next_page = "first"
    while next_page != "":
        rows = soup.find("tr", class_="tableclmhdr") 
        # Move to next row (this takes two sibling calls for some reason...)
        rows = rows.next_sibling
        rows = rows.next_sibling
        
        while rows is not None and rows.name == "tr":
            cells = rows.find_all("td")  
            dict1 = {}
            dict1["Name"] = cells[1].find("a").string
            dict1["Team"] = cells[2].string
            dict1["Position"] = "TE"
            dict1["REREC"] = cells[4].string
            dict1["REYD"] = cells[5].string
            dict1["RETD"] = cells[6].string
            #print dict1
            rows_list.append(dict1)
            
            #Move to the next row (this takes two sibling calls for some reason...)
            rows = rows.next_sibling
            rows = rows.next_sibling
        if soup.find(string="Next Page") is not None:
            next_page = soup.find(string="Next Page").find_parents("a")[0]["href"]
            print "Opening " + BASE_URL + next_page
            r = urlopen(BASE_URL + next_page).read()
            soup = BeautifulSoup(r, "lxml")
        else:
            next_page = ""
    return rows_list   

def getKProjections(week="season"):
    
    if week == "season":
        r = urlopen("http://www.fftoday.com/rankings/playerproj.php?PosID=80&LeagueID=1").read()
    else: 
        r = urlopen("http://www.fftoday.com/rankings/playerwkproj.php?Season=2015&GameWeek=" + week + "&PosID=80&LeagueID=1").read()
    soup = BeautifulSoup(r, "lxml")
    rows_list = []
    next_page = "first"
    while next_page != "":
        rows = soup.find("tr", class_="tableclmhdr") 
        # Move to next row (this takes two sibling calls for some reason...)
        rows = rows.next_sibling
        rows = rows.next_sibling
        
        while rows is not None and rows.name == "tr":
            if week == "season":
                cells = rows.find_all("td")  
                dict1 = {}
                dict1["Name"] = cells[1].find("a").string
                dict1["Team"] = cells[2].string
                dict1["Position"] = "K"
                dict1["FG"] = cells[4].string
                dict1["FGA"] = cells[5].string
                dict1["XP"] = cells[7].string
            else:
                cells = rows.find_all("td")  
                dict1 = {}
                dict1["Name"] = cells[1].find("a").string
                dict1["Team"] = cells[2].string
                dict1["Position"] = "K"
                dict1["FG"] = cells[4].string
                dict1["FGA"] = str(int(cells[4].string) + int(cells[5].string))
                dict1["XP"] = cells[6].string
                #print dict1
            rows_list.append(dict1)
            
            #Move to the next row (this takes two sibling calls for some reason...)
            rows = rows.next_sibling
            rows = rows.next_sibling
        if soup.find(string="Next Page") is not None:
            next_page = soup.find(string="Next Page").find_parents("a")[0]["href"]
            print "Opening " + BASE_URL + next_page
            r = urlopen(BASE_URL + next_page).read()
            soup = BeautifulSoup(r, "lxml")
        else:
            next_page = ""
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
    df["source"] = "FFToday"
    return df  
    


