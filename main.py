from jumble import Jumble

ngram = 4
filename = "wordlist/words_eng.txt"

def main():
    jumble = (
        Jumble.Builder()
        .set_source_file(filename)
        .set_ngram(ngram)
        .build()
    )

    # keep generating words
    while True:
        print(jumble.generate_word(), end="")
        input()


if __name__ == "__main__":
    main()
