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


a, b = input('문자열과 파일이름 입력').split()

line_no = 1
with open(b, 'r', encoding = 'UTF-8') as file :
    for line in file :
        if line.find(a) >= 0:
            print('%3d:' % line_no, line, end='')
            line_no += 1



# 4. 파일 생성 후 이동
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
import shutil


# 폴더 생성
PATH = 'c:/Temp/help'
os.mkdir(PATH)
os.chdir(PATH)
for dirname in ('low', 'mid', 'high') :
    os.mkdir(PATH + '/' + dirname)
    for num in ('1','2','3'):
        os.mkdir(PATH + '/' + dirname + '/'+ num)

# 파일 생성
for i in range(0,100):
    file_num = rd.randint(0,9999)
    file_contents =str(rd.randint(1,3))
    file_name = '%04d.txt' % file_num
    file = open(file_name,'w')
    file.write(file_contents)
    file.close()

# fileList 에 os.listdir 로 PATH안의 모든 파일 정보를 담는다
fileList = os.listdir(PATH)
for filename in fileList:
    filename2 = int(filename[0:4])
    file = open(filename, 'r')
    content = file.read(1)
    file.close()
# 파일 이동을 위한 이름 분류 작업
    if filename2 <= 3333:
        dirname = 'low'
    elif filename2 <= 6666:
        dirname = 'mid'
    else:
        dirname = 'high'
    dst = dirname + '/' + content + '/' + filename
    shutil.move(filename, dst)


#6. 16진수

import binascii as ba
import os

def showHexa(addr, buf, size):
    if addr % 1024 == 0 and addr != 0:
        print()
    print('%08X: ' % addr, end = ' ')
    if size != 16:
        for i in range(size):
            if i == 8:
                print(end=' ')
            print('%02X' % buf[i], end=' ')
        for i in range(size, 16):
            if i == 8:
                print(end=' ')
            print('  ', end=' ')
    else:
        for i in range(size):
            if i == 8:
                print(end=' ')
            print('%02X' % buf[i], end=' ')
    print('  ', end='')
    for i in range(size):
        if i == 8:
            print(end=' ')
        if buf[i] < 0x20 or buf[i] > 0x7e:
            print('.', end='')
        else:
            print(chr(buf[i]), end='')
    print()

filename = input('읽을 파일> ')
fileLength = os.path.getsize(filename)
with open(filename, 'rb') as file:
    count = 0
    for i in range(0, fileLength, 16):
        buf = file.read(16)
        if fileLength - i < 16:
            size = fileLength - i
        else:
            size = 16
        showHexa(i, buf, size)