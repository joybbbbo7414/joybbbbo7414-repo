print= "fdgfd"
with open (file, "a+") as f:
  f.write("Hello")

with open (file, "r") as f:
  for line in f.readlines():
    print(line)
