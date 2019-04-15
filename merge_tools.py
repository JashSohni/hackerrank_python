def merge_the_tools(string1, k):
    string2 = list(string1)
    length = len(string2)
    ans = []
    count = -1
    for i in range(0,length,1):
        if i % k == 0:
            count = count + 1
            ans.append(string2[i])
            
        else:
            temp = i % k
            flag = 0
            for j in range(i-temp,i,1):    
                if string2[j] == string2[i]:
                    flag = 1
                    break
            if flag == 0:
                ans[count] += string2[i]
        
    for i in ans:
        print(i)




if __name__ == '__main__':
    inputt = raw_input()
    inputt2 = input()
    merge_the_tools(inputt,inputt2)