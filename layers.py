import os
from cryptography.fernet import Fernet


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


def crypto(old_str, method='encrypt'):
    key = b'JriDryy8jgLxrkUNuivnvCBUGRHt6oUeN8ltlRxyfok=' # it should be spelled otherwise e.g like shift i think
    f = Fernet(key)
    if method=='decrypt':
        token = f.decrypt(old_str.encode('utf-8'))
        return token.decode('utf-8')
    token = f.encrypt(old_str.encode('utf-8'))
    return token.decode('utf-8')

