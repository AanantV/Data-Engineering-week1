import os 

def file_analyser():

    def count_words(fn):
        with open(fn, "r") as file:
            content = file.read()
            words = content.split()
            print(f"The total words in the document are: {len(words)}")
            return len(words)

    def count_lines(fn):
        with open(fn, "r") as file:
            content = file.read()
            lines = content.split("\n")
            print(f"The total number of lines in the list are: {len(lines)}")
            return len(lines)


    def find_word(fn):
        with open(fn, "r") as file:
            content = file.read()
            words = content.split()
            print(words)
            try:
                text = input("Enter the word you want to find in the document: ")
                count = 0
                if text in words:
                    count += 1
                print(f"the word {text} occurs {count} times")
            except ValueError:
                print("Text not found")

    summary = "summary.txt"

    def write_analysis(fn):
       with open(summary, "w") as summarize:
            words_summary = count_words(fn)
            line_summary = count_lines(fn)
            summarize.write(f"The word count summary is {words_summary}.\n The line count summary is {line_summary}")


    try:
        filename = input("Enter the filename you want to analyse(with '.txt' extension): ")
    except FileNotFoundError:
        print("Invalid file name")


    while True:
        print("File Analyses")
        print("1. word count")
        print("2. line count")
        print("3. word occurence count")
        print("4. File analysis")
        print("5. quit")

        choice = input("Enter a choice between 1 to 5: ")

        if choice == "1":
            count_words(filename)
        elif choice == "2":
            count_lines(filename)
        elif choice == "3":
            find_word(filename)
        elif choice == "4":
            write_analysis(filename)
        elif choice == "5":
            print("quitting...")
            break
        else:
            print("Invalid choice")



file_analyser()