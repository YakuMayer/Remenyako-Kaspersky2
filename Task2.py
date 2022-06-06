file = input("Введите имя файла:")
text = ""
with open(file, "rb") as f:
  text = f.read(2).decode("utf-8")
if text == "MZ":
  print("executable, OS Windows")
else:
  print("non-executable")
