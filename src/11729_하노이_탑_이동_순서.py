def hanoi(N, departure, arrival, layover):
    if N == 1:
        print(departure, arrival)
    else:
        hanoi(N-1, departure, layover, arrival)
        print(departure, arrival)
        hanoi(N-1, layover, arrival, departure)

number = int(input())
print(2**number -1)
hanoi(number, 1, 3, 2)