list_nums = []
list_nums_part2 = []


with open("input_day1.txt", "r") as inputfile:
    data = inputfile.readlines()
    string = data[0].strip()
for i in range(0, len(string)):
    if string[i] == string[i-1]:
        list_nums.append(int(string[i]))
    if string[i] == string[i-(len(string)/2)]:
        list_nums_part2.append(int(string[i]))

print(list_nums)
print(sum(list_nums))
print(list_nums_part2)
print(sum(list_nums_part2))
