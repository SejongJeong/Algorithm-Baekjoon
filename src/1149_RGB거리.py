street = []
number_of_house = int(input())
for _ in range(number_of_house):
    street.append(list(map(int, input().split())))
for i in range(1, number_of_house):
    street[i][0] += min(street[i-1][1], street[i-1][2])
    street[i][1] += min(street[i-1][0], street[i-1][2])
    street[i][2] += min(street[i-1][0], street[i-1][1])
print(min(street[number_of_house-1][0],
      street[number_of_house-1][1], street[number_of_house-1][2]))