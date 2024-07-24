import tkinter as tk
import random
import math

root=tk.Tk()

root.resizable(False,False)
title=root.title("Encoder/Decode")

label=tk.Label(root,text="Enter text to encode",font=("Ariel",25))
label.pack(side="top")

ui=tk.Entry(root,font=("Ariel",25))
ui.pack(side="top")

def Start():
    global decrypt
    pt=ui.get()
    pt = pt.upper()
    
    print("Plaint text : ", pt)
    print("==================")

    encrypted_ans = []
    decrypted_ans = []
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    break_three = []
    spliting_word = []
    ascii_pt = []
    key_pt_mult = []
    mode_for_pt = [] # not a 2d array
    mode_for_pt_3d = []
    encrypt = []
    expand_key =[]
    adjoint = []
    inv_adj = []
    key_inverese = []
    dec_key_mult = [] 
    dec_sum = []
    decrypt = []

    # removing spaces from the plain text
    if " " in pt:
        pt = pt.replace(" ", "")
        
    # len of plain text
    print(len(pt))
    print("==================")

    pt_break = 0
    if len(pt) > 4 : 
        if(len(pt)%2 == 0):
            pt_break = 3
            start = 0
            
            # breaking string in the pair of 3
            for i in range(len(pt)):
                break_three.append(pt[start:start+pt_break])
                start += pt_break
                
            break_three = [text for text in break_three if text != ""]

            print("breaking words into 3 words : ", break_three)
            print("==================")
            
            # filtering 'x'
            for i in range(len(break_three)):
                if len(break_three[i]) != 3:
                    while len(break_three[i]) != 3:
                        break_three[i] += 'X'
                        if len(break_three[i]) == 3:
                            break
            
            print("filtering x : ", break_three)
            print("==================")
            
            # spliting words
            for word in break_three:
                temp_word = []
                for chars in word:
                    temp_word.append(chars)
                spliting_word.append(temp_word)
            
            print("Spliting words : ")
            for i in range(len(spliting_word)):
                for j in range(len(spliting_word[i])):
                    print(spliting_word[i][j], end= " ")
                print()
            print("==================")
            
            # ascii characters (0-25) of alphabets
            for i in range(len(spliting_word)):
                temp_ascii_pt =[]
                for j in range(len(spliting_word[i])):
                    split = spliting_word[i][j]
                    assci = alphabets.index(split)
                    temp_ascii_pt.append(assci)
                ascii_pt.append(temp_ascii_pt)
              
            print("Index of plain text")    
            for i in range(len(ascii_pt)):
                for j in range(len(ascii_pt[i])):
                    print(ascii_pt[i][j], end=" ")
                print()
                
            print("==================")
            
            # key
            # hard coded key
            key = [[17,17,5],[21,18,21],[2,2,19]]
            PK=tk.Label(root,text="Key : ",font=("Ariel",25))
            PK.pack(side="top")
            print("key")
            for i in range(3):
                for j in range(3):
                    key1= ""
                    key1 += " " + str(key[i][j])
                    PK.config(text=PK.cget("text") + key1)
