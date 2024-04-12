import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("Zomato data .csv")

print(dataframe.head())

def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)

print(dataframe.head())

dataframe.info()

def countplot():
    sns.countplot(x=dataframe['listed_in(type)'])
    plt.xlabel("Type of restaurant")
    plt.show()

def groupbyvoats():
    grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes': grouped_data}) 
    plt.plot(result, c="green", marker="o")
    plt.xlabel("Type of restaurant")
    plt.ylabel("Votes")
    plt.show()

def findmaxvote():
    max_votes = dataframe['votes'].max()
    restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
    print("Restaurant(s) with the maximum votes:")
    print(restaurant_with_max_votes)

def countplotonlineorder():
    sns.countplot(x=dataframe['online_order'])
    plt.xlabel("Online Order")
    plt.show()

def histogramrating():
    plt.hist(dataframe['rate'], bins=5)
    plt.title("Ratings Distribution")
    plt.show()

def countplotcouplecost():
    sns.countplot(x=dataframe['approx_cost(for two people)'])
    plt.xlabel("Approximate Cost for Two People")
    plt.show()

def boxplotonvsoffline():
    plt.figure(figsize=(6, 6))
    sns.boxplot(x='online_order', y='rate', data=dataframe)
    plt.xlabel("Online Order")
    plt.ylabel("Rate")
    plt.show()

while True:
    print("*****The options are*****")
    print(" 1. countplot dataframe for listed data")
    print(" 2. groupby dataframe for votes of restaurants")
    print(" 3. find the restaurant with maximum votes")
    print(" 4. countplot dataframe for online orders")
    print(" 5. historam daraframe for rating distributions")
    print(" 6. countplot dataframe for approximate cost for couple")
    print(" 7. boxplot dataframe for online vs offline ratings")

    choice= input("enter your choice from 1-7: ")
    if choice == "1":
        countplot()
    elif choice == "2":
        groupbyvoats()
    elif choice == "3":
        findmaxvote()
    elif choice == "4":
        countplotonlineorder()
    elif choice == "5":
        histogramrating()
    elif choice == "6":
        countplotcouplecost()
    elif choice == "7":
        boxplotonvsoffline()

    else:
        print("invalid option")
        break
