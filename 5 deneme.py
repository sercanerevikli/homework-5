def fakeprimes():
    ListOfFakePrime = []
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
    for i in range(0,len(primes)-1):
        fakeprime = primes[i]*primes[i+1]
        ListOfFakePrime.append(fakeprime)
    for k in range(0,len(primes)-1):
        print("Fake prime in position ", k+1 , "is",  ListOfFakePrime[k] ,".It is generated using", primes[k] , "and", primes[k+1], ".")

fakeprimes()