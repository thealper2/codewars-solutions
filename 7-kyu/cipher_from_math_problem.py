def encrypt(word, n):
    result = [ord(c) - ord('a') + 1 for c in word]
    for _ in range(n):
        for i in range(len(word)):
            result[i] = result[i] * 3 - 5
            
    return result
        
        
def decrypt(encrypted_word, n):
    for _ in range(n):
        for i in range(len(encrypted_word)):
            encrypted_word[i] = (encrypted_word[i] + 5) // 3
            
    return ''.join([chr(c + ord('a') - 1) for c in encrypted_word])
