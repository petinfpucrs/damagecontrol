import os
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 
print("Damage Control!")

print("Escolha um par dos seguintes componentes:")
print("1 - Álcool")
print("2 - Água Sanitária")
print("3 - Amônia")
print("4 - Alvejantes")


c1 = int(input("Primeiro Componente "))

def Comp1(c1):
    match c1:
        case 1:
            return "Álcool"
        case 2:
            return "Água Sanitária"
        case 3:
            return "Amônia"
        case 4:
            return "Alvejantes"





c2 = int(input("Segundo Componente "))

def Comp2(c2):
    match c2:
        case 1:
            return "Álcool"
        case 2:
            return "Água Sanitária"
        case 3:
            return "Amônia"
        case 4:
            return "Alvejantes"

print(Comp1(c1), Comp2(c2))