##                    print(key[i][j], end = " ")
                print()
            print("==================")
            
            # multiplcation of key and plain text
            for i in range(len(ascii_pt)):
                for j in range(len(key)):
                    temp_solution = []
                    for k in range(len(key)):
                        print(f'{ascii_pt[j][k]} * {key[k][j]}', end = " ")
                        temp_solution.append(ascii_pt[i][k] * key[k][j])
                    key_pt_mult.append(temp_solution)
                    print()
            
                    
            print("==================")
           
            print("just multiplcation of key and plain text(index)")
            for i in range(len(key_pt_mult)):
                for j in range(len(key_pt_mult[i])):
                    print(key_pt_mult[i][j], end = " ")
                print()
                
            print("==================")
            for i in range(len(key_pt_mult)):
                print(f'sum of : {key_pt_mult[i]} is {sum(key_pt_mult[i])} and mode 26 is {sum(key_pt_mult[i])%26}')
                mode_for_pt.append(sum(key_pt_mult[i])%26)
            
            print("==================")    
            for i in range(len(mode_for_pt)):
                print(mode_for_pt[i])
                
            on = 0 # start
            off = 3 # stop
            
            for i in range(len(mode_for_pt)):
                mode_for_pt_3d.append(mode_for_pt[on:on+off])
                on += off
                
            print("==================") 
            # 3d array of solution
            print("Encryption in the form of numbers")
            mode_for_pt_3d = [subarray for subarray in mode_for_pt_3d if subarray]
            for i in range(len(mode_for_pt_3d)):
                for j in range(len(mode_for_pt_3d[i])):
                    if mode_for_pt_3d[i][j] is None:
                        continue
                    else:
                        print(mode_for_pt_3d[i][j], end= " ")
                print()
                
            print("==================") 
            
            # Encryption in the form of text
            for i in range(len(mode_for_pt_3d)):
                for j in range(len(mode_for_pt_3d[i])):
                    text = mode_for_pt_3d[i][j]
                    print(f'{mode_for_pt_3d[i][j]} --> {alphabets[text]}')
                    encrypt.append(alphabets[text])
            
            print("==================") 
            print("Encryption of the plain text is : ", "".join(encrypt))
            print("==================")
            ET.config(text=f"Encryption of the plain text is : {''.join(encrypt)}")
            button_e.config(text="Decode",command=decode_)
            # determinant of key
            a = key[0][0] * (key[1][1] * key[2][2] - key[1][2] * key[2][1])
            b = key[0][1] * (key[1][0] * key[2][2] - key[1][2] * key[2][0])
            c = key[0][2] * (key[1][0] * key[2][1] - key[1][1] * key[2][0])
            determinant = (a-b+c) % 26
            
            print(determinant)
            print("==================") 
            
            if determinant == 0:
                print("Can't solve further")
                quit()
                
            elif determinant < 0 and determinant < 26:
                determinant += 26
                print(determinant)
                
            else:
                    
                # expanding key matrix
                print("Expanded key : ")
                expand_key = [
                    [key[0][0], key[0][1], key[0][2], key[0][0], key[0][1]], 
                    [key[1][0], key[1][1], key[1][2], key[1][0], key[1][1]],
                    [key[2][0], key[2][1], key[2][2], key[2][0], key[2][1]],          
                    [key[0][0], key[0][1], key[0][2], key[0][0], key[0][1]], 
                    [key[1][0], key[1][1], key[1][2], key[1][0], key[1][1]]
                ]
                
                print(len(expand_key))
                print("==================") 
                for i in range(len(expand_key)):
                    for j in range(len(expand_key)):
                        print(expand_key[i][j], end= " ")
                    print()
                
                print("==================") 
                
                # solving for ajoint of key
                # row 1 
                r1c1 = (expand_key[1][1] * expand_key[2][2] - expand_key[1][2] * expand_key[2][1]) % 26
                r1c2 = (expand_key[2][1] * expand_key[3][2] - expand_key[2][2] * expand_key[3][1]) % 26
                r1c3 = (expand_key[3][1] * expand_key[4][2] - expand_key[3][2] * expand_key[4][1]) % 26
                # row 2
                r2c1 = (expand_key[1][2] * expand_key[2][3] - expand_key[1][3] * expand_key[2][2]) % 26
                r2c2 = (expand_key[2][2] * expand_key[3][3] - expand_key[2][3] * expand_key[3][2]) % 26
                r2c3 = (expand_key[3][2] * expand_key[4][3] - expand_key[3][3] * expand_key[4][2]) % 26
                # row 3
                r3c1 = (expand_key[1][3] * expand_key[2][4] - expand_key[1][4] * expand_key[2][3]) % 26
                r3c2 = (expand_key[2][3] * expand_key[3][4] - expand_key[2][4] * expand_key[3][3]) % 26
                r3c3 = (expand_key[3][3] * expand_key[4][4] - expand_key[3][4] * expand_key[4][3]) % 26
                
                print(r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3 )
                print("Adjoint")
                
                adjoint = [
                    [r1c1, r1c2, r1c3],
                    [r2c1, r2c2, r2c3],
                    [r3c1, r3c2, r3c3]
                ]
                
                for i in range(3):
                    for j in range(3):
                        print(adjoint[i][j], end = " ")
                    print()
                print("==================")
                
                # inverse of determinant
                inv_der = 0
                
                if determinant%2 == 0:
                    for i in range(1,100):
                        mo = (determinant * i + 1) % 26
                        if mo == 1:
                            inv_der = i
                            break
                    print(inv_der) 
                else:
                    for i in range(1,100):
                        mo = (determinant * i) % 26
                        if mo == 1:
                            inv_der = i
                            break
                    print('inverse of determinant : ', inv_der) 
                    
                print("==================")
                
                # multiplying adjoint with inverse of determinant
                print('multiplying adjoint with inverse of determinant')
                for i in range(3):
                    temp = []
                    for j in range(3):
                        print(f'{adjoint[i][j]} * {inv_der} = {adjoint[i][j] * inv_der}', end=" ")
                        temp.append(adjoint[i][j] * inv_der)
                    inv_adj.append(temp)
                    print()  
                    
                    
                print("==================")  
                
                # inverse of key
                for i in range(3):
                    temp_mod = []
                    for j in range(3):
                        print(f'{inv_adj[i][j]} % {26} = {inv_adj[i][j] % 26}', end=" ")
                        temp_mod.append(inv_adj[i][j] % 26)
                    key_inverese.append(temp_mod)
                    print()
                
                print("==================")  
                print("key inverse :")    
                for i in range(len(key_inverese)):
                    for j in range(len(key_inverese)):
                        print(key_inverese[i][j], end = " ")
                    print()
                    
                print("==================")     
                   
                for i in range(len(mode_for_pt_3d)):
                    for j in range(len(key_inverese)):
                        temp_dec_num = [] 
                        for k in range(len(key_inverese)):
                            print(f'{(mode_for_pt_3d[i][k] * key_inverese[k][j]) % 26}', end = " ")
                            temp_dec_num.append((mode_for_pt_3d[i][k] * key_inverese[k][j]) % 26)
                        dec_key_mult.append(temp_dec_num)
                        print()
                      
                print("==================")         
                        
                for i in range(len(dec_key_mult)):
                    print(f'sum of : {dec_key_mult[i]} is {sum(dec_key_mult[i])} and mode 26 is {sum(dec_key_mult[i])%26}')
                    dec_sum.append(sum(dec_key_mult[i])%26)
                    
                print("==================")
                
                for i in range(len(dec_sum)):
                    print(alphabets[dec_sum[i]] , " is decrypted answer")
                    if alphabets[dec_sum[i]] != 'X':
                        decrypt.append(alphabets[dec_sum[i]])
                
                print("Decrypted answer is : ", "".join(decrypt))    

def decode_():
    ET.config(text=f"Decrypted answer is : {''.join(decrypt)}")

    quit_=tk.Button(root,text="Quit",height=2,width=8,command=Quit,font=("Ariel",25))
    quit_.pack(side="top")
    
def Quit():
    exit()
    
button_e=tk.Button(root,text="Encode",height=2,width=8,command=Start, font=("Ariel", 25))
button_e.pack(side="top")
ET=tk.Label(root,text="",font=("Ariel",25))
ET.pack(side="top")




