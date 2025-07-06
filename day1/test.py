# a,b = map(int , input("Enter two values which saprate by space ").split())


# su = int(a+b)
# print(su)


def av(*args):

    avg = sum(args)/len(args) 
    print(avg)

# lst = [12,10,11,9,13]
lst = map(int,input("Enter number of values which saprate by space:").split())
av(*lst)