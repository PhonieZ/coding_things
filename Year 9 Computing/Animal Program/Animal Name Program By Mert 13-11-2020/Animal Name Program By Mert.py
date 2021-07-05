#Animal Thing by Mert Aydin 13/11/2020
animal_name = input("Enter the name of an animal: ")#gets an animal name

if animal_name[0].lower() == "a" or "e" or "i" or "u":#checks if animal name starts with a  vowel or not so the a or an before the name is gramatically correct
    a = "An "
else:
    a = "A "

animal_description = input("How would you describe "+a+animal_name)#asks for description of the animal
print(a+animal_name+" is "+animal_description)#compiles description of animal with inputs
print("you will find it under "+animal_name[0].lower()+" in a dictionary")#says where in a dictionary you could find the animal
