demo_set1= {10,20,30,40,50}
demo_set2= {10,20,"30",40, 40.5}
demo_set3= {"10","30"}
demo_set4= set((45, 45, "67", 65))

print(demo_set1)
print(demo_set4)
print(len(demo_set1)) # LEN cuantos elementos tiene el conjunto x? .....

print (20 in demo_set1)
print (20 in demo_set3) #  IN valoracion de verdad esta tal numero en el conjunto x? true or false

demo_set3.add(498) #  add agrega valores al conjunto

print(demo_set3)

# demo_set3.remove("10") elimina un valor del conjunto

#print(demo_set3)

#demo_set3.pop()   remueve un elemento 
#demo_set3.clear()   limpia el conjunto 
#print(demo_set3)
demo_set3= demo_set1.union(demo_set2) #une dos conjuntos y solo coloca los elementos una sola vez, no coloca las repeticionesç

print(demo_set3)

demo_set4= demo_set1.update(demo_set2) # 
print(demo_set4)

demo_set3= demo_set1.intersection(demo_set2) #
print(demo_set3)

demo_set1.intersection_update(demo_set2) 
print(demo_set1)




demo_set5= {"Maria","Carla", "Juana", "Perla"}
demo_set6= {"Marta","Soledad", "Juana", "Perla"}
demo_set8= {"Jose", "Pedro"}

demo_set8= demo_set5.difference(demo_set6) # me devuelve los valores que no son comunes del conjunto A respecto del conjunto B ambos conjuntos y los guarda como conj 3
print(demo_set8)

demo_set5.symmetric_difference_update(demo_set6) #me devuelve los valores no comunes a los conj comparados 
print(demo_set5)

demo_set8= demo_set5.issubset(demo_set6) # me pregunta si interseccion de  conju 5 y 6 es igual conjunto 8
print(demo_set8)



z= demo_set5.issubset(demo_set6) # me pregunta si interseccion de  conju 5 y 6 es igual conjunto 8
print(z)
z= demo_set5.issuperset(demo_set6) # me pregunta si interseccion de  conju 5 y 6 es igual conjunto 8
print(z)

