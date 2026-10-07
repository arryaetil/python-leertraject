fruits = ["banana", "orange", "mango", "lemon", "lime"]
first,second, *rest = fruits
print(first)
print(second)
print(rest)

# --- slicing ---
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits[0:2])
print(fruits[1:])
print(fruits[-3:-1])

# --- Modifying ---
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "advocado"
print(fruits)
fruits[-1] = "lime"
print(fruits)

# --- in / toevoegen / verwijderen ---
fruits = ["banana", "orange", "mango"]
print("mango" in fruits)
print("apple" in fruits)
fruits.append("lemon")
fruits.insert(1, "kiwi")
print(fruits)
fruits.remove("banana")
fruits.pop()
print(fruits)

# --- copy / join / count / index / reverse / sort ---
a = ["kiwi", "apple", "kiwi"]
b = ["mango"]
c = a + b
print(c)
print(c.count("kiwi"))
print(c.index("apple"))
c.sort()
print(c)
c.reverse()
print(c)