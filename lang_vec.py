import random_idx
import utils
import numpy as np
import string
import pandas as pd
import matplotlib.pyplot as plt

k = 5000
N = 10000
# cluster_sizes is mapping to n-gram size
# cluster_sz in random_idx referring to specific element (int) in cluster_sizes, array
cluster_sizes = [1, 2, 3, 4, 5, 6, 7, 8]
ordered = 1
#assuming this is the alphabet bc of precedent in generate_text.py
#alph = 'abc' 
alph = string.lowercase + ' '

# create language vector for Alice in Wonderland made of summed n-gram vectors for each
# n in cluster_sizes
def create_lang_vec(cluster_sizes, N=N, k=k):
    
    total_lang = np.zeros((1,N))
    # generate english vector
    for cz in cluster_sizes:
        print "generating language vector of cluster size", cz
        # which alphabet to use
        lang_vector = random_idx.generate_RI_text_fast(N, RI_letters, cz, ordered, "preprocessed_texts/AliceInWonderland.txt", alph)
        total_lang += lang_vector
    return total_lang

RI_letters = random_idx.generate_letter_id_vectors(N, k, alph)

# lang_vectors in sizes 1-8
lang_vectors = []
for size in cluster_sizes:
    lang_vectors.append(create_lang_vec([size]))
lang_vectors.insert(0, np.zeros(1,N))

up2_lang_vec = np.add(lang_vectors[1], lang_vectors[2])
qu_vector = random_idx.generate_RI_str(N, RI_letters, 2, ordered, "uq", alph)

if __name__ == "__main__":
    """
    Take the language vector representing single letters of
    Alice and compute its dot product with the 26 different
    letter vectors.  Can you see a relation between the dot
    products and the letter counts in Alice?  Alice has
    about 300 instances of "q".  I'd expect a dot product
    with the Q-vector to be around 3 million.
    """
    for i in range(26):
        result = np.dot(lang_vectors[1], RI_letters[i])
        print "dot product of single-letter vector and %s-vector is %d" % (alph[i], result) 

    """
    Then take the language vector representing the bigrams
    of Alice and compute its dot product with QU.  What do
    you get?  And what is this language vector's dot
    product with Q?
    """    
    result = np.dot(lang_vectors[2], np.transpose(qu_vector))
    print "dot product of bigrams vector and qu is %d" % (result) 

    """
    Next, add the two language vectors into a single vector
    that represents both individual letters and bigrams.
    Compute its dot product with Q and with QU.  What do
    you get?
    """
    
    result = np.dot(up2_lang_vec, RI_letters[16])
    print "dot product of up2_lang_vec and q is %d" % (result) 
    result = np.dot(up2_lang_vec, np.transpose(qu_vector))
    print "dot product of up2_lang_vec and qu is %d" % (result) 

    """
    One more set of tests: Take the language vector for
    bigrams and (pointwise) multiply it with sQ (Q shifted
    once).  Compare the resulting vector (with dot product
    or cosine) to the letter vectors A, B, C, ....  Which
    letter wins?  Do the same using the language vector for
    individual letters, and once more using a language
    vector that is the sum of the above two.
    """
    # assuming that shifting is rolling...
    sQ = np.roll(RI_letters[16], 1)
    bigrams_sQ = np.multiply(lang_vectors[2], sQ)
    # still need to compare to see which letter wins
    for i in range(26):
        result = np.dot(RI_letters[i], bigrams_sQ)
        print "dot product of bigrams_sQ and %s is %d" % (alph[i], result) 

    single_sQ = np.multiply(lang_vectors[1], sQ)
    for i in range(26):
        result = np.dot(RI_letters[i], single_sQ)
        print "dot product of single_sQ and %s is %d" % (alph[i], result) 

    up2_lang_vec_sQ = np.multiply(up2_lang_vec, sQ)
    for i in range(26):
        result = np.dot(RI_letters[i], up2_lang_vec_sQ)
        print "dot product of up2_lang_vec_sQ and %s is %d" % (alph[i], result) 












