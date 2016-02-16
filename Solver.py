import math




#lista con TODOS las posiciones (str's)
position = []
#create list of all position names (str's)
for i in range (1,10):
    for j in range (1,10):
        name = 'x%ry%r' %(j, i)
        position.append(name)

#diccionario con todos los nombres de posiciones y sus valores posibles
possibles = {}
y = []

x = []
z = []
for i in range (9):
    z.append([])

#give all position all possibilities
for xy in position:
    possibles[xy] = [1,2,3,4,5,6,7,8,9]
    
#create horizontal lines    
for i in range(9):
    y.append([])
    for j in range(9*(i),9*(i+1)):
        y[i].append(position[j])
        
#create vertical lines        
for i in range(9):
    x.append([])
    for j in range(i ,81,9):
        x[i].append(position[j])

#create squares
for i in range (9):
    for j in range (9): 
        z[int((math.ceil(int(y[i][j][3])/3.0)-1)*3+(math.ceil(int(y[i][j][1])\
        /3.0))-1)].append(y[i][j])
        

def simple_remove():
    '''
    if a number is in a position, it removes it as a possiblity
    from the rest of its column, row, and square
    '''
    for check in range (81):
        #si solo tiene un numero
        if len(possibles[position[check]]) == 1:
            #quitarle ese numero a todos los 9x
            #vamos de x1 a x9 (fila y)
            #quitamos en FILAS
            for xval in range(9):
                #que no esté quitado antes y que no sea el mismo
                #si el que es solo uno esta en el valor que iteramos
                if ( possibles[position[check]][0] in 
                possibles[y[int(position[check][3])-1][xval]]
                and len(possibles[y[int(position[check][3])-1][xval]])  != 1):
                        possibles[y[int(position[check][3])-1][xval]].\
                        remove(possibles[position[check]][0])
            #quita en COLUMNAS 
            for yval in range(9):
                #que no esté quitado antes y que no sea el mismo
                #si el que es solo uno esta en el valor que iteramos
                if ( possibles[position[check]][0] in 
                possibles[x[int(position[check][1])-1][yval]]
                and len(possibles[x[int(position[check][1])-1][yval]]) != 1):
                        possibles[x[int(position[check][1])-1][yval]].\
                        remove(possibles[position[check]][0])
                        
            zsquare = int((math.ceil(int(position[check][3])/3.0)-1)*3+(math.ceil(int(position[check][1])/3.0))-1)
            
            for zval in range(9):
                #que no esté quitado antes y que no sea el mismo
                #si el que es solo uno esta en el valor que iteramos
                if ( possibles[position[check]][0] in 
                possibles[z[zsquare][zval]]
                and len(possibles[z[zsquare][zval]])  != 1):
                        possibles[z[zsquare][zval]].\
                        remove(possibles[position[check]][0])

def adv_remove():   
    def applicable_x(each):
        return x[int(results[num_pos][0][1])-1][each] not in z[i]\
        and len(possibles[x[int(results[num_pos][0][1])-1][each]]) \
        > 1 \
        and num_pos+1 in\
        possibles[x[int(results[num_pos][0][1])-1][each]]
    
    def applicable_y(each):
        return y[int(results[num_pos][0][3])-1][each] not in z[i]\
        and len(possibles[y[int(results[num_pos][0][1])-1][each]])\
        > 1\
        and num_pos+1 in\
        possibles[y[int(results[num_pos][0][3])-1][each]]
        
    def remove_x(each):
        possibles[x[int(results[num_pos][0][1])-1][each]].\
        remove(num_pos+1)
    
    def remove_y(each):
        possibles[y[int(results[num_pos][0][3])-1][each]].\
        remove(num_pos+1)
        
    def count_check(zlist):
        results = []
        for i in range (9):
            results.append([])
        for check in range (1,10):    
            for value in range(9):
                if check in possibles[z[zlist][value]]:
                    
                    results[check-1].append(z[zlist][value])
        return results   
        
    for i in range (9):
        results = count_check(i) 
        for num_pos in range(9):
            if len(results[num_pos]) == 1:
                possibles[results[num_pos][0]] = [num_pos+1]
            if len(results[num_pos]) == 2:
                if  results[num_pos][0][1] == results[num_pos][1][1]:
                    for each in range(9):
                        if applicable_x(each):
                            remove_x(each)
                if  results[num_pos][0][3] == results[num_pos][1][3]:
                    for each in range(9):
                        if applicable_y(each):
                            remove_y(each)
                    
            if len(results[num_pos]) == 3:
                if  results[num_pos][0][1] == results[num_pos][1][1]\
                and results[num_pos][0][1] == results[num_pos][2][1]:
                    for each in range(9):
                        if applicable_x(each):
                            remove_x(each)
                if  results[num_pos][0][3] == results[num_pos][1][3]\
                and results[num_pos][0][3] == results[num_pos][2][3]:
                    for each in range(9):
                        if applicable_y(each):
                            remove_y(each)
                             

def solve():
    count = 2
    tally = 0
    while count > 1 and tally < 100:
        count = 1
        for i in range(len(possibles)):
            if len(possibles[position[i]]) > 1:
                count += 1
                break
        tally += 1
        simple_remove()
        adv_remove()
        
def new_values():
    for i in range(len(possibles)):
        print 'Constant in position', position[i],
        
        constant = raw_input(': ')
        if constant:
            possibles[position[i]] = [int(constant)]

#preexisting games used to test functionability. the program still can't solve these 
def prueba (x):

    if x == 1: #puzzle 91
        possibles[position[2]] = [9]
        possibles[position[3]] = [2]
        possibles[position[13]] = [3]
        possibles[position[19]] = [8]
        possibles[position[21]] = [7]
        possibles[position[24]] = [5]
        possibles[position[25]] = [6]
        possibles[position[30]] = [6]
        possibles[position[32]] = [4]
        possibles[position[33]] = [3]
        possibles[position[34]] = [7]
        possibles[position[38]] = [5]
        possibles[position[41]] = [7]
        possibles[position[42]] = [2]
        possibles[position[44]] = [6]
        possibles[position[47]] = [6]
        possibles[position[52]] = [9]
        possibles[position[53]] = [1]
        possibles[position[54]] = [9]
        possibles[position[58]] = [6]
        possibles[position[68]] = [3]
        possibles[position[70]] = [2]
        possibles[position[71]] = [4]
        possibles[position[73]] = [4]
        possibles[position[74]] = [1]
        possibles[position[75]] = [9]
        possibles[position[80]] = [3]
    
    if x == 2: #puzzle 81
        possibles[position[0]] = [9]
        possibles[position[1]] = [4]
        possibles[position[5]] = [6]
        possibles[position[9]] = [5]
        possibles[position[11]] = [1]
        possibles[position[21]] = [4]
        possibles[position[25]] = [3]
        possibles[position[26]] = [5]
        possibles[position[28]] = [3]
        possibles[position[31]] = [9]
        possibles[position[40]] = [3]
        possibles[position[41]] = [4]
        possibles[position[43]] = [8]
        possibles[position[44]] = [9]
        possibles[position[49]] = [8]
        possibles[position[50]] = [2]
        possibles[position[52]] = [7]
        possibles[position[53]] = [3]
        possibles[position[57]] = [1]
        possibles[position[61]] = [2]
        possibles[position[62]] = [6]
        possibles[position[63]] = [2]
        possibles[position[65]] = [6]
        possibles[position[72]] = [3]
        possibles[position[73]] = [9]
        possibles[position[77]] = [5]
        
        
    return possibles
