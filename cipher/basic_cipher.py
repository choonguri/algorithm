from enum import Enum

# This is the basic cipher algorithm
# Shift Cipher, Multiplicative Cipher, Affine Cipher, Hill Cipher

class CipherType(Enum):
    none = 0
    shift = 1
    multiplicative = 2
    affine = 3
    hill = 4

class BasicCipher:
    p_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    mod = len(p_list)  # 26
    candidate_key_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    key = candidate_key_list[1]

    m = 1  # case affine
    block_size = 2  # case hill, here allows number 2 only...:-)
    key_list_for_hill = [3, 5, 6, 1]  # case hill
    dummy_char = 'x'  # case hill

    def __init__(self, cipher_type):
        self.cipher_type = cipher_type

    def encrypt(self, plain_text):
        r = []

        if self.cipher_type == CipherType.shift:

            for s in plain_text:
                new_idx = (self.p_list.index(s) + 1 + self.key) % self.mod
                r.append(self.p_list[new_idx - 1])

        elif self.cipher_type == CipherType.multiplicative:

            for s in plain_text:
                new_idx = ((self.p_list.index(s) + 1) * self.key) % self.mod
                r.append(self.p_list[new_idx - 1])

        elif self.cipher_type == CipherType.affine:

            for s in plain_text:
                new_idx = ((self.p_list.index(s) + 1) * self.key + self.m) % self.mod
                r.append(self.p_list[new_idx - 1])

        elif self.cipher_type == CipherType.hill:

            last_empty_position_cnt = len(plain_text) % self.block_size
            if last_empty_position_cnt > 0:
                for i in range(last_empty_position_cnt):
                    plain_text = plain_text + self.dummy_char  # padding
            str_list = list(plain_text)

            for i in range(0, len(str_list), self.block_size):
                new_idx1 = (self.key_list_for_hill[0] * (self.p_list.index(str_list[i]) + 1)
                            + self.key_list_for_hill[1] * (self.p_list.index(str_list[i + 1]) + 1)) % self.mod
                new_idx2 = (self.key_list_for_hill[2] * (self.p_list.index(str_list[i]) + 1)
                            + self.key_list_for_hill[3] * (self.p_list.index(str_list[i + 1]) + 1)) % self.mod
                r.append(self.p_list[new_idx1 - 1])
                r.append(self.p_list[new_idx2 - 1])

        else:
            r = list(plain_text)

        return ''.join(r)

    def decrypt(self, encrypted_text):

        r = []

        if self.cipher_type == CipherType.shift:

            for s in encrypted_text:
                ori_idx = self.p_list.index(s) + 1 - self.key
                if ori_idx < 1:
                    ori_idx = ori_idx + self.mod
                r.append(self.p_list[ori_idx - 1])

        elif self.cipher_type == CipherType.multiplicative:

            for s in encrypted_text:
                idx = self.p_list.index(s) + 1
                temp_idx = idx
                while True:
                    if temp_idx % self.key == 0:
                        break
                    temp_idx = temp_idx + self.mod
                ori_idx = int(temp_idx / self.key)
                r.append(self.p_list[ori_idx - 1])

        elif self.cipher_type == CipherType.affine:

            for s in encrypted_text:
                idx = (self.p_list.index(s) + 1) - self.m
                temp_idx = idx
                while True:
                    if temp_idx % self.key == 0:
                        break
                    temp_idx = temp_idx + self.mod
                ori_idx = int(temp_idx / self.key)
                r.append(self.p_list[ori_idx - 1])

        elif self.cipher_type == CipherType.hill:

            # 1) k1*k4-k2*k3 inverse value
            v = self.key_list_for_hill[0] * self.key_list_for_hill[3] \
                - self.key_list_for_hill[1] * self.key_list_for_hill[2]
            m_v = v % self.mod
            if m_v < 0:
                m_v = self.m + m_v

            i_v = 0

            # If inverse value exists..
            for i in range(1, self.mod):
                if (m_v * i) % self.mod == 1:
                    i_v = i
                    break

            # inverse key list
            m_list = [i_v * self.key_list_for_hill[3] % self.mod,
                      i_v * -1 * self.key_list_for_hill[1] % self.mod,
                      i_v * -1 * self.key_list_for_hill[2] % self.mod,
                      i_v * self.key_list_for_hill[0] % self.mod]

            for i in range(0, len(encrypted_text), self.block_size):
                temp_p1_idx = m_list[0] * (self.p_list.index(encrypted_text[i]) + 1) + m_list[1] * (
                    self.p_list.index(encrypted_text[i + 1]) + 1)
                temp_p2_idx = m_list[2] * (self.p_list.index(encrypted_text[i]) + 1) + m_list[3] * (
                    self.p_list.index(encrypted_text[i + 1]) + 1)
                r.append(self.p_list[(temp_p1_idx % self.mod) - 1])
                r.append(self.p_list[(temp_p2_idx % self.mod) - 1])

        else:
            r = list(encrypted_text)

        return ''.join(r)


plain_text = 'jackyakorea'

print("\nInput Plain Text===> %s" % plain_text)
print("\n---------------encrypt..-------------------\n")

shift_cipher = BasicCipher(CipherType.shift)
multiplicative_cipher = BasicCipher(CipherType.multiplicative)
affine_cipher = BasicCipher(CipherType.affine)
hill_cipher = BasicCipher(CipherType.hill)

shift_enc_text = shift_cipher.encrypt(plain_text)
multiplicative_enc_text = multiplicative_cipher.encrypt(plain_text)
affine_enc_text = affine_cipher.encrypt(plain_text)
hill_enc_text = hill_cipher.encrypt(plain_text)

print("Shift Cipher Result===> %s" % shift_enc_text)
print("Multiplicative Cipher Result===> %s" % multiplicative_enc_text)
print("Affine Cipher Result===> %s" % affine_enc_text)
print("Hill Cipher Result===> %s" % hill_enc_text)

print("\n---------------decrypt..-------------------\n")

print("Shift Ori Text===> %s" % shift_cipher.decrypt(shift_enc_text))
print("Multiplicative Ori Text===> %s" % multiplicative_cipher.decrypt(multiplicative_enc_text))
print("Affine Ori Text===> %s" % affine_cipher.decrypt(affine_enc_text))
print("Hill Ori Result===> %s" % hill_cipher.decrypt(hill_enc_text))
