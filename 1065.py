n = input()
num = int(n)

count = 0


for i in range(num+1):

    if (i<100):
        count += 1

    else:
        now = 0
        x = str(i)
        diff = int(x[0]) - int(x[1])
        while(now < len(x)-2):
            now += 1
            tmpdiff = int(x[now]) - int(x[now+1])

            if (diff != tmpdiff):
                break
            count += 1
print(count-1)
