# [91] #35 ASCII
# list.clear() borra 
# list.insert(i, x) inserta un valor x en la posicion especificada 
# list.append() agrega un valor 
# list.index(x [, start [, end]]) 
# list.count(x) cuenta los lugares hasta x, comenzando de cero
# list.sort (*, key=None, reverse=False) 
# list.reverse() coloca el listado al reverso 
# list.copy() 
# list.pop(x) acorta la lista a la cantidad x


cities= ["Mendoza", "Cordoba", "Misiones","Salta"]
print(cities)
cities.append("Misiones")
print(cities)
cities.insert(1,"San Luis")
print(cities)
cities.remove("Salta")
print(cities)
cities.pop(3)
print(cities)
print(cities.index("Misiones"))
print(cities.count("Misiones"))
cities.sort()
cities.reverse()
new_cities=cities.copy()
print(cities)
print(new_cities)
updatedlist=new_cities.clear()
print(updatedlist)