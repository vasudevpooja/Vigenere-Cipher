# [Vigenère Cipher](https://github.com/vasudevpooja/Vigenere-Cipher/blob/main/Vigen%C3%A8re%20Cipher%20Code.py)
Vigenère Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets. The encryption of the original text is done using the Vigenère square or Vigenère table.
 
The table consists of the alphabets written out 26 times in different rows, each alphabet shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar Ciphers.
![image](https://user-images.githubusercontent.com/76071184/145519088-22d3626e-28d7-48f2-b4d4-4c9ef87299ef.png)

At different points in the encryption process, the cipher uses a different alphabet from one of the rows.

The alphabet used at each point depends on a repeating keyword.

# Encryption 
The first letter of the plaintext is combined with the first letter of the key.Similarly, the second letter of the plaintext is combined with the second letter of the key. This process continues continuously until the plaintext is finished.

# Decryption 
Decryption is done by the row of keys in the vigenere table. First, select the row of the key letter, find the ciphertext letter's position in that row, and then select the column label of the corresponding ciphertext as the plaintext.

A more easy implementation could be to visualize Vigenère algebraically by converting [A-Z] into numbers [0–25]. 

# [Caesar Cipher](https://github.com/vasudevpooja/Vigenere-Cipher/blob/main/Caesar%20Shift.py)
The Caesar Cipher is a monoalphabetic rotation cipher used by Gaius Julius Caesar. Caesar rotated each letter of the plaintext forward three times to encrypt, so that A became D, B became E, etc.
    
![Caesar Shift](https://user-images.githubusercontent.com/76071184/145519859-6816908b-bbf7-4637-bdfd-4bbeaf0d411e.png)
