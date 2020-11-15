from secrets import token_bytes
from typing import Tuple

def random_key(lenght: int) -> int:
    # gera lenght bytes aleatórios
    tb: bytes = token_bytes(lenght)
    # converte esses bytes em uma cadeia de bits e a devolve
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes : bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy # XOR
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

if __name__ == '__main__':
    key1, key2 = encrypt("One Time Pad!")
    print(f"key1: {key1}\nkey2: {key2}")
    result: str = decrypt(key1, key2)
    print(result)
