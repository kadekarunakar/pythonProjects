alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(message,shift_number):
    cipher_text=""
    for item in message:
        position=alphabet.index(item)
        new_position=(position+shift_number)%26
        cipher_text+=alphabet[new_position]
    print(cipher_text)  

def decrypt(message,shift_number):
    normal_text=""
    for item in message:
        position=alphabet.index(item)
        new_position=(position-shift_number)%26
        normal_text+=alphabet[new_position]
    print(normal_text)

end=False   
while not end:

    crypt=input("Type 'encrypt' for encryption, type 'decrypt' for decryption\n").lower()
    message=input("Type the message:\n").lower()
    shift_number=int(input("Type the shift number:\n"))

    if(crypt=='encrypt'):
        encrypt(message,shift_number)
    elif(crypt=='decrypt'):
        decrypt(message,shift_number)
    play_again=input("Type 'yes' to continue,type 'no' to exit\n")

    if(play_again=='yes'):
        end=False
    elif(play_again=='no'):
        end=True
        print("Have a nice day!, BYE.....")