## ex_05_01_01 예제 5-28 ~ 5-38 ##
## --------------------- ##
## 집합형 데이터 타입 예제 소스 ##
## --------------------- ##

## 예제 5-28
a = {101:'smart'}
a[201] = 'graphic'
print(a)
## 예제 5-28.2
a['id'] = 'cskisa'
print(a)
## 예제 5-28.3
a['one'] = [101, 102, 103]
print(a)


## 예제 5-29
print(a)
## 예제 5-29.2
del a['one']
print(a)
## 예제 5-29.3
del a[201]
print(a)


## 예제 5-30
print(a)
## 예제 5-30.2
print(a['id'])
## 예제 5-30.3
print(a[101])


## 예제 5-31
a = {101:'space', 101:'zone'}
print(a[101])
## 예제 5-31.2
print(a)


## 예제 5-32.2
a = {(1,2) : 'speed'}
print(a[(1,2)])


## 예제 5-33
a = {'id' : 'mskwon', 'pw' : 114046, 'email' : 'staralstjr@naver.com'}
print(a.keys( ))
## 예제 5-33.2
print(list(a.keys( )))


## 예제 5-34
a = {'id' : 'mskwon', 'pw' : 114046, 'email' : 'staralstjr@naver.com'}
print(a.values( ))
## 예제 5-34.2
print(list(a.values( )))


## 예제 5-35
a = {'id' : 'mskwon', 'pw' : 114046, 'email' : 'staralstjr@naver.com'}
print(a.items( ))
## 예제 5-35.2
print(list(a.items( )))


## 예제 5-36
a = {'id' : 'mskwon', 'pw' : 114046, 'email' : 'staralstjr@naver.com'}
print(a.get('id'))
## 예제 5-36.2
print(a.get('pw'))
## 예제 5-36.3
a = {'id' : 'mskwon', 'pw' : 114046, 'email' : 'staralstjr@naver.com'}
print(a.get('name', 'no key'))
## 예제 5-36.4
a = {'id' : 'mskwon', 'pw' : 114046, 'email' : 'staralstjr@naver.com'}
print(a.get('name', 'non-name'))


## 예제 5-37
a = {'id' : 'mskwon', 'pw' : 114046, 'email' : 'staralstjr@naver.com'}
print('name' in a)
## 예제 5-37.2
print('pw' in a)

## 예제 5-38
a = {'id' : 'mskwon', 'pw' : 114046, 'email' : 'staralstjr@naver.com'}
a.clear( )
print(a)
