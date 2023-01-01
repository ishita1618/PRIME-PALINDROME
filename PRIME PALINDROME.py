#for taking input
n = int(input("Enter The Value of n: "))

#for variable
c = 0

#palindrome number starts form a least 2 digit
num = 11

#for variable
ans = 0

# run loop if n is not 0
while c != n:
    a = False
    for i in range(2, num):
        if (num % i) == 0:

            # will assign composite so that prime remains in false or a
            a = True

    if a== False:
        k = num
        temp = k

        # reverse variable
        rev = 0
        while (k > 0):

            # get lastdigit Eg.123 last is 3
            digit = k % 10

            # will store the rev. digit
            rev = rev*10+digit
            k = k//10

            # if rev and num is same its palindrome
        if (temp == rev):
            ans = temp

            # will increase value of c by 1
            c = c + 1

    num = num + 1
print("The Answer is:",ans)