# Unit 34. "클래스 사용하기"

## 34.2 속성사용하기
class Person :
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1} 입니다.'.format(self.hello, self.name))     # class안에서 속성값을 불러오려면 "self.속성" 형식으로 접근해야함



james1 = Person('제스본드중독', 30, '대전광역시')
james1.greeting()

print(james1.address)     # class 밖에서 속성값에 접근하려면 "인스턴트.속성"으로 접근해야함 /  해당 문장에선 james1 가 인스턴트 이기 때문에 james1.adress

### 참고 '클래스의 위치 인수, 키워드 인수
#### 위치 인수 (*args)
class Person :
    def __init__(self, *args):
        self.name = args[0]    # *args 의 언패킹을 통해 args[인덱스] 형식으로 속성값 부여 가능
        self.age = args[1]
        self.address = args[2]


maria = Person(*['마리아', 30, '조선인민공화국 평양시'])
print(maria.name)
print(maria.age)
print(maria.address)

#### 키워드 인수 (*kwargs)

class Person :
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']


maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')       # 키워드 인수 지정시 입력 형식1
maria2 = Person(**{'name': '마리아', 'age': 30, 'address' : '함경북도'})    # 키워드 인수 지정시 입력 형식2


### 인스턴트 생성 후 인스턴트의 속성을 추가하는 법
### 속성과 메소드가 없는 클래스 생성
class Person:
    pass

maria = Person()          # maria  인스턴트 생성
maria.name = '김덕자'     # maria 인스턴트에 name = '김덕자' 속성 추가
maria.name

james = Person()
james.name       # 위에서 추가한 .name = '김덕자'의 속성은 maria 인스턴트 해당 속성이므로, 다른 인스턴트에선 속성이 생성되지 않음

### __init__ 메서드가 아닌 타 메서드에서 속성 추가하기
class Person():
    def greeting(self):
        self.hello = '안녕하세요.'

maria = Person()
maria.hello      # 타 메서드에서 속성을 생성할 경우 상위 메서드, 즉 속성을 만든 메서드를 한번 호출 한 후 속성을 불러 올 수 있음
maria.greeting()
maria.hello


### __slot__ = [속성이름1, '속성이름2']
class Person :
    __slots__ =['name', 'age']

maria = Person()
maria.name = '김덕순'
maria.age = 33
maira.address = '강원도 양양'     # address는 __slot__=[]으로 지정되지 않아 속성이 추가되지 않음 에러발생


## 34.3 비공개 속성 사용하기

class Person :
    def __init__(self, name, age, address, wallet):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.naddress = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0} 원 남았네요'.format(self.__wallet))

    def pay1(self, amount):
        if amount > self.__wallet :
            print('돈이 모자란다 아껴써라 !')
            return
        self.__wallet -= amount


maria = Person('마리아', 30, '서울시 반포동', 10000)
maria.name    # name은 호출 됨
maria.wallet  # wallet은 '__' 로 지정해 비공개 속성이 됨으로 class밖에선 호출 되지 않음
maria.pay1(13000)   # 잔액도 보여주기 싫은 경우 if문을 써서 해당 가진 금액보다 큰 경우 조건 성립

#### 연습문제 34.5

class Knight :
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')



x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()


#### 심화문제

class Annie :
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print('티버 : 피해량' , self.ability_power * 0.65 + 400)


health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
