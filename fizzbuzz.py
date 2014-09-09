'''
print numbers 1 through 100 (inclusive).
for those numbers that are divisible by 3, print 'Fizz'
for those numbers that are divisible by 5, print 'Buzz'
for those numbers that are divisible by 3 and 5, print 'FizzBuzz'
'''

# create the list
my_list = []
for x in range(101):
  if x == 0:
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