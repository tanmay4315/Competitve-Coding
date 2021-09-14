def minimumMoves(arr1,arr2):
    #counting step
    d=0     
    for j in range(len(arr1)):
        num1=arr1[j]     
        num2=arr2[j]
        # We have to change arr1 to arr2 and count the number of step needs to change digit
        # every digit in number
        while num1>0 or num2>0 :
            #to get every digit of number we store remainder
            remain1=num1%10     
            remain2=num2%10
            #updating number
            num1=num1//10
            num2=num2//10
            d=d+abs(remain1-remain2) #adding number of steps steps can't be negative so abs
    #return the number of way
    return d    
arr1_count = int(input().strip())
arr1 = []
for _ in range(arr1_count):
    arr1_item = int(input().strip())
    arr1.append(arr1_item)
arr2_count = int(input().strip())
arr2 = []
for _ in range(arr2_count):
    arr2_item = int(input().strip())
    arr2.append(arr2_item)
result = minimumMoves(arr1, arr2)
# printing result
print(result)
        
