def palindrome():
    pd = str(input("Enter a word or sentence to check if it is a palindrome: "))
    pd_lower = pd.lower()
    
    trimmed_pd = pd_lower.replace(" ", "")
    rev = trimmed_pd[::-1]
    print(rev)

    if trimmed_pd == rev:
        print("The word/sentence is a palindrome")
    else:
        print("The word/sentence is not a palindrome")


palindrome()