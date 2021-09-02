import src as sc

# print(temp := sc.convert.string_to_array("🇮🇳asdn98qn-as9dn--a sd9adabf-9sd"))

# print(sc.convert.array_to_string(temp))

# print(sc.convert._char_array)


print(temp := sc.genrate.array_generate(15))
print(temp := sc.padding.pad_to_blocksize_PKCS(temp, 16))
