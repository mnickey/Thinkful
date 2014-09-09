'''
Using functions to refactor fizzbuzz.py
Get the upper bounds, first divisor & second divisor
Then use that information to check if one or both are divisable
If neither are divisable, print the divisor instead of the divisor
If only one is divisable, print fizz or buzz instead of the divisor
If both are divisable, print fizzbuzz instead of the divisor
'''
import sys
def first_check(x, first_num):
  if x % int(first_num) == 0:
    return True
  else: return False

def second_check(x, second_num):
  if x % int(second_num) == 0:
    return True
  else: return False

if len(sys.argv) == 1 or len(sys.argv) != 4:
  upper_limit = raw_input("Enter the maximum value to fizz through: ")
  first_num = raw_input("Enter the first divisor: ")
  second_num = raw_input("Enter the second divisor: ")
else:
  upper_limit = sys.argv[1]
  first_num = sys.argv[2]
  second_num = sys.argv[3]

# Populate the list using the upper bound entered through the sys argv or prompt
def populate_list(upper_limit):
  for x in range(int(upper_limit)+1):
    if x == 0: # Skipping 0
      continue
    else:
      my_list.append(x)
  print "Fizz buzz counting up to %s" % len(my_list)

def fizzbuzz_list(my_list):
  for _ in my_list:
    if first_check(_, first_num) == True and second_check(_, second_num) == True:
      print "FizzBuzz",
    elif first_check(_, first_num) == True and second_check(_, second_num) == False:
      print "Fizz",
    elif first_check(_, first_num) == False and second_check(_, second_num) == True:
      print "Buzz",
    else: print _,

if __name__ == '__main__':
  my_list = [] #declare an empty list
  populate_list(upper_limit) # populate my_list
  fizzbuzz_list(my_list)
