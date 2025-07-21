alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt():
    message=list(input("Type your message:\n").lower())
    shift=int(input("Type the shift number:\n"))
    cipher_text=""
    for letter in message:
        position=alphabets.index(letter)
        new_positon=position+shift
        if new_positon<0:
            new_positon=new_positon+26
        new_positon=new_positon%26
        cipher_text+=alphabets[new_positon]
    print(f"Here's the encrypted result: {cipher_text}")
def decrypt():
    message=list(input("Type your message:\n").lower())
    shift=int(input("Type the shift number:\n"))
    cipher_text=""
    for letter in message:
        position=alphabets.index(letter)
        new_positon=position-shift
        if new_positon<0:
            new_positon=new_positon+26
        new_positon=new_positon%26
        cipher_text+=alphabets[new_positon]
    print(f"Here's the decrypted result: {cipher_text}")
code=input("Type 'encrypt' for encryption, type 'decrypt' for decryption: \n")
if (code=='encrypt'):
    encrypt()
elif (code=='decrypt'):
    decrypt()
else:
    print("Enter correct choice")
    exit()
while True:
    char=input("Type 'yes' to continue,type 'no' to stop\n")
    if (char=='yes'):
        code=input("Type 'encrypt' for encryption, type 'decrypt' for decryption: \n")
        if (code=='encrypt'):
            encrypt()
        elif (code=='decrypt'):
            decrypt()
        else:
            print("Enter correct choice")
            exit()
    else:
        exit()