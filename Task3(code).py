file = input("Введите название файла: ")
with open(file, "r") as f:
    text = f.read()
text2 = text
text = text.replace(" ", "")
n = 0
eq = 0
srez = []
srez1 = []
names = []
massive = []
arguments = (text[text.find("(") + 1:text.find(")")].split(","))
for i in range(len(text)):
    if text[i] == "\n":
        n = i
    if text[i] == "=":
        eq = i
        srez.append(n)
        srez.append(eq)
n = 0
eq = 0
for i in range(len(text)):
    if text[i] == "\n":
        n = i
    if text[i] == "[":
        if "=" in text[i - 5:i]:
            eq = i
            srez1.append(n)
            srez1.append(eq)
for i in range(0, len(srez), 2):
    if i + 1 < len(srez):
        if text[srez[i + 1] + 1] != "[":
            names.append(text[srez[i] + 1:srez[i + 1]].replace(" ", ""))
for i in range(0, len(srez1), 2):
    if i + 1 < len(srez1):
        massive.append(text[srez1[i] + 1:srez1[i + 1] - 1].replace(" ", ""))
arguments = list(set(arguments))
massive = list(set(massive))
for i in range(len(arguments)):
    name = "a" + str(i + 1)
    text2 = text2.replace(arguments[i], name)
for i in range(len(arguments), len(arguments) + len(names)):
    name = "a" + str(i + 1)
    for j in range(len(names)):
        text2 = text2.replace(names[j], name)
for i in range(len(massive)):
    name1 = "R" + str(i + 1)
    text2 = text2.replace(massive[i], name1)
print(text2)
