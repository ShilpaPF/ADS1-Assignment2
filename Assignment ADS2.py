# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Readind csv file to extract data from Population,Total
def population():
    
    population_data = pd.read_csv("C:\\Population,Total.csv")

#Making Transpose

    population_data_transpose = population_data.transpose()

#Printing the transposed data

    print(population_data_transpose)
    print(population_data)



#Ploting Figure
    plt.figure()

#Prints country names with population in the year of 2010,2011 and 2012

    data=population_data[['Country Name','2010','2011','2012']]
    p = data.iloc[1:9]
    print(p)
    a=p['Country Name']
    print(a)
    c=np.arange(len(a))
    plt.bar(c-0.1, p['2010'], width=0.2, label="2010")
    plt.bar(c+0.1, p['2011'], width=0.2, label="2011")
    plt.bar(c+0.3, p['2012'], width=0.2, label="2012")
    plt.xticks(c,a,rotation=90)

#Set The Title
    plt.title("Population Total")
    plt.legend()
    plt.xlabel("Country")
    plt.ylabel("Population")

#Save The Figure
    plt.savefig("Population.png",bbox_inches="tight")
    plt.show()

def electricity():
    
#Reading csv file to extract data from Electric Power Consumption
    elec_data = pd.read_csv("C:\\Electric Power Consumption.csv")
    elec_data_Transpose = elec_data.transpose()
    print(elec_data_Transpose)
    print(elec_data)

#Plot The Figure
    plt.figure()
    """Prints Countries Based on the Electric Power Consumption in the Year of 2010,2011 and 2012"""

    data1=elec_data[['Country Name','2010','2011','2012']]
    print(data1.iloc[1:9])
    p=data1.iloc[1:9]
    print(p)
    a=p['Country Name']
    print(a)
    c=np.arange(len(a))
    plt.bar(c-0.1, p['2010'], width=0.2, label="2010")
    plt.bar(c+0.1, p['2011'], width=0.2, label="2011")
    plt.bar(c+0.3, p['2012'], width=0.2, label="2012")
    plt.xticks(c,a,rotation=90)

   #Setting the Title
    plt.title("Electric Power Consumption")
    plt.legend()
    plt.xlabel("Country")
    plt.ylabel("Electric Power Consumption")

#Saving Figure
    plt.savefig("Electric Power Consumption.png",bbox_inches="tight")
    plt.show()

population()
electricity()

def line():
    
    population_data1 = pd.read_csv("C:\\Population,Total.csv") 
   # Year = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
    #Population = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  
    plt.plot()#(Year, Population, color='red', marker='o')
    plt.title('Population vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Population', fontsize=14)
    plt.show()           



line()



















