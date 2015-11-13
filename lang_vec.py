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

# how apply text_vector from Alice text to lang_vector which doesn't seem to use it as input?
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
    # generate RI vector for "text_name"
    # assumes text_name has .txt
    text_vector = generate_RI_text(N, RI_letters, cluster_sz, ordered, "AliceInWonderland.txt", alph=alphabet):
        
def generate_RI_lang(N,RI_letters, cluster_sz, ordered, languages=None):
def generate_RI_text_words(N, RI_letters, text_name, alph=alphabet):
def generate_RI_str(N, RI_letters, cluster_sz, ordered, string, alph=alphabet):


