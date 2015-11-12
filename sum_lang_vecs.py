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
cluster_sz = [1, 2, 3, 4, 5, 6]
ordered = 1
#alph = 'abc' 
alph = string.lowercase + ' '

# from generate_text.py
# copy pasted for now. 
def gen_lets(N=N,k=k):
        # generate letter vectors
        RI_letters = random_idx.generate_letter_id_vectors(N,k)
        RI_letters_n = RI_letters/np.linalg.norm(RI_letters)
        return RI_letters, RI_letters_n

def create_lang_vec(N=N,k=k, cluster_sz = [2]):
        print "generating english vector of cluster size", cluster_sz
        total_eng = np.zeros((1,N))
        # generate english vector
        for cz in cluster_sz:
                english_vector = random_idx.generate_RI_lang(N, RI_letters, cz, ordered, languages=['eng'])
        total_eng += english_vector


        normed_eng = total_eng/np.linalg.norm(total_eng)
        return total_eng, normed_eng

RI_letters, RI_letters_n = gen_lets()
english_vector, normed_eng = create_english_vec(cluster_sz=cluster_sz)

def generate_words(cluster_sz, english_vector=english_vector, normed_eng=normed_eng):
        print "generating english vector of cluster size", cluster_sz
        # generate english vector
        #english_vector = random_idx.generate_RI_text_words(N, RI_letters, './lang_texts/texts_english/eng.txt')
        # generate new string of letters
        length = 30
        alphy = utils.generate_ordered_clusters(alph, cluster_sz=cluster_sz)
        gstr = alph[np.random.randint(len(alph))]
        temp_str = gstr
        for i in xrange(length):
                max_idx = 0
                maxabs = 0
                for j in xrange(len(alphy)):
                        temp_str = gstr + alphy[j]
                        temp_id = random_idx.generate_RI_str(N,RI_letters,cluster_sz,ordered,temp_str)
                        #temp_id += 1e1*np.random.randn(1,N)
                        temp_id /= np.linalg.norm(temp_id)
                        absy = np.abs(temp_id.dot(normed_eng.T))
                        #print temp_str, absy
                        if absy > maxabs:
                                max_idx = j
                                maxabs = absy
                gstr += alphy[max_idx]
                print len(gstr), maxabs, gstr

def summed_lang_vec:

def generate_n_gram(n):
	with open("AliceInWonderland.txt", "r") as f:
		f.write(str(max_cluster_size))

if __name__ == "__main__":
	for i in range(1, 7):
		generate_n_grams(i)



