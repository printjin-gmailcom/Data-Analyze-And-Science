"""
## No.1
### 임의의 숫자를 입력받아,
### 첫 번째 입력한 숫자에서 그 뒤에 입력한 숫자를 전부 빼는 sub 함수를 구현하고자 합니다.
### 아래 코드의 빈 부분을 채워 코드를 완성하세요.
#### 예1)
#### 입력: sub(5, 4, 9)
#### 출력: -8
#### 예2)
#### 입력: sub(5, 4, 3, 2, 1)
#### 출력: -5
"""

def sub(*args):
    result = args[0]
    for i in args[1:]:
        result = result - i
    return result

sub(5,4,3,2,1)

"""## No.2
### 아래 코드의 빈 부분을 채워 직각삼각형의 대각선 길이를 구하는 클래스를 구현하세요.
### a는 직각삼각형의 밑변, b는 높이를 나타냅니다.
#### 예)
#### 입력: diag(3,4)
#### 출력: 5
"""

class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def diag(self):
        print((self.a**2 + self.b**2)**(1/2))

z = Triangle(3,4)
z.diag()

"""## No.3 (2점)
### 어떤 한 게임 캐릭터는, 현재 체력이 100, 최대 체력이 200입니다.
### 여러분은 이제 Character 클래스에서 캐릭터가 공격받을 때 체력이 깎이는 attacked 메서드,
### 포션을 섭취할 때 체력이 회복되는 potion 메서드를 구현하고자 합니다.
####
### attacked 메서드에서는 입력받은 만큼 데미지를 받는 메서드를 구현하되,
### 체력이 0이 되었을 경우 'YOU DIED'를 출력해야하며, 체력을 0으로 초기화해야 합니다.
####
### potion 메서드에서는 입력받은 만큼 체력을 회복하는 메서드를 구현하되,
### 체력이 최대치에 도달했을 경우 최대치까지만 회복하도록 하세요.
####
### 또한, 인스턴스가 메서드를 수행할때마다 현재 남은 체력을 보여주게 하세요.
### 예를 들어, 30의 데미지를 입었을 경우 70, 여기에서 50을 회복하면 120을 출력하게 됩니다.
####
### 아래 코드의 빈 부분을 채워 위에서 설명하는 클래스를 구현하세요.
"""

class Character:
    def __init__(self):
        self.max_life = 200
        self.life = 100
    def attacked(self, damage):
        if damage >= 1:
            self.life -= damage
            if self.life <= 0:
                print('YOU DIED')
            else:
                print(self.life)
    def potion(self, recovery):
        if recovery >= 1:
            self.life += recovery
            if self.life >= 200:
                self.life = 200
                print(self.life)
            else:
                print(self.life)



class Character:
    def __init__(self, max_life, life):
        self.max_life = max_life
        self.life = life
    def attacked(self, damage):
        if damage >= 1:
            self.life -= damage
            if self.life <= 0:
                print('YOU DIED')
            else:
                print(self.life)
    def potion(self, recovery):
        if recovery >= 1:
            self.life += recovery
            if self.life >= 200:
                self.life = 200
                print(self.life)
            else:
                print(self.life)

cha = Character(200, 100)

cha.attacked(20)
cha.attacked(10)
cha.potion(100)
cha.potion(100)
cha.attacked(100)
cha.attacked(120)

"""## No.4
### 어떠한 숫자를 input으로 입력받았을 때,
### 해당 숫자가 0이라면 '0은 안됩니다'라는 에러 메시지를,
### 소수라면 '소수는 안됩니다'라는 에러 메시지를 출력하는 코드를 작성하세요.
### 0일 때는 ZeroDivisionError, 소수일 때는 ValueError를 활용하시면 됩니다.
"""

try:
    x = int(input("숫자를 입력하세요: "))
except ValueError :
    print("소수는 안됩니다")
if x == 0:
    raise ZeroDivisionError

