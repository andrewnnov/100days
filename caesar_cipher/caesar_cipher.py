alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encr_word = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if position + shift_amount >= len(alphabet):
            new_letter = alphabet[position + shift_amount - len(alphabet)]
            encr_word += new_letter
        else:
            new_letter = alphabet[position + shift_amount]
            encr_word += new_letter             
    print(f"The encoded text is {encr_word}")
    
    

encrypt(plain_text = text, shift_amount = shift)



