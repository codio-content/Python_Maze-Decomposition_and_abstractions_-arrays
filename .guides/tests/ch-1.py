
try:
  execfile('/home/codio/workspace/public/py/ch-1.py')
  
  if len(numbers) == 5 and numbers[0] == 0 and numbers[1] == 10 and numbers[2] == 20 and numbers[3] == 30 and numbers[4] == 40 :  
    print 'well done'
    exit(0)
  
except (IOError, SyntaxError, ValueError) as e:
  print str(e)
  exit(1)
  
print 'Not quite right, try again!'
exit(1)
