# 출력값 
1. 소수점 자리
    ```python
    a = int(input())
    b = a * 2.2046

    print(f"{a:0.2f} kg =>  {b:0.2f} lb")
    ```
    f-string 변환 할 때 {} 안에 변수:0.xf 를 넣어주면 소수점 x자리 까지 나타낼 수 있다


2. 포맷팅
    ```python
    a = int(input())

    for x in range(1, a+1):
        if a % x == 0:
            print("%d(은)는 %d의 약수입니다." % (x, a))
    ```
    %d 는 숫자를 받을 때 사용


3. input 여러개 받기
    ```python
    dic = {1:"가위", 2:"바위", 3:"보"}

    a, b = map(int, input().split())

    A = dic[a]
    B = dic[b]
    ```
    split은 공백을 기준으로 input을 나눠준다  
    map을 통해 각각의 항목에 함수 적용


4. 대소문자로 바꿔주기
    ```python
    al = input()

    big = al.upper()
    small = al.lower()
    ```


5. 아스키코드로 변환
    ```python
    al = input()
    num = int(input())

    al1 = ord(al)       # 문자 > 숫자
    num1 = chr(num)     # 숫자 > 문자
    ```


6. 언패킹
    ```python
    num = []

    for i in range(1, 201):
        if i % 7 == 0 and i % 5 != 0:
            num.append(i)

    print(*num)         # list를 벗겨준다
    # 출력값 7 14 21 28 42 49 56 63 77 84 91 98 112 119 126 133 147 154 161 168 182 189 196
    ```


7. 구분자
    ```python
    num = []

    for i in range(1, 201):
        if i % 7 == 0 and i % 5 != 0:
          num.append(i)

    print(*num, sep=',')        # sep 를 이용해서 사이에 구분자를 넣어 줄 수 있다
    # 출력값 7,14,21,28,42,49,56,63,77,84,91,98,112,119,126,133,147,154,161,168,182,189,196
    ```


8. 백의 자리, 십의 자리, 일의 자리
    ```python
    i = "3자리 정수"
    a = i % 10                # 일의 자리
    b = i % 100 // 10         # 십의 자리
    c = i // 100              # 백의 자리
    ```


9. dictinary
    ```python
    scores = {1: 88, 2:30, 3:61, 4:55, 5:95}
    for stu in scores.keys():
         # print(stu) = 1 2 3 4 5
        if scores[stu] >= 60:
         # print(socres[stu]) = 88 30 61 55 95
    ```
    dic.keys() > key 값만 list로 불러오기  
    dic[key] > key 값에 해당하는 value 값 불러오기


10. list  
    list.pop(index) : index에 해댕하는 항목을 꺼내 출력해주고 list 안에서 지워준다  
    list.sort() : list 내의 항목들을 오름차순으로 정렬  
    list.sort(reverse=True) : list 내의 항목들을 내림차순으로 정렬  
    반환받고 싶을 때는 change = sorted(list) 로 두면 된다  
    list 내의 문자들을 하나의 문자열로 합치고 싶을 때는 join을 사용한다
    ```python
    lst = ['f', 'u', 'u', 'q', 'j']
    ''.join(lst)
    >> fuuqj
    ','.join(lst)
    >> f,u,u,q,j
    ```

11. 별찍기  
    while 역삼각형
    ```python
    i = 5

    while i > 0:
        print("*" * i)
        i = i - 1
    ```
    while 트리형
    ```python
    i = 7

    while i > 0:
        print("{0:^7}".format("*" * i))
        i = i - 2
    ```
    for 우측정렬 삼각형
    ```python
    for i in range(1, 6):
        print("{0:>5}".format("*" * i))
    ```


12. 다른 진수로 변환
```python
s = "2진수: {0:b}, 8진수: {0:o}, 10진수: {0:d}, 16진수: {0:x}".format(60)

print(s)
```
2진수 : 0b  
8진수 : 0o  
10진수 : 0d  
16진수 : 0x  


13. 문자 거꾸로 출력
```python
sen = input()

def reverse(a):
    a = sen[::-1]
    return a
    
print(reverse(sen))
if reverse(sen) == sen:
    print("입력하신 단어는 회문(Palindrome)입니다.")
```
list나 문자 뒤에 [::-1]를 붙여주면 거꾸로 출력가능  

# 입력값
1. for i in ()  
() 부분에 문자 자체가 들어갈 수 있다  
```python
a = 'happy'
for chars in a:
    print(chars, end=' ')
>> h a p p y
```

# if 문
1. 조건을 충족하면 list에 추가하기
```python
a = int(input())
b = []

for x in range(1, a+1):
    if a % x == 0:
        print("%d(은)는 %d의 약수입니다." % (x, a))
        b.append(x)
    if len(b) == 2:
        print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." % (a, b[0], b[1]))
```

2. 대소문자 판별
```python
a = input()

if a.isupper():
    print("%s 는 대문자 입니다." % (a))
elif a.islower():
    print("%s 는 소문자 입니다." % (a))
```

3. 가위바위보
```python
what1 = input()
what2 = input()

if what1 == '가위' and what2 == '보':
    print(f"{what1}가 이겼습니다!")
elif what1 == '바위' and what2 == '가위':
    print(f"{what1}가 이겼습니다!")
elif what1 == '보' and what2 == '바위':
    print(f"{what1}가 이겼습니다!")
elif what1 == '가위' and what2 == '바위':
    print(f"{what2}가 이겼습니다!")
elif what1 == '바위' and what2 == '보':
    print(f"{what2}가 이겼습니다!")
elif what1 == '보' and what2 == '가위':
    print(f"{what2}가 이겼습니다!")
```

4. 피보나치
```python
num = int(input())

# print(lst)

def fibo(n):
    a = b = 1
    if n == 1 or n == 2:
        return 1
    for i in range(1, n):
        a, b = b, a + b
    return a

```

5. in, not in
```python
lst = [1, 2, 3, 4, 3, 2, 1]
l_set = []

def rem(n):
    for i in range(len(lst)):
        if lst[i] not in l_set:
            l_set.append(lst[i])
        else:
            pass
    return l_set
```
포함되어 있는지 확인하려면 in, 아니면 not in 을 사용해 확인한다

6. 재귀함수
```python
n = int(input())

def fac(x):
    if x == 0:
        return 1
    return x * fac(x-1)
    

print(fac(n))
```
factorial