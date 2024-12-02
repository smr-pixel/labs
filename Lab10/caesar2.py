def encrypt(plaintext, key):
        ciphertext = ''

        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
                elif char.isupper():
                    encrypted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
                ciphertext += encrypted_char
            elif char == " ":
                ciphertext += char
            else:
                encrypted_symbol = chr(ord(char) + key)
                ciphertext += encrypted_symbol
        return ciphertext

def decrypt(ciphertext, key):
      plaintext = ''
      for char in ciphertext:
          if char.isalpha():
              if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
              elif char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
              plaintext += decrypted_char
          elif char == " ":
              plaintext += char
          else:
              decrypted_symbol = chr((ord(char) - key))
              plaintext += decrypted_symbol
      return plaintext


text = "Hello World!"
key = 3
encrypted_text = encrypt(text, key)
print(f"Encrypted: {encrypted_text}")
decrypted_text = decrypt(encrypted_text, key)
print(f"Decrypted: {decrypted_text}")