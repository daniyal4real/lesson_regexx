import re

# s = 'AC/DCAC/DCAC/DCAC/DCAC/DC'
# result = re.fullmatch("A", s)
#
#
#
# # result = re.split("/", s, maxsplit=3)
# # result = re.sub("A", "D", s)
# print(result)



# line1 = "87+7832645  ----jknwelafkjwhebfwehfbvwef HFGDTFVFGhjgdhjff"

# result = re.search(r"j.n", line1)

# digit
# result = re.search(r"\d\d\d", line1)
# everything except digits
# result = re.search(r"\D", line1)
# find space
# result = re.search(r"\s", line1)
# everything except space
# result = re.search(r"\S", line1)
# letter, number, or underline
# result = re.search(r"\w", line1)

# capital letters
# result = re.search(r"\bHFG", line1)

# result = re.search(r"[jkn]", line1)

# result = re.search(r"[4-8]", line1)
# result = re.search(r"[^4-8]", line1)
# result = re.search(r"H|f", line1)
# result = re.search(r"\d{3}", line1)
# print(result)

# line1 = "Привет, здесь есть какой-то текст, проверю А"
# result = re.findall(r'[бвгджзклмнрстпфхчшщБВГДЖЗКЛМНПРСТФХЧШЩ]\w+', line1)
# print(result)

# pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
# print("Введите почту: ")
# user_input = input()
# if(re.search(pattern, user_input)):
#     print("Все хорошо")
# else:
#     print("Не правильная почта")


pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d)"
new_pattern = r"\1\2\3"
print("Введите: ")
user_input = input()
new_user_input = re.sub(pattern, new_pattern, user_input)
print(new_user_input)