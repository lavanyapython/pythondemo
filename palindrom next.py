def Previous_Palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x
 
num = int(input("Enter the Number :"))			
print(Previous_Palindrome(num))
