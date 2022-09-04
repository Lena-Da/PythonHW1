#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
#Предикату можно заменить на понятие "бит".
#Должна получиться таблица истинности.

print('x y z')
for x in range(2):
  for y in range(2):
    for z in range(2):
        print(x, y, z, end=" ")
        if (not (x or y or z) == (not x and not y and not z)):
            print ("True")
        else:
            print ("False")