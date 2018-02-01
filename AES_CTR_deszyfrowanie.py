from Crypto.Util import Counter
from Crypto import Random
from Crypto.Cipher import AES






hex_iv = "43b51aeb42d826e71726de23b7384077"

count = Counter.new(128, initial_value=int(hex_iv,16))



def decryption(key, count, cipher):
    deciph = AES.new(key, AES.MODE_CTR, counter = count)
    return deciph.decrypt(cipher)




key = "fb202e894b38838b29f878d02e0df633".decode("hex")



cipher = "7a1dda4f9ae6f54eafb72b41e17242aabe4efc2ceac62b2bea688afd0165f7f31f6f7fc3465b084ddabc30fcf4603176e867843dc3cf697ca68d187761f31342694f39459bb69eca0a8fb7903c588dbc3a7d82c47320979355b8403d0b9b0bf424b104afc0717af1074d41becdcbcf4aaca4eecd0b247ba2014784a8d7ac0ee68a2bad91eeeaf1fcd0553c97d65b6adf65ebc30c34f7f3d418ccee1ff1864042cc84ce867079dc24b62df9e87b7d1b93ed4651310fe6d94d15b60602194c8743f68df99ad42850fea8e30c73176e5d3fec8cc0cbc8775b4c9370168bd051eaccad327b96585bd2a5209e438550510b77e542f14b86d0959527265d39cb2f7f6db04c7a82ca62226d799b6c38042e37c35f3f971e450cfd5ce7d71c6b42891bd96c6e44c399fa3d45f2f2ed6d1d5fea2da05227887e4a8992788d1d16eef5fdfe52129cd131c7c91a9b8ddc2f98ac4273a433ce52ddcb64cbe2c25bc16be31b8e7e70d7591277bd71a164aa7235a50f7381ba75dfce4e017c5362500144a45a0e56a6887f2ed8c6f106daa9b479ae2d56520db79923439b0a772e1aded76e7f238ed32f761ddf20ecf8eab4".decode("hex")
message = decryption(key, count, cipher)
print "Odszyfrowana wiadomosc = %s" % message
