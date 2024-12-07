import random  # Importing the random module for generating random numbers

# Function to generate public and private keys for the ElGamal algorithm
def generate_keys(p, g):
    """Generates public and private keys for ElGamal."""
    a = random.randint(2, p - 2)  # Select a random integer as the private key, between 2 and p-2
    h = pow(g, a, p)  # Compute the public key component h = g^a mod p
    return {'private_key': a, 'public_key': (p, g, h)}  # Return both private and public keys

# Function to encrypt a plaintext using ElGamal
def encrypt(public_key, plaintext):
    """Encrypts a plaintext using the ElGamal encryption algorithm."""
    p, g, h = public_key 
    b = random.randint(2, p - 2)  # Generate a random ephemeral key b
    c1 = pow(g, b, p)  # Compute c1 = g^b mod p
    c2 = (plaintext * pow(h, b, p)) % p  
    return (c1, c2)  

# Function to decrypt a ciphertext using ElGamal
def decrypt(private_key, public_key, ciphertext):
    """Decrypts a ciphertext using the ElGamal decryption algorithm."""
    p, g, h = public_key  # Unpack the public key components
    c1, c2 = ciphertext  # Unpack the ciphertext components
    a = private_key 
    s = pow(c1, a, p)  
    s_inv = pow(s, p - 2, p)  
    plaintext = (c2 * s_inv) % p  
    return plaintext  # Return the decrypted plaintext

# Example usage of the algorithm
p = 2027  # Example prime number that should be large in real applications
g = 5   # Example primitive root modulo p

# Key generation
keys = generate_keys(p, g)  # Generate public and private keys
public_key = keys['public_key']  # Extract the public key
private_key = keys['private_key']  # Extract the private key

# Display the generated keys
print("Public Key:", public_key)  # Print the public key
print("Private Key:", private_key)  # Print the private key

# Encryption
message = 2005  # Example plaintext message must be less than p
ciphertext = encrypt(public_key, message)  # Encrypt the message
print("Ciphertext:", ciphertext)  # Print the resulting ciphertext

# Decryption
decrypted_message = decrypt(private_key, public_key, ciphertext)  # Decrypt the ciphertext
print("Decrypted Message:", decrypted_message)  # Print the decrypted message
