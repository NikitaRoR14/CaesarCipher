import art

def encrypt(original_text,shift_amount):
    encrypted_message = ""
    for letter in original_text:
        if not letter in alphabet:
            encrypted_message += letter
        else:
            shifted_index = alphabet.index(letter)+shift_amount
            while shifted_index > len(alphabet)-1:
                shifted_index -= len(alphabet)
            encrypted_message += alphabet[shifted_index]
    print(encrypted_message)

def decode(original_text,shift_amound):
    decoded_message = ""
    for letter in original_text:
        if not letter in alphabet:
            decoded_message += letter
        else:
            shifted_index = alphabet.index(letter)-shift_amound
            while shifted_index < 0:
                shifted_index += len(alphabet)
            decoded_message += alphabet[shifted_index]
    print(decoded_message)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(art.logo)
while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt,or 0 to leave:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text,shift)
    elif direction == 'decode':
        decode(text,shift)
    elif direction == 0:
        break
    else:
        print("Incorrect symbol,try again.")
