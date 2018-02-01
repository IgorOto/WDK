from Crypto import Random
from Crypto.Cipher import AES


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def encryption(random_key, message):
    message = pad(message)
    cipher = AES.new(random_key, AES.MODE_ECB)
    return (cipher.encrypt(message)).encode("hex")



random_key = Random.new().read(16)
hex_key = random_key.encode("hex")
print "Losowy klucz = %s" % hex_key




message = "Autorzy zlosliwego oprogramowania stale szukaja nowych sposobow na wykorzystanie naszych smartfonow do niecnych celow, ale program, ktory niedawno wykryla firma Kasperky Lab, chyba bije pod tym wzgledem wszelkie rekordy."
encrypt = encryption(random_key, message)
print "Zaszyfrowana wiadomosc = %s" % encrypt


