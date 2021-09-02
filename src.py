import numpy as np
import secrets
import string
import base64

_char_array = string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_"


class convert:
    # _char_array = string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_"
    # = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

    @staticmethod
    def string_to_b64(string1):
        """
        converts UTF-8 string to URL-Safe Base64 string
        """
        try:
            string1 = string1.encode(encoding="UTF-8")
            string1 = base64.urlsafe_b64encode(string1)
            string1 = string1.decode(encoding="UTF-8")
            string1 = string1.replace("=", "")
            return string1
        except TypeError:
            raise Exception("Invalid data type entered")

    @staticmethod
    def b64_to_string(string1):
        """
        converts only Base64 encoded string back to UTF-8 string
        """
        try:
            paddingLenght = 4 - (len(string1) % 4)
            padding = "=" * paddingLenght
            string1 += padding

            string1 = string1.encode(encoding="UTF-8")
            string1 = base64.urlsafe_b64decode(string1)
            string1 = string1.decode(encoding="UTF-8")
            string1 = string1.replace("=", "")
            return string1
        except UnicodeDecodeError:
            raise Exception("Invalid String provide for decode")
        except TypeError:
            raise Exception("Invalid Data Type entered")

    @staticmethod
    def string_to_array(string1):
        """
        converts UTF-8 string to int array with value range 0-63
        """
        string1 = convert.string_to_b64(string1)
        array1 = np.zeros((len(string1)), dtype=np.uint8)
        for temp in range(len(string1)):
            array1[temp] = _char_array.index(string1[temp])
        return array1

    @staticmethod
    def array_to_string(array1):
        """
        converts int array with value range 0-63 back to UTF-8 string
        """
        string1 = ""
        for temp in array1:
            string1 += _char_array[temp]
        string1 = convert.b64_to_string(string1)
        return string1


class padding:
    @staticmethod
    def pad_with(array1, padder, amount):
        """
        appeds a array of lenght (amount) filled with (padder) to (array1)
        """
        temp = [padder for _ in range(amount)]
        array1 = np.append(array1, temp)
        return array1

    @staticmethod
    def pad_with_DEL(array1, padder, amount):
        # NOTE : add padding delete option
        pass

    @staticmethod
    def pad_to_blocksize(array1, padder, amount):
        """
        (array1) is appended with (padder) until its lenght is multiple of (amount)
        """
        topad = amount - (len(array1) % amount)
        temp = [padder for _ in range(topad)]
        array1 = np.append(array1, temp)
        return array1

    @staticmethod
    def pad_to_blocksize_PKCS(array1, amount):
        """
        (array1) is appended with (padder) until its lenght is multiple of (amount)
        """
        topad = amount - (len(array1) % amount)
        temp = [topad for _ in range(topad)]
        array1 = np.append(array1, temp)
        return array1


class process:
    @staticmethod
    def XOR_array(array1, array2):
        """
        performs XOR between (array1,array2) of same lengh
        """
        if len(array1) == len(array2):
            return [x ^ y for x, y in zip(array1, array2)]
        else:
            raise Exception("Invalid lengths of array entered")

    @staticmethod
    def ADD_array(array1, array2):
        """
        performs ADD between (array1,array2) of same lengh with (mod 64)
        """
        if len(array1) == len(array2):
            return (array1 + array2) % 64
        else:
            raise Exception("Invalid lengths of array entered")

    @staticmethod
    def shift(array1, amount, direction):
        """
        performs shift operation on (array1) in "l" or "r" (direction) by (amount)
        """
        if direction == "l":
            return np.roll(array1, -amount)
        elif direction == "r":
            return np.roll(array1, amount)

    @staticmethod
    def s_box(array1, sbox):
        """
        performs substititution on (array1) with reference from (sbox)
        """
        for temp in range(len(array1)):
            array1[temp] = sbox[array1[temp]]
        return array1

    @staticmethod
    def p_box(array1, pbox):
        """
        performs permutation on (array1) with reference from (sbox)
        """
        array2 = [0 for _ in range(len(pbox))]
        for temp in range(len(array1)):
            array2[pbox[temp]] = array1[temp]
        return array2

    @staticmethod
    def swap(array1):
        if len(array1) % 2 == 0:
            length = len(array1)
            return array1[length // 2 :] + array1[: length // 2]
        else:
            raise Exception("Invalud size of array for swaping entered")


class genrate:
    @staticmethod
    def box_generate(size):
        """
        generates an array of lenght (size) with elements from {0,size-1} in random order
        """
        array = np.arange(size, dtype=np.uint8)
        for temp in range(size):
            thern = secrets.randbelow(size)
            array[temp], array[thern] = array[thern], array[temp]
        return array

    @staticmethod
    def string_generate(size):
        """
        generates a string of lenght (size) with random base64 characters
        """
        string = "".join(secrets.choice(_char_array) for _ in range(size))
        return string

    @staticmethod
    def array_generate(size):
        """
        generates a numpy array of lenght (size) with value between {0,63}
        """
        array = [secrets.randbelow(63) for _ in range(size)]
        return array
