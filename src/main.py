import pandas as pd

#DataFrame
fonte = pd.read_csv('src/misturas.csv')
df = pd.DataFrame(fonte)

#Menu
print("Damage Control!")
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
c1 = int(input("Digite o número correspondente ao 1° componente da mistura: "))

#operações para pesquisa no SGBD da composição1
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

#operações para pesquisa no SGBD da composição2
c2 = int(input("Agora, digite o número correspondente ao 2° componente da mistura: "))

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
            case _:
                return 5

#entregando resultado
Compos1 = Comp1(c1)
Compos2 = Comp2(c2)
analise = df.loc[(df['composição 1'] == Compos1) & (df['composição 2'] == Compos2),['resultado']]

if(Comp1(c1 or c2) == 5):
    print("Opção Inválida")

else:

    if(len(analise.index) <= 0):
        print("Esta mistura é segura!")


    else:
        print(df.loc[(df['composição 1'] == Compos1) & (df['composição 2'] == Compos2),['resultado']])
