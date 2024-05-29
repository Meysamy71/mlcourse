"""
File: S2-02.py
Author: Meysam Yavarikhoo
Date: 2024/05/28
Version: 1.0.0
License: GPLv3
Description: A simple Python script to Data analysis
"""
import pandas as pd
import math

df = pd.read_csv('train.csv')

# 1 Total Players

TotalPlayers = df.playerId.unique().shape[0]

print("1- Total Players: " + str(TotalPlayers))

# 2 Most Goals Player

MostGoalPlayer = df[df.outcome == 'گُل'].playerId.value_counts().idxmax()

print("2- Most Goals Player: " + MostGoalPlayer)

# 3 Conversion Rate Goals

ConversionRate = (df[df.outcome == 'گُل'].playerId.value_counts() / df[df.outcome != 'گُل'].playerId.value_counts()) * 100
MaxConversionRate = ConversionRate.idxmax()
MinConversionRate = ConversionRate.idxmin()

print('3- Max Conversion Rate Player: ' + MaxConversionRate)
print('3- Min Conversion Rate Player: ' + MinConversionRate)

# 4 Euclidean distance

p = df.x
q = df.y

Euclideandistance = math.dist(p, q)