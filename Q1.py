Animal = []
Animal.append("horse")
Animal.append("lion")
Animal.append("rabbit")
Animal.append("mouse")
Animal.append("bird")
Animal.append("deer")
Animal.append("whale")
Animal.append("elephant")
Animal.append("kangaroo")
Animal.append("tiger")

def SortDescending():
    global Animal
    ArrayLength = len(Animal)
    for x in range(0, ArrayLength - 1):
        for y in range(0,ArrayLength - x - 1):
            if Animal[y][0:1] < Animal[y + 1][0:1]:
                temp = Animal[y]
                Animal[y] = Animal[y + 1]
                Animal[y + 1] = temp

SortDescending()
for x in range(len(Animal)):
    print(Animal[x])