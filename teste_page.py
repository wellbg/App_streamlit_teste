import streamlit as st
import pandas as pd
import numpy as np


def converte(lista):
    y = [lista[-1]]
    for i in range(0,len(lista[:-1])):
        y.append(lista[i])
    return y

def insira():
    
    c = st.number_input('Insert a number', min_value=4, max_value=20)

def matrizpB():
    
    c = st.number_input('Insert a number', min_value=4, max_value=20)
        
    if c <5:
        print('Deve usar PB8')
#         lista = []
        pb = [1,1,1,-1,1,-1,-1]
        mult = 7
        pos = 7
    elif 5<=c<=8:
        print('Deve usar PB12')
#         lista = []
        pb = [1,1,-1,1,1,1,-1,-1,-1,1,-1]
        mult = 11
        pos = 11
    elif 8<c<13:
        print('Deve usar PB16')
#         lista = []
        pb = [1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1]
        mult = 15
        pos = 15
    elif 13<=c<17:
        print('Deve usar PB20')
#         lista = []
        pb = [1, 1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1]
        mult = 19
        pos = 19
    elif 17<=c<21:
        print('Deve usar PB21')
#         lista = []
        pb = [1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1]
        mult = 23
        pos = 23
   

#Criando a matriz codificada a partir da primeira coluna
    lista = []
    lista.append(pb)

    for i in range(mult):
        tmp=converte(lista[i])
        lista.append(tmp)
        matriz = pd.DataFrame(lista).T
        new_pos=matriz.shape[1]*[-1]
        matriz.loc[pos] = new_pos
    
#Trocando o nome das colunas pelos fatores a serem trabalhados
    columns  = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16',
                'X17','X18','X19','X20','X21','X22','X23','X24']
    col = []
    for i in range(0,len(matriz)):
         col.append(columns[i])
    matriz.columns = col
    
#Trocando o index
    index_name = np.arange(1,len(matriz)+1)
    matriz.index = index_name
    
#Recortando a matriz segundo o número de fatores
    
    matriz = matriz.iloc[:,0:c]
    data = pd.DataFrame(matriz)
    
            
    return data



st.title("Matriz codificada")


x = matrizpB()
st.dataframe(x)
