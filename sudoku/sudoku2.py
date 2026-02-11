"""
SUDOKU
Volem saber si un sudoku està perfectament resolt.
VERSIÓ 2: COMPROVAM TOT EL SUDOKU

"""


def comprovaGrup(grup):
    #retorna true si el valor és un grup de sudoku és correcte
    #grup: linia, columna, quadrat
    #El grup ha de tenir tots els nombres i no repetirne cap.
    print("comprovant el grup:", grup)
    comprovador = []
    for x in grup:
        
        if (x not in comprovador):
            comprovador.append(x)
            #print (x, "no existeix l'afegim")
        else:
            print (x, " ja existeix, sortim de l'algoritme")
            return False
    return True

def comprovaSudoku(taula):
    print ("iniciant la comprovació del sudoku")
    
    #COMPROVAM FILES
    print("COMPROVAM FILES")
    for i,v in enumerate(taula):
        grup = []
        for j,v in enumerate(taula):
            #print("taula: analisi i: ", i)
            grup.append(taula[i][j])
        if(comprovaGrup(grup)):
            #print("Fila ", i, " correcte", grup)
            pass
        else:
            print ("incorrecte")
            return False
    
    #COMPROVAM COLUMNES
    print("COMPROVAM COLUMNES")
    for j,v in enumerate(taula):
        grup = []
        for i,v in enumerate(taula):
            #print("taula: analisi i: ", i)
            grup.append(taula[i][j])
        if(comprovaGrup(grup)):
            #print("Fila ", i, " correcte", grup)
            pass
        else:
            print ("incorrecte")
            return False
    
    #COMPROVAM QUADRATS
    print("COMPROVAM QUADRATS")
    
    grup=[]
    for i in range(0,3):
        for j in range(0,3):
            grup.append(taula[i][j])
    comprovaGrup(grup)
    
    grup=[]
    for i in range(0,3):
        for j in range(3,6):
            grup.append(taula[i][j])
    comprovaGrup(grup)
    
    grup=[]
    for i in range(0,3):
        for j in range(6,9):
            grup.append(taula[i][j])
    comprovaGrup(grup)

    grup=[]
    for i in range(3,6):
        for j in range(0,3):
            grup.append(taula[i][j])
    comprovaGrup(grup)
    
    grup=[]
    for i in range(3,6):
        
        for j in range(3,6):
            grup.append(taula[i][j])
    comprovaGrup(grup)
    
    grup=[]
    for i in range(3,6):
        for j in range(6,9):
            grup.append(taula[i][j])
    comprovaGrup(grup)

    grup=[]
    for i in range(6,9):
        for j in range(0,3):
            grup.append(taula[i][j])
    comprovaGrup(grup)
    
    grup=[]
    for i in range(6,9):
        for j in range(3,6):
            grup.append(taula[i][j])
    comprovaGrup(grup)
    
    grup=[]
    for i in range(6,9):
        for j in range(6,9):
            grup.append(taula[i][j])
    comprovaGrup(grup)
    


sudoku =[   [9,6,3,1,7,4,2,5,8],
            [1,7,8,3,2,5,6,4,9],
            [2,5,4,6,8,9,7,3,1],
            [8,2,1,4,3,7,5,9,6],
            [4,9,6,8,5,2,3,1,7],
            [7,3,5,9,6,1,8,2,4],
            [5,8,9,7,1,3,4,6,2],
            [3,1,7,2,4,6,9,8,5],
            [6,4,2,5,9,8,1,7,3]
            ]

sudoku2 =[   [9,3,3,1,7,4,2,5,8],
            [1,7,8,3,2,5,6,4,9],
            [2,5,4,6,8,9,7,3,1],
            [8,2,1,4,3,7,5,9,6],
            [4,9,6,8,5,2,3,1,7],
            [7,3,5,9,6,1,8,2,4],
            [5,8,9,7,1,3,4,6,2],
            [3,1,7,2,4,6,9,8,5],
            [6,2,2,5,9,8,1,7,3]
            ]

comprovaSudoku(sudoku)

comprovaSudoku(sudoku2)

print