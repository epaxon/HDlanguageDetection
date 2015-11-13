import random_idx
import utils
import numpy as np
import string
import pandas as pd
import matplotlib.pyplot as plt

k = 5000
# cluster_sizes is mapping to n-gram size
# cluster_sz in random_idx referring to specific element (int) in cluster_sizes, array
cluster_sizes = [1, 2, 3, 4, 5, 6, 7, 8]
ordered = 1
#alph = 'abc' 
alph = string.lowercase + ' '

# from generate_text.py
# copy pasted for now. 
def gen_lets(N=N,k=k):
    # generate letter vectors
    RI_letters = random_idx.generate_letter_id_vectors(N,k)
    return RI_letters

#need to process the text itself. lang vector made with summed n_grams (assuming cluster_sizes map to n_grams)
#text_vector for vectors of text where don't know what language it is in yet. Since we know AliceInWonderland 
#is in english and is used to create our language vector, our lang_vector is our text_vector.
def create_lang_vec(N=N,k=k, cluster_sizes):
    print "generating english vector of cluster size", cluster_sz
    total_eng = np.zeros((1,N))
    # generate english vector
    for cz in cluster_sizes:
        # which alphabet to use
        lang_vector = random_idx.generate_RI_text(N, RI_letters, cz, ordered, "AliceInWonderland.txt", alph)
        total_lang += lang_vector
    return total_lang

RI_letters = gen_lets()
lang_vector = create_lang_vec(cluster_sizes)

if __name__ == "__main__":
    #do testing here
    """
Take the language vector representing single letters of
Alice and compute its dot product with the 26 different
letter vectors.  Can you see a relation between the dot
products and the letter counts in Alice?  Alice has
about 300 instances of "q".  I'd expect a dot product
with the Q-vector to be around 3 million.

Then take the language vector representing the bigrams
of Alice and compute its dot product with QU.  What do
you get?  And what is this language vector's dot
product with Q?

Next, add the two language vectors into a single vector
that represents both individual letters and bigrams.
Compute its dot product with Q and with QU.  What do
you get?

One more set of tests: Take the language vector for
bigrams and (pointwise) multiply it with sQ (Q shifted
once).  Compare the resulting vector (with dot product
or cosine) to the letter vectors A, B, C, ....  Which
letter wins?  Do the same using the language vector for
individual letters, and once more using a language
vector that is the sum of the above two.
    """


