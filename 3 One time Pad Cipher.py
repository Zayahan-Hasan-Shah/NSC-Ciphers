import tkinter as tk
import random

root=tk.Tk()
##root.geometry("320x210")
root.resizable(True,True)
title=root.title("ONE TIME PAD CIPHER")

label=tk.Label(root,text="Enter text to encode",font=("Ariel",25))
label.pack(side="top")

ui=tk.Entry(root,font=("Ariel",25))
ui.pack(side="top")

def Start():
    global decryptrd_message
    plaintext = (ui.get())
    key_length = len(plaintext)
    key = generate_random_key(key_length)
    print(f"Plaintext: {plaintext}")
    KT.config(text=f"Key: {key}",font=("Ariel",25))

    plaintext_binary = plaintext_to_binary(plaintext)
    key_repeated = repeat_key(key, key_length)
    key_binary = key_to_binary(key_repeated)

    print(f"plain text in binary is : {plaintext_binary}")
    print(f"Binary key: {key_binary}")
    encrypted_message = encrypt(plaintext_binary, key_binary)
    EM.config(text=f"Encrypted(Binary): {encrypted_message}",font=("Ariel",25))

    button_e.config(text="Decode",command=Decode)
    decryptrd_message = decrypt(encrypted_message, key_binary)
def Decode():
    
    EM.config(text=f"decoded(binary): {decryptrd_message}")

    button_e.config(text="Encode",command=Start)

    quit_=tk.Button(root,text="Quit",height=2,width=8,command=Quit,font=("Ariel",15))
    quit_.pack(side="top")

def generate_random_key(length):
    return ''.join([chr(random.randint(65, 90)) for i in range(length)])

# plain text to binary conversion
def plaintext_to_binary(pt):
    return [format(ord(char), '08b') for char in pt]

# repeating key to the length of plain text
def repeat_key(key, length):
    repeats = length // len(key)
    remainder = length % len(key)
    return (key * repeats) + key[:remainder]

# key to binary conversion
def key_to_binary(key):
    return [format(ord(char), '08b') for char in key]

# encrypting plaintext using XOR gate
def encrypt(plaintext_binary, key_binary):
    encrypted = []
    for pt, key in zip(plaintext_binary, key_binary):
        encrypted.append(''.join(str(int(pt_bit) ^ int(key_bit)) for pt_bit, key_bit in zip(pt, key)))
##    encrypted = [text for text in encrypted 
    return encrypted

# decrypting cipher text using XOR gate
def decrypt(encrypted_message, key_binary):
    decrypted = []
    for em, key in zip(encrypted_message, key_binary):
        decrypted.append(''.join(str(int(enc_bit) ^ int(key_bit)) for enc_bit, key_bit in zip(em,key)))
    return decrypted



def Quit():
    exit()

button_e=tk.Button(root,text="Encode",height=2,width=8,command=Start,font=("Ariel",25))
button_e.pack(side="top")

KT=tk.Label(root,text="")
KT.pack(side="top")
EM=tk.Label(root,text="")
EM.pack(side="top", fill='both')


