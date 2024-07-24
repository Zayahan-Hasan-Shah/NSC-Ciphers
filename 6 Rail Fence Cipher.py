
def encrypt_rail_fence(text, rails):
    # Initialize rail matrix
    rail_matrix = [['' for j in range(len(text))] for i in range(rails)]

    # Direction variables for zigzag pattern
    direction_down = False
    row, col = 0, 0

    # Fill the rail matrix
    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        rail_matrix[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    # Print the rail matrix for visualization
    tl1=""
    tl2=""
    tl3=""
    TL=[]
    TL1=[]
    TL2=[]
    TL3=[]
    L2.config(text="Rail Fence Zigzag Table (Encryption):")
    for i in range(rails):
        for j in range(len(text)):
            if rail_matrix[i][j] != '':
##                print(rail_matrix[i][j], end=' ')
                TL.append(rail_matrix[i][j])
            else:
##                print('=', end=' ')
                TL.append("=")
##        print()
        if i == 0:
            TL1=TL
            TL=[]
        if i == 1:
            TL2=TL
            TL=[]
        if i == 2:
            TL3=TL
            TL=[]
    for x in range(len(TL1)):
        tl1+=TL1[x]+" "
        tl2+=TL2[x]+" "
        tl3+=TL3[x]+" "
    L3.config(text=f"{tl1}\n{tl2}\n{tl3}")

    ec.config(text="Decrypt",command=Decode)
    
    # Read ciphertext row by row
    cipher_text = ''
    for i in range(rails):
        for j in range(len(text)):
            if rail_matrix[i][j] != '':
                cipher_text += rail_matrix[i][j]

    return cipher_text

def decrypt_rail_fence(cipher_text, rails):
    
    # Initialize rail matrix
    rail_matrix = [['' for j in range(len(cipher_text))] for i in range(rails)]

    # Direction variables for zigzag pattern
    direction_down = None
    row, col = 0, 0

    # Fill the rail matrix with placeholders
    for _ in range(len(cipher_text)):
        rail_matrix[row][col] = '*'
        col += 1

        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False

        if direction_down:
            row += 1
        else:
            row -= 1

    # Fill the rail matrix with characters from ciphertext
    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if rail_matrix[i][j] == '*' and index < len(cipher_text):
                rail_matrix[i][j] = cipher_text[index]
                index += 1

    # Print the rail matrix for visualization.
    tl1=""
    tl2=""
    tl3=""
    TL=[]
    TL1=[]
    TL2=[]
    TL3=[]
    L2.config(text="Rail Fence Zigzag Table (Decryption):")
    for i in range(rails):
        for j in range(len(cipher_text)):
            if rail_matrix[i][j] != '':
                TL.append(rail_matrix[i][j])
##                print(rail_matrix[i][j], end=' ')
            else:
                TL.append("=")
##                print('=', end=' ')
##        print()
        if i == 0:
            TL1=TL
            TL=[]
        if i == 1:
            TL2=TL
            TL=[]
        if i == 2:
            TL3=TL
            TL=[]
    for x in range(len(TL1)):
        tl1+=TL1[x]+" "
        tl2+=TL2[x]+" "
        tl3+=TL3[x]+" "
    L3.config(text=f"{tl1}\n{tl2}\n{tl3}")
    
    # Read plaintext column by column
    plain_text = ''
    row, col = 0, 0
    for i in range(len(cipher_text)):
        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False

        if rail_matrix[row][col] != '*':
            plain_text += rail_matrix[row][col]
            col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return plain_text


    

def Code():
    global rails
    global encrypted_text

    plaintext = str(Entry.get())
    plaintext = plaintext.replace(" ","")
    rails = 3

    encrypted_text = encrypt_rail_fence(plaintext, rails)
    L4.config(text=f"Encrypted: {encrypted_text}")

    Quit=tk.Button(root,text="Quit",height=2,width=8,command=Quit_)
    Quit.pack(side="bottom")

def Decode():

    decrypted_text = decrypt_rail_fence(encrypted_text, rails)
    L4.config(text=f"Decrypted: {decrypted_text}")
        
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
    L3=tk.Label()
    L3.pack()
    L4=tk.Label()
    L4.pack()

    
    
