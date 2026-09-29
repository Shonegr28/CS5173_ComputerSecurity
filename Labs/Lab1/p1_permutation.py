''' Store each character of the ciphertext along with its index '''
''' Find the length of the key '''
''' Convert each character in the key into an integer '''
''' Split the ciphertext into blocks based on the length of the key '''
''' Loop through each block '''
''' Loop through the key and place each ciphertext character
    into the correct plaintext position based on the key '''
''' Join the plaintext characters together '''
''' Return the plaintext '''
    
def permutationCipher(cipherText, key):
    cipherArray = list(cipherText)
    key = [int(char) for char in key]
    key_length = len(key)
    plaintext = []

    for i in range(0, len(cipherArray), key_length):
        rows = cipherArray[i:i + key_length] # according to the key length create a row for each chatacter in the plaintext 
        #print(rows)  # Testing: if it prints the correct row
        plainRow = [""] * key_length
        # print(plainRow)  # Testing: if it prints the c
        for j in range(key_length):
            plainRow[key[j] - 1] = rows[j]
        plaintext.extend(plainRow)
        #print(plaintext)  # Testing: if it prints the correct plaintext after extending with the current row
    plaintext = ''.join(plaintext)
    return plaintext

print(permutationCipher("Q9fL3XvT8pR2mN7kD1sA6cH0yZ5uJ4eBqWn","7145236"))