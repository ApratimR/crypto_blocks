import numpy as np
import base64


class convert:
    _char_array = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

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
            array1[temp] = convert._char_array.index(string1[temp])
        return array1

    @staticmethod
    def array_to_string(array1):
        """
        converts int array with value range 0-63 back to UTF-8 string
        """
        string1 = ""
        for temp in array1:
            string1 += convert._char_array[temp]
        string1 = convert.b64_to_string(string1)
        return string1


class padding:
    @staticmethod
    def pad_with(array1, padder, amount):
        temp = [padder for _ in range(amount)]
        array1 = np.append(array1, temp)
        return array1

    @staticmethod
    def pad_to_blocksize(array1, padder, amount):
        topad = amount - (len(array1) % amount)
        temp = [padder for _ in range(topad)]
        array1 = np.append(array1, temp)
        return array1

    @staticmethod
    def pad_to_blocksize_PKCS(array1, amount):
        topad = amount - (len(array1) % amount)
        temp = [topad for _ in range(topad)]
        array1 = np.append(array1, temp)
        return array1


class process:
    @staticmethod
    def XOR_array(array1, array2):
        if len(array1) == len(array2):
            return [x ^ y for x, y in zip(array1, array2)]
        else:
            raise Exception("Invalid lengths of array entered")

    @staticmethod
    def shift(array1, amount, direction):
        if direction == "l":
            return np.roll(array1, -amount)
        elif direction == "r":
            return np.roll(array1, amount)

    @staticmethod
    def s_box(array1, sbox):
        for temp in range(len(array1)):
            array1[temp] = sbox[array1[temp]]
        return array1

    @staticmethod
    def p_box(array1, pbox):
        array2 = [0 for _ in range(len(pbox))]
        for temp in range(len(array1)):
            array2[pbox[temp]] = array1[temp]
        return array2


class genrate:
    @staticmethod
    def box_generate(size):
        array = np.arange(size, dtype=np.uint8)
        np.random.shuffle(array)
        return array

    @staticmethod
    def string_generate(size):
        pass
