fb_list = []
for x in range(1,101):
    if x %3 == 0 and x %5 == 0:
        fb_list.append("FizzBuzz")
    elif x %3 == 0:
        fb_list.append("Fizz")
    elif x %5 == 0:
        fb_list.append("Buzz")
    else:
        fb_list.append(int(x))
print(fb_list)

