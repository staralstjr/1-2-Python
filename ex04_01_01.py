## --------------------- ##
## 기본형 데이터 타입 예제 소스 ##
## --------------------- ##
## IT융합자율학부 1학년 권민석입니다. ##
## email : staralstjr@naver.com ##

print("---------------------")
print("기본형 데이터 타입 예제 소스")
print("---------------------")

## 예제 4-12 ~ 4-27 ##

# 4-12.2 
print('I "Love" Python')

# 4-13
a = "Good "
b = "Programming"
print(a + b)

# 4-14
a = "Good "
b = "Programming"
print(a * 3)

# 4-14.2
print("=" * 50)

# 4-15
a = "Spacezone"
print(a[3])

# 4-15.2
print(a[-2])

# 4-16
a = "Python Programming"
print(a[:2])

# 4-16.2
print(a[3:])

# 4-16.3
print(a[:5])

# 4-16.4
print(a[:])

# 4-17
a = "20330815Monday"
year = a[:4]
print(year)

# 4-17.2
month = a[4:6]
print(month)

# 4-17.3
day = a[6:8]
print(day)

# 4-17.4
week = a[8:]
print(week)

# 4-17.5
print(year + '년 ' + month + '월 ' + day + '일 ' + week)

# 4-18
a = "sprce"
print(a[:2])

# 4-18.2
print(a[3:])

# 4-18.3
print(a[:2] + 'a' + a[3:])

# 4-19
a = "Spacezone"
print(a.count('e'))

# 4-20
a = "I can do it"
print(a.find('a'))

# 4-20.2
print(a.find('do'))

# 4-20.3
print(a.find('s'))

# 4-21
a = "Have a good time"
print(a.index('a'))

# 4-21.2
print(a.index('me'))

# 4-22
a = " power"
print(a.strip( ))

# 4-22.2
print(a.lstrip( ))

# 4-22.3
print(a.rstrip( ))

# 4-23
a = "Speed Zone"
print(a.upper( ))

# 4-23.2
print(a.lower( ))

# 4-24
a = " / "
print(a.join('asdf'))

# 4-24.2
a = " or "
print(a.join('asdf'))

# 4-25
a = "speed zone"
print(a.replace("speed", "power"))

# 4-26
a = "One Two Three"
print(a.split( ))

# 4-26.2
a = "spring:summer:fall:winter"
print(a.split(':'))

# 4-27
a = (100 < 100)
print(a)

# 4-27.2
b = (300 == 300)
print(b)

# 4-27.3
c = True
print(type(c))
