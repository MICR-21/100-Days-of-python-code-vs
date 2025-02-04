import art 
print(art.logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def caesar (text, shift,encode_decode):
    output_text = " "
    if encode_decode == "decode":
        shift_position *= -1 
    for letter in text:
        if letter not in alphabet:
            output_text += letter
        else:
            shift_position = alphabet.index(letter) + shift
            shift_position %= len(alphabet)
            output_text += alphabet[shift_position]
         
    print(f"Your text message is {output_text}") 
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text,shift=shift,encode_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n ")
    if restart == "no":
        should_continue = False
        print("GoodBye")



    
