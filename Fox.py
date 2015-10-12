# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:06:42 2015

@author: jdomini6
"""


from bs4 import BeautifulSoup
from urllib2 import urlopen
import pandas as pd
from decimal import Decimal

BASE_URL = "http://www.foxsports.com"

def getAllOffenseProjections(week="season"):
    rows_list = []
    page = 1
    end_page = 1
    if week == "season":
        r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=-1&split=3&playerSearchStatus=1").read()
    else: 
        r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=-1&split=4&playerSearchStatus=1").read()
    soup = BeautifulSoup(r, "lxml")
    if soup.find(id='MainColumn_LastPageLink') is not None:
        end_page = int(soup.find(id='MainColumn_LastPageLink').string)
    #Get the week of the projections if it's not season
    if week != "season" and week != soup.find(id='projectionsSplitSelection_dropDown').find(attrs={"value":"4"}).string.split(" ")[1]:
        return rows_list
        
    
    while page <= end_page:
        if page != 1:
            if week == "season":
                r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=-1&split=3&playerSearchStatus=1").read()
            else: 
                r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=-1&split=4&playerSearchStatus=1").read()
            soup = BeautifulSoup(r, "lxml")
        
        
        rows = soup.find("tbody").find_all('tr')    
        for row in rows:          
            cells = row.find_all("td")
            dict1 = {}
            dict1["Name"] = cells[0].find("a").string
            teamPos = cells[0].find("div", class_="TeamPosPlayerInfo").string[1:-1].split(" - ")
            
            dict1["Team"] = teamPos[0]
            dict1["Position"] = teamPos[1]
            dict1["PTD"] = cells[2].string
            dict1["PYD"] = cells[3].string
            dict1["PATT"] = cells[4].string
            dict1["PCMP"] = cells[5].string
            dict1["PINT"] = cells[6].string
            dict1["RUTD"] = cells[7].string
            dict1["RUYD"] = cells[8].string
            dict1["RUATT"] = cells[9].string
            dict1["RETD"] = cells[10].string            
            dict1["REYD"] = cells[11].string
            dict1["REREC"] = cells[12].string    
            dict1["FL"] = cells[15].string
            rows_list.append(dict1)      
        page = page + 1
    return rows_list
    
    
def getKProjections(week="season"):
    rows_list = []
    
    page = 1
    end_page = 1
    if week == "season":
        r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=64&split=3&playerSearchStatus=1").read()
    else: 
        r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=64&split=4&playerSearchStatus=1").read()
    soup = BeautifulSoup(r, "lxml")
    
    #Get the week of the projections if it's not season
    if week != "season" and week != soup.find(id='projectionsSplitSelection_dropDown').find(attrs={"value":"4"}).string.split(" ")[1]:
        return rows_list
        
    
    while page <= end_page:
        if page != 1:
            if week == "season":
                r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=64&split=3&playerSearchStatus=1").read()
            else: 
                r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=64&split=4&playerSearchStatus=1").read()
            soup = BeautifulSoup(r, "lxml")
        if soup.find(id='MainColumn_NextPageLink', class_="aspNetDisabled") is None:
            end_page = end_page + 1
        
        rows = soup.find("tbody").find_all('tr')    
        for row in rows:        
            cells = row.find_all("td")
            dict1 = {}
            dict1["Name"] = cells[0].find("a").string
            teamPos = cells[0].find("div", class_="TeamPosPlayerInfo").string[1:-1].split(" - ")
            dict1["Team"] = teamPos[0]
            dict1["Position"] = teamPos[1]
            dict1["FG"] = cells[2].string
            if cells[3].string == "--":
                dict1["FGA"] = "--"
            else:
                dict1["FGA"] = str(Decimal(cells[3].string) + Decimal(cells[2].string))
            dict1["XP"] = cells[4].string
            rows_list.append(dict1)     
        page = page + 1
    return rows_list   
    
    
def getDEFProjections(week="season"):
    rows_list = []
    
    page = 1
    end_page = 1
    if week == "season":
        r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=32768&split=3&playerSearchStatus=1").read()
    else: 
        r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=32768&split=4&playerSearchStatus=1").read()
    soup = BeautifulSoup(r, "lxml")
    
    #Get the week of the projections if it's not season
    if week != "season" and week != soup.find(id='projectionsSplitSelection_dropDown').find(attrs={"value":"4"}).string.split(" ")[1]:
        return rows_list
        
    
    while page <= end_page:
        if page != 1:
            if week == "season":
                r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=32768&split=3&playerSearchStatus=1").read()
            else: 
                r = urlopen("http://www.foxsports.com/fantasy/football/commissioner/Research/Projections.aspx?page=" + str(page) + "&position=32768&split=4&playerSearchStatus=1").read()
            soup = BeautifulSoup(r, "lxml")
        if soup.find(id='MainColumn_NextPageLink', class_="aspNetDisabled") is None:
            end_page = end_page + 1
        
        rows = soup.find("tbody").find_all('tr')    

        for row in rows:
            cells = row.find_all("td")
            dict1 = {}
            dict1["Name"] = cells[0].find("a").string
            teamPos = cells[0].find("div", class_="TeamPosPlayerInfo").string[1:-1].split(" - ")
            dict1["Team"] = teamPos[0]
            dict1["Position"] = "DEF"
            
            
            
            dict1["DINT"] = cells[5].string
            dict1["DDFR"] = cells[3].string
            dict1["DSACK"] = cells[4].string
            dict1["DDTD"] = cells[2].string
            dict1["DSTY"] = cells[6].string
            dict1["DPA"] = cells[7].string
            rows_list.append(dict1)        

        page = page + 1
    return rows_list   
      
def getAllProjections(week="season"):
    preds = []
    preds = preds + getAllOffenseProjections(week)  
    preds = preds + getKProjections(week)
    preds = preds + getDEFProjections(week)
    df = pd.DataFrame(preds)
    df = df.fillna(0)
    df["source"] = "FOX"
    return df

preds = getAllProjections()