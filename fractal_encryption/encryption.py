def encrypt_message(message, fractal_pixels, iv):
    encrypted_message = []
    iv_int = int.from_bytes(iv.encode('utf-8'), 'big')
    for i, char in enumerate(message):
        fractal_value = fractal_pixels[i // len(fractal_pixels)][i % len(fractal_pixels[0])]
        encrypted_char = chr(ord(char) ^ fractal_value ^ iv_int)
        encrypted_message.append(encrypted_char)
    return ''.join(encrypted_message)

def decrypt_message(encrypted_message, fractal_pixels, iv):
    decrypted_message = []
    iv_int = int.from_bytes(iv.encode('utf-8'), 'big')
    for i, char in enumerate(encrypted_message):
        fractal_value = fractal_pixels[i // len(fractal_pixels)][i % len(fractal_pixels[0])]
        decrypted_char = chr(ord(char) ^ fractal_value ^ iv_int)
        decrypted_message.append(decrypted_char)
    return ''.join(decrypted_message)
