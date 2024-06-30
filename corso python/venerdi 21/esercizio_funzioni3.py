#esercizio1.Funzione area triangolo,quadrato e rettangolo

def area_triangolo(base,altezza):
    area=base*altezza/2
    print("L'area del triangolo è: ", area)         #area del triangolo



def area_quadrato(lato):                            #area quadrato
    area1=lato*lato
    print("L'area del quadrato è:", area1)



def area_rettangolo(base,altezza):                  #area rettangolo
    area2=base*altezza
    print("L'area del rettangolo è: ",area2)



controllo=True
while controllo:
    print("Area triangolo, Area quadrato, Area rettangolo")
    utente=(input("Quale operazione vuoi fare? "))
    if utente == "Area triangolo":
        area_triangolo(10,20)
    elif utente == "Area quadrato":
        area_quadrato(5)
    elif utente == "Area rettangolo":
        area_rettangolo(5,8)
    else:
        break
    
