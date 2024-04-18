demo_tuple=(1,2,3,4)
demo_tuple1=("Rusia", "Marruecos","Africa")
demo_tuple2=("A", 1,"Africa", True)
demo_tuple3=(True, False)


#print(demo_tuple2[0]) #imprime lo que hay en la posicion indicada en los corchetesa [91] #35
#print(len(demo_tuple2)) # cuanta cuantos lugares tiene la tupla
#print(demo_tuple1.count("Marruecos")) # busca la posicion de marruecos
# print(demo_tuple1.index("Africa"))
#print(demo_tuple1[2])

for x in demo_tuple1: #hago un for dentro de la tupla que recorre todas las posiciones 
    print(x)
    
    
joined_tuple= demo_tuple1 + demo_tuple + demo_tuple2 + demo_tuple3

print(joined_tuple) #suma todo 
print(type (joined_tuple)) #que tipo es??? es una tupla 


