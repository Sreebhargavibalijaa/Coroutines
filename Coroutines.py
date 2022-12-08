def tracker(d, limit=0):
    'tracker to find the number of odd numbered seconds that have been iterated over.'
    assert isinstance(limit, int)
    corotine= next(d) 
    odd=0
    x= yield
    print(x) 
    if x:
      limit= x

    while(odd<limit):
        a=corotine.seconds
        if(a%2 ==1):
            odd =odd+1 

        yield odd
        corotine= next(d) 