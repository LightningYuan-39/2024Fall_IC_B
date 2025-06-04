import re
email_pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}$"
print(bool(re.match(email_pattern,"2400017837@stu.pku.edu.cn")))

strings0 = ['ac', 'abc', 'abbc', 'abbbbbbc', 'addc']
#1：? 表示前面的字符串需要出现0-1次
for i in strings0:
    print(bool(re.match(r'ab?c', i)), end=' ')
#True True False False False
print()
#2. * 表示前面的字符串需要出现0-多次
for i in strings0:
    print(bool(re.match(r'ab*c', i)), end=' ')
#True True True True False
print()
#3. + 表示前面的字符串需要出现1-多次
for i in strings0:
    print(bool(re.match(r'ab+c', i)), end=' ')
#False True True True False
print()
#4.{x, y}表示前面的字符串需要出现x - y 次(含两边)
#{x}表示出现x次，{x,}表示出现≥x次，{,x}表示出现0-x次
for i in strings0:
    print(bool(re.match(r'ab{2,6}c', i)), end=' ')
#False False True True False
print()
#5.匹配多个字符使用多个括号
strings1 = ['time limit exceeded', 'Compile error', 'accepted']

for i in strings1:
    print(bool(re.match(r'.*(ed){2}.*', i)), end=' ')
#True False False
print()
#6.匹配正则表达式的或运算符
for i in strings1:
    print(bool(re.match(r'.*(exceeded|error).*', i)), end=' ')
#True True False
print()
#7.字符类型
for i in strings1:
    print(bool(re.match(r'[d-tA-C]', i)), end=' ')
#True True False
print()
#8.非运算符^
for i in strings1:
    print(bool(re.fullmatch(r'[^amd]', i)), end=' ')
#True True False
print()
