# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Shilpa
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Readind csv file to extract data from Population,Total


def population():

    population_data = pd.read_csv(
        "C:/Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Population,Total.csv")

    # Making Transpose

    population_data_transpose = population_data.transpose()

    # Printing the transposed data

    print(population_data_transpose)
    print(population_data)

    # Ploting Figure
    plt.figure()

    # Prints country names with population in the year of 2010,2011 and 2012

    data = population_data[['Country Name', '2010', '2011', '2012']]
    p = data.iloc[1:9]
    print(p)
    a = p['Country Name']
    print(a)
    c = np.arange(len(a))
    plt.bar(c-0.1, p['2010'], width=0.2, label="2010")
    plt.bar(c+0.1, p['2011'], width=0.2, label="2011")
    plt.bar(c+0.3, p['2012'], width=0.2, label="2012")
    plt.xticks(c, a, rotation=90)

    # Set The Title
    plt.title("Population Total")
    plt.legend()
    plt.xlabel("Country")
    plt.ylabel("Population")

    # Save The Figure
    plt.savefig("Population.png", bbox_inches="tight")
    plt.show()

# Defining electricity using function


def electricity():

    # Reading csv file to extract data from Electric Power Consumption

    elec_data = pd.read_csv(
        "C://Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Electric Power Consumption.csv")
    elec_data_Transpose = elec_data.transpose()
    print(elec_data_Transpose)
    print(elec_data)

    # Plot The Figure
    plt.figure()
    """Displays Countries Based on the Electric Power Consumption in the Year of 2010,2011 and 2012"""

    data1 = elec_data[['Country Name', '2010', '2011', '2012']]
    print(data1.iloc[1:9])
    p = data1.iloc[1:9]
    print(p)
    a = p['Country Name']
    print(a)
    c = np.arange(len(a))
    plt.bar(c-0.1, p['2010'], width=0.2, label="2010")
    plt.bar(c+0.1, p['2011'], width=0.2, label="2011")
    plt.bar(c+0.3, p['2012'], width=0.2, label="2012")
    plt.xticks(c, a, rotation=90)

    # Setting the Title
    plt.title("Electric Power Consumption")
    plt.legend()
    plt.xlabel("Country")
    plt.ylabel("Electric Power Consumption")

    # Saving Figure
    plt.savefig("Electric Power Consumption.png", bbox_inches="tight")
    plt.show()


population()
electricity()

# Defining line graph for CO2 Emissions using function


def line():

    # Reading csv file CO2 Emissions

    df = pd.read_csv(
        "C://Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/CO2 Emissions.csv")
    df_transpose = df.transpose()
    print(df)
    # Plotting line graph based on the CO2 Emission rates for the countries in the year of 2010,2011 and 2012

    ax = df.plot(x='Country Name', y=['2010', '2011', '2012'])
    plt.title("CO2 Emissions (kt)")
    ax.set_ylabel("Emission Rate")
    plt.xticks(rotation=90)
    plt.legend()
    plt.savefig("CO2line.png", bbox_inches="tight")
    plt.show()

# Calling the function


line()

# Defining Line graph  for Cereal Yield using function


def line1():
    # Reading csv file to extract data from the file Cereal Yield

    df = pd.read_csv(
        "C://Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Cereal Yield (kg per hectare).csv")
    df_transpose = df.transpose()
    print(df)
    # Plotting line graph based on the Cereal Yield for the countries in the year of 2010,2011 and 2012
    ax = df.plot(x='Country Name', y=['2010', '2011', '2012'])
    ax.set_ylabel("kg per hectare")
    plt.title("Cereal Yield (kg per hectare)")
    plt.xticks(rotation=90)
    plt.legend()
    plt.savefig("line.png", bbox_inches="tight")
    plt.show()


# Calling the function
line1()
# read in the two csv files
pop_total = pd.read_csv(
    "C:/Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Population,Total.csv")
co2_emissions = pd.read_csv(
    "C://Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/CO2 Emissions.csv")

# merge the two datasets on Country Name and Country Code
data = pd.merge(pop_total, co2_emissions, on=['Country Name', 'Country Code'])

# calculate the population and emissions averages for each year
data['Avg Pop'] = data.iloc[:, 2:15].mean(axis=1)
data['Avg Co2'] = data.iloc[:, 15:29].mean(axis=1)

# calculate the correlation between population and emissions
corr = np.corrcoef(data['Avg Pop'], data['Avg Co2'])[0, 1]
print('The correlation between population and emissions is: ', corr)


def read_files():

    # return original format
    print(pop_total)
    print(co2_emissions)

    # transpose population total file
    pop_total_T = pop_total.T
    # transpose co2 emissions file
    co2_emissions_T = co2_emissions.T

    # return transposed format
    print(pop_total_T)
    print(co2_emissions_T)


# call the function
read_files()
# Reading the datasets
pop_total = pd.read_csv(
    "C:/Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Population,Total.csv")
co2_emissions = pd.read_csv(
    "C://Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/CO2 Emissions.csv")
# Calculating mean, median and mode

mean_population_total = pop_total.mean()
median_population_total = pop_total.median()
mode_population_total = pop_total.mode()

mean_co2_emissions = co2_emissions.mean()
median_co2_emissions = co2_emissions.median()
mode_co2_emissions = co2_emissions.mode()

# Printing the results
print("Mean of population total:")
print(mean_population_total)
print("Median of population total:")
print(median_population_total)
print("Mode of population total:")
print(mode_population_total)
print("Mean of co2 emissions:")
print(mean_co2_emissions)
print("Median of co2 emissions:")
print(median_co2_emissions)
print("Mode of co2 emissions:")
print(mode_co2_emissions)

# import population total data set
pt = pd.read_csv(
    "C:/Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Population,Total.csv")

# import electric power consumption data set
epc = pd.read_csv(
    "C://Users/rejot/OneDrive - University of Hertfordshire/Statistics and trends/Electric Power Consumption.csv")

# merge the two datasets into one
data_merged = pd.merge(
    pt, epc, on=['Country Name', 'Country Code'], how='inner')

# calculate the average population for all countries
avg_pop = data_merged.iloc[:, 2:].mean(axis=1)

# add the avg_pop column to the merged dataframe
data_merged['Avg Pop'] = avg_pop

# sort the dataframe based on the avg_pop column
data_sorted = data_merged.sort_values(by='Avg Pop', ascending=False)

# print the sorted dataframe
print(data_sorted)
