# Jumble

A Markov Chain based random word generator

## How to use

Make sure you have Python 3 installed. To execute the program, run `python main.py`.

To change the n-gram length or the wordlist being used, in `main.py`, change variables `ngram` and `filename` respectively.

## Behind the scenes

### Markov Chains

The random word generator relies on what's called a Markov chain. According to [brilliant.org](https://brilliant.org/wiki/markov-chains/), a Markov chain is:

> a mathematical system that experiences transitions from one state to another according to certain probabilistic rules.

Here's a sample of a Markov chain

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Finance_Markov_chain_example_state_space.svg/800px-Finance_Markov_chain_example_state_space.svg.png" width="500">

In the given image, there are three states: bull, bear, and stagnant. The edges (lines) between each state represents the probability of moving from one state to the other. For example, in th given graph, there is a 15% (0.15) probability of transitioning from a bear market to a bull market. Notice that the sum of the outgoing edges equals to 1.

### Model representation

We represent an n-gram as a single state. For example, if we decided to use bigrams (2-gram), then the words `able`, `stable`, and `abrupt` will turn into states `ab`, `le`, `st`, `ru`, and `pt`. A word start/end will be represented as `#`.

We still need to create the edges. A consecutive n-gram `a` and `b` will add +1 to the edge `a -> b`. For example, the word `stable` will add +1 to edges `# -> st`, `st -> ab`, `ab -> le`, `le -> #`. Here's the full graph:

![sample-1](https://i.imgur.com/I9c5KFX.png)

To turn this into a Markov chain, the outgoing edges should be normalized, as shown in the following image:

![sample-norm](https://i.imgur.com/idJLRQs.png)

### Random generator

Generating a random word starts from state `#`. From here, there's a 67% chance to go to `ab` and a 33% chance to go to `st`. Let's say we got lucky and went to `st`. Now our word is `st`.

The current state is `st`. There is a 100% chance of going to `ab` after `st`. Now our word is `stab`.

From `ab`, we can go to `le` and `ru` with chances 67% and 33% respectively. Let's say we go to `le`. Now our word is `stable`.

After `le`, we have 100% chance to go to `#`. Thus, the word ends.

### Example generated words

In reality, the generator uses a (much) larger list than the example we've shown you. We also added a list of English words in this repository.

Here are some sample generated words using a 5-gram state:

- `derivate`
- `cracky`
- `nyctipetans`
- `porosine`
- `moringaevia`
- `nonexations`
- `polical`
- `table`
- `parro`
- `ohit`
- `intrations`
- `approborets`
- `perdozers`
- `franchling`
- `maharmoriamblycot`
- `unamuscosponences`

## Credits

- List of english words: [dwyl/english-words](https://github.com/dwyl/english-words/)