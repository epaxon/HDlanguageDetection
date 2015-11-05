import subprocess
import tempfile
root_dir = "~/Documents/Pentti/language_detection_with_memory/"
			"raw_texts/texts_"
all_texts = [root_dir "afrikaans/digters_uit_Suid_afrika.txt",
			root_dir "dutch/hermaphrodisie_en_uranisme.txt",
			root_dir "finnish/Finnish-Kivi-7.txt",
			root_dir "finnish/hamlet_finnish.txt"
]
cmd = 'ffmpeg -i %s 2>&1 | grep "Duration" | cut -d \' \' -f 4 | sed s/,//' % ("Video.mov")
duration = os.system(cmd)
print duration

import subprocess
proc=subprocess.Popen('echo "to stdout"', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
print output
