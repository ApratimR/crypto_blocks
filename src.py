import numpy as np
import base64


class convert:
    _char_array = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

    @staticmethod
    def b64encode(string1):
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
    def b64decode(string1):
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
    def array_encode(string1):
        """
        converts UTF-8 string to int array with value range 0-63
        """
        string1 = convert.b64encode(string1)
        array1 = np.zeros((len(string1)), dtype=np.uint8)
        for temp in range(len(string1)):
            array1[temp] = convert._char_array.index(string1[temp])
        return array1

    @staticmethod
    def array_decode(array1):
        """
        converts int array with value range 0-63 back to UTF-8 string
        """
        string1 = ""
        for temp in array1:
            string1 += convert._char_array[temp]
        string1 = convert.b64decode(string1)
        return string1


class process:
    pass
