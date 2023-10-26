## 예제 5-1
a = ['one', 2, 3.0]
print(a[0])

## 예제 5-1.2
print(a[1] + a[2])

## 예제 5-1.3
print(a[-1])

## 예제 5-2
a = [1, 2, 3, ['One', 'Two', 'Three']]
print(a[0])

## 예제 5-2.2, 5-2.3, 5-2.4
print(a[-1])

print(a[-1][0])

print(a[-1][-1])

## 예제 5-3
a = [101, 102, ['a', 'b', ['Spring', 'Summer']]]
print(a[2][2][0])

## 예제 5-3.2, 5-3.3
print(a[-1][-1][-1])

print(a[-1][0][0])

# 예제 5-4
a = [101, 102, 103, 104, 105]
print(a[0:3])

# 예제 5-6
a = [101, 102, ['One', 'Two', 'Three'], 103, 104, 105]
print(a[1:4])

# 예제 5-6.2
print(a[2][:2])

# 예제 5-7
a = [101, 102, 103]
b = [201, 202, 203]
print(a + b)

# 예제 5-7.2
c = ['one', 'two']
d = ['Three']
print(c + d)

# 예제 5-8
a = ['one', 'two', 'three']
print(a * 3)

# 예제 5-9.2
a = [11, 12, 13]
print(str(a[2])+ "회")

# 예제 5-10
a = [101, 102, 103]
a[2] = 201
print(a)

# 예제 5-11
a = [201, 202, 203]
a[1:2] = ['one', 'two', 'three']
print(a)

# 예제 5-11.2, 5-11.3
print(a[1])

a[1] = ['하나', '둘', '셋']
print(a)

# 예제 5-12, 5-12.2, 5-12.3
print(a)

print(a[1:3])

a[1:3] = [ ]
print(a)

# 에제 5-13
print(a)

# 예제 5-13.2
del a[1]
print(a)

# 예제 5-14
a = [301, 302, 303]
print(a.index(302))

# 예제 5-14.2
print(a.index(303))

# 예제 5-15
a = [101, 102, 103]
a.extend([201], [202])
print(a)

# 예제 5-15.2
b = [301, 302, 303]
a.extend(b)
print(a)

# 예제 5-16
a = ['one', 'two']
a.append('three')
print(a)

# 예제 5-16.2
a.append([5, 10])
print(a)

# 예제 5-17
a = [101, 102, 103]
a.insert(1, 201)
print(a)

# 예제 5-17.2
a.insert(2, 'three')
print(a)

# 예제 5-17.3
a.insert(3, [301, 302])
print(a)

# 예제 5-18
a = [88, 35, 97, 35, 88]
a.remove(35)
print(a)

# 예제 5-20
a = ['one', 'two', 'three']
print(a.pop( ))

# 예제 5-20.2
print(a)



