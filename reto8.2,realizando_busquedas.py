
import string
import random
import os


if not os.path.exists("censo.txt"):
	with open ("censo.txt","w",encoding="UTF-8") as censo:
		
		alfabeto=string.ascii_lowercase
		cantidad=1_000

		conteo_censo=0
		numero=0 
		for i in range(cantidad):
			aumento=random.randint(1,2)
			numero+=aumento

			letras=random.sample(alfabeto,5) 							
			nombre="".join(letras)

			edad=random.randint(18,99)   								

			impuesto=random.choice((True,True,True,False)) 				

			conteo_censo+=1

			if conteo_censo % (cantidad/10) == 0:
				print("Se han creado: ",conteo_censo," censos")

			censo.write(f"{numero},{nombre},{edad},{impuesto}\n")
		


with open ("censo.txt","r",encoding="UTF-8") as censo:
	texto_lista=censo.readlines()							
	
	texto_formateado=[]										
	for elemento in texto_lista:
		linea=elemento.strip()					
		texto_formateado.append(linea)


	texto_lista_str=[]										
	for elemento in texto_formateado:
		linea2=elemento.split(",")
		texto_lista_str.append(linea2)

	texto_lista_float=[]									
	for elemento in texto_lista_str:
		if elemento != [""]:
			elemento[0]=int(elemento[0])
			elemento[2]=int(elemento[2])
			texto_lista_float.append(elemento)



def validar_opciones():
	"""
	Allow counting the options input by the user and limit them to one defined quantity. 
	Do not accept any parameters as arguments, and return the input number
	"""
	conteo=3
	while conteo >0:
		try:
			print(f'Tienes ',conteo,' oportunidades para seleccionar')
			numero=int(input("Introduce un numero de la lista (1,2,3): ----> "))
		except BaseException:
			print("No has introducido un numero entero")
			conteo-=1
		else: 
			if numero <=3 and numero!=0:
				return numero
			else:
				conteo-=1
		finally:
			if conteo==0:
				print("No tienes mas oportunidades")
				os.system("cls")
				break
		


def presentacion():
	"""
	Allow displaying the options selected by the user without accepting any parameters as arguments.
	"""
	print("-----")
	print("- CENSO DE POBLACION -")
	print("-----")
	print("1. Buscar por numero")
	print("2. Buscar por nombre")
	print("3. Salir")

def continuar():
	"""
	Reduce the code when interacting with the user, without accepting any parameters as arguments."
	"""
	continuar=input("Presione ENTER para continuar")
	os.system("cls")


def busqueda_binaria_numero(lista,buscar):
	"""
	Allow finding a number and counting the times it appears in the record through the asymptotic notation 
	O(log n), along with its position. It accepts a list and an element to search for as parameters
	"""
	inicio=0
	fin=len(lista)-1
	contador=0

	while inicio <= fin:								
		medio=(inicio+fin)//2						
		
		if lista[medio][0]==buscar:
			contador+=1

			izquierda=medio-1
			while  izquierda>=0 and buscar==lista[izquierda][0]:
				contador+=1
				izquierda-=1

			derecha=medio+1
			while derecha<=len(lista)-1 and buscar==lista[derecha][0]:
				contador+=1
				derecha+=1
			
			return True,medio,contador

		elif buscar>lista[medio][0]:
			inicio=medio+1 							
		
		elif buscar<lista[medio][0]:
			fin=medio-1

			
	return False,"sin posicion",contador


def busqueda_lineal(lista,buscar):
	"""
	Busqueda lineal O(n)
	"""
	posiciones_encontradas=[]
	contador=0
	for i in range(0,len(lista)):
		if lista[i][1] == buscar:
			posiciones_encontradas.append(i)
			contador+=1
	if posiciones_encontradas!=[]:
		return True,posiciones_encontradas,contador

	return False,"sin posicion","sin conteo"



####################################		flujo del programa		#####################################

activar=True
while activar:
	presentacion()
	print()
	opcion=validar_opciones()

	if opcion==1:
		print("Vamos a buscar por numero")
		print()
		conteo=3
		while conteo>=1:
			numero=input("porfavor introduce el numero a buscar en el censo: ")
			if numero.isdigit() == True:
				numero=int(numero)

				encontrado,posicion,contador=busqueda_binaria_numero(texto_lista_float,numero)
				if encontrado == True:
					print("Encontrado el",numero," ",contador, " veces, en la posicion: ", posicion)
					continuar()
					break
				elif encontrado == False:
					print("No encontrado")
					continuar()
					break

			else:
				if conteo>=1:
					conteo-=1
					print("Introduce solo numeros,Te quedan ",conteo," intentos")
					
		if conteo==0:
			print("Se acabaron los intentos")
			continuar=input("Presione ENTER para volver a empezar")
			os.system("cls")
			continue
		
	elif opcion==2:
		print("Vamos a buscar por nombre")
		print()
		conteo=3
		while conteo>=1:
			nombre=input("porfavor introduce el NOMBRE a buscar en el censo: ")
			if nombre.isalpha() == True:

				encontrado,posicion,contador=busqueda_lineal(texto_lista_float,nombre)
				if encontrado == True:
					print("Encontrado el nombre ",nombre," en la posicion: ", *posicion," , ", contador , " veces")
					continuar()
					break
				elif encontrado == False:
					print("No encontrado")
					continuar()
					break

			else:
				if conteo>=1:
					conteo-=1
					print("Introduce solo letras,Te quedan ",conteo," intentos")


	elif opcion==3:
		print("Fin del programa")
		continuar()
		break

	os.system("cls")