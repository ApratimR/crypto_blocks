import src as sc

# print(temp := sc.convert.string_to_array("🇮🇳asdn98qn-as9dn--a sd9adabf-9sd"))

# print(sc.convert.array_to_string(temp))

# print(sc.convert._char_array)


print(temp := sc.genrate.array_generate(5))
temp2, temp3 = sc.genrate.box_generate(5)
# print(temp2, temp3)
print(temp := sc.process.p_box(temp, temp2))
print(temp := sc.process.p_box(temp, temp3))
