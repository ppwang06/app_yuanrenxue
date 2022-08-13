"""
猿人学app 逆向第一题
未做之前 大概已知道是个java层的md4加密
输入:page=21660284103  输出 8566491c142d570269da3ac27600cdd
"""
from loguru import logger
import ctypes
import time


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shift(n, i):
    if i == 0 and n < 0:
        return n + 2 ** 32
    if n < 0:
        n = ctypes.c_uint32(n).value
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)


class Sign:

    def __init__(self):
        self.A = 1732584193
        self.B = -271733879
        self.C = -1732584194
        self.D = 271733878

    @staticmethod
    def f(i, i2, i3):
        return ((~i) & i3) | (i2 & i)

    @staticmethod
    def g(i, i2, i3):
        return (i & i3) | (i & i2) | (i2 & i3)

    @staticmethod
    def h(i, i2, i3):
        return int_overflow(int_overflow(i ^ i2) ^ i3)

    def ff(self, i, i2, i3, i4, i5, i6):
        return self.rotate_left(i + self.f(i2, i3, i4) + i5, i6)

    def gg(self, i, i2, i3, i4, i5, i6):
        return self.rotate_left(int_overflow(i + self.g(i2, i3, i4) + i5 + 1518565785), i6)

    def hh(self, i, i2, i3, i4, i5, i6):
        return self.rotate_left(int_overflow(i + self.h(i2, i3, i4) + i5 + 1859775393), i6)

    @staticmethod
    def rotate_left(i, i2):
        # logger.info(f"i:{i}, i2:{i2}")
        return unsigned_right_shift(i, (32-i2)) | int_overflow(i << i2)

    def padding(self, str_list):
        new_list = []
        length = len(str_list) * 8
        for one in str_list:
            new_list.append(one)
        new_list.append(128)
        while ((len(new_list) * 8) + 64) % 512 != 0:
            new_list.append(0)
        for i in range(8):
            a = (unsigned_right_shift(length, (i * 8)) & 255)
            new_list.append(a)
        return new_list

    @staticmethod
    def change_to_hex(c):
        if c > 0:
            return hex(c).replace("0x", "")
        return hex(c & 0xFFFFFFFF).replace("0x", "")

    def sign(self, target_str: str):
        target_list = [ord(s) for s in target_str]
        res_list = self.padding(target_list)
        i = self.A
        i2 = self.B
        i3 = self.C
        i4 = self.D

        i5 = 0
        i_arr = ["" for _ in range(16)]
        for i6 in range(16):
            i7 = (i5 * 64) + (i6 * 4)
            i_arr[i6] = res_list[i7 + 3] << 24 | res_list[i7] | res_list[i7 + 1] << 8 | res_list[i7 + 2] << 16

        i_arr2 = [0, 4, 8, 12]
        i8 = i
        i9 = i2
        i10 = i3
        i11 = i4
        i12 = 0
        while i12 < 4:
            i13 = i_arr2[i12]
            i8 = self.ff(i8, i9, i10, i11, i_arr[i13], 3)
            ff = self.ff(i11, i8, i9, i10, i_arr[i13 + 1], 7)
            i10 = self.ff(i10, ff, i8, i9, i_arr[i13 + 2], 11)
            i9 = self.ff(i9, i10, ff, i8, i_arr[i13 + 3], 19)
            i12 += 1
            i11 = ff
        i_arr3 = [0, 1, 2, 3]
        i14 = i8
        i15 = i11
        i16 = 0
        while i16 < 4:
            i17 = i_arr3[i16]
            i14 = self.gg(i14, i9, i10, i15, i_arr[i17], 3)
            i15 = self.gg(i15, i14, i9, i10, i_arr[i17 + 4], 5)
            i10 = self.gg(i10, i15, i14, i9, i_arr[i17 + 8], 9)
            i9 = self.gg(i9, i10, i15, i14, i_arr[i17 + 12], 13)
            i16 += 1
        i_arr4 = [0, 2, 1, 3]
        i18 = i14
        i19 = 0
        while i19 < 4:
            i20 = i_arr4[i19]
            hh = self.hh(i18, i9, i10, i15, i_arr[i20], 3)
            i15 = self.hh(i15, hh, i9, i10, i_arr[i20 + 8], 9)
            i10 = self.hh(i10, i15, hh, i9, i_arr[i20 + 4], 11)
            i9 = self.hh(i9, i10, i15, hh, i_arr[i20 + 12], 15)
            i19 += 1
            i18 = hh
        i = int_overflow(i + i18)
        i2 = int_overflow(i2 + i9)
        i3 = int_overflow(i3 + i10)
        i4 = int_overflow(i4 + i15)
        return self.change_to_hex(i) + self.change_to_hex(i2) + self.change_to_hex(i3) + self.change_to_hex(i4)


if __name__ == '__main__':
    cstr = "page=21660284103"
    s = Sign()
    res_sign = s.sign(cstr)
    logger.info(f"sign:{res_sign}")




