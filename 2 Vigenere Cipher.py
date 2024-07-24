import tkinter as tk
import random

root=tk.Tk()
root.resizable(False,False)
root.geometry("400x400")
title=root.title("Encoder/Decode")

label=tk.Label(root,text="Enter text to encode",font=("Arial", 25))
label.pack(side="top")

ui=tk.Entry(root,font=("Arial", 25))
ui.pack(side="top")

def Start(CF=False):
    global decode
    pt=(ui.get())
    pt = pt.upper()
    print(pt)
    keyword = []
    for i in range(random.randint(4,5)):
       keyword.append(chr(random.randint(65,90)))
    key = ''.join(keyword)
    print(key)
    button_e.config(text="Decode",command=ET_)

    def equalkey(key, pt):
        key_len = len(key) # length of keyword
        pt_len = len(pt) # length of plain text
        key_repeat = '' # repeated keyword
        if key_len == pt_len:
            return key
        elif key_len < pt_len:
            repeat = pt_len // key_len # need to be repeat the keyword
            reminder = pt_len % key_len # additional character after repeatition
            key_repeat += key * repeat 
            key_repeat += key[:reminder]
            return key_repeat
        elif key_len > pt_len:
            key_repeat += key[:pt_len]
            return key_repeat
     
    def generate_vigenere_table():
        global repeate_key
        global vigenere_table
        Capital = [] # ascii 65 to 90
        for i in range(26):
            Capital.append([])
            for j in range(26):
                Capital[i].append(chr(((i + j) % 26) + 65))
        for row in Capital:
           print(" ".join(row))
        return Capital 

    # Generate and print the Vigenère table
    vigenere_table = generate_vigenere_table()
        
    repeate_key = equalkey(key, pt)
    print(repeate_key)

    # encryption , encryption is done by matrix method
    def encrypt(pt, repeate_key, vigenere_table):
        global ET
        pt = list(pt)
        encrypted = []
        for i in range(len(pt)):
            row = ord(repeate_key[i]) - 65  # Calculate the row index in the Vigenère table
            print(row)
            col = ord(pt[i]) - 65  # Calculate the column index in the Vigenère table
            print(col)
            encrypted_char = vigenere_table[row][col]  # Get the character from the Vigenère table
            encrypted.append(encrypted_char)  # Add the encrypted character to the list
        return ''.join(encrypted)
        
    
    encode = encrypt(pt, repeate_key, vigenere_table)
    print('===============')
    ET.config(text=f"Encoded:{encode}")
    
    print(encode)

    # decryption, decryption is done by Mod method
    
    def decrypt(encode, vigenere_table, repeate_key):
        global decode
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        encode = list(encode)
        decrypted = ''
        for i in range(len(encode)):
            result = ( ord(encode[i]) - ord(repeate_key[i]) ) % 26
            decrypted += alphabet[result]
        return decrypted
        
    decode = decrypt(encode, vigenere_table, repeate_key)
    print(decode)
def ET_():
    ET.config(text=f"Defcoded:{decode}")
    quit_=tk.Button(root,text="Quit",height=2,width=8,command=Quit,font=("Arial", 25))
    quit_.pack(side="bottom")
    
def Quit():
    exit()


button_e=tk.Button(root,text="Encode",height=2,width=8,command=Start,font=("Arial", 25))
button_e.pack(side="top")
ET=tk.Label(root,text="",font=("Arial", 25))
ET.pack(side="top")


