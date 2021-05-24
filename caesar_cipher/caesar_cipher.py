import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
print(art.logo)

def caesar(text, shift, direction):
    result_word = ""
    shift = shift % len(alphabet)
    
    if direction == 'decode':
        shift *= -1
        
    for letter in text:
        if letter not in alphabet:
            new_letter = letter
            result_word += new_letter
            continue      
        position = alphabet.index(letter)
        if position + shift >= len(alphabet):            
            new_letter = alphabet[position + shift - len(alphabet)]
            result_word += new_letter
        else:
            new_letter = alphabet[position + shift]
            result_word += new_letter
        
    print(f"Here's the {direction}d result: {result_word}")
    

    
while should_continue == True:    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    choose_user = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if choose_user == "no":
        should_continue = False
        print("Goodbye")
        









    
