menu_item = 0
lista =[]
while menu_item != 5:
	print ("-----------------------------------")
	print ("1. Print the list")
	print ("2. Add an item to the list")
	print ("3. Remove an item from the list")
	print ("4. Change an item in the list")
	print ("5. Quit")
	menu_item = int(input("Choose an option: "))
	if menu_item == 1:
		current = 0
		if len(lista)> 0:
			while current < len(lista):
				print (current, ".", lista[current])
				current = current + 1
		else:
			print ("Nothing in the list")
	elif menu_item == 2:
		item_add = input("What's the item you want to add?: ")
		lista.append(item_add)
	elif menu_item == 3:
		delete_a = input("What is the name of the item you want to remove?: ")
		if delete_a in lista:
			lista.remove(delete_a)
		else:
			print ("No such item")
	elif menu_item == 4:
		old= input("What is the name of item you wish to change?: ")
		if old in lista:
			new_number = lista.index(old)
			new = input("What's the new name of the item?: ")
			lista[new_number]= new
		else:
			print ("No such item")

    
