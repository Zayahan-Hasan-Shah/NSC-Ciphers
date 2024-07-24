def encrypt_transposition(plain_text: str, key: str) -> str:
    global cipher_text
    table = []
    key_lst = sorted(key)
    k = 0

    total_rows = (len(plain_text) + len(key) - 1) // len(key)  # ceil(len(plain_text) / len(key))
    
    for _ in range(total_rows):
        row = []
        for _ in range(len(key)):
            if k > len(plain_text) - 1:
                row.append("-")
            else:
                row.append(plain_text[k])
            k += 1
        table.append(row)

    cipher = ""
    for k_indx in range(len(key)):
        curr_idx = key.index(key_lst[k_indx])
        for row in table:
            cipher += row[curr_idx]

    return cipher
def decrypt_transposition(cipher: str, key: str) -> str:
    total_rows = (len(cipher) + len(key) - 1) // len(key)  # ceil(len(cipher) / len(key))
    total_columns = len(key)
    key_lst = sorted(key)

    table = [[""] * total_columns for _ in range(total_rows)]

    k = 0
    for col in range(total_columns):
        original_index = key.index(key_lst[col])
        for row in range(total_rows):
            if k < len(cipher):
                table[row][original_index] = cipher[k]
                k += 1

    plain_text = ""
    for row in table:
        plain_text += "".join(row)

    plain_text = plain_text.rstrip('-')
    return plain_text

def Code():
    global cipher_text,key

    plain_text = Entry.get()
    key = "SECRET"
    
    cipher_text = encrypt_transposition(plain_text.replace(" ", "").upper(), key.upper())
    L2.config(text=f"Cipher Text: {cipher_text}")

    ec.config(text="Decrypt",command=Decode)
    Quit=tk.Button(root,text="Quit",height=2,width=8,command=Quit_)
    Quit.pack(side="bottom")

def Decode():
    decrypted_text = decrypt_transposition(cipher_text, key.upper())
    L2.config(text=f"Decrypted Text: {decrypted_text}")

def Quit_():
    quit()
    
if __name__ == "__main__":
    
    import tkinter as tk
    import re

    root=tk.Tk()
    root.resizable(False,False)

    Label1=tk.Label(text="Enter the text for encryption ")
    Label1.pack(side="top")
    
    Entry=tk.Entry()
    Entry.pack()

    ec=tk.Button(root,text="Encrypt",height=2,width=8,command=Code)
    ec.pack(side="top")

    L2=tk.Label()
    L2.pack()

    
