# solution 1
def isPrime(n):
    if n == 1:
        return False
    for d in range(2, n//2+1):
        if n % d == 0:
            return False
    return True

def solution(k):
    ans = 0
    for n in range(k*k, (k+1)*(k+1)):
        if isPrime(n):
            ans += 1
            
    return ans


# solution 2
def solution(k):
    
    isPrime = [1]*(k+1)*(k+1)
    isPrime[0] = isPrime[1] = 0
    
    for n in range(len(isPrime)):
        if isPrime[n] == 1:
            m = 2
            while m*n < len(isPrime):
                isPrime[m*n] = 0
                m += 1

    return sum(isPrime[k*k:])