import hashlib

# TASK 1: Computing and Storing the Hash
Messagefile = open("message.txt", "w")
Messagefile.write("Computer Security")
Messagefile.close()

# Read the message.txt file
messageFile = open("message.txt", "rb")
message = messageFile.read()
messageFile.close()

print("TEST1: UNCHANGED")

# Create the reference hash
referenceHash = hashlib.sha256(message).hexdigest()

# Task 2: Verifying File Integrity
print("Reference Hash:", referenceHash)

# Write the reference hash to reference_hash.txt
writeReferenceHash = open("reference_hash.txt", "w")
writeReferenceHash.write(referenceHash)
writeReferenceHash.close()

#compute the current hash
currentHash = hashlib.sha256(message).hexdigest()
print("Current Hash:", currentHash)

#compare the current hash with the reference hash determine wheather they pass or fail
if currentHash == referenceHash:
    print("PASS \n")
else:
    print("FAIL \n")

print("TEST2: CHANGED")

# Change message.txt
changeFile = open("message.txt", "w")
changeFile.write("computer Security")
changeFile.close()

# Read the changed file
openChangedFile = open("message.txt", "rb")
changedMessage = openChangedFile.read()
openChangedFile.close()

# Compute the new hash
currentHash = hashlib.sha256(changedMessage).hexdigest()

print("Reference Hash:", referenceHash)
print("Current Hash after change:", currentHash)

#compare the current hash with the reference hash determine wheather they pass or fail
if currentHash == referenceHash:
    print("PASS")
else:
    print("FAIL")