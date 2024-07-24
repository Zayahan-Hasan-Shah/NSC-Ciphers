



def createPlayFairMatrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    preparedKey = []
    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            preparedKey.append(char)
            
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' 
    for char in alphabet:
        if char not in seen:
            preparedKey.append(char)
            
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(preparedKey[i:i+5])
        
    return matrix

def findPosition(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    raise ValueError(f'Character {char} not found in matrix')
    
def preProcessText(text):
    text = re.sub(r'[^A-Z]', '', text.upper().replace("J", "I"))
    processedText = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text):
            char2 = text[i + 1]
        else:
            char2 = 'X'
        if char1 == char2:
            processedText += char1 + "X"
            i += 1
        else:
            processedText += char1 + char2
            i += 2
    if len(processedText) % 2 != 0:
        processedText += "X"
    return processedText

def encrypt(plainText, matrix):
    plainText = preProcessText(plainText)
    cipherText = ""
    for i in range(0, len(plainText), 2):
        char1, char2 = plainText[i], plainText[i + 1]
        row1, col1 = findPosition(char1, matrix)
        row2, col2 = findPosition(char2, matrix)
        if row1 == row2:
            cipherText += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipherText += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            cipherText += matrix[row1][col2] + matrix[row2][col1]
    return cipherText

def decrypt(cipherText, matrix):
    plaintext = ""
    for i in range(0, len(cipherText), 2):
        char1, char2 = cipherText[i], cipherText[i + 1]
        row1, col1 = findPosition(char1, matrix)
        row2, col2 = findPosition(char2, matrix)
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext

def printMatrix(matrix):
    La1=[]
    
    for row in matrix:
        PL3=(" ".join(row))
        La1.append(PL3)
        
    L3.config(text=f"{La1[0]}\n{La1[1]}\n{La1[2]}\n{La1[3]}\n{La1[4]}")

    
        
def checkPlaintext(plaintext):
    bot = False
    specialChars = r"[\.\\\^\$\*\+\?\{\}\[\]\|()]"
    if re.findall(specialChars, plaintext):
        return not bot
        # raise ValueError(f'Do not enter the special character!')
    return bot
        
key = "playfair example"
matrix = createPlayFairMatrix(key)

def Code():
    global ciphertext
    plaintext = str(Entry.get())


    checker = checkPlaintext(plaintext)
    if checker == True:
        print("Enter the text for encryption : ")
        plaintext = input("")

    L2.config(text="Playfair Matrix:")
    printMatrix(matrix)
    print("==============================")


    ciphertext = encrypt(plaintext, matrix)
    L4.config(text=f"Encrypted Text: {ciphertext}")
    
    Quit=tk.Button(root,text="Quit",height=2,width=8,command=Quit_)
    Quit.pack(side="bottom")
    
    ec.config(text="Decrypt",command=Decode)


def Decode():
    global ciphertext
    decrypted_text = decrypt(ciphertext, matrix)
    L4.config(text=f"Decrypted Text: {decrypted_text}")

    L2.pack_forget()
    L3.pack_forget()

def Quit_():
    exit()
        

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



