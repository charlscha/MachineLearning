hello python world

str = hello python world
>>> str[0:5]
'hello'
>>> str[-18:-13]
'hello'


배열 슬라이싱
배열 객체로 구현한 다차원 배열의 원소 중 복수 개를 접근하려면 일반적인 파이썬 슬라이싱(slicing)과 comma(,)를 함께 사용하면 된다.


a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
a
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])

a[0, :]  # 첫번째 행 전체
array([0, 1, 2, 3])

a[:, 1]  # 두번째 열 전체
array([1, 5])

a[1, 1:]  # 두번째 행의 두번째 열부터 끝열까지
array([5, 6, 7])

a[:2, :2]
array([[0, 1],
       [4, 5]])
       
       
       
