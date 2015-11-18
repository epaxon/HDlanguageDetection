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
#assuming this is the alphabet bc of precedent in generate_text.py
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
english_alphabet = "abcdefghijklmnopqrstuwxyz"
RI_letters = gen_lets()
lang_vector = create_lang_vec(cluster_sizes)
single_letter_lang_vector = create_lang_vec([1])
bigrams_lang_vector = create_lang_vec([2])
up2_lang_vec = np.add(single_letter_lang_vector, bigrams_lang_vector)
qu_vector = random_idx.generate_RI_str(N, RI_letters, 2, ordered, "qu", alph)

if __name__ == "__main__":
    """
    Take the language vector representing single letters of
    Alice and compute its dot product with the 26 different
    letter vectors.  Can you see a relation between the dot
    products and the letter counts in Alice?  Alice has
    about 300 instances of "q".  I'd expect a dot product
    with the Q-vector to be around 3 million.
    """
    for i in range(0,26):
        result = np.dot(single_letter_lang_vector, RI_letters[i])
        print "dot product of %s and %s-letter vector is %f" % (english_alphabet[i], english_alphabet[i], result) 
        print "\n"

    """
    Then take the language vector representing the bigrams
    of Alice and compute its dot product with QU.  What do
    you get?  And what is this language vector's dot
    product with Q?
    """
    
    result = np.dot(bigrams_lang_vector, qu_vector)
    print "dot product of bigrams_lang_vector and qu is %f" % (result) 
    print "\n"
    """
    Next, add the two language vectors into a single vector
    that represents both individual letters and bigrams.
    Compute its dot product with Q and with QU.  What do
    you get?
    """
    
    result = np.dot(up2_lang_vec, RI_letters[16])
    print "dot product of up2_lang_vec and q is %f" % (result) 
    print "\n"
    result = np.dot(up2_lang_vec, qu_vector)
    print "dot product of up2_lang_vec and qu is %f" % (result) 
    print "\n"

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
    sQ = np.roll(list(RI_letters[16], 1)
    bigrams_sQ = np.multiply(bigrams_lang_vector, sQ)
    # still need to compare to see which letter wins
    for i in range(0,26):
        result = np.dot(RI_letters[i], bigrams_sQ)
        print "dot product of bigrams_sQ and %s is %f" % (english_alphabet[i], result) 
        print "\n"

    single_sQ = np.multiply(single_letter_lang_vector, sQ)
    for i in range(0,26):
        result = np.dot(RI_letters[i], single_sQ)
        print "dot product of single_sQ and %s is %f" % (english_alphabet[i], result) 
        print "\n"

    up2_lang_vec_sQ = np.multiply(up2_lang_vec, sQ)
    for i in range(0,26):
        result = np.dot(RI_letters[i], up2_lang_vec_sQ)
        print "dot product of up2_lang_vec_sQ and %s is %f" % (english_alphabet[i], result) 
        print "\n"













