def word_counter():
    sentence = str(input("Enter a sentence: "))
    words = sentence.lower().split(" ")
    print(words)

    word_count = {}
    for word in words:

        if word in word_count:
            word_count[word] +=1
            print(word_count)
        else:
            word_count[word] = 1

    print("Word frequency")
    for word,count in word_count.items():
        print(f"{word} : {count}")

word_counter() 