def Solve (N):
    divisible_numbers = []
    for number in range(1, N):
        if N%number == 0:
            divisible_numbers.append(number)
    summed_numbers = sum(divisible_numbers)
    if summed_numbers == N:
        return 'YES'
    else:
        return 'NO'

testing = Solve(28)
testing_2 = Solve(6)
testing_3 = Solve(5)
testing_4 = Solve(48)
print(testing) 
print(testing_2) 
print(testing_3) 
print(testing_4) 