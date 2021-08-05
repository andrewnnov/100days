
#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = open("\\Projects\\100days\\Mail_Merge_Project\\Input\\Names\\invited_names.txt", "r")
list_of_names = names.readlines()
print(list_of_names)
new_list = []
for el in list_of_names:
    new_list.append(el.strip("\n"))
print(new_list)

with open("\\Projects\\100days\\Mail_Merge_Project\\Input\\Letters\\starting_letter.txt", "r") as file:
    text_from_file = file.read()
    print(text_from_file)


for name in new_list:
    with open(f'\\Projects\\100days\\Mail_Merge_Project\\Output\\ReadyToSend\\starting_letter_{name}.txt', mode='w') as file:
        file.write(text_from_file.replace("[name]", name))
        file.close()



