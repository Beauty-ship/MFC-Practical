import numpy as np

def text_to_numbers(text):
    text = text.upper()
    return [0 if ch == ' ' else ord(ch) - 64 for ch in text if ch.isalpha() or ch == ' ']

def numbers_to_text(numbers):
    chars = []
    for n in numbers:
        n = round(n)
        if n == 0:
            chars.append(' ')
        else:
            chars.append(chr(int(n) + 64))
    return ''.join(chars)

def encode_message(message, key):
    """Encode the message using the key matrix."""
    nums = text_to_numbers(message)
    n = key.shape[0]

    while len(nums) % n != 0:
        nums.append(0)

    blocks = [nums[i:i+n] for i in range(0, len(nums), n)]
    
    encoded_blocks = [key.dot(block) for block in blocks]
    encoded_message = np.concatenate(encoded_blocks)
    return encoded_message

def decode_message(encoded, key):
    n = key.shape[0]
    inv_key = np.linalg.inv(key)
    blocks = [encoded[i:i+n] for i in range(0, len(encoded), n)]
    decoded_blocks = [inv_key.dot(block) for block in blocks]
    decoded_message = np.concatenate(decoded_blocks)
    return numbers_to_text(decoded_message)

if __name__ == "__main__":
    key = np.array([[2, 1],
                    [3, 2]])

    message = "Linear Algebra is fun"

    print("Original message:", message)

    encoded = encode_message(message, key)
    print("\nEncoded numeric message:\n", encoded)

    decoded = decode_message(encoded, key)
    print("\nDecoded message:\n", decoded)
