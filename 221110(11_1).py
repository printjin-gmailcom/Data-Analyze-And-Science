# try, except만 쓰는 방법
try:
    4/0
except:
    print('zero division')

#2. 발생 오류만 포함한 except문
try:
    4/0
except ZeroDivisionError:
    print('zero division')

#3. 발생 오류와 오류 메시지 변수까지 포함한 except문
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

#try .. finally
try:
    4/0
except IndexError:
    print("IndexError")
finally:
    print('2')

# 여러개의 오류처리하기
try:
    a = [1,2]
    print(a[3]) #인덱스에러발셍->여기서끗
    4/0 #여기까지 안내려감
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)



try:
    a = [1,2]
    print(a[3]) #인덱스에러발셍->여기서끗
    4/0 #여기까지 안내려감
except:
    pass

a=1
if a ==1:
    raise NotImplemetedError

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

class Eagle(Bird):
    def fly(self):
        print("ggiruk")

eagle = Eagle()
eagle.fly()



class MyError(Exception):
    pass

def eagle(baldEagle):
    if baldEagle == 'nohair':
        raise MyError()
    print(baldEagle)

eagle('hair')
eagle('nohair')

class MyError(Exception):
    pass

def eagle(baldEagle):
    if baldEagle == 'nohair':
        raise MyError()
    print(baldEagle)

try:
    eagle('hair')
    eagle('nohair')

except MyError:
    print('사용할 수 없습니다.')

class MyError(Exception):
    pass

def eagle(baldEagle):
    if baldEagle == 'nohair':
        raise MyError()
    print(baldEagle)

try:
    eagle('hair')
    eagle('nohair')

except MyError as e:
    print(e)

class MyError(Exception):
    def __str__(self):
        return "사용할 수 없습니다."

def eagle(baldEagle):
    if baldEagle == 'nohair':
        raise MyError()
    print(baldEagle)

try:
    eagle('hair')
    eagle('nohair')

except MyError as e:
    print(e)



x=['10.32','','8.54','삼쩜오']
new_x = [ ]

for i in x:
    try:
        j=float(i)
    except:
        j=0
    new_x.append(j)

print(new_x)



