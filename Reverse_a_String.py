#Given String.....
given_str = "This is a Reversed String example"

# first Method....................... 
reversed_str = given_str[::-1]
print(reversed_str)

#Second Method........................
reversed_str = ""
while(len(given_str) > 0):
    last_ind = len(given_str) - 1
    reversed_str += given_str[last_ind]
    given_str = given_str[:last_ind]

print(reversed_str)
