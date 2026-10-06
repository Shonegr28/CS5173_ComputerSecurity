import hashlib

# Create the original message.txt file
with open("message.txt", "w") as file:
    file.write("Computer Security")

# Read the original file
with open("message.txt", "rb") as file:
    data = file.read()

# Compute the SHA-256 hash
referenceHash = hashlib.sha256(data).hexdigest()

# Store the original hash
with open("reference_hash.txt", "w") as file:
    file.write(referenceHash)

# Test 1: unchanged file
with open("message.txt", "rb") as file:
    data = file.read()

currentHash = hashlib.sha256(data).hexdigest()

print("Test 1")
print("Stored Hash: ", referenceHash)
print("Current Hash:", currentHash)

if currentHash == referenceHash:
    print("Result: PASS")
else:
    print("Result: FAIL")


# Change the contents of message.txt
with open("message.txt", "w") as file:
    file.write("computer Security")

# Test 2: modified file
with open("message.txt", "rb") as file:
    data = file.read()

currentHash = hashlib.sha256(data).hexdigest()

print("\nTest 2")
print("Stored Hash: ", referenceHash)
print("Current Hash:", currentHash)

if currentHash == referenceHash:
    print("Result: PASS")
else:
    print("Result: FAIL")