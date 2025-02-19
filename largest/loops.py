num=1

while num<=10:
    print(num)
    num=num+1

#for loop
    for num2 in range(1,11):
        print(num2)

fruits=["banana","mangoes","apples","oranges","avocados"]
for i in fruits:
    print(i)
jina="eMobilis"
for n in jina:
    print(n)
numbers=[4,-7,-4,9,2,1,6,2,4,7,6,2,4,7,6,5,8,10,12]
sum_even=0

for n in numbers:
    if n % 2 == 0:
        sum_even+=n

print(f"The sum of even is {sum_even}")




