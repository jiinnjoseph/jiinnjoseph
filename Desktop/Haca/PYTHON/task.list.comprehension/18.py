n=list(range(1,51))
nl=["FizzBuzz" if i%3==0 and i%5==0 
    else "Fizz" if i%3==0
    else  "Buzz" if i%5==0 
    else str(i) for i in n]
print(nl)