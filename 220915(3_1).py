t1 = ()

t1



t2 = (1,)

t2, type(t2)

a1 = (1)

a1, type(a1)



t3 = (1, 2, 3)

t3



t4 = 1, 2, 3

t4



t5 = ('a', 'b', ('ab', 'cd'))

t5



t6 = (1, 2, 'a', 'b')
del t6[0]



t6 = (1, 2, 'a', 'b')
t6[0] = 'c'

t7 = (1, 2, ['a', 'b'])

type(t7)

t7 = (1, 2, ['a', 'b'])

t7[2][0] = 'c'

t7

a2 = [1, 2, ('a', 'b')]

type(a2)

a2 = [1, 2, ('a', 'b')]

a2[2][0] = 'c'

a2



t6 = (1, 2, 'a', 'b')
t6[0]



t6 = (1, 2, 'a', 'b')
t6[1:]



t6 = (1, 2, 'a', 'b')
t8 = (3, 4)

t6 + t8



t8 = (3, 4)
t8 * 3



t6 = (1, 2, 'a', 'b')
len(t6)



t9 = ('a', 'b', 'c', 'd')
t9[3] = 'e'
t9[4] = 'f'

t9

t10 = (1,2,3)
t11 = (0,)

t11 + t10





dic = {'name':'pey', 'cat':'happy', 'phone':'011'}

dic



spider = {1:'맥과이어', 2:'가필드'}

spider, spider[1], type(spider)



spider = {1:'맥과이어', 2:'가필드'}

spider[3] = '홀랜드'

spider

spider = {1:'맥과이어', 2:'가필드', 3: '홀랜드'}

del spider[1]

spider



spider1 = {1:'맥과이어', 1:'가필드', 1: '홀랜드'}

spider1



spider2 = {[1]:'맥과이어'}

spider2



spider3 = {(1,):'맥과이어'}

spider3



burger = {'싸이':4100, '휠렛':3900, '불고기':3300}

burger

burger = {'싸이':4100, '휠렛':3900, '불고기':3300}

burger['갈릭바베큐'] = 5600

burger

burger = {'싸이': 4100, '휠렛': 3900, '불고기': 3300, '갈릭바베큐': 5600}

burger['싸이'] + mom['휠렛']*2

burger = {'싸이': 4100, '휠렛': 3900, '불고기': 3300, '갈릭바베큐': 5600}

del burger['휠렛']

burger



spider = {1:'맥과이어', 2:'가필드'}

spider.keys()
list(spider.keys())



spider = {1:'맥과이어', 2:'가필드'}

spider.values()
list(spider.values())



spider = {1:'맥과이어', 2:'가필드'}

spider.items() #쌍을 튜플형태로 변환
type(spider.items())

spider = {1:'맥과이어', 2:'가필드'}

spider.items() #쌍을 튜플형태로 변환
list(spider.items())



spider = {1:'맥과이어', 2:'가필드'}

spider.clear



spider = {1:'맥과이어', 2:'가필드'}

1 in spider
'홀랜드' in spider



spider = {1:'맥과이어', 2:'가필드'}

spider.get(1)

spider = {1:'맥과이어', 2:'가필드'}

spider.get(3, 'new')



burger = {'싸이': 4100, '휠렛': 3900, '불고기': 3300, '갈릭바베큐': 5600}

list(burger.values())[0]+list(burger.values())[1]+list(burger.values())[2]+list(burger.values())[3]

burger = {'싸이': 4100, '휠렛': 3900, '불고기': 3300, '갈릭바베큐': 5600}

price = list(burger.values())
price[0] + price[1] + price[2] + price[3]

burger = {'싸이': 4100, '휠렛': 3900, '불고기': 3300, '갈릭바베큐': 5600}

sum(list(burger.values()))

