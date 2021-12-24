# 'A' -> 'A'
# 'AA' -> 'A2'
# 'ABAA' -> 'ABA2'
# 'AABBACAAAA' -> 'A2B2ACA4'
# '' -> ''
# '222' -> '23'

str1, str2 = 'AABBBACBBAaaAA', ''
accum, length = 1, len(str1)

for j in range(length):
    
    if j != (length-1):
        
        if str1[j] == str1[j+1]:
            accum += 1
        
        else:
            
            if accum != 1:
                print(str1[j]+str(accum), end = '')
            
            else:
                print(str1[j], end = '')
            accum = 1
    
    else:
        
        if accum != 1:
            str2 += str1[j] + str(accum)
        
        else:
            str2 += str1[j]

print(str2)