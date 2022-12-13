# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt

#Reading csv file
data = pd.read_csv('Age Dependency Ratio.csv')

#choosing the data of 9 countries from the data set
selected_data = data[15:24]


def linegraph():
    """This function is used to plot the line plot between country name and age
    in 2010, 2015 and 2020"""
    plt.figure()
    plt.plot(selected_data['Country Name'],selected_data["2010"],label="2010")
    plt.plot(selected_data['Country Name'],selected_data["2015"],label="2015")
    plt.plot(selected_data['Country Name'],selected_data["2020"],label="2020")
    plt.xlabel("Country Name")
    plt.ylabel("Age")
    plt.title("Age Dependency Ratio of 9 different Countries ")
    plt.xticks(rotation=90)
    plt.legend()
    plt.savefig("line.png",bbox_inches="tight")
    plt.show()
    
def bargraph():
    """This function is used to plot the bargraph of age in different
    countries in 2021"""
    plt.figure(1)
    plt.bar(selected_data['Country Name'],selected_data["2021"])
    plt.xlabel("Country Name")
    plt.ylabel("Age")
    plt.title("Age Dependency Ratio of 9 different countries in 2021")
    plt.xticks(rotation=90)
    plt.savefig("bar.png",bbox_inches="tight")
    plt.show(1)
    

def boxplot():
    """This function is used to plot the boxplot which compares the data in 2015 and 2020"""
    plt.figure(2)
    plt.boxplot([selected_data['2015'],selected_data["2020"]], labels = ["2015", "2020"])
    plt.xlabel("Year")
    plt.ylabel("Age")
    plt.title("Age Dependency Ratio of 9 different Countries in 2015 and 2020")
    plt.xticks(rotation=90)
    plt.savefig("boxplot.png", bbox_inches="tight")
    plt.show(2)
    
#Calling the functions

linegraph()
bargraph()
boxplot()