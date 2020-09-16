"""
July Zhou
Section AF
CSE 163
Final Project
This file includes functions to construct a new data frame from
multiple files, build a regression decision tree, optimize the
tree/max tree depth based on the mean squared errors of training
and testing data vs. the max tree depth. This file answers my 3rd
research problem.
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def newdf(popfile, emsfile):
    """
    It takes the population excel file and the CO2 emission text file
    and constructs a new file which have CO2 emission values for different
    year, state, population of the state in the US. 2 states per geographic
    region were chosen, year 2015 and 2010 were chosen to have a total of 20
    data.It is not enough data for a valid decision tree model but I wanted
    to present the ideas of different parameters can affect the value of CO2
    emission and we can optimize the tree by plotting mean squared error vs.
    max tree depth.
    """
    df = pd.read_excel(popfile)
    df1 = df.rename(columns={'table with row headers in column A and '
                             'column headers in rows 3 through 4. '
                             '(leading dots indicate sub-parts)': 'region',
                             'Unnamed: 3': '2010', 'Unnamed: 8': '2015'})
    df2 = df1.filter(items=['region', '2010', '2015'])
    df2 = df2.dropna()
    pop = []
    region = ['.Washington', '.Oregon', '.Minnesota', '.Wisconsin',
              '.Arizona', '.Texas', '.Virginia', '.Florida',
              '.Pennsylvania', '.Maryland']
    for state in region:
        df3 = df2[df2['region'] == state]
        for i in [df3['2015'], df3['2010']]:
            a = i.to_numpy()
            pop.append(a[0])
    with open(emsfile) as json_file:
        data = json.load(json_file)
    df4 = pd.DataFrame.from_records(data)
    df5 = df4.filter(items=['name', 'geography', 'data'])
    df5 = df5.dropna()
    name = ['Total carbon dioxide emissions from all sectors, '
            'all fuels, Washington',
            'Total carbon dioxide emissions from all sectors, '
            'all fuels, Oregon',
            'Total carbon dioxide emissions from all sectors, '
            'all fuels, Minnesota',
            'Total carbon dioxide emissions from all sectors, '
            'all fuels, Wisconsin',
            'Total carbon dioxide emissions from all sectors, '
            'all fuels, Arizona',
            'Total carbon dioxide emissions from all sectors, '
            'all fuels, Texas',
            'Total carbon dioxide emissions from all sectors, '
            'all fuels, Virginia',
            'Total carbon dioxide emissions from all sectors, '
            'all fuels, Florida',
            'Total carbon dioxide emissions from all sectors, '
            'all fuels, Pennsylvania',
            'Total carbon dioxide emissions from all sectors, '
            'all fuels, Maryland']
    final = []
    for i in name:
        df6 = df5[df5['name'] == i]
        statedata = df6['data']
        sd = statedata.to_numpy()[0]
        ems = []
        for i in sd:
            ems.append(i[1])
        final.append(ems[2])
        final.append(ems[7])

    state = ['WA'] * 2 + ['OR'] * 2 + ['MN'] * 2 + ['WI'] * 2 + \
            ['AZ'] * 2 + ['TX'] * 2 + ['VA'] * 2 + ['FL'] * 2 + \
            ['PA'] * 2 + ['MD'] * 2
    year = ['2015', '2010'] * 10
    new = {'state': state, 'pop': pop, 'year': year, 'emission': final}
    new = pd.DataFrame(new, columns=['state', 'pop', 'year', 'emission'])
    return new


def mse_maxtreedepth(new):
    """
    It takes the the new dataframe constructed by the function newdf
    and plots the test and train mean squared error vs. max tree depth.
    we can determine the optimal max tree depth from the graph.
    """
    features = new.loc[:, new.columns != 'emission']
    labels = new['emission']
    features = pd.get_dummies(features)
    labels = pd.get_dummies(labels)
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2, random_state=10)
    model = DecisionTreeRegressor(max_depth=1)
    model.fit(features_train, labels_train)
    # train_predictions = model.predict(features_train)
    # test_predictions = model.predict(features_test)
    trainerror = []
    testerror = []
    trees = np.arange(1, 18, 1)
    for t in trees:
        model = tree.DecisionTreeRegressor(max_depth=t)
        model.fit(features_train, labels_train)
        trainerror.append(mean_squared_error(labels_train, model.predict(
            features_train)))
        testerror.append(mean_squared_error(labels_test, model.predict(
            features_test)))
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.plot(trees, trainerror, marker='o', label='testerror')
    plt.plot(trees, testerror, marker="s", label='trainerror')
    plt.legend()
    plt.xlabel('Max tree depth')
    plt.ylabel('MSE mean squared error')
    plt.subplot(122)
    plt.plot(trees, trainerror, marker='o', label='testerror')
    plt.plot(trees, testerror, marker="s", label='trainerror')
    plt.ylim((0, 0.2))
    plt.xlim((0, 10))
    plt.legend()
    plt.xlabel('Max tree depth')
    plt.ylabel('MSE mean squared error')
    plt.savefig('MSE vs Max tree depth')
    plt.savefig('mse_maxtreedepth.png')


def treeerror(new):
    """
    It prints out the max tree depth was determined by the graph
    produced by mse_maxtreedepth, calculates and prints the test
    mean squared error.
    """
    features = new.loc[:, new.columns != 'emission']
    labels = new['emission']
    features = pd.get_dummies(features)
    labels = pd.get_dummies(labels)
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2, random_state=100)
    model = DecisionTreeRegressor(max_depth=1)
    model.fit(features_train, labels_train)
    # train_predictions = model.predict(features_train)
    test_predictions = model.predict(features_test)
    error = mean_squared_error(labels_test, test_predictions)
    print('From the graph on mse_maxtreedepth.png, I determined that '
          'the optimal maximum decision tree depth to be 1. '
          'The test mean squared error is:', error)


def main():
    popfile = 'NST-EST2015-01.xlsx'
    emsfile = 'EMISS.json'
    new = newdf(popfile, emsfile)
    mse_maxtreedepth(new)
    treeerror(new)


if __name__ == '__main__':
    main()
