file = "export_24-04-2022-14_52.txt"

with open (file, "a+") as f:
  f.write("Hello")

with open (file, "r") as f:
  for line in f.readlines():
    print(line)
