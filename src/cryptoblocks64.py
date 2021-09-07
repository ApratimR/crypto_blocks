"""
Crypto Blocks(B64 Edition)
===

Provides
    1.Various general functions required for creating your own Cryptographic algorithm.
    2.Functions are Classified into classes for ease of use.
    3.instead of operating on a single bit this edition works in B64 style (instead of {0 OR 1} its {0,....,63} values per element)
    4.Provides easy encoding conversion,S&P Box generation,and many more

Available subpackages
---------------------
convert
    consists of various datatype and encoding conversion functions.
padding
    consists of array padding and removing function. works in PKCS style.
process
    consists of general cryptography related math functions.
generate
    consists of tools to generate string,arrays and S&P Box generators.
    With Cryptographically secure methods.
"""


import numpy as np
import secrets
import string
import base64

_char_array = string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_"


class convert:
    @staticmethod
    def string_to_b64(string1):
        """
        converts input string to URL-Safe Base64 encoded string.

        Args:
        ----------
            string1:(str) enter string that needs to be encoded in b64

        Returns:
        ----------
            (str): string encoded in b64format without padding.

        Raises:
        ----------
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
        converts only Base64 encoded string back UTF-8 encoded string.

        Args:
        ----------
            string1:(str)string encoded in b64format.

        Returns:
        ----------
            (str): string encoded in UTF-8

        Raises:
        ----------
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
        converts base64 string to int array with value range 0-63.

        Args:
        ----------
            string1:(str)string encoded in b64format.

        Returns:
        ----------
            (numpy.array[uint32]): array with its element value range in {0,63}.(B64 encoded)
        """
        string1 = convert.string_to_b64(string1)
        array1 = np.zeros((len(string1)), dtype=np.uint32)
        for temp in range(len(string1)):
            array1[temp] = _char_array.index(string1[temp])
        return array1

    @staticmethod
    def array_to_string(array1):
        """
        converts int array with value range 0-63 back to UTF-8 string.

        Args:
        ----------
            array1:(numpy.array[uint32]) array with element value range in {0,63}.(B64 encoded)

        Returns:
        ----------
            (str): base64 encoded string without padding
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
        padd's the array in PKCS standard to lenght specified by user.

        Args:
        ----------
            array1:(numpy.array[uint32])array with element value range in {0,63}.(B64 encoded)
            amount:(int) the block size

        Returns:
        ----------
            (numpy.array[uint32]): array with PKCS style padding

        """
        topad = amount - (len(array1) % amount)
        temp = [topad for _ in range(topad)]
        array1 = np.append(array1, temp)
        return array1

    @staticmethod
    def pad_REMOVE(array1):
        """
        removes the padding from the array.

        Args:
        ----------
            array1:(numpy.array[uint32])the padded array of which the padding is to be removed

        Returns:
        ----------
            (numpy.array[uint32]): array without the padding
        """
        to_trim = array1[-1]
        array1 = array1[:-to_trim]
        return array1


class process:
    @staticmethod
    def XOR_array(array1, array2):
        """
        performs XOR between two arrays of same length.

        Args:
        ----------
            array1:(numpy.array[uint32]) array with element value range in {0,63}.(B64 encoded)
            array2:(numpy.array[uint32]) array with element value range in {0,63}.(B64 encoded)

        Returns:
        ----------
            (numpy.array[uint32]): array with element value range in {0,63}.(B64 encoded)

        Raises:
        ----------
            Error: Invalid lengths of array entered.
        """
        if len(array1) == len(array2):
            return [x ^ y for x, y in zip(array1, array2)]
        else:
            raise Exception("Invalid lengths of array entered")

    @staticmethod
    def ADD_array(array1, array2):
        """
        performs ADD between (array1,array2) of same lengh with (mod 64).

        Args:
        ----------
            array1:(numpy.array[uint32]) array with element value range in {0,63}.(B64 encoded)
            array2:(numpy.array[uint32]) array with element value range in {0,63}.(B64 encoded)

        Returns:
        ----------
            (numpy.array[uint32]): array with element value range in {0,63}.(B64 encoded)

        Raises:
        ----------
            Error: Invalid lengths of array entered.
        """
        if len(array1) == len(array2):
            return (array1 + array2) % 64
        else:
            raise Exception("Invalid lengths of array entered")

    @staticmethod
    def shift(array1, amount, direction):
        """
        performs shift operation on array in left or right direction by specified amount.

        Args:
        ----------
            array1:(numpy.array[uint32]) array with element value range in {0,63}.(B64 encoded)
            amount:(int) the shift amount
            direction:(str):
                - "l" for left shift
                - "r" for right shift

        Returns:
        ----------
            (numpy.array[uint32]): array with its element shifted
        """
        if direction == "l":
            return np.roll(array1, -amount)
        elif direction == "r":
            return np.roll(array1, amount)

    @staticmethod
    def s_box(array1, sbox):
        """
        performs substititution on the array with reference from sbox array.

        Args:
        ----------
            array1:(numpy.array[uint32]) array with element value range in {0,63}.(B64 encoded)
            sbox:(numpy.array[uint32]) array with all unique values between {0,sbox.size-1} in random order

        Returns:
        ----------
            (numpy.array[uint32]): array with substituted values as per sbox
        """
        for temp in range(len(array1)):
            array1[temp] = sbox[array1[temp]]
        return array1

    @staticmethod
    def p_box(array1, pbox):
        """
        performs permutation on the array with reference from pbox array.

        Args:
        ----------
            array1:(numpy.array[uint32]) array with element value range in {0,63}.(B64 encoded)
            pbox:(numpy.array[uint32]) array with all unique values between {0,sbox.size-1} in random order

        Returns:
        ----------
            (numpy.array[uint32]): array with permuted values as per pbox
        """
        array2 = [0 for _ in range(len(pbox))]
        for temp in range(len(array1)):
            array2[pbox[temp]] = array1[temp]
        return array2

    @staticmethod
    def swap_half(array1):
        """
        swaps the two half in the array.

        Args:
        ----------
            array1:(numpy.array[uint32]) array with element value range in {0,63}.(B64 encoded)

        Returns:
        ----------
            array1:(numpy.array[uint32]) array with the two halves of it swaped

        Raises:
        ----------
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
        generates an array of size mentioned with elements from {0,size-1} in random order and also returns its inverse.

        Args:
        ----------
            size:(int) the size of box required.

        Returns:
        ----------
            (numpy.array[uint32]): array with all unique values in range {0,size-1} in random arrangement
            (numpy.array[uint32]): array with all unique values in range {0,size-1}. its the inverse of the random arrangement above

        Note:
        ----------
            used for generating s_box or p_box arrays
        """
        array = np.arange(size, dtype=np.uint32)
        for temp in range(size):
            thern = secrets.randbelow(size)
            array[temp], array[thern] = array[thern], array[temp]

        array2 = np.zeros(size, dtype=np.uint32)
        for temp in range(size):
            array2[array[temp]] = temp

        return array, array2

    @staticmethod
    def string_generate(size):
        """
        generates a string of mentiond size with random base64 characters.

        Args:
        ----------
            size:(int) the size of box required.

        Returns:
        ----------
            (str): string with random characters from B64 character list
        """
        string = "".join(secrets.choice(_char_array) for _ in range(size))
        return string

    @staticmethod
    def array_generate(size):
        """
        generates a numpy array of lenght (size) with value between {0,63}.

        Args:
        ----------
            size:(int) the size of box required.

        Returns:
        ----------
            (numpy.array[uint32]) array with random elements with value in range {0,63}
        """
        array = [secrets.randbelow(63) for _ in range(size)]
        return array
