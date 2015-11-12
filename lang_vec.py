"""
We can also sum these different language vectors into a
single vector and use it for finding words.  I think we
should do that next.  Do you think you can change the
program so that it produces a language vector that is
the sum of six language vectors, one that is based on
single letters, another that is based on bigrams, third
based on trigrams, fourth on tetragrams, fifth on
pentagrams, and the sixth based on hexagrams.  You
can use Alice in Wonderland for data:

  http://www.gutenberg.org/ebooks/11

Remove all non-letters from the text and make all
letters the same case (upper of lower).  That should be
about 100,000 letters.

How this combination vector can be used to find the
number of different letters, bigrams, trigrams, etc. in
the text will be the next exercise.  You can start
thinking about it.

generate_text.py
"""
import random_idx
import utils
import numpy as np
import string
import pandas as pd
import matplotlib.pyplot as plt

k = 5000
# assuming that cluster_sizes is mapping to n-gram size
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

def create_lang_vec(N=N,k=k, cluster_sizes):
    print "generating english vector of cluster size", cluster_sz
    total_eng = np.zeros((1,N))
    # generate english vector
    for cz in cluster_sizes:
        lang_vector = random_idx.generate_RI_lang(N, RI_letters, cz, ordered, languages=['eng'])
    total_lang += lang_vector
    return total_lang

RI_letters = gen_lets()
lang_vector = create_lang_vec(cluster_sizes)

#need to process the text itself. lang vector made with summed n_grams (assuming cluster_sizes map to n_grams)

def read_text(n):
	#with open("AliceInWonderland.txt", "r") as f:
	#	f.write(str(max_cluster_size))

if __name__ == "__main__":
	create_lang_vec(cluster_sizes)



