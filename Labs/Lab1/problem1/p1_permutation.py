# Permutation Cipher implementation in Python by Shone Renjan lvl: Easy spend 10 mins

def permutationCipher(plainText, key):
    key = [int(char) for char in key] # turns the string to a list of integers
    key_length = len(key) # gets the length of the key
    cipherText = [] # stores the ciphertext in the list

    for i in range(0, len(plainText), key_length):
        # According to the key length, create a row for each block of plaintext
        row = plainText[i:i + key_length]
        # Testing if the correct row is created
        # print(row)
        
        cipherRow = [""] * key_length
        # Testing if the empty ciphertext row is created correctly
        # print(cipherRow)
        for j in range(key_length):
            cipherRow[key[j] - 1] = row[j]
        cipherText.extend(cipherRow)
        # Testing the ciphertext after adding the current row
        # print(cipherText)

    cipherText = ''.join(cipherText) # joins the list of ciphertext
    return cipherText

def permutationDecrypt(cipherText, key):
    key = [int(char) for char in key] # turns the string to a list of integers
    key_length = len(key) # gets the length of the key
    plainText = [] # stores the plaintext in the list

    for i in range(0, len(cipherText), key_length):
        # According to the key length, create a row for each block of ciphertext
        row = cipherText[i:i + key_length]
        # Testing if the correct row is created
        # print(row)

        plainRow = [""] * key_length
        # Testing if the empty plaintext row is created correctly
        # print(plainRow)

        for j in range(key_length):
            plainRow[j] = row[key[j] - 1]

        plainText.extend(plainRow)

        # Testing the plaintext after adding the current row
        # print(plainText)

    plainText = ''.join(plainText) # joins the list of plaintext
    return plainText



plainText = "Q9fL3XvT8pR2mN7kD1sA6cH0yZ5uJ4eBqWn"
key = "7145236"
cipherText = permutationCipher(plainText, key)
print("Plaintext:", plainText)
print("Ciphertext:", cipherText)
print("Decrypted Plaintext:", permutationDecrypt(cipherText, key))