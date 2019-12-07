from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple
from bisect import bisect_right
import random, sys

Chain = Dict[str, List[Tuple[str, float]]]

def train(filename: str, gramlen: int) -> Chain:
    f = open(filename, "r")
    lines = f.readlines()
    
    # Init tmp count
    tmp = defaultdict(lambda: defaultdict(int))

    # Iterate per ngram
    for word in lines:
        word = word.strip()
        prev = "#"
        for i in range(0,len(word), gramlen):
            ngram = word[i:i+gramlen]
            tmp[prev][ngram] += 1
            prev = ngram
        tmp[prev]["#"] += 1

    # Normalize matrix
    matrix: Chain = {}
    for k, v in tmp.items():
        # store in temporary list
        vals = [(ngram, cnt) for ngram, cnt in v.items()]
        # normalize values
        total = sum(x for _, x in vals)
        vals = [(ngram, cnt/total) for ngram, cnt in vals]
        # create cumulative distribution
        cum = [("", 0)]
        [cum.append((ngram, cum[-1][1] + x)) for ngram, x in vals]
        cum = cum[1:]

        # store in matrix
        matrix[k] = cum

    return matrix

def generate_word(chain: Chain) -> str:
    def generate_next(ngram: str) -> str:
        vals = chain[ngram]
        keys = [x[1] for x in vals]
        
        # generate random and find
        x = random.uniform(0, 1)
        ngram = vals[bisect_right(keys, x)]
        return ngram[0]
    
    # generate until stop
    prev, word = "#", ""
    while True:
        ngram = generate_next(prev)
        if ngram == "#":
            break
        
        word += ngram
        prev = ngram

    return word

def main():
    filename = "words_alpha.txt"
    # train the model using n-gram of size 4
    chain = train(filename, 4)
    
    # keep generating words
    while True:
        print(generate_word(chain), end="")
        input()

if __name__ == "__main__":
    main()


