#que son los diccionarios en Python?
#definicion de diccionarios los diccionarios se definen con {}..... diccio={}
#type: me dice que tipo de clase es; tupla,diccionario, arreglo, lista 


#ejemplo

demo_dict={}

print(type(demo_dict))

demo_dict1={1:20, 2:30, 3:40, 6:67}
demo_dict2={"testing":"prueba", "uat":"uaturl"}
demo_dict3={'qa':50, 2:"url"}

demo_dict2['prod']='product' #agregar prod: producto
demo_dict2[25]=45 #agregar prod: producto

print(demo_dict2)

demo_dict2.pop(25)# elimino el valor de lugar 25, que en este caso es 45
print(demo_dict2)