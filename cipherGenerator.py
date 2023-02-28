from Crypto.Cipher import AES
import time
key = bytes(input('Think of any secret key\nIts size must be exactly 16 characters!\n'), 'utf-8')
if len(key) == 16:
    cipher = AES.new(key, AES.MODE_CBC)
    with open('cipher_file', 'wb') as c_file:
        c_file.write(cipher.iv)
        c_file.write(key)
    print('Done!')
else:
    print('ERROR: This is a bad key, restart the script and enter exactly 16 characters')
time.sleep(3)