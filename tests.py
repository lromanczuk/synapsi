# python -m pytest tests.py
from layers import caesar, crypto


def test_encode_decode():
    text = '''
# LoremIpsumi simplydumm ytextofthe LoremIpsumi 
#     mIp     sbe        d              mIp 
#     anu     nprinterto alleyo         anu
#     mIp     simplydumm     xtoft      mIp
#     mIp     sbe         stssss        mIp
#     anu     nprinterto okssssssss     anu
'''
    # encode
    encoded = crypto(text)
    encoded_caesar = caesar(encoded)
    
    # decode
    decoded_caesar = caesar(encoded_caesar, method="decrypt")
    decoded = crypto(decoded_caesar, method="decrypt")
    assert decoded==text



