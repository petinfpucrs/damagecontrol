
import pandas as pd

fonte = pd.read_csv('misturas.csv')
df = pd.DataFrame(fonte)

print("Damage Control!")
#Programa da print nas opções
print("################################")
print("* 1 - Álcool                  *")
print("* 2 - Água Sanitária          *")
print("* 3 - Amônia                  *")
print("* 4 - Alvejantes              *")
print("* 5 - Vinagre                 *")
print("* 6 - Detergente              *")
print("* 7 - Bicarbonato de Sódio    *")
print("* 8 - Água Oxigenada          *")
print("* 9 - Desinfetante            *")
print("###############################")
c1 = int(input("Digite o número correspondente ao componente que você deseja misturar: "))

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
        case 5:
            return "Vinagre"
        case 6:
            return "Detergente"
        case 7:
            return "Bicarbonato de Sódio"
        case 8:
            return "Água Oxigenada"
        case 9:
            return "Desinfetante"
        case _ :
            return 5

#entregando resultado
Compos = Comp1(c1)

if(Comp1(c1) == 5):
    print("Opção Inválida")

else:
    print(df.loc[df['composição 1'] == Compos])
