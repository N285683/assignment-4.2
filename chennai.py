def  square_num(n):
    return n*n
nums=[5,10,15,20]
print("original list:",nums)
result=map(square_num,nums)
print("square the elements of the said list using map():",)
print(list(result))