
try:
  execfile('/home/codio/workspace/public/py/ch-2.py')
  
  if len(reversed) == 5 and reversed[0] == 'Mary' and reversed[1] == 'Had' and reversed[2] == 'A' and reversed[3] == 'Little' and reversed[4] == 'Lamb' :  
    print 'well done'
    exit(0)
  
except (IOError, SyntaxError, ValueError) as e:
  print str(e)
  exit(1)
  
print 'Not quite right, try again!'
exit(1)
