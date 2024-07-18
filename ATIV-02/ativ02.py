import numpy as np
import math

def q1(list):
    list1 = []
    for i in list:
        if i%2==1:
            list1.append(i)
    return list1


def primoq2(number):
    for i in range(2, number):
        if number%i==0 and number!=2:
            return False
    return True

def q2(list):
    list1 = []
    for i in list:
        if primoq2(i) and i!=1:
            list1.append(i)
    return list1


def q3(list1, list2):
    a= int(input('Qual lista você deseja? '))
    match a:
        case 1:
            return list1
        case 2: 
            return list2
        
    
def q4(list):
    maior = -math.inf
    segmaior = -math.inf
    for i in list:
        if i > maior:
            segmaior = maior
            maior = i
        elif i > segmaior:
            segmaior = i
    return segmaior
    
            
def q5(list):
    list = sorted(list, key=lambda x: x[0])
    return list

## Questão 6 ##
import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
layout="constrained")
for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
            transform=axs[row, col].transAxes,
            ha='center', va='center', fontsize=18,
            color='darkgrey')
fig.suptitle('plt.subplots()')

## Questão 7 ##

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)

## Questão 8 ##

import pandas as pd

df = pd.read_csv('ATIV-02/caminho.csv')
n = 5 #numeros de linhas para exibir
print(df.head(n))

## Questão 9 ##
df = pd.read_csv('ATIV-02/caminho.csv')
#usar query para elementos na coluna A maiores que 30
df_filter = df.query("A > 30")
print(df_filter)

## Questão 10 ##
# Existem várias formas de tratar dados ausentes, irei citar duas.

# 1. Remover linhas com valores ausentes:

df = pd.read_csv('ATIV-02/caminho.csv')
df_filter = df.dropna()
print(df_filter)

# 2. Tratar valores ausentes, adicionando a média:
df = pd.read_csv('ATIV-02/caminho.csv')
#para a coluna target
target = 'A'
df[target] = df[target].fillna(df[target].mean())
print(df_filter)
    
