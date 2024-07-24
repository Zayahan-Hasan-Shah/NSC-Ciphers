def isPrime(number):
    if number < 2 :
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def generatePrime(minValue, maxValue):
    prime = random.randint(minValue, maxValue)
    while not isPrime(prime):
        prime = random.randint(minValue, maxValue)
    return prime

def modInverse(e, phi):
    for d in range(3, phi):
        if (d * e ) % phi == 1:
            return d
    raise ValueError("Mod inverse does not exist")

def Code():

    global cipherText , d , n

    p,q = generatePrime(1000, 5000), generatePrime(1000, 5000)

    while p == q:
        q = generatePrime(1000, 5000)
        
    n = p * q
    phi_n = (p-1) * (q-1)

    e = random.randint(3, phi_n-1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n-1)
        

    d = modInverse(e, phi_n)

    message = Entry.get()
    message = message.lower()

    message_encoded = [ord(c) for c in message]

    # encryption : (m^e) mod n = c
    cipherText = [pow(c,e,n) for c in message_encoded]
    L2.config(text=cipherText)
    ec.config(text="Decode",command=Decode)
    Quit=tk.Button(root,text="Quit",height=2,width=8,command=Quit_)
    Quit.pack(side="bottom")
    
def Decode():
    
    message_decoded = [pow(ch, d, n) for ch in cipherText]
    dec_message = "".join(chr(ch) for ch in message_decoded)

    L2.config(text=dec_message)

def Quit_():
    quit()

if __name__ == "__main__":
    import tkinter as tk
    import random
    import math

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
