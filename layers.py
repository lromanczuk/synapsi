import os
from cryptography.fernet import Fernet


# This function can be used in two ways. 
# To encode or decode a string
# For it to work properly you will need an env variable named SHIFT
# It will decide how much to "move" the unicode string to "left or right"
def caesar(old_str, method='encrypt'):
    shift = int(os.environ.get('SHIFT'))  
    if method=='decrypt':
        shift = -shift
    new_str = ''
    for l in old_str:
        if l == '\n' or l == ' ':
            new_str += l
        else:
            new_str += (chr(ord(l) + shift))
    return new_str


# This function can be used in two ways. 
# To encode or decode a string
# For it to work properly you will need an env variable named KEY
# The KEY must be compatible with Fernet
def crypto(old_str, method='encrypt'):
    key = os.environ.get('KEY').encode('utf-8')
    f = Fernet(key)
    if method=='decrypt':
        token = f.decrypt(old_str.encode('utf-8'))
        return token.decode('utf-8')
    token = f.encrypt(old_str.encode('utf-8'))
    return token.decode('utf-8')

