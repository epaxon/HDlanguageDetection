#!/usr/bin/python
import subprocess
import re,fileinput

root_dir = "~/Documents/Pentti/language_detection_with_memory/"
			"raw_texts/texts_"
all_texts = [root_dir "afrikaans/digters_uit_Suid_afrika.txt",
	     root_dir "danish/det_hvide_hus.txt",
	     root_dir "dutch/hermaphrodisie_en_uranisme.txt",
	     root_dir "english/AliceInWonderland.txt",
	     root_dir "english/a_christmas_carol.txt", 
	     root_dir "english/hamlet_english.txt",
	     root_dir "english/percy_addleshaw.txt",
	     root_dir "finnish/Finnish-Kivi-7.txt",
	     root_dir "finnish/hamlet_finnish.txt"
	     root_dir "french/les_miserables_tome_I.txt",
	     root_dir "german/freud.txt",
	     root_dir "norwegian/hamsun_markens.txt",
	     root_dir "spanish/tres_comedias_modernas.txt",
	     root_dir "swedish/Swedish-Topelius-Historisk.txt"

	     
]

for file_name in all_texts:
	# remove all whitespace from text
	# however, it's not writing to file
	subprocess.call(["cat", file_name, "|", "tr", "-d", "[:space:]"])
	# converts uppercase to lower case
	subprocess.call("vim", file_name])
	subprocess.call(["gg^guGZZ"])
	# for lines in fileinput.FileInput(file_name, inplace=1):
	#      lines = lines.strip()
	#      lines = re.sub("[A-Z]{2,}",'',lines).replace(" ", " ")
	#      # print lines
	# or do
	# tr '[:upper:]' '[:lower:]' < input
	# however, it's not writing to file
