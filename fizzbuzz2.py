'''
Use sys argvs to determine the upper limit. 
If there is no upper limit, prompt the user to enter one and use that as the upper bound.
for those numbers that are divisible by 3, print 'Fizz'
for those numbers that are divisible by 5, print 'Buzz'
for those numbers that are divisible by 3 and 5, print 'FizzBuzz'
'''
import sys
my_list = [] #declare an empty list

# Check to see if there is an argument passed during runtime.
# If there is an argument the length will be greater than 1
if len(sys.argv) == 1:
  upper_limit = raw_input("Enter the maximum value to fizz through: ")
else:
  upper_limit = sys.argv[1]

# Populate the list using the upper bound entered through the sys argv or prompt
for x in range(int(upper_limit)):
  if x == 0: # Skipping 0
    continue
  else:
    my_list.append(x)
print "Fizz buzz counting up to %s" % len(my_list)

# Run through the list to find 'fizz', 'buzz' & 'fizzbuzz' items
for _ in my_list:
  if _%3 == 0 and _%5 == 0:
    print "FizzBuzz",
  elif _%3 == 0 and _%5 != 0:
      print "Fizz",
  elif _%3 != 0 and _%5 == 0:
    print "Buzz",
  else:
    print _,
