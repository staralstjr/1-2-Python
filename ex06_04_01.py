## 본인의 체질량지수(BMI)를 산출하는 프로그램 ##
# --------------------------------------
# ex06_04_01.py
# IT 융합자율학부 202114046 1학년 권민석
# 키를 입력할때에는 x.xx로 사이에 .을 입력해주십시오
# --------------------------------------
print("=" * 36)
print("◼︎ IT융합자율학부 1학년 권민석 6장 파이선 실습1")
print("◼︎ 본인의  체질량지수(BMI)를  산출하는 프로그램  ")
print("-" * 36)
height = eval(input(">키를 입력(m)  : "))
weight = eval(input(">체중 입력(kg) : "))
result = weight / (height * height)
print("-" * 36)
print(">>본인의 BMI는 : ", end='')
print(format(result, ".2f"))
print("=" * 36)
