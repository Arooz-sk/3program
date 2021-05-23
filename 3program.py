def printEvenDivisors(n) :
    i = 1
    even = []
    while i <= n :
      if (n % i==0 and i % 2 == 0) :
        even.append(i)
      i = i + 1
    if(n < 10):
      print('Invalid Number')
    elif(len(even) == 0):
      print('Please input a different number')
    else:
      even.sort(reverse = True)
      print(*even)
      sum = 1
      for i in even:
        sum *= i
      print(sum)
n = int(input())
printEvenDivisors(n)