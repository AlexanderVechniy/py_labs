def IsGood(x):
    if x%2==0 and x%7!=0 and x%11!=0 and x%13!=0 and x%23!=0:
        return True;
    return False;
 
i = 1098
counter = 0;
while i <= 13765:
    if IsGood(i):
        if counter == 0:
            min_num = i
        counter+=1
    i+=1
print(counter, min_num)
