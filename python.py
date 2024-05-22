# 2nd question answers
def cube(a):
  c = []
  for i in range(1,a+1):
    c.append(i**3)
  return c
a = int(input())
print(cube(a))


# 1st question anser 
# option 1
a = list(map(str, input().split()))
for i in range(len(a)):
    if (i%2!=0):
      ans = a[i]
      print("odd index position value:",ans)

#option 2
def odd(a):
  for i in range(len(a)):
    if (i%2!=0):
      ans = a[i]
      return ans
      
a = list(map(str, input().split()))
print("odd index position value:",odd(a))
