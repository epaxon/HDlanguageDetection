import random_idx
import utils
import numpy as np
import string
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import sys

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

# RI_letters = random_idx.generate_letter_id_vectors(N, k, alph)

# lang_vectors in sizes 1-8
# lang_vectors = []
# for size in cluster_sizes:
#     lang_vectors.append(create_lang_vec([size]))
# lang_vectors.insert(0, np.zeros((1,N)))

# save vectors to file
#np.savetxt('alice_RI_letters.txt', RI_letters, '%d')
#np.savetxt('alice_lang_vectors.txt', lang_vectors, '%f')
# fwrite = open("alice_RI_letters", "w")
# fwrite1 = open("alice_lang_vectors", "w")
# pickle.dump(RI_letters, fwrite)
# pickle.dump(lang_vectors, fwrite1)
# fwrite.close()
# fwrite1.close()

#read from serialized files
fread = open("alice_RI_letters", "r")
fread1 = open("alice_lang_vectors", "r")
RI_letters = pickle.load(fread)
lang_vectors = pickle.load(fread1)
fread.close()
fread1.close()

up2_lang_vec = np.add(lang_vectors[1], lang_vectors[2])
up3_lang_vec = np.add(up2_lang_vec, lang_vectors[3])
qu_vector = random_idx.id_vector(N, "qu", alph, RI_letters, ordered)

if __name__ == "__main__":

    up2_lang_vec = np.add(lang_vectors[1], lang_vectors[2])
    qu_vector = random_idx.id_vector(N, "qu", alph, RI_letters, ordered)

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
    print ""

    """
    Then take the language vector representing the bigrams
    of Alice and compute its dot product with QU.  What do
    you get?  And what is this language vector's dot
    product with Q?
    """    
    result = np.dot(lang_vectors[2], np.transpose(qu_vector))
    print "dot product of bigrams vector and qu is %d\n" % (result) 

    """
    Next, add the two language vectors into a single vector
    that represents both individual letters and bigrams.
    Compute its dot product with Q and with QU.  What do
    you get?
    """
    
    result = np.dot(up2_lang_vec, RI_letters[alph.find("q")])
    print "dot product of up2_lang_vec and q is %d\n" % (result) 
    result = np.dot(up2_lang_vec, np.transpose(qu_vector))
    print "dot product of up2_lang_vec and qu is %d\n" % (result) 

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
    sQ = np.roll(RI_letters[alph.find("q")], 1)
    bigrams_sQ = np.multiply(lang_vectors[2], sQ)
    # still need to compare to see which letter wins
    for i in range(26):
        result = np.dot(RI_letters[i], np.transpose(bigrams_sQ))
        print "dot product of bigrams_sQ and %s is %d" % (alph[i], result) 
    print ""

    single_sQ = np.multiply(lang_vectors[1], sQ)
    for i in range(26):
        result = np.dot(RI_letters[i], np.transpose(single_sQ))
        print "dot product of single_sQ and %s is %d" % (alph[i], result) 
    print ""

    up2_lang_vec_sQ = np.multiply(up2_lang_vec, sQ)
    for i in range(26):
        result = np.dot(RI_letters[i], np.transpose(up2_lang_vec_sQ))
        print "dot product of up2_lang_vec_sQ and %s is %d" % (alph[i], result)
    print ""

    """
    So try this: make a language vector of bigrams only.
    If you test it with (calculate its dot produce with)
    the letter vectors, you should get numbers like those
    in the second block of "results.txt" that starts with

    dot product of bigrams_sQ and a is -31528

    Some are positive, some negative, and none is in the
    hundreds of thousands.  All that is "noise" in
    signal-processing terms.  But if you test it with the
    vector for QU (which equals sQ * U) or with any other
    bigram vector, you should get that bigram's frequency
    times 10K.  That's referred to as "signal."
    """
    for i in range(26):
        result = np.dot(lang_vectors[2], RI_letters[i])
        print "dot product of bigrams vector and %s-vector is %d" % (alph[i], result) 
    print ""

    """
    Now it gets more subtle and interesting.  Take the
    language vector for bigrams and MULTIPLY it
    (coordinate-wise) with Q that has been rotated once
    (i.e., multiply it with sQ) and then test the result
    with the letter vectors.  The dot product should be
    high for U only.  Can you figure out the reason why,
    do you see what's happening?
    """
    bigrams_sQ = np.multiply(lang_vectors[2], single_sQ)
    for i in range(26):
        result = np.dot(bigrams_sQ, RI_letters[i])
        print "dot product of bigrams_sQ vector and %s-vector is %d" % (alph[i], result) 
    print ""

    """
    After you have gotten this far, make a language vector
    that combines individual letters, bigrams and trigrams:
    just add those three language vectors into a single
    vector (by normal vector addition.).  Then test it for
    single letters and bigrams as above.  Also, multiply it
    with sQ and test the result as above.  The dot products
    should be close to what you got before.
    """
    for i in range(26):
        result = np.dot(up3_lang_vec, RI_letters[i])
        print "dot product of up3_lang_vec vector and %s-vector is %d" % (alph[i], result) 
    print ""

    temp = np.transpose(up3_lang_vec)
    print(temp)
    print(lang_vectors[2])
    result = np.dot(temp, lang_vectors[2])
    print(result)
    #    up2_lang_vec_sQ = np.multiply(up2_lang_vec, sQ)
    #for i in range(26):
    #    result = np.dot(RI_letters[i], np.transpose(up2_lang_vec_sQ))


    print "dot product of up3_lang_vec vector and bigrams vector is %d" % (result)
    
    up3_lang_vec_sQ = np.multiply(up3_lang_vec, single_sQ)
    for i in range(26):
        result = np.dot(up3_lang_vec_sQ, RI_letters[i])
        print "dot product of up3_lang_vec vector and %s-vector is %d" % (alph[i], result) 
    print ""

    result = np.dot(up3_lang_vec_sQ, lang_vectors[2])
    print "dot product of up3_lang_vec vector_sQ and bigrams vector is %d" % (result)





