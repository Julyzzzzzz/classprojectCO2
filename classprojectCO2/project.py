"""
July Zhou
Section AF
CSE 163
Final Project
This file includes functions to clean and organize the data
and plot graphs for research problem 1 and 2.
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json


def dataclean(file):
    """
    It cleans the txt data file which is in json format and return
    a dirable dataframe without data that is not needed or missing.
    It also select the appropriate data to present the result of
    research problem 1.
    """
    with open(file) as json_file:
        data = json.load(json_file)
    df = pd.DataFrame.from_records(data)
    df1 = df.filter(items=['name', 'geography', 'data'])
    df2 = df1.dropna()
    df3 = df2[df2['name'] ==
              'Transportation carbon dioxide emissions, '
              'all fuels, Washington']
    df4 = df2[df2['name'] ==
              'Industrial carbon dioxide emissions, '
              'all fuels, Washington']
    data3 = df3['data']
    data4 = df4['data']
    wa3 = data3.to_numpy()[0]
    wa4 = data4.to_numpy()[0]
    year = []
    ems = []
    ems1 = []
    for i in wa3:
        year.append(i[0])
        ems.append(i[1])
    for i in wa4:
        ems1.append(i[1])
    tra = {'year': year, 'tra_emission': ems, 'ind_emission': ems1}
    dfwa = pd.DataFrame(tra, columns=['year', 'tra_emission',
                                      'ind_emission'])
    dfwa = dfwa.sort_values(by=['year'], ascending=True)
    return dfwa


def prob1(dfwa):
    """
    It takes a dataframe from the dataclean function that was well
    constructed for this function and plots a 1 by 2 line graph to
    present the comparison of transportation and industry CO2
    emission change over 40 years in WA.
    """
    fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(10, 8))
    fig.suptitle('Transportation and industry CO2 emission over '
                 '40 years in WA state')
    ax1.plot(dfwa['year'], dfwa['tra_emission'])
    ax1.set_title('Transportation CO2 emission')
    ax1.set_ylabel('CO2 emission, metric tons')
    ax1.grid(True)
    ax2.plot(dfwa['year'], dfwa['ind_emission'])
    ax2.set_title('Industry CO2 emission')
    ax2.set_ylabel('CO2 emission, metric tons')
    ax2.tick_params(axis='x', labelrotation=45)
    ax2.grid(True)
    plt.savefig('WA_trans_ind.png')


def prob2(file):
    """
    It takes a the txt data file which is in json format and cleans
    up the data followed by plotting a 1 by 2 pie chart to show the
    CO2 emission from different fuels in 2007 and 2017 in the US.It
    also print out the % CO2 emission from different feuls.
    """
    with open(file) as json_file:
        data = json.load(json_file)
    # data type is a list of dictionaries, 5119 items, 15 keys per item
    df = pd.DataFrame.from_records(data)
    df1 = df.filter(items=['name', 'geography', 'data'])
    df2 = df1.dropna()
    df2 = df1[df1['name'] ==
              'Total carbon dioxide emissions from all sectors, '
              'coal, United States']
    df3 = df1[df1['name'] ==
              'Total carbon dioxide emissions from all sectors, '
              'natural gas, United States']
    df4 = df1[df1['name'] ==
              'Total carbon dioxide emissions from all sectors, '
              'petroleum, United States']
    coal = df2['data'].to_numpy()[0]
    ngas = df3['data'].to_numpy()[0]
    petro = df4['data'].to_numpy()[0]
    ems = []
    ems1 = []
    ems2 = []
    for i in coal:
        ems.append(i[1])
    for i in ngas:
        ems1.append(i[1])
    for i in petro:
        ems2.append(i[1])
    emssum17 = [ems[0],  ems1[0], ems2[0]]
    emssum07 = [ems[10],  ems1[10], ems2[10]]
    total17 = np.sum(emssum17)
    total07 = np.sum(emssum07)
    df5 = pd.DataFrame({'CO2 emission in 2017, metric tons': emssum17,
                        'CO2 emission in 2007, metric tons': emssum07},
                       index=['coal', 'natural gas', 'petroleum'])
    df5.plot.pie(subplots=True, figsize=(16, 8))
    plt.title('CO2 emission from different fuels in 2017 and 2007 in the US')
    print('total CO2 emission in 2017: ', round(total17, 2), 'metric tons')
    print('coal 2017: ', round(ems[0]/total17*100, 2), '%')
    print('natural gas 2017: ', round(ems1[0]/total17*100, 2), '%')
    print('petroleum 2017: ', round(ems2[0]/total17*100, 2), '%')
    print('total CO2 emission in 2007: ', round(total07, 2), 'metric tons')
    print('coal 2007: ', round(ems[10]/total07*100, 2), '%')
    print('natural gas 2007: ', round(ems1[10]/total07*100, 2), '%')
    print('petroleum 2007: ', round(ems2[10]/total07*100, 2), '%')
    plt.savefig('US_fuels.png')


def main():
    file = 'EMISS.json'
    df = dataclean(file)
    prob1(df)
    prob2(file)


if __name__ == '__main__':
    main()
