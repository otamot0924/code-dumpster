import random

nums = [0,1,2,3,4,5,6,7,8,9] #會用到的數字
ans = []

for i in range(4):
    if i == 0:
        rand_num = nums[random.randint(1,len(nums)-1)] #第一個數字不為零
    else:
        rand_num = nums[random.randint(0,len(nums)-1)] #隨機取數
    ans.append(rand_num)
    nums.remove(rand_num) #把用過的數字刪除避免重複

#print("Answer: ", *ans, sep="")

inp = 0

while inp != ans:
    inp = list(map(int, input()))

    a = 0
    b = 0

    for i in range(4):
        if inp[i] == ans[i]: #正確數字在正確位置
            a += 1
        elif inp[i] in ans: #正確數字在錯誤位置
            b += 1

    print("{0}A{1}B".format(a, b))
