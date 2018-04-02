import re

# find digit

a = "a1b2c3dd44"

l = re.findall("\d+", a)

print(l)

m = filter(str.isdigit, a)
mm = list(m)
print(mm)
for i in m:
    print(i)