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

    print "Take the language vector representing single letters of\n\
    Alice and compute its dot product with the 26 different\n\
    letter vectors.  Can you see a relation between the dot\n\
    products and the letter counts in Alice?  Alice has\n\
    about 300 instances of 'q'.  I'd expect a dot product\n\
    with the Q-vector to be around 3 million.\n"
    for i in range(26):
        result = np.dot(lang_vectors[1], RI_letters[i])
        print "dot product of single-letter vector and %s-vector is %d" % (alph[i], result) 
    print ""

    print "Then take the language vector representing the bigrams\n\
    of Alice and compute its dot product with QU.  What do\n\
    you get?  And what is this language vector's dot\n\
    product with Q?\n"
    
    result = np.dot(lang_vectors[2], np.transpose(qu_vector))
    print "dot product of bigrams vector and qu is %d\n" % (result) 

    print "Next, add the two language vectors into a single vector\n\
    that represents both individual letters and bigrams.\n\
    Compute its dot product with Q and with QU.  What do\n\
    you get?\n"
    
    result = np.dot(up2_lang_vec, RI_letters[alph.find("q")])
    print "dot product of up2_lang_vec and q is %d\n" % (result) 
    result = np.dot(up2_lang_vec, np.transpose(qu_vector))
    print "dot product of up2_lang_vec and qu is %d\n" % (result) 

    print "One more set of tests: Take the language vector for\n\
    bigrams and (pointwise) multiply it with sQ (Q shifted\n\
    once).  Compare the resulting vector (with dot product\n\
    or cosine) to the letter vectors A, B, C, ....  Which\n\
    letter wins?  Do the same using the language vector for\n\
    individual letters, and once more using a language\n\
    vector that is the sum of the above two.\n"
    
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

    print "So try this: make a language vector of bigrams only.\n\
    If you test it with (calculate its dot produce with)\n\
    the letter vectors, you should get numbers like those\n\
    in the second block of 'results.txt' that starts with\n\
    dot product of bigrams_sQ and a is -31528\n\
    Some are positive, some negative, and none is in the\n\
    hundreds of thousands.  All that is 'noise' in\n\
    signal-processing terms.  But if you test it with the\n\
    vector for QU (which equals sQ * U) or with any other\n\
    bigram vector, you should get that bigram's frequency\n\
    times 10K.  That's referred to as signal.\n"
    
    for i in range(26):
        result = np.dot(lang_vectors[2], RI_letters[i])
        print "dot product of bigrams vector and %s-vector is %d" % (alph[i], result) 
    print ""

    print "After you have gotten this far, make a language vector\n\
    that combines individual letters, bigrams and trigrams:\n\
    just add those three language vectors into a single\n\
    vector (by normal vector addition.).  Then test it for\n\
    single letters and bigrams as above.  Also, multiply it\n\
    with sQ and test the result as above.  The dot products\n\
    should be close to what you got before.\n"
    print up3_lang_vec
    for i in range(26):
        result = np.dot(up3_lang_vec, RI_letters[i])
        print "dot product of up3_lang_vec vector and %s-vector is %d" % (alph[i], result) 
    print ""

    #idk why the vectors are nested in lists
    print up3_lang_vec

    result = np.dot(up3_lang_vec[0], lang_vectors[2][0])
    print "dot product of up3_lang_vec vector and bigrams vector is %d" % (result)
    print ""

    up3_lang_vec_sQ = np.multiply(up3_lang_vec, sQ)
    for i in range(26):
        result = np.dot(up3_lang_vec_sQ, RI_letters[i])
        print "dot product of up3_lang_vec_sQ vector and %s-vector is %d" % (alph[i], result) 
    print ""

    result = np.dot(np.transpose(up3_lang_vec_sQ[0]), lang_vectors[2][0])
    print "dot product of up3_lang_vec_sQ and bigrams vector is %d" % (result)


