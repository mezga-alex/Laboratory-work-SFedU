def fizzbuzz(upper_limit):
    for num in xrange(1, upper_limit+1):
        if num % 15 == 0:
            print "FizzBuzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        else:
            print num

if __name__ == '__main__':
    fizzbuzz(1)


"""
- Does the main routine make sense?

  If not, please read this:
  https://github.com/mjhea0/thinkful-mentor/tree/master/python/main_routine

- Why did I add one to the upper_limit?
"""
