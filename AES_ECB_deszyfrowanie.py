from Crypto import Random
from Crypto.Cipher import AES


unpad = lambda s: s[0:-ord(s[-1])]


def decryption(key, cipher):

    deciph = AES.new(key, AES.MODE_ECB)
    return unpad(deciph.decrypt(cipher))


key = "32461636d541e5e8dc97e5c2c51acfd7".decode("hex")


cipher = "5e43406b98a05300e3614d7434ed3d15fa3d36dafbb1472be7b3bf5e6b053120f59556ed8afcb7a6d29903b896074c8fc7fea23c8e01259819921b7568c375552cb315ec7a49836ec0c64144b2f7d76b0fc286c5652a6ab5fe7cb41617881018f164824a4eb1365af03a8952673a4803238441a3a9b7ad15d43c58f29b1e47c206d09eefd9ca75b7f3d59022a82c36741e8ae0ffc3f0d9700047e35f6e4459dc5c3dc2dfd9e8064496e1b4408fc5d8b1073ac2d199c89f5bd1058ad7ff8e388090fabf4fb7f94226f6a1ecbbd7d7f59f3be7253ba1f8791fce7fd0e4d444c8852f1748366fd8fd28a443667b8c85fba884763524f021a026be9d23c5672440041bfb185034b6dd6546f159608b282fb84b482e828f869ae42de73198c9946ec671affd71549002e909c3a8f6c7d21c923ba94ecef817ca0a6f2dc77e2b9a71d062cb9914930ce049fa31cbae3d1be284".decode("hex")
message = decryption(key, cipher)
print "Odszyfrowana wiadomosc = %s" % message
