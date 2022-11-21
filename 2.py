count = 0

my_string = "going to go to goa"
my_char = "go"

for i in my_string:
    if i == my_char[-1]:
        count += 1

print(count)
