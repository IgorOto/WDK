from Crypto.Util import Counter
from Crypto import Random
from Crypto.Cipher import AES




random_iv = Random.new().read(16)
hex_iv = random_iv.encode("hex")
print "Losowy wektor iv = %s" % hex_iv


count = Counter.new(128, initial_value=int(hex_iv,16))


def encryption(random_key, count, message):
    cipher = AES.new(random_key, AES.MODE_CTR, counter = count)
    return (cipher.encrypt(message)).encode("hex")




random_key = Random.new().read(16)
hex_key = random_key.encode("hex")
print "Losowy klucz = %s" % hex_key




message = "Autorzy zlosliwego oprogramowania stale szukaja nowych sposobow na wykorzystanie naszych smartfonow do niecnych celow, ale program, ktory niedawno wykryla firma Kasperky Lab, chyba bije pod tym wzgledem wszelkie rekordy."
encrypt = encryption(random_key, count, message)
print "Zaszyfrowana wiadomosc = %s" % encrypt


