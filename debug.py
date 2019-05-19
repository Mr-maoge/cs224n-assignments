from nltk import data
from nltk.corpus import reuters
import nltk
#设置数据在本地的存储位置
nltk_data_path = "E:\\NLP\\CS224N(2019)\\assignment\\nltk_data"
data.path.append(nltk_data_path)
nltk.download('reuters',"E:\\NLP\\CS224N(2019)\\assignment\\nltk_data")

def read_corpus(category="crude"):
    """ Read files from the specified Reuter's category.
        Params:
            category (string): category name
        Return:
            list of lists, with words from each of the processed files
    """
    files = reuters.fileids(category)
    return [[START_TOKEN] + [w.lower() for w in list(reuters.words(f))] + [END_TOKEN] for f in files]

reuters_corpus = read_corpus()