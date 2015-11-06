# corpus_test.py
# experiment to test language identification on fixed corpus

# libraries
import random_idx
from tsne import *
import utils
import sys
import scipy.io as scio
import numpy as np
import glob
import os
from tqdm import trange
import time
import matplotlib.pyplot as plt
import pandas as pd
import string
pd.set_option('precision',2)

# constants
now = time.strftime("%Y-%m-%d %H:%M")
print now
alph = string.lowercase + ' '

# important directories
main_base = os.getcwd()
test_dir = '/lang_texts/test/processed_test'

# parameters
N = 10000 # dimension of random index vectors
k = 5000 # number of + (or -)

cluster_min = 1
cluster_max = int(subprocess.check_output(['tail', '-1', n_gram_size_file])) # size of max letter cluster
ordy = [1]
lang_map = {'af':'afr','bg':'bul','cs':'ces','da':'dan','nl':'nld','de':'deu','en':'eng','et':'est','fi':'fin','fr':'fra','el':'ell','hu':'hun','it':'ita','lv':'lav','lt':'lit','pl':'pol','pt':'por','ro':'ron','sk':'slk','sl':'slv','es':'spa','sv':'swe'}
#lang_map = {'af':'afrikaans','bg':'bulgarian','cs':'czech','da':'danish','nl':'dutch','de':'german','en':'english','et':'estonian','fi':'finnish','fr':'french','el':'greek','hu':'hungarian','it':'italian','pl':'polish','pt':'portuguese','ro':'romanian','sk':'slovak','sl':'slovenian','es':'spanish','sv':'swedish'}
del lang_map['af'] # no afrikaans in test corpus
lang_tots = lang_map.values()
languages = lang_map.values()
#languages = ['french','italian','finnish','estonian']
total_vectors = []


t0 = time.time()
###############################
# generate random indexing for letters, reused throughout
cluster_sizes = xrange(cluster_min,cluster_max+1)
RI_letters = random_idx.generate_letter_id_vectors(N,k)

##############################
# iterate over cluster sizes for language vectors ONLY
# language vectors are the n-grams derived from actual words in the lang_texts
for cluster_sz in cluster_sizes:
  	for ordered in ordy:

    print "~~~~~~~~~~"
    # calculate language vectors
    lang_vectors = random_idx.generate_RI_lang(N, RI_letters, cluster_sz, ordered, languages=languages)
    total_vectors.append(lang_vectors)

    # print cosine angles 
    print '=========='
    if ordered == 0:
    	ord_str = 'unordered!'
    else:
        ord_str = 'ordered!'

    print 'N = ' + str(N) + '; k = ' + str(k) + '; letters clusters are ' + str(cluster_sz) + ', ' + ord_str + '\n'
    cosangles,lbled_lang_vectors = utils.cosangles(lang_vectors, languages)
    variance = utils.var_measure(cosangles)
    print "variance of language values: " + str(utils.var_measure(cosangles))
final_lang = sum(total_vectors)

t1 = time.time()
tt1 = t1- t0
print "time to create " + str(len(languages)) + " language vectors: " + str(tt1)


t0 = time.time()
###############################
# dimension reduction plot to view vectors in 2-d


print '========='
print 'N = ' + str(N) + '; k = ' + str(k) + '; max size letters clusters are ' + str(cluster_max) + '\n'
cosangles, _ = utils.cosangles(final_lang, languages, display=0)
print "variance of language values: " + str(utils.var_measure(cosangles))

# plot language points
fig = plt.figure()
Y = tsne(cosangles,no_dims=2,initial_dims=100,perplexity=8)
plt.scatter(Y[:,0],Y[:,1])#,len(languages),np.r_[1:len(languages)])
for label, x, y in zip(languages, Y[:, 0], Y[:, 1]):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (-2, 2),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        #bbox = dict(boxstyle = 'round,pad=0.5',fc='w'),
        #arrowprops = dict(arrowstyle = '-', 
        #connectionstyle = 'arc3,rad=0.3'),
        fontsize='22')
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([])
plt.savefig(os.getcwd() + '/plots/cosangle_'+ now +'.png')
plt.show()
t1 = time.time()
tt3 = t1 - t0
print "dimension reduction: " + str(tt3)

t0 = time.time()
def find_letter_partner(test_letter, lang_vector):
    # testing letter blocks for their "block partners"
    # block partners like predicting the next letter?
    test_vec = random_idx.id_vector(N,test_letter,alph, RI_letters, ordered=ordered)
    #test_vec = test_vec/np.linalg.norm(test_vec)

    '''
    sub_eng = np.copy(english_vector)
    for r in xrange(len(blocks)):
        block = blocks[r]
        if test_letter != block[0]:
            sub_eng[:, RI_blocks[r,:] != 0] = 1e-2
    print sub_eng
    '''

    cz = len(test_letter)
    #if cz > 1:
    #    for i in xrange(len(alph)):
    #        english_vector -= RI_letters[i,:]
    #english_vector /= np.linalg.norm(english_vector)

    #factored_eng = np.multiply(english_vector, np.roll(letter, 1))
    factored_lang = np.multiply(lang_vector, np.roll(test_vec, 1))
    #factored_eng = np.roll(np.multiply(english_vector, letter), -1)
    #factored_RI_letters = RI_letters, np.roll(letter,1))


    #if len(test_letter) == 1:
    likely_block_partner, values, partners = utils.find_language(test_letter, factored_lang, RI_letters, alph, display=1)
    return likely_block_partner, values, partners

block_list = ['th']
print lbled_lang_vectors[:][1]
lang_vector = np.reshape(lang_vectors[1,:],len(lang_vectors[1,:]),1)

for block in block_list:
    likely_block_partner, values, partners = find_letter_partner(block, lang_vector)

t1 = time.time()
tt4 = t1 - t0
print "finding letter partner time: " + str(tt4)

print "total time of execution: " + str(tt1 + tt2 + tt3 + tt4)
