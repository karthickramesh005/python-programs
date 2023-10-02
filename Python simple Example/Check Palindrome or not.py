# Check Palindrome or not :

txt =input("Enter a text is here :  ")

rev = txt[::-1]

if rev != txt:
    print("Its a not Palindrome word")
else:
    print("Its a  Palindrome word")
print(rev)
