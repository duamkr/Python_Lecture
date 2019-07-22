# 1. 대칭수 구하기(가장 큰 대칭수 구하기)

for i in range(101,1000) :
    for k in range(i, 1000):
        result = i * k
        word = str(result)
            if word == ''.join(reversed(word)):
                maxword = i * k
                aword = i
                bword = k

print(maxword, aword, bword)

word
''.join(reversed((word)))


# 2번문제 시저암호 ( 수정 완료, z 이후의 값 a부터 시작)
a, b = input().split()
b= int(b)

from string import ascii_lowercase
al = list(ascii_lowercase)

pass_word = ""
for i in a:
    key_index = al.index(i) + b
    if key_index < 26 :
        pass_word = pass_word + al[key_index]
    else :
        pass_word = pass_word + al[key_index -26]

print(pass_word)


# 3번 문제 linux명령어 중 grep을 윈도우스에서 만들어보시오.


a, b = input('').split()




# 4.
import os
os.chdir("c:\Temp")
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

#5.
import os
os.chdir("c:\Temp\help")
import random as rd

for i in range(0,100):
    file_num = rd.randint(0,9999)
    file_contents =str(rd.randint(1,3))
    file_name = '%04d.txt' % file_num
    file = open()
