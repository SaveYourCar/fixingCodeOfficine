def sum_even_numbers(list_lenght, numbers):
    sum=0
    for i in numbers:
        if (i%2)==0:
            sum+=i
    return sum

list_lenght=int(input())
numbers=[]
for i in range(list_lenght):
    numbers.append(int(input()))

print(sum_even_numbers(list_lenght,numbers))
