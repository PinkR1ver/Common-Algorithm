import math
import random

def isprime(x):
    if x <=1:
        return False
    for i in range(2, int(x/2) + 1):
        if x%i == 0:
            return False
    return True

def find_coprime(x:int):
    while True:
        y = random.randint(3, x)
        if (math.gcd(y, x) == 1):
            return y


def generate_key(start_point):
    p = start_point
    while True:
        if isprime(p):
            break
        else:
            p += 1

    q = int(1.5 * p) # avoid too close p and q, it will make RSA be easy to break
    while True:
        if isprime(q):
            break
        else:
            q  += 1
    
    n = p * q
    r = (p - 1) * (q - 1)
    e = find_coprime(r)
    
    while True:
        d = random.randint(3, 1000000)
        if (d * e) % r == 1:
            break
    
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

def encryption(message, public_key):
    return message**public_key[1] % public_key[0]

def decryption(message, private_key):
    return message**private_key[1] % private_key[0]

if __name__ == '__main__':
    public_key, private_key = generate_key(700)

    print(public_key, private_key)

    message = "FUCK YOU"

    message_value = [ord(i) for i in message]

    print(message_value)

    encrypted_message = [encryption(i, public_key) for i in message_value]

    print(encrypted_message)

    decrypted_message = [decryption(i, private_key) for i in encrypted_message]

    print(decrypted_message)

    receive_message = ''.join([chr(i) for i in decrypted_message])
    print(receive_message)
