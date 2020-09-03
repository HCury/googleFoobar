def test_prime(n):
    if n > 1:
      if (n==2):
          return True;
      else:
          for x in range(2,n):
              if(n % x==0):
                  return False
          return True

def solution(i):
    result = ''
    x = 2

    while len(result) < 10005:
      if test_prime(x) == True:
        result += str(x)
      x+=1

    result = result[i:i+5]
    return result
