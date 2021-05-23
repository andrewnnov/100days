alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(text, shift, direction):
    result_word = ""
    if direction == 'decode':
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        if position + shift >= len(alphabet):
            new_letter = alphabet[position + shift - len(alphabet)]
            result_word += new_letter
        else:
            new_letter = alphabet[position + shift]
            result_word += new_letter
        
    print(f"Here's the {direction}d result: {result_word}")        

    
caesar(text, shift, direction)    









    
