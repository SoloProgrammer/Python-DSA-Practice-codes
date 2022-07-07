
Given_list = [1,2,3,4]

print(list(reversed(Given_list))) ## First method ...................

print(sorted(Given_list,reverse = True)) ## Second method ....................

print(Given_list[::-1]) ## Third method ...............................................

## fourth method using loop................................................................................

reversed_list = []

for i in range(len(Given_list) - 1, -1, -1):
    reversed_list.append(Given_list[i])

print(reversed_list)