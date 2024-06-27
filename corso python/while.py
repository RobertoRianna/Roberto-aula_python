#booleano di controllo
controllo_ciclo1= True
x=0

#while booleano
while controllo_ciclo1:
    print(x)
    x+=1

    if x>3:
        #condizione di rottura
        controllo_ciclo1=False 
else:
    print("Ciclo infinito")