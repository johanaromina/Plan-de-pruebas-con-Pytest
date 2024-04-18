

x = 0
y = 0

while x <= 10: #mientras x sea menor que 
    print(x)
    x= x + 1
   # break     si coloco break solo ejecuta la primera opcion no hace ciclo
    #continue    # si coloco continue hace todo el ciclo hasta terminar el loop
    print("inside while")
    while y < 5:
        print(y)
        y= y + 1
        continue # continua hasta que se cumple la condicion y sale
        #break #para salir de y 
        print("inner loop")
print("out of while loop")

z= 0
while z <= 25: #mientras x sea menor que 
    print(z)
    z= z + 1
    if z == 18:
        break
else:   
    print("out of while loop")
    