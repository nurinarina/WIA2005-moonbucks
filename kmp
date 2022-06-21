from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer


def stem_sentence(sentence):
    porter = PorterStemmer()
    porter.stem(sentence)
    token_words = word_tokenize(sentence)
    token_words
    stemmed_sentence = []
    for word in token_words:
        stemmed_sentence.append(porter.stem(word))
        stemmed_sentence.append(" ")
    # print ("".join(stem.sentence)+'\n')
    return "".join(stem_sentence)


# Place to put article
document1 = open(
    'test.txt', 'r').readlines()
document2 = open(
    'test1.txt', 'r').readlines()

# Remove / and .
modify = document1
final1 = []
for i in modify:
    t = i.split('.')
for i in t:
    final1.append(i)

for i in range(0, final1.count(' \n')):
    final1.remove(' \n')
for i in range(0, final1.count('\n')):
    final1.remove('\n')

modify = document2
final2 = []
for i in modify:
    t = i.split('.')
    for i in t:
        final2.append(i)

for i in range(0, final2.count(' \n')):
    final2.remove(' \n')
for i in range(0, final2.count('\n')):
    final2.remove('\n')


def remove_common_words_stemming(main, generic):
    finalized = []
    for q in main:
        # Print
        query = q
        stopwords = generic
        query_words = query.split()

        result_words = [word for word in query_words if word.lower() not in stopwords]
        result = ' '.join(result_words)
        finalized.append(stem_sentence(result))
    # Print(finalized)
    return finalized


# Print(final)
common_word_list = ['do', 'she', 'they', 'we',
                    'are', 'is', 'a', 'an', 'in', 'as', 'in', 'of']
document1 = remove_common_words_stemming(final1, common_word_list)
document2 = remove_common_words_stemming(final2, common_word_list)


def get_prefix_table(needle):
    prefix_set = set()
    n = len(needle)
    prefix_table = [0] * n
    delimiter = 1
    while delimiter < n:
        prefix_set.add(needle[:delimiter])
        j = 1
        while j < delimiter + 1:
            if needle[j:delimiter + 1] in prefix_set:
                prefix_table[delimiter] = delimiter - j + 1
                break
            j += 1
        delimiter += 1
    return prefix_table


def new_string(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    if (needle_len > haystack_len) or (not haystack_len) or (not needle_len):
        return -1
    prefix_table = get_prefix_table(needle)
    m = i = 0
    while (i < needle_len) and (m < haystack_len):
        if haystack[m] == needle[i]:
            i += 1
            m += 1
        else:
            if i != 0:
                i = prefix_table[i - 1]
            else:
                m += 1
    if i == needle_len and haystack[m - 1] == needle[i - 1]:
        return m - needle_len
    else:
        return -1


count = 0
document2_joined = ".".join(document2)

for i in document1:
    check = 0
    check = (new_string(document2_joined, i))
    if check > 0:
        count = count + 1

print("the matches are " + str(count))
print("\n The rate of plagiarism is " + str((2 * count) / (len(document1) + len(document2))))
