from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple
from bisect import bisect_right
import random

Chain = Dict[str, List[Tuple[str, float]]]

class Generator:
    class Builder:
        def __init__(self):
            self.__reset()

        def build(self) -> 'Generator':
            self.__generator.train(filename=self.__filename, gramlen=self.__ngram)

            generator = self.__generator
            self.__reset()
            return generator

        def set_source_file(self, filename: str) -> 'Builder':
            self.__filename = filename
            return self
        
        def set_ngram(self, ngram: int) -> 'Builder':
            self.__ngram = ngram
            return self

        def __reset(self) -> None:
            self.__generator = Generator()
            self.__filename = ""
            self.__ngram = 0

    
    def train(self, filename: str, gramlen: int):
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

        self.__model = matrix

    def generate_word(self) -> str:
        def generate_next(ngram: str) -> str:
            vals = self.__model[ngram]
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