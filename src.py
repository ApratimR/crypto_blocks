import numpy as np
import secrets
import string
import base64

_char_array = string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_"


class convert:
    @staticmethod
    def string_to_b64(string1):
        """
        converts any string to URL-Safe Base64 string.

        Args:
            string1:(str)

        Returns:
            (str) encoded in b64format without padding.

        Raises:
            TypeError: Invalid data type entered.
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
        converts only Base64 encoded string back to UTF-8 string.

        Args:
            string1:(str) encoded in b64format.

        Returns:
            (str)

        Raises:
            TypeError: Invalid data type entered.
            UnicodeDecodeError: Invalid String provide for decode
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
        converts base64 string to int array with value range 0-63

        Args:
            string1:(str) encoded in b64format.

        Returns:
            (numpy.array[uint8])
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

        Args:
            array1:(numpy.array[uint8]) encoded in b64format.

        Returns:
            (str) in original format
        """
        string1 = ""
        for temp in array1:
            string1 += _char_array[temp]
        string1 = convert.b64_to_string(string1)
        return string1


class padding:
    @staticmethod
    def pad(array1, amount):
        """
        padd's the array in PKCS standard to lenght specified by user

        Args:
            array1:(numpy.array[uint8]) encoded in b64format.
            amount:(int) the block size

        Returns:
            array1:(numpy.array[uint8])

        """
        topad = amount - (len(array1) % amount)
        temp = [topad for _ in range(topad)]
        array1 = np.append(array1, temp)
        return array1

    @staticmethod
    def pad_REMOVE(array1):
        """
        removes the padding from the array

        Args:
            array1:(numpy.array[uint8]) encoded in b64format.

        Returns:
            array1:(numpy.array[uint8])
        """
        to_trim = array1[-1]
        array1 = array1[:-to_trim]
        return array1


class process:
    @staticmethod
    def XOR_array(array1, array2):
        """
        performs XOR between two arrays of same lengh

        Args:
            array1:(numpy.array[uint8]) encoded in b64format.
            array2:(numpy.array[uint8]) encoded in b64format.

        Returns:
            array1:(numpy.array[uint8])

        Raises:
            Error: Invalid lengths of array entered.
        """
        if len(array1) == len(array2):
            return [x ^ y for x, y in zip(array1, array2)]
        else:
            raise Exception("Invalid lengths of array entered")

    @staticmethod
    def ADD_array(array1, array2):
        """
        performs ADD between (array1,array2) of same lengh with (mod 64)

        Args:
            array1:(numpy.array[uint8]) encoded in b64format.
            array2:(numpy.array[uint8]) encoded in b64format.

        Returns:
            array1:(numpy.array[uint8])

        Raises:
            Error: Invalid lengths of array entered.
        """
        if len(array1) == len(array2):
            return (array1 + array2) % 64
        else:
            raise Exception("Invalid lengths of array entered")

    @staticmethod
    def shift(array1, amount, direction):
        """
        performs shift operation on array in left or right direction by specified amount

        Args:
            array1:(numpy.array[uint8]) encoded in b64format.
            amount:(int) the shift amount
            direction:(str):
                - "l" for left shift
                - "r" for right shift

        Returns:
            array1:(numpy.array[uint8])
        """
        if direction == "l":
            return np.roll(array1, -amount)
        elif direction == "r":
            return np.roll(array1, amount)

    @staticmethod
    def s_box(array1, sbox):
        """
        performs substititution on the array1 with reference from sbox array

        Args:
            array1:(numpy.array[uint8]) encoded in b64format.
            sbox:(numpy.array[uint8]) encoded in b64format.

        Returns:
            array1:(numpy.array[uint8])
        """
        for temp in range(len(array1)):
            array1[temp] = sbox[array1[temp]]
        return array1

    @staticmethod
    def p_box(array1, pbox):
        """
        performs permutation on (array1) with reference from (sbox)

        Args:
            array1:(numpy.array[uint8]) encoded in b64format.
            pbox:(numpy.array[uint8]) encoded in b64format.

        Returns:
            array1:(numpy.array[uint8])
        """
        array2 = [0 for _ in range(len(pbox))]
        for temp in range(len(array1)):
            array2[pbox[temp]] = array1[temp]
        return array2

    @staticmethod
    def swap(array1):
        """
        swaps the two half in the array

        Args:
            array1:(numpy.array[uint8]) encoded in b64format.

        Returns:
            array1:(numpy.array[uint8])

        Raises:
            Error: Invalud size of array for swaping entered.
        """
        if len(array1) % 2 == 0:
            length = len(array1)
            return array1[length // 2 :] + array1[: length // 2]
        else:
            raise Exception("Invalud size of array for swaping entered")


class genrate:
    @staticmethod
    def box_generate(size):
        """
        generates an array of size mentioned with elements from {0,size-1} in random order

        Args:
            size:(int) the size of box required.

        Returns:
            array1:(numpy.array[uint8])

        Note:
            used for generating s_box or p_box arrays
        """
        array = np.arange(size, dtype=np.uint8)
        for temp in range(size):
            thern = secrets.randbelow(size)
            array[temp], array[thern] = array[thern], array[temp]
        return array

    @staticmethod
    def string_generate(size):
        """
        generates a string of mentiond size with random base64 characters

        Args:
            size:(int) the size of box required.

        Returns:
            array1:(numpy.array[uint8])
        """
        string = "".join(secrets.choice(_char_array) for _ in range(size))
        return string

    @staticmethod
    def array_generate(size):
        """
        generates a numpy array of lenght (size) with value between {0,63}

        Args:
            size:(int) the size of box required.

        Returns:
            array1:(numpy.array[uint8])
        """
        array = [secrets.randbelow(63) for _ in range(size)]
        return array
