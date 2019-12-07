from generator import Generator

def main():
    filename = "words_alpha.txt"
    generator = (
        Generator.Builder()
            .set_source_file(filename)
            .set_ngram(4)
            .build()
    )
    
    # keep generating words
    while True:
        print(generator.generate_word(), end="")
        input()

if __name__ == "__main__":
    main()


