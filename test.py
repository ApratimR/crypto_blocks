import src as sc

# print(temp := sc.convert.string_to_array("🇮🇳asdn98qn-as9dn--a sd9adabf-9sd"))

# print(sc.convert.array_to_string(temp))

# print(sc.convert._char_array)

temp1 = sc.convert.string_to_array("123")
temp2 = sc.convert.string_to_array("321")

temp3 = sc.process.XOR_arrays(temp1, temp2)
temp3 = sc.padding.padtomultipleof(temp3, 0, 10)
temp3 = sc.process.shift(temp3, 3, "l")
print(temp3)
