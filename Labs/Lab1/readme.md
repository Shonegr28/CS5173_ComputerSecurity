# Lab 1 – Cryptography
## Course
5173 Computer Security
### By
Shone George Kutty Renjan

## Description
This lab goes over three cryptography Problems Permutation Cipher, SHA-256 Hash Function, and  RSA Cipher

## Files

- `p1_permutation.py`  
   Given plaintext and key uses permutation to return the cipher text .The code encrypts the plaintext by splitting it into rows of 7 characters and rearranging each row using the key 7145236. It then joins all the rearranged charcters together to create the ciphertext. Using reverse process decrypts the ciphertext.

    Run Command: python3 p1_permutation.py
    INPUT: PLAINTEXT: Q9fL3XvT8pR2mN7kD1sA6cH0yZ5uJ4eBqWn
           KEY: 7 1 4 5 2 3 6
    OUTPUT: Plaintext: Q9fL3XvT8pR2mN7kD1sA6cH0yZ5uJ4eBqWn
            Ciphertext: 93XfLvQ82mpRNTksAD167HZ50yuc4qWeBnJ
            Decrypted Plaintext: Q9fL3XvT8pR2mN7kD1sA6cH0yZ5uJ4eBq

- `p2_hash.py`  
  Uses SHA-256 to check if the files have been changed or not providing us with intergrity. The code open the message file writes the "Computer Security" then 
  Then reads it SHA-256 format saves the reference hash and compares to the current hash that determine hash values to determine if they pass or not. Then Changes message file to "computer Security" and when comparing to the reference hash value and the current hash value it fails.

  ### In 2-3 sentences, explain how the comparison detects the modification and why storing a hash can save space compared with keeping a duplicate of a large file. according to the lecuture and the lab

    The contents of the file will change, thus the SHA-256 hash of the file will change and the new hash will not match the stored reference hash . This modification is detected by the comparison. Storing the hash saves space . A hash is a fixed length digest that is much smaller than a complete copy of a large file. 
    
    Run Command: python3 p2_hash.py

    OUTPUT: TEST1: UNCHANGED
            Reference Hash: a3fa73779dd6d4c3fbe123d8ee1b18ed5702ab9a1ff4e56fc96393636062d3cf
            Current Hash: a3fa73779dd6d4c3fbe123d8ee1b18ed5702ab9a1ff4e56fc96393636062d3cf
            PASS 

            TEST2: CHANGED
            Reference Hash: a3fa73779dd6d4c3fbe123d8ee1b18ed5702ab9a1ff4e56fc96393636062d3cf
            Current Hash after change: 05246ba3ef845a26ed12dc584820571653012cfdef1a5db80cead7c6130a1469
            FAIL

- `p3_rsa.py`  
   RSA using the given hexadecimal values of `p`, `q`, and `e`. The program calculates the private key `d` using RSA formual, encrypts the given message, and decrypts the ciphertext back to the original message.

    Run Command: python3 p3_rsa.py

   OUTPUT: Private Key: 3587A24598E5F2A21DB007D89D18CC50ABA5075BA19A33890FE7C28A9B496AEB
           Ciphertext: 264D96FB2A6ABF5CF7702E5B8CBCDA4D298D56B1005A5E6916D7DF9E3077ECEB
           Decrypted Message: B7A19C3D5E2

- `message.txt`  
  Contains the message used for the SHA-256 hash test.

- `reference_hash.txt`  
  Stores the original SHA-256 hash of `message.txt`.
