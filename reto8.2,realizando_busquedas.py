
import string
import random
import os


if not os.path.exists("census.txt"):
	with open ("census.txt","w",encoding="UTF-8") as census:
		
		alphabet=string.ascii_lowercase
		quantity=1_000

		count_census=0
		number=0 
		for i in range(quantity):
			increase=random.randint(1,2)
			number+=increase

			letters=random.sample(alphabet,5) 							
			name="".join(letters)

			age=random.randint(18,99)   								

			tax=random.choice((True,True,True,False)) 				

			count_census+=1

			if count_census % (quantity/10) == 0:
				print("have been created: ",count_census," census")

			census.write(f"{number},{name},{age},{tax}\n")
		


with open ("census.txt","r",encoding="UTF-8") as census:
	text_list=census.readlines()							
	
	text_formatted=[]										
	for element in text_list:
		line=element.strip()					
		text_formatted.append(line)


	text_list_str=[]										
	for element in text_formatted:
		line2=element.split(",")
		text_list_str.append(line2)

	text_list_float=[]									
	for element in text_list_str:
		if element != [""]:
			element[0]=int(element[0])
			element[2]=int(element[2])
			text_list_float.append(element)


def validate_options():
	"""
	Allow counting the options input by the user and limit them to one defined quantity. 
	Do not accept any parameters as arguments, and return the input number
	"""
	count=3
	while count >0:
		try:
			print(f'You have ',count,' oportunities to select')
			number=int(input("Enter number from the list (1,2,3): ----> "))
		except BaseException:
			print("you have not entered an integer number")
			count-=1
		else: 
			if number <=3 and number!=0:
				return number
			else:
				count-=1
		finally:
			if count==0:
				print("you have not more opportunities")
				os.system("cls")
				break
		


def presentation():
	"""
	Allow displaying the options selected by the user without accepting any parameters as arguments.
	"""
	print("-----")
	print("- CENSO DE POBLACION -")
	print("-----")
	print("1. Buscar por numero")
	print("2. Buscar por nombre")
	print("3. Salir")

def continue_program():
	"""
	Reduce the code when interacting with the user, without accepting any parameters as arguments."
	"""
	continue_program=input("Presione ENTER para continuar")
	os.system("cls")


def binary_search_number(list_find,find):
	"""
	Allow finding a number and counting the times it appears in the record through the asymptotic notation 
	O(log n), along with its position. It accepts a list and an element to search for as parameters
	"""
	start=0
	end=len(list_find)-1
	counter=0

	while start <= end:								
		middle=(start+end)//2						
		
		if list_find[middle][0]==find:
			counter+=1

			left=middle-1
			while  left>=0 and find==list_find[left][0]:
				counter+=1
				left-=1

			right=middle+1
			while right<=len(list_find)-1 and find==list_find[right][0]:
				counter+=1
				right+=1
			
			return True,middle,counter

		elif find>list_find[middle][0]:
			start=middle+1 							
		
		elif find<list_find[middle][0]:
			end=middle-1

			
	return False,"without position",counter


def lineal_search(list_find,find):
	"""
	lineal_search O(n)
	"""
	found_positions=[]
	counter=0
	for i in range(0,len(list_find)):
		if list_find[i][1] == find:
			found_positions.append(i)
			counter+=1
	if found_positions!=[]:
		return True,found_positions,counter

	return False,"without positions","without counter"



####################################		program flow		#####################################

activate=True
while activate:
	presentation()
	print()
	option=validate_options()

	if option==1:
		print("let's search by number")
		print()
		counter=3
		while counter>=1:
			number=input("Please, Enter the number by find for in the census: ")
			if number.isdigit() == True:
				number=int(number)

				found,position,counter=binary_search_number(text_list_float,number)
				if found == True:
					print("Found the ",number," ",counter, " times, in the position: ", position)
					continue_program()
					break
				elif found == False:
					print("Not found")
					continue_program()
					break

			else:
				if counter>=1:
					counter-=1
					print("Enter only numbers,you have ",counter," attempts left")
					
		if counter==0:
			print("attempts have been exhausted")
			continuar=input("Press ENTER to start again")
			os.system("cls")
			continue
		
	elif option==2:
		print("let's search by name")
		print()
		counter=3
		while counter>=1:
			name=input("Please,enter only name to find from the census: ")
			if name.isalpha() == True:

				found,position,counter=lineal_search(text_list_float,name)
				if found == True:
					print("Name: ",name,", found in the position: ", *position," , ", counter , " times")
					continue_program()
					break
				elif found== False:
					print("Not found")
					continue_program()
					break

			else:
				if counter>=1:
					counter-=1
					print("Enter only letters,you have only",counter," attempts left")


	elif option==3:
		print("End of program")
		continue_program()
		break

	os.system("cls")