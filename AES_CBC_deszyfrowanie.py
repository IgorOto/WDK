from Crypto import Random
from Crypto.Cipher import AES



unpad = lambda s: s[0:-ord(s[-1])]



def decryption(key, vector_iv, cipher):
    deciph = AES.new(key, AES.MODE_CBC, vector_iv)
    return unpad(deciph.decrypt(cipher))



key = "316f0dad60b45412a3457a89cdada7f5".decode("hex")


vector_iv = "ef809392865fa5dc95d05767a6ea84dc".decode("hex")




cipher = "fce4f3f7b2fd55a5068e8fbeaea40a81a85ce404eb9a7a9da3f0b33273f22d1ce128508c5ac19db4d5997980d9fb62c204c8fd34b03035ce3cd6b3e56bb2ea98d017a151dfbb316bd8a66cb7c77ae0d20aabf70bb3b367aa94c37bd72bbbc465a5bcf3bc98f616d890f1bfcc3df8ed2c".decode("hex")
message = decryption(key, vector_iv, cipher)
print ("Odszyfrowana wiadomosc = %s") % message
