x = int(input("Give me number:"))

if x % 2 == 0:
    print("")
    print("even")
else:
    print("odd")
print("end of the program")

a = len("happy")
if a > 2:
    print('hello world')

# Exercise While:
for i in range(2,12,2):
    print(i)
print("Goodbye!")

num = 0
while num < 10:
    num += 2
    print(num)
print("Goodbye!")

print('Hello!')
num = 10
while num <= 10:
    print(num)
    num -= 2
    if num == 0:
        break

summary = 0
end = 5
current = 1

while current <= end:
    summary += current
    current += 1
print(summary)

# Exercise: for
for i in range(2,11,2):
    print(i)
print("Goodbye!")

print("Hello!")
for i in range(10,1,-2):
    print(i)

end = 6
total = 0
for i in range(0, end+1):
    total += i
print(total)

phrase = "Hello world!"
print(len(phrase))


