print('Enter a Whole Number:')
number = int(input())

if ((number % 2 == 0)):
  print('The number', number,'is a multiple of 2')
else:
   print('The number', number,'is not multiple of 2')

if ((100 % number == 0)):
  print('The number', number,'is a factor of 100')
else:
   print('The number', number,'is not a factor of 100')

