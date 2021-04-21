#RSA code.py
import math
import string
import random
    
print("Enter p and q as prime numbers")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))

def primility_check(a): #check if p and q are prime or not

    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True
    
p_check = primility_check(p)
q_check = primility_check(q)

while(((p_check==False)or(q_check==False))): #Repead inputs if p or q is not a prime
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q:"))
    p_check = primility_check(p)
    q_check = primility_check(q)

n = p * q # RSA moduls
print("=====================================================")
print("RSA modulus is:",n)

print("=====================================================") 
phi= (p-1)*(q-1) # Calculating of Phi(n)
print("The value of phi(n) is:", phi)

e = random.randint(1, phi-1)
def gcd_e (e,phi): #Calculation the gcd of e % phi(n)
    while(phi!=0):
        e,phi=phi,e%phi
    return e
 
def gcd_euclid(e,phi): #Euclid's Algorithm
    for i in range(1,phi-1):  #Select public exponent from the set of (1,phi-1, and checking if gcd(e,phi(n)=1) if not chose again before the condition is met. 
        while(e!=0):
            a,b=phi//e,phi%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(phi,a,e,b))
            phi=e
            e=b
            
s=int(512*0.3)
for i in range(1,s): # s=512*0.3
    if(gcd_e(i,phi)==1): # e calculation
        e=i 
print("=====================================================")
print("The value of e is:",e)
print("=====================================================")

def eea(n, e):
    if n == 0:
        return (e,0, 1)
    else:
        gcd, s, t = eea(e % n, n)
        print("%d*(%d) + (%d)*(%d)"%(n,s,t,e))
        t= t - (e // n) * s
        return (gcd, t , s)
 
def mult_inv(e,phi):#Multiplicative Inverse
    gcd,t,_=eea(e,phi)
    if(gcd!=1):
        return None
    else:
        if(t>0):
            print("t =", t)
        elif(t<0):
            t=t%phi
            print("Because t<0: t =",t)
            return t
 

def encrypt(pub_key,plain_text): #Encryption
    e,n=pub_key
    y=[]
    for i in plain_text:
        if(i.islower()):               
            message= ord(i)-97
            cipher=(message**e)%n
            y.append(cipher)
        elif(i.isupper()):#If characters in the string are uppercase return->True.If the string does not contain uppercase characters->False
                message = ord(i)-65 #Return the integer that represents the character "i" in ASCII
                cipher=(message**e)%n # Encryption of message
                y.append(cipher)
        elif(i.isspace()):
            space=32
            y.append(space)
    return y
     
def decrypt(priv_key,cipher):# Decryption
    d,n=priv_key
    cipher_txt=cipher.split(',')
    x=''
    for i in cipher_txt:
        if(i=='32'): # White space
            x+=' '
        else:
            message=(int(i)**d)%n # Decryprion of message y^d%n every character in text
            message+=65 # to upper case ASCII
            character=chr(message) # conversion from ASCII numbers to characters
            x+=character
    return x
def main():

    d = mult_inv(e,phi)
    print("=====================================================")
    print("The value of d is:",d)
    print("=====================================================")
    public_key = (e,n)
    private_key = (d,n)
    print("Private Key is:",private_key)
    print("Public Key is:",public_key)
    print("=====================================================")
     
    message = input("Enter the message => ")
    print("The message is : ", message)
    enc_or_dec = input("For encryption please print 'e' for for decrytion print 'd': =>")
    if(enc_or_dec=='e'):
        encripted_msg=encrypt(public_key,message)
        print("The encrypted message is:",encripted_msg)
    elif(enc_or_dec=='d'):
        print("Your decrypted message is:",decrypt(private_key,message))
    else:
        print("Something went wrong. Please try again.")
        
main()
