# len(12345)

print(type("Hello"))
print(type(123456))
print(type(123.0))
print(type(True))

# 数据类型转换
print("123" + "456")
print(int("123") + int("456"))

int()
float()
str()
bool()


# print("Number of letters in your name: " + len(int(input("Enter your name\n"))))

name_of_the_user = input("Enter your name: \n")
length_of_the_name = len(name_of_the_user)
print(type(name_of_the_user))
print(type(length_of_the_name))
print("Number of letters in your name: " + str(length_of_the_name))