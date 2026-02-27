def word_count():

    s = str(input("Enter a sentence: "))

    if " " in s:
        t = s.replace(" ", "")
        sent1 = len(t)
        print(f"The string length without space is {sent1}")
        sent2 = len(s)
        print(f"the string length with whitespace is {sent2}")

word_count()