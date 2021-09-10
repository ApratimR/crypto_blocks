# <img src="logo/CB64.svg" height=80>
Crypto Blocks is a simple package that consists of various fundamental functions for building cryptogaphic algorithms.

To Install
---
Just use `pip install cryptoblocks64` to install.

### It provides:

* Various general functions required for creating your own Cryptographic algorithm.
* Functions are Classified into classes for ease of use.
* instead of operating on a single bit this edition works in B64 style (instead of {0 or 1} its **{0,....,63}** values per element)
* Provides easy encoding conversion,S&P Box generation,and many more functions

## The Structure:

There are total 4 main classes which are:
* Convert
* Padding
* Process
* Generate

### **Convert:**
consists of various datatype and encoding conversion functions

| function | description | code example |
| :-- | :-- | :-- |
| string_to_b64 | converts input string to URL-Safe Base64 encoded string. |`encoded_string = cb.convert.string_to_b64(string1)` |
| b64_to_string |converts only Base64 encoded string back UTF-8 encoded string. |`original_string = cb.convert.b64_to_string(encoded_string)` |
| string_to_array | converts base64 string to int array with value range 0-63. | `array = cb.convert.string_to_array(encoded_string)` |
|array_to_string|converts int array with value range 0-63 back to UTF-8 string.|`encoded_string = cb.convert.string_to_array(array)`|

### **Padding:**
consists of array padding and removing function. works in PKCS style.

| function | description | code example |
| :-- | :-- | :-- |
|pad|padd's the array in PKCS standard to lenght specified by user.|`array_with_padding = cb.padding.pad(array_without_padding,block_size)`|
|pad_REMOVE|removes the padding from the array.|`array_without_padding = cb.padding.pad_REMOVE(array_with_padding)`|


### **Process:**
consists of general cryptography related math functions.

| function | description | code example |
| :-- | :-- | :-- |
|XOR_array|performs XOR between two arrays of same length.|`XOR_of_arrays = cb.process.XOR_array(array1,array2)`|
|ADD_array|performs ADD between (array1,array2) of same lengh with (mod 64).|`ADD_of_arrays = cb.process.ADD_array(array1,array2)`|
|shift|performs shift operation on array in left or right direction by specified amount.|`shifted_array = cb.process.shift(array1,shiftamount,direction)`|
|s_box|performs substititution on the array with reference from sbox array.|`substituted_array = cb.process.s_box(array1,s_box)`|
|s_box_inverse|performs inverse substititution on the array with reference from sbox array.Used in decryption|`inverse_substituted_array = cb.process.s_box_inverse(array1,s_box)`|
|p_box|performs permutation on the array with reference from pbox array.|`permutated_array = cb.process.p_box(array1,p_box)`|
|p_box_inverse|performs inverse permutation on the array with reference from pbox array.Used in decryption|`inverse_permutated_array = cb.process.p_box_inverse(array1,p_box)`|
|swap_half|swaps the two half in the array (use `shift` if you want to swap at custom position).|`swapped_array = cb.process.swap_half(array1)`|

### **Gnerate:**
consists of tools to generate string,arrays and S&P Box generators with cryptographically secure methods.

| function | description | code example |
| :-- | :-- | :-- |
|box_generate|generates an array of size mentioned with elements from {0,size-1} in random order and also returns its inverse.|`s_box,inv_s_box=cb.generate.box_generate(boxsize)`|
|string_generate|generates a string of mentiond size with random base64 characters|`random_string=cb.generate.string_generate(stringsize)`|
|array_generate|generates a numpy array of lenght (size) with value between {0,63}.|`random_array=cb.generate.array_generate(arraysize)`|