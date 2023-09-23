n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
    set1.add(int(input()))

print("Введите элементы второго множества:")
for i in range(m):
    set2.add(int(input()))

common_elements = sorted(list(set1 & set2))

print("Общие элементы множеств:", end=" ")
for element in common_elements:
    print(element, end=" ")
