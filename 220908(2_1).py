a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b

a = "Life is too short, You need Python"
a[0:4] #0<=a<3



c = 'pithon'
c

c[1] = 'y'

c = 'pithon'
d = c[:1] + 'y' + c[2:]
d



e = '12가 3456'
e[4:]
e[-4:]



'I eat 3 apples.'

"I eat %d apples." % 3

"I eat %s apples." % "five"

number = 3
"I eat %d apples." % number

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)

num =  3
fruit = 'melons'
f = 'I eat %d %s' %(num*2, fruit)
f

num =  3
fruit = 'melons'
f = 'I eat %s %s' %(num*2, fruit)
f

num =  3500
fruit = 'melons'
f = 'I eat %f%% %s' %(num, fruit)
f

# %s	문자열(String)
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수
# %%	Literal % (문자 % 자체)



fruit = 'melons'
a = '%10s' %fruit
a

fruit = 'melons'
a = '%-10s' %fruit
a



"%0.4f" % 3.42134234

"%10.4f" % 3.42134234



name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

age = 30
f'내년에 나는 {age+1}살이 됩니다.'

f'{"hi":<10}'   # 왼쪽 정렬
f'{"hi":>10}'   # 오른쪽 정렬
f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기

y = 3.42134234
f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤



f'{"TUK":~^11}'



a = "hobby"
a.count('b')

a = "hobby"
a.count('bb')

a = "Python is the best choice"
a.find('b')

a = "Python is the best choice"
a.index('t')

a = "Python is the best choice"
a.index('k')



",".join('abcd')

",".join(['a', 'b', 'c', 'd'])



a = "hi"
a.upper()

a = "HI"
a.lower()

a = "   hi    "
a.lstrip()

a = "    hi   "
a.rstrip()

a = "    hi   "
a.strip()

a = "    h            i   "
a.strip()



a = "Life is too short"
a.replace("Life", "Your leg")

a = "Life is too short"
a.replace("o", "e")



a = "Life is too short"
a.split() #공백기준

b = "a:b:c:d"
b.split(':') #:기준



a = '010-1234-5678'

a.replace("-", " ")

a.replace("-", "")

a.split('-')

