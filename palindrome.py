def ispalindrome(s):
    return s==s[::-1]
s="manasa"
ans=ispalindrome(s)
if ans:
    print("yes")
else:
    print("no")
