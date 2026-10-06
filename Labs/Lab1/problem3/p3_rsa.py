# RSA implementation in Python by Shone Renjan lvl easy spend 10 mins
def rsa(p, q, e):
    
    # need to convert p, q, and e from hexadecimal to integers in order to perform RSA calculations
    p = int(p, 16)
    q = int(q, 16)
    e = int(e, 16)

    # TASK 1; DERIVE PRIVATE KEY
    # calculate n, the product of p and q
    n = p * q
    #  p and q are prime so we need to calculare the totient of n the equation is (p-1)*(q-1)
    totient = (p - 1) * (q - 1)

    # calculate the private key d such that (d * e) mod totient = 1
    d = pow(e, -1, totient)
    print("Private Key:", hex(d)[2:].upper())

    # TASK 2; ENCRYPT 
    message = int("B7A19C3D5E2", 16)
    # Formula: c = m^e mod n
    cipherText = pow(message, e, n)
    print("Ciphertext:", hex(cipherText)[2:].upper())

    # TASK 3; DECRYPT
    # Formula: m=e^d mod n
    decryptedMessage = pow(cipherText, d, n)
    print("Decrypted Message:", hex(decryptedMessage)[2:].upper())


rsa("F7E75FDC469067FFDC4E847C51F452DF", "E85CED54AF57E53E092113E62F436F4F","0D88C3")