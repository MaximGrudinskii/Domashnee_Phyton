# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# # Пример:
# 4 4 -> 2 2
# 5 6 -> 2

s = int(input("Сумма чисел равна: "))
p = int(input("Произведение чисел равно: "))

















# s, p = map(int, input().split())
# x = (s-int((s**2-4*p)**0.5))//2
# y = (s+int((s**2-4*p)**0.5))//2
# print(x, y)

# a, b = map(int, input().split())
# c = 0
# for i in range(a + b):
#     if c:
#         break
#     for j in range(a + b):
#         if i + j == a and i * j == b:
#             c = 1
#             print(*sorted([i, j]))
#             break

# a, b = map(int, input().split())
# res = []
# for i in range(a + b):
#     if i == (a * i - b)**0.5:
#         res.append(i)
# print(*res if len(res) == 2 else res + res)