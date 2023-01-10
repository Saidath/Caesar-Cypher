diction='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def interface():
    fin=input("Enter message for encryption or decryption: ") 
    message=fin
    message=message.replace(" ","") #to remove blankspace
    message=message.upper() #to convert in uppercase
    userInput=input("Welcome to CC Tool(type 'e' for encryption or type 'd' for decryption)\n")
    if userInput=='e':
            print("Enter the key value")
            key=int(input())
            print(Encrypt(message,key)+"\n")
    else:
        if userInput=='d':
            print("Enter the key value")
            key=int(input())
            print(Decrypt(message,key)+"\n")
        else:
            print("Wrong value entered")
            interface()

def Encrypt(message,key):
    encrypted_message=" "
    for i in message:
        location=key + diction.index(i)
        location%=26
        encrypted_message+=diction[location]
    print("Encryption is complete! please check the encrypted code")
    return encrypted_message
def Decrypt(message,key):
    decrypted_message=" "
    for i in message:
        location=diction.index(i)- key
        location%=26
        decrypted_message+=diction[location]
    print("Decryption is complete! please check the decrypted code")
    return decrypted_message

interface()
