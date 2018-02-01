from Crypto import Random
from Crypto.Cipher import AES


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def encryption(random_key, random_iv, message):
    message = pad(message)
    cipher = AES.new(random_key, AES.MODE_CBC, random_iv)
    return (cipher.encrypt(message)).encode("hex")





random_key = Random.new().read(16)
hex_key = random_key.encode("hex")
print ("Losowy klucz = %s") % hex_key




random_iv = Random.new().read(16)
hex_iv = random_iv.encode("hex")
print ("Losowy wektor iv = %s") % hex_iv




message = "Autorzy zlosliwego oprogramowania stale szukaja nowych sposobow na wykorzystanie naszych smartfonow do niecnych celow, ale program, ktory niedawno wykryla firma Kasperky Lab, chyba bije pod tym wzgledem wszelkie rekordy."
encrypt = encryption(random_key, random_iv, message)
print ("Zaszyfrowana wiadomosc = %s") % encrypt


