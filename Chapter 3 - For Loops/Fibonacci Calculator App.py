'''
Description:
You are responsible for writing a program that will compute the first n terms of the Fibonacci
Sequence. Your program will then display these terms. Next, your program will calculate the
ratios of consecutive Fibonacci numbers to prove that these ratios approach the irrational
mathematical constant of Phi; 1.618....

Example Output:
Welcome to the Fibonacci Calculator App
How many digits of the Fibonacci Sequence would you like to compute: 15
The first 15 numbers of the Fibonacci sequence are:
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610

The corresponding Golden Ratio values are:
1.0
2.0
1.5
1.6666666666666667
1.6
1.625
1.6153846153846154
1.619047619047619
1.6176470588235294
1.6181818181818182
1.6179775280898876
1.6180555555555556
1.6180257510729614
1.6180371352785146
The ratio of consecutive Fibonacci terms approaches Phi; 1.618...

'''

def fibonacci(n):
    if n in [0, 1]:
        return n
    return (fibonacci(n-1)+fibonacci(n-2))


n=int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
golden_ratios=[]

print(f"The first {n} numbers of the Fibonacci sequence are:")
for x in range(n):
    n1=fibonacci(x)
    n2=fibonacci(x+1)
    print(n1)
    if (n1!=0):
        golden_ratios.append(n2/n1)
    
print("\nThe corresponding Golden Ratio values are:")
for ratio in golden_ratios:
    print(ratio)
        
