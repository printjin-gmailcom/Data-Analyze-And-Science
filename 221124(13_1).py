import numpy as np

a = np.array([[4,  3,  5,  7],
              [1, 12, 11,  9],
              [2, 15,  1, 14]])

print(np.sort(a))
print(np.sort(a, axis=0))

a = np.array([[4,  3,  5,  7],
              [1, 12, 11,  9],
              [2, 15,  1, 14]])

print(np.sort(a))
print(a)
print(a.sort())
print(a)

a = np.array([[4,  3,  5,  7],
              [1, 12, 11,  9],
              [2, 15,  1, 14]])
print(a)
print(np.argsort(a))  #-방향으로 줄세우기 3,4,5,7 을 1번째 0번째 2번째 3번째

a = np.array([[  1,    2,    3,    4],
              [ 46,   99,  100,   71],
              [ 81,   59,   90,  100]])

print(np.argsort(a[1]))
print(a[:])
print(a[:, np.argsort(a[1])])



x = np.array([18,   5,  10,  23,  19,  -8,  10,   0,   0,   5,   2,  15,   8,
              2,   5,   4,  15,  -1,   4,  -7, -24,   7,   9,  -6,  23, -13])

print(len(x))
print(np.mean(x))
print(np.var(x))
print(np.std(x))
print(np.max(x))
print(np.min(x))
print(np.median(x))
print(np.percentile(x,10))
print(np.percentile(x,25))
print(np.percentile(x,50))
print(np.percentile(x,99))



print(np.random.rand())
print(np.random.rand(5))
print(np.random.rand(10))
print(np.random.rand(2,3))

print(np.random.seed(0))
print(np.random.rand(5))
print(np.random.rand(5))
print(np.random.rand(10))
print(np.random.rand(10))



print(np.random.rand(10)) # 0부터 1사이에서 균일한 확률 분포로 실수 난수를 생성
print(np.random.randn(10)) # 기댓값이 0이고 표준편차가 1인 표준 정규 분포
print(np.random.randint(10, size=10))
#numpy.random.randint(low, high, size), high를 입력하지 않으면 0과 low사이의 숫자를, high를 입력하면 low와 high는 사이의 숫자를 출력. size는 난수의 숫자

np.random.seed(0)
print(np.random.randn(10))

print(np.random.randint(10, 20, size=10))
print(np.random.randint(10, 20, size=(3, 5)))



x = np.arange(10)
print(x)

np.random.shuffle(x)
print(x)



