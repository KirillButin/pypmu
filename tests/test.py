def foo(x,y):
    try:
       # print(list([0])[1])
        return x/y
        
    except ZeroDivisionError:
        print("catch ZeroDivisionError")
        return 0
    finally:
        print("finally")
    print("after try")


foo(1,0)



#with open("C:/work/PMU/pypmu/tests/test.zip", "rb") as f:
#    byte = f.read(1)
#    while byte:
#        # Do stuff with byte.
#        byte = f.read(1)
   
#        print(byte.hex(), end = ' ')