### Section 1. Import the film data from wikipedia ###
# Function 1-1. Import Wikipedia Data by name
def wiki_data(a):
    from mediawiki import MediaWiki
    """This function takes 1 parameter, a string.
    This function then returns the content for the wikipedia under this name"""
    wikipedia = MediaWiki()
    text = wikipedia.page(a)
    return text.content
#wiki_data('Alice in Wonderland')

# Function 1-2. Import Movie rating by name
def imdb_rating(a):
    """This function takes 1 parameter, a string.
    This function then returns the rating on IMDB under this name"""
    from imdb import Cinemagoer
    ia = Cinemagoer()
    movie = ia.get_movie(ia.search_movie(a)[0].movieID)
    return(movie['rating'])
#imdb_rating('Alice in Wonderland')

### Section 2. Data Anlysis
# Analysis 2-1. Word Frequencies
def text_list(a):
    """This function will take a string and break them into list of words"""
    lst = a.split()
    new_list = list()
    for word in lst:
        if '=' in word:
            continue
        else:
            word = word.replace(')',' ')
            word = word.replace('(',' ')
            word = word.replace('.',' ')
            word = word.replace(',',' ')
            word = word.replace('-',' ')
            word = word.replace('"',' ')
            word = word.replace(':',' ')
            word = word.replace('?',' ')
            word = word.strip()
            new_list.append(word)
    return new_list
#text_list(wiki_data('Alice in Wonderland'))

def freq_dict(a):
    """This function takes one parameter, a list.
    Then counts the frequency of each words in the list and return a dictionary: key are words, value are frequencies"""
    d = dict()
    for word in a:
        if word in d:
            d[word] = d[word]+1
        else:
            d[word] = 1
    return d
#freq_list(['z','d','a'])

def stop_word_list():
    """This function read the stop word list and store it into list of strings
    Stop words such as 'a', 'an', 'in' are excluded automatically in the following analysis
    (the list is obtained from Sebleier's open repository)"""
    f = open('text-mining/stopwords.txt')
    words = f.readlines()
    new_list = list()
    for line in words:
        new_list.append(line.strip())
    return new_list
#print(stop_word_list())

def freq_word_wiki(name):
    """This function takes 1 paramter: name, a string, the name to research in wikipedia
    The function will return a new dictionary, key is frequency, value is list fo words appear in this frequency
    This function also exclude all the words from stop word list"""
    old_d = freq_dict(text_list(wiki_data(name)))
    new_d = dict()
    stop_list= stop_word_list()
    for word in old_d:
        value = old_d[word]
        if word in stop_list:
            continue
        else:
            if value in new_d:
                new_d[value].append(word)
            if value not in new_d:
                new_d[value] = list()
                new_d[value].append(word)
    return new_d
# freq_word_wiki('Alice in Wonderland')

# Analysis 2-2. 
