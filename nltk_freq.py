import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

def freq_dist(path, out):
    """Write the most common words from each text of the selected path into a file using FreqDist.
    Params:
        path: path with texts to apply freq_dist.
        out: output file.
    """
    my_path = path
    target = open(out, 'w')

    tokenizer = RegexpTokenizer(r'\w+')
    stops = stopwords.words('spanish')

    target.truncate()
    most_common = []
    for dir_name, subdir_list, file_list in os.walk(my_path):
        for fname in file_list:
            with open (my_path + fname, 'r') as myfile:
                data=myfile.read().replace('\n', '')
            all_words = tokenizer.tokenize(data)
            all_words = map(lambda x:x.lower(),all_words)
            filt_words = filter(lambda x: x not in stops, all_words)
            #FreqDist with the 10 most common words
            freq_dist = nltk.FreqDist(filt_words).most_common(10)
            target.write(fname)
            target.write('\n')
            for mc in freq_dist:
                target.write(str(mc))
                target.write(' ')
            target.write('\n')
    target.close()
