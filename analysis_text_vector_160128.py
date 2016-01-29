# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:24:48 2016

@author: epaxon
"""

import random_idx
import utils

from pylab import *

#%%
fread = open("alice_RI_letters", "r")
fread1 = open("alice_lang_vectors", "r")
RI_letters = pickle.load(fread)
lang_vectors = pickle.load(fread1)
fread.close()
fread1.close()

N=RI_letters.shape[1]

text_name="preprocessed_texts/AliceInWonderland.txt"

text = utils.load_text(text_name)

# generate text vector from alice based on each character
alice_text_vector1 = random_idx.generate_text_vector(N, RI_letters, 1, text_name)

#%%
# generate text vector based on each pair of characters
alice_text_vector2 = random_idx.generate_text_vector(N, RI_letters, 2, text_name)

#%%

# This is now a normalized vector operation, which means the probability
# should be encoded, and that the sum over all letters should be 1
letter_vals = np.dot(RI_letters/N, alice_text_vector1.T)

print sum(letter_vals)


#%%

# So, this is really just encoding the expected value of each letter based on 
# the given text. This means that letter_vals should be very close to the counts
# of the letters found in the text

letter_counts = np.zeros(len(random_idx.alphabet))

for i,letter in enumerate(random_idx.alphabet):
    letter_counts[i] = text.count(letter)

letter_prob = letter_counts / sum(letter_counts)

#%%
figure()

bar(arange(len(letter_vals))+0.15, letter_vals, width=0.35, color='b')
bar(arange(len(letter_vals))+0.5, letter_prob, width=0.35, color='r')

ax = gca()

ax.set_xticks(arange(len(letter_vals))+1)
ax.set_xticklabels(list(random_idx.alphabet))

#%%

# If we look for individual letters in alice_text_vector2, then they will have
# low counts, because we only stored expected counts of letter pairs. Each 
# letter pair has its own unique hash, and this is different than the individual
# letter. In a text vector made up of only letter pairs, the individual hashes
# will never show up. This means that the lookup of individual letters will all
# have very small values near 0 -- i.e. the text never contained indivual letters

letter_vals12 = np.dot(RI_letters/N, alice_text_vector2.T)

figure;
bar(arange(len(letter_vals12)), letter_vals12)

ax = gca()

ax.set_xticks(arange(len(letter_vals))+1)
ax.set_xticklabels(list(random_idx.alphabet))


#%%

letter_vals2 = np.zeros(len(random_idx.alphabet)**2)
letter_counts2 = np.zeros(len(random_idx.alphabet)**2)
letter_pairs = []
c = 0

for i, letter1 in enumerate(random_idx.alphabet):
    for j, letter2 in enumerate(random_idx.alphabet):
        
        letter_pairs.append(letter1+letter2)
        
        letter_counts2[c] = text.count(letter_pairs[c])
        
        vector = np.roll(RI_letters[i,:], 1) * RI_letters[j,:]
        
        letter_vals2[c] = np.dot(vector/N, alice_text_vector2.T)
        c+=1

#%%
letter_prob2 = letter_counts2 / sum(letter_counts2)

#%%
figure()

sig_idx = find(letter_vals2 > 0.005)

bar(arange(len(letter_vals2[sig_idx]))+0.15, letter_vals2[sig_idx], width=0.35, color='b')
bar(arange(len(letter_prob2[sig_idx]))+0.5, letter_prob2[sig_idx], width=0.35, color='r')

ax = gca()

ax.set_xticks(arange(len(letter_vals2[sig_idx]))+0.5)

pair_labels = []
for i in sig_idx:
    pair_labels.append(letter_pairs[i])
    
ax.set_xticklabels(pair_labels)


