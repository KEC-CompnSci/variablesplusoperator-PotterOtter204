# Create the requested sentence by converting and combining these variables
# You may not add any additional string or numeric literals
# You can only use these variables, type conversion, and string concatenation

num_str_1 = "42"
num_str_2 = "13"
num_str_3 = "7"
word_1 = " robots "
word_2 = "built "
word_3 = "today"
word_4 = "were "

new_num = int(num_str_1) + int(num_str_2)

sentence = str(new_num) + word_1 + word_4 + word_2 + word_3
print(sentence)
