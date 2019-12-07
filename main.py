from jumble import Jumble

def main():
    filename = "words_eng.txt"
    jumble = (
        Jumble.Builder()
            .set_source_file(filename)
            .set_ngram(4)
            .build()
    )
    
    # keep generating words
    while True:
        print(jumble.generate_word(), end="")
        input()

if __name__ == "__main__":
    main()


