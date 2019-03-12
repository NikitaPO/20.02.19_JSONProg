import json
import pytest

r = 5

#Testing
if __name__ == '__main__':
  print('Testing:')
  def testJsonModule():
    print('Test of JSON module is running...')
    try:
      assert r == 9 , "Fail to import JSON module"
    except:
      print("Error")


#Functions
def maxLong(lis):
  l = max(len(elem) for elem in lis)
  return l

def toString(lis):
  n = 0
  for i in lis:
    lis[n] = str(i)
    n += 1
  return lis

#Start of programm
with open('table.json') as jsonTable:
  t = json.load(jsonTable)
  jsonTable.close()

keys = toString(list(dict.keys(t)))
values = toString(list(dict.values(t)))
print()
m = max(maxLong(keys), maxLong(values))

n = 0
print("="*7,end='')
print("=="*m)
for i in dict.keys(t):
  print(f'| {keys[n].ljust(m)} | {values[n].ljust(m)} |')
  n+=1
print("="*7,end='')
print("=="*m)
