limit=100
nfizz=3
nbuzz=5
for i in range(1,limit):
    if (i % nfizz==0) and (i % nbuzz==0):
        print ("fizzbuzz",i)
    elif (i%nfizz==0):
        print ("Fizz",i)
    elif (i%nbuzz==0):
        print ("Buzz",i)
    else:
        print (i)
