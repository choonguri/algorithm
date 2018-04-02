f = 'Fizz'
b = 'Buzz'
for i in range(1,101):
    r = []

    if i%3==0:
        r.append(f)

    if i%5==0:
        r.append(b)

    if len(r) == 0:
        print(i)
    else:
        print(''.join(r))



c = [-1,2,3]

print([ abs(x) for x in c])