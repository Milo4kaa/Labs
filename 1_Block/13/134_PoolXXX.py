a = input("Введите длину бассейна: ")
b = input("Введите ширину бассейна: ")
c = input("Введите высоты бассейна: ")
d = input("Введите с какой скоросью наливается вода: ")
S = float(a) * float(b) * float(c)
time = float(S) / float(d)
print(time)