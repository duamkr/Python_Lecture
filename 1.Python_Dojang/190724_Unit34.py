
files = input().split()
print(list(map(lambda x : "{:0>3}.{}".format(x.split('.')[0], x.split('.')[1]),files)))


class Person:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting()


james = Person()

james.hello()

# 특정 클래스의 인스턴트인지 확인 isinstance(인스턴트, 클래스)  Ture / False
isinstance(james, Person)


# isinstance의 활용 예 factorial
def factorial(n) :
    if not isinstance(n, int) or n < 0:   # n의 클래스가 int가 아닐경우를 체크
        return None
    if == 0 :
        return 1
    return n * factorial(n-1)


# 속성사용하기

class Person :
    def __init__(self):
        self.hello = '안녕하세요'

    def greeting(self):
        print(self.hello)

james = Person()
james.greeting()

james.hello = '안녕하세요? 여러분!'     # Person속성값이 Public이기 떄문에 바깥쪽에서 속성값을 변경할 수 있음
james.greeting()


# 인스턴트를 만들 때 값 받기
class Person :
    def __init__(self, name, age, address):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1} 입니다.'.format(self.hello, self.name))


maria = Person('마리아', 20, '서울시 반포동')
maria.greeting()
print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)



# __slots__

# 비공개 속성 self.__속성 = 값

class Person :
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet      # 변수 앞에 __를 붙여서 비공개 속성으로 만듬


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000       # 클래스 바깥쪽에서 비공개 속성에 접근시 에러 발생

class Person :
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet      # 변수 앞에 __를 붙여서 비공개 속성으로 만듬

    def pay(self, amount):
        self.__wallet -= amount    # 비공개 속성은 클래스 안의 매서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)

# 금액이 표시 되지 않도록
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듬

    def pay(self, amount):
        if amount > self.__wallet :
            print('돈이 모자라네..')
            return
        self.__wallet-= amount

maria = Person('마리아', 30, '서울시', 10000)
maria.pay(12000)



# Unit 35클래스 속성과 정적 클래스 메서드 사용하기
class Person:
    bag = []    # bag 은 클래스 속성으로 생성

    def put_bag(self, stuff):
        self.bag.append(stuff)


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)   # james. maria의 풋백에 각각 책과 열쇠를 넣었지만, 두 인스턴트에 책, 열쇠 둘다 들어가 있음


# 정적 메서드 사용하기

class Calc :
    @staticmethod
    def add(a,b):
        print(a+b)

    def mul(a,b):
        print(a*b)


Calc.add(10,20)
Calc.mul(10,20)





# Unit 36 클래스 상속 사용하기

class Person :
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    def stude(self):
        print('공부하기')


james = Student()
james.greeting()     # .greetin은 Person의 메서드, 즉 부모의 메서드 , james는 Student로 자식클래스지만 부모의 메서드를 불러올 수 있음
james.stude()        # .stude는 Student의 메서드, 자식의 메서드


# 메서드 오버라이딩 사용하기

class Person :
    def greeting(self):
        print('안녕하세요')

class Student(Person) :
    def greeting(self):
        print('안녕하세요.저는학생입니다.')


철수 = Student()
철수.greeting()

엄마 = Person()
엄마.greeting()


# 추상 클래스 사용하기

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):


