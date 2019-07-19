# 1. 대칭수 구하기
a, b = map(int, input().split())

if a <= 999 and b <= 999 :
    result = a * b
    word = str(result)
    print(word)

print(word == ''.join(reversed(word)))


# 2번문제 시저암호
a, b = input().split()
b= int(b)

from string import ascii_lowercase
al = list(ascii_lowercase)

pass_word = ""
for i in a:
    key_index = al.index(i) + b
    pass_word = pass_word + al[key_index]

print(pass_word)


# 4.
with open('hello.txt', 'r') as file:
    text = file.read()

word_lst = []
for word in text.split():
    word_lst.append(word.strip('.,'))

word_cnt = []
for word in set(word_lst):
    cnt = word_lst.count(word)
    word_cnt.append((cnt, word))

word_cnt.sort(reverse=True)

for cnt, word in word_cnt[:10]:
    print(word, cnt)

