import tkinter as tk # for GUI

root=tk.Tk()
root.geometry("400x250")
root.resizable(True,False)
title=root.title("Encode/Decode")

decode = []
encode = []
Upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def Quit1():
        root.destroy()

def Decode():
    global Quit
    for i in range(len(encode)):
        if encode[i] == 'A':
            decode.append('X')
        elif encode[i] == 'B':
            decode.append('Y')
        elif encode[i] == 'C':
            decode.append('Z')
        elif encode[i] == 'a':
            decode.append('x')
        elif encode[i] == 'b':
            decode.append('y')
        elif encode[i] == 'c':
            decode.append('z')
        else:
            if encode[i].islower():
                # print(i)
                next_elem = encode[i]
                # print("elem", next_elem)
                index = Upper.index(next_elem)
                # print(index)
                shifted_index = (index - 3) % 52
                # print(shifted_index)
                decode.append(Upper[shifted_index])
            else:
                # print(i)
                next_elem = encode[i]
                # print("elem", next_elem)
                index = Upper.index(next_elem)
                # print(index)
                shifted_index = (index - 3) % 52
                # print(shifted_index)
                decode.append(Upper[shifted_index])
    cs()
    decoded=tk.Label(root,text=f"Decoded:{decode}")
    decoded.pack()
    
    Quit=tk.Button(root,text="Quit",height=2,width=6,command=Quit1)
    Quit.pack()

def Encode():
    global Quit
    user=inp.get()
    for j in range(len(user)):
        if user[j] == 'X':
            encode.append('A')
        elif user[j] == 'Y':
            encode.append('B')
        elif user[j] == 'Z':
            encode.append('C')
        elif user[j] == 'x':
            encode.append('a')
        elif user[j] == 'y':
            encode.append('b')
        elif user[j] == 'z':
            encode.append('c')
        else:
            if user[j].islower() :
                # print(j)
                next_elem = user[j]
                # print("elem", next_elem)
                index = Upper.index(next_elem)
                # print(index)
                shifted_index = (index + 3) % 52
                # print(shifted_index)
                encode.append(Upper[shifted_index])
            else:
                # print(j)
                next_elem = user[j]
                # print("elem", next_elem)
                index = Upper.index(next_elem)
                # print(index)
                shifted_index = (index + 3) % 26
                # print(shifted_index)
                encode.append(Upper[shifted_index])
    
    cs()
    encoded=tk.Label(root,text=f"Encoded:{encode}")
    encoded.pack(pady=40)

    decode=tk.Button(root,text="Decode",height=2,width=6,command=Decode)
    decode.place(x=40,y=80)

    Quit=tk.Button(root,text="Quit",height=2,width=6,command=Quit1)
    Quit.place(x=100,y=80)

    
    
def cs():
    cs=tk.Button(root,height=20,width=10000)
    cs.place(x=-10,y=-10) 

inp=tk.Entry(root)
inp.place(x=40,y=40)

Encode=tk.Button(root,text="Encode" ,height=1,width=16,command=Encode)
Encode.place(x=40,y=80)