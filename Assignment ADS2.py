# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Shilpa
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Readind csv file to extract data from Population,Total
def population():
    
    population_data = pd.read_csv("C:/Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Population,Total.csv")

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
    
#Defining electricity using function

def electricity():
    
    #Reading csv file to extract data from Electric Power Consumption
    
    elec_data = pd.read_csv("C://Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Electric Power Consumption.csv")
    elec_data_Transpose = elec_data.transpose()
    print(elec_data_Transpose)
    print(elec_data)

    #Plot The Figure
    plt.figure()
    """Displays Countries Based on the Electric Power Consumption in the Year of 2010,2011 and 2012"""

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

#Defining line graph for CO2 Emissions using function

def line():

    #Reading csv file CO2 Emissions
    
    df = pd.read_csv("C://Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/CO2 Emissions.csv")
    df_transpose=df.transpose()
    print(df)
    #Plotting line graph based on the CO2 Emission rates for the countries in the year of 2011,2012,2013 and 2014
    
    ax = df.plot(x='Country Name', y=['2011','2012','2013','2014'])
    plt.title("CO2 Emissions (kt)")
    ax.set_ylabel("Emission Rate")
    plt.xticks(rotation=90)
    plt.legend()
    plt.savefig("CO2line.png",bbox_inches="tight")
    plt.show()
    
#Calling the function

line()

#Defining Line graph  for Cereal Yield using function

def line1():
    #Reading csv file to extract data from the file Cereal Yield
    
    df = pd.read_csv("C://Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Cereal Yield (kg per hectare).csv")
    df_transpose=df.transpose()
    print(df)
    #Plotting line graph based on the Cereal Yield for the countries in the year of 2011,2012,2013 and 2014
    ax = df.plot(x='Country Name', y=['2011','2012','2013','2014'])
    ax.set_ylabel("kg per hectare")
    plt.title("Cereal Yield (kg per hectare)")
    plt.xticks(rotation=90)
    plt.legend()
    plt.savefig("line.png",bbox_inches="tight")
    plt.show()

#Calling the function

line1()












