# variable 只能是一个整体，不能是分开的单词；不能以数字开头；不能和常用的python代码函数重合

print(len(input('what is your name?\n')))

user_name = input('what is your name?\n') #把上面分解成三个步骤，能够把复杂的代码分成较小的模块将是救命稻草
length = len(user_name)
print(len(user_name))