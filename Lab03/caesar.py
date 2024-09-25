class Caesar:
   def __init__(self, key = 0):
        self._key = key

   def get_key(self):
       return self._key
   
   def set_key(self, key):
       self._key = key
   
   def encrypt(self, plaintext):
        plaintext = plaintext.lower()
        ciphertext = []

        for char in plaintext:
            if char.isalpha():
                encrypted_char = chr((ord(char) - ord('a') + self._key) % 26 + ord('a'))
                ciphertext.append(encrypted_char)
            elif char == " ":
                ciphertext.append(char)
            else:
                encrypted_symbol = chr(ord(char) + self._key)
                ciphertext.append(encrypted_symbol)
        return "".join(ciphertext)
   
   def decrypt(self, ciphertext):
      ciphertext = ciphertext.lower()
      plaintext = []
      for char in ciphertext:
          if char.isalpha():
              decrypted_char = chr((ord(char) - ord('a') - self._key) % 26 + ord('a'))
              plaintext.append(decrypted_char)
          elif char == " ":
              plaintext.append(char)
          else:
              decrypted_symbol = chr((ord(char) - self._key))
              plaintext.append(decrypted_symbol)
      return "".join(plaintext)
   

cipher = Caesar()
cipher.set_key(3)
print(cipher.encrypt('hello WORLD!')) # prints “khoor zruog$”
print(cipher.decrypt('KHOOR zruog$')) #prints “hello world!”
cipher.set_key(6)
print(cipher.encrypt('zzz')) #prints “fff”
print(cipher.decrypt('FFF')) #prints “zzz”
cipher.set_key(-6) #Negative keys should be supported!
print(cipher.encrypt('FFF')) #prints “zzz”
