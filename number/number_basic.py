

def mathact():
     
     x,y,z= 5,6,7
     mathact = (x+y)*z   #! never use mathact = x+y*z
     print(mathact)

def samedatatype():
        x = float(1) #! x = 1.0
        y = float(2.8) #! y = 2.8
        print(x+y) #? always use same data type for any math operation
        
def printingtrics():
    x = "Hello"
    y = "World"
    z = "ran"
    y_repr = repr(y)  #! repr()  => string apperar in code
    y_str = str(y)   #! str() => string like for human reading
    
    print(f"repr version of y {y_repr} and str version of y {y_str}")
    print(y) #! used for debugging, show output in terminal . return = None


def main():
      mathact()
      samedatatype()
      printingtrics()

     
if __name__ == '__main__':
    main()
    