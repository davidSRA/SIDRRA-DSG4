import Instanciaciones as Instanciaciones

def organizaIngredientesAlfabetico():
    lista=Instanciaciones.todosLosIngredientes()
    n=len(lista)-1
    for i in range(n):
        for j in range(n):
            contador=0
            string1=lista[j].getNombre()
            string2=lista[j+1].getNombre()
            while (contador<=len(string1) and contador<=len(string2)):
                if contador==len(string1):
                    break
                if contador==len(string2):
                    auxiliar=lista[j+1]
                    lista[j+1]=lista[j]
                    lista[j]=auxiliar
                    break
                if (string1[contador]<string2[contador]):
                    break
                if (string1[contador]>string2[contador]):
                    auxiliar=lista[j+1]
                    lista[j+1]=lista[j]
                    lista[j]=auxiliar
                    break
                contador+=1 
        n-=1     
    for i in range(len(lista)):
        print(lista[i].getNombre())
        
organizaIngredientesAlfabetico()