import base64


def encode_username(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode_username(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def test(username):
    password = 'this@isExtra1'

    enc = encode_username(password, username)
    username_dec = (decode_username(password, enc))
    print(enc)

    if username != username_dec:
        print('no match')
    else:
        print('match')


#test('sion_cohen.the.man_on_themoon')
