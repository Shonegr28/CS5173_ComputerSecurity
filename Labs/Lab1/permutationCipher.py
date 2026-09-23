def permutationCipher(cipherText, key):
    key_length = len(key)
    for index, letter in enumerate(cipherText):
        for key_length in letter:
            print(key_length)
        

permutationCipher("Q9fL3XvT8pR2mN7kD1sA6cH0yZ5uJ4eBqWn","7145236")