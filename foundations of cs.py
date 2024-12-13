import random

def generate_prime():
    """Find a random prime number between 10,000 and 50,000."""
    for num in range(random.randint(10000, 50000), 50000):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            return num

def find_primitive_root(p):
    """Find a small number that works as a primitive root for p."""
    for g in range(2, p):
        if pow(g, p - 1, p) == 1:
            return g

def generate_keys(p, g):
    """Create private and public keys."""
    private_key = random.randint(2, p - 2)
    public_key = (p, g, pow(g, private_key, p))
    return private_key, public_key

def encrypt(public_key, plaintext):
    """Encrypt the message."""
    p, g, h = public_key
    random_key = random.randint(2, p - 2)
    c1 = pow(g, random_key, p)
    c2 = (plaintext * pow(h, random_key, p)) % p
    return c1, c2

def decrypt(private_key, public_key, ciphertext):
    """Decrypt the message."""
    p, _, _ = public_key
    c1, c2 = ciphertext
    s = pow(c1, private_key, p)
    s_inv = pow(s, p - 2, p)
    return (c2 * s_inv) % p

# Main program
p = generate_prime()
g = find_primitive_root(p)
private_key, public_key = generate_keys(p, g)

print("Public Key:", public_key)
print("Private Key:", private_key)

message =   # Your message to encrypt
ciphertext = encrypt(public_key, message)
print("Ciphertext:", ciphertext)

decrypted_message = decrypt(private_key, public_key, ciphertext)
print("Decrypted Message:", decrypted_message)
