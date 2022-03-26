### Section 1. Import the film data from wikipedia ###
# Function 1-1. Import Wikipedia Data by name
def wiki_data(a):
    from mediawiki import MediaWiki
    """This function takes 1 parameter, a string.
    This function then returns the content for the wikipedia under this name"""
    wikipedia = MediaWiki()
    text = wikipedia.page(a)
    return text.content
#print(wiki_data('Alice in Wonderland'))

# Function 1-2. Import Movie rating by name
def imdb_rating(a):
    """This function takes 1 parameter, a string.
    This function then returns the rating on IMDB under this name"""
    from imdb import Cinemagoer
    ia = Cinemagoer()
    movie = ia.get_movie(ia.search_movie(a)[0].movieID)
    return(movie['rating'])
#print(imdb_rating('Alice in Wonderland'))

# Function 1-3. Import Movie basic information by name
def imdb_info(a):
    """This function takes 1 parameter, a string.
    This function then returns the genre on IMDB under this name"""
    from imdb import Cinemagoer
    ia = Cinemagoer()
    movie = ia.get_movie(ia.search_movie(a)[0].movieID)
    year = movie['year']
    plot = movie['plot'][0]
    actor1 = movie['cast'][0]
    actor2 = movie['cast'][1]
    actor3 = movie['cast'][2]
    actor4 = movie['cast'][3]
    director1 = movie['director'][0]
    print(f'The movie <{a} ({year})> is directed by {director1}. It is casted by {actor1}, {actor2}, {actor3}, and {actor4}. It tells the story of: {plot}')
# imdb_info('The Batman')

# Function 1-4. Import Movie first n review by name
def imdb_review(a):
    """This function takes 1 parameter, a, a string, the moview name;
    This function then returns the dictionary of first 5 movie reviews, with the rating as key, and content as values"""
    from imdb import Cinemagoer
    ia = Cinemagoer()
    movie_review = ia.get_movie_reviews(ia.search_movie(a)[0].movieID)
    d = dict()
    i = 0
    while i < 5:
        if movie_review['data']['reviews'][i]['rating']:
            rating = movie_review['data']['reviews'][i]['rating']
            review = movie_review['data']['reviews'][i]['content']
            d[rating] = review
        i += 1
    return d
# print(imdb_review('Alice in Wonderland'))

# Function 1-5. Turn first n movie review into 2 string by good/bad rating
def imdb_review_string(a):
    """This function takes 1 parameter, a, a string, the moview name; 
    The breakpoint of rating for good rating and bad rating is defined as the mean of all reviews
    The function will return a list with 2 items, the first item is a string will all good review
    the second is a string with all bad review
    """
    d = imdb_review(a)
    l_good = list()
    l_bad = list()
    l_total = list()
    bp_total = 0
    count = 0
    for key in d:
        if key:
            bp_total = bp_total + key
            count += 1
    bp = bp_total/count
    for key in d:
        if key and key >= bp:
            l_good.extend(d[key].split())
        if key and key < bp:
            l_bad.extend(d[key].split())
    l_total.append(' '.join(l_good))
    l_total.append(' '.join(l_bad))
    return l_total
# imdb_review_string('Alice in Wonderland')

### Section 2. Data Anlysis Function
# Function 2-1. Word Frequencies
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
#freq_dict(['z','z','d','a'])

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

def freq_word(a):
    """This function takes 1 paramter: name, the data source, in string
    The function will return a new dictionary, key is frequency, value is list fo words appear in this frequency
    This function also exclude all the words from stop word list"""
    old_d = freq_dict(text_list(a))
    new_d = dict()
    stop_list= stop_word_list()
    for word in old_d:
        value = old_d[word]
        if value in new_d and word.lower() not in stop_list:
            new_d[value].append(word)
        if value not in new_d and word.lower() not in stop_list:
            new_d[value] = list()
            new_d[value].append(word)
    return new_d
# freq_word(wiki_data('Alice in Wonderland'))

def top_word_print(a,n):
    """This function takes 2 paramter: a, a string;
    n, the top n frequent words to print
    It print the top n frequent word in content and their term frequency"""
    d = freq_word(a)
    total_num = sum(freq_dict(text_list(a)).values())
    count = 0
    order = list(d.keys()).copy()
    order.sort(reverse=True)
    for i in order:
        if count < n:
            for word in d[i]:
                print(f'{i} times, {word}, frequency:{(i/total_num):%}')
            count += len(d[i])
        else:
            break
# top_word_print(wiki_data('Alice in Wonderland'),20)
# top_word_print(imdb_review_string('Alice in Wonderland')[1],20) #This print the top 20 words in bad reviews
# top_word_print(imdb_review_string('Alice in Wonderland')[0],20) #This print the top 20 words in good reviews

# Function 2-2. Word different b/w 2 texts
def top_word_save(a,n):
    """This function takes 2 paramter: a, a string;
    n, the top n frequent words to print
    It save the top n frequent word in content as a list"""
    d = freq_word(a)
    count = 0
    order = list(d.keys()).copy()
    order.sort(reverse=True)
    lst = list()
    for i in order:
        if count < n:
            for word in d[i]:
                lst.append(word)
            count = count + len(d[i])
        else:
            break
    return lst
# top_word_save(wiki_data('Alice in Wonderland'),20)
# top_word_save(imdb_review_string('Alice in Wonderland')[0],10) # Top 10 words for good reviews
# top_word_save(imdb_review_string('Alice in Wonderland')[1],10) # Top 10 words for bad reviews

def word_different(a, b, n):
    """This function idntify the different words between 2 contents' top n words
    The function takes 3 paramters: a and b are strings to analyze, n an integer, specify n top words to review"""
    a_words = top_word_save(a,n)
    b_words = top_word_save(b,n)
    for word in a_words:
        if word not in b_words:
            print(word)
# word_different(imdb_review_string('Alice in Wonderland')[0], imdb_review_string('Alice in Wonderland')[1], 10)
# The above example examine how good review are different from bad
# word_different(imdb_review_string('Alice in Wonderland')[1], imdb_review_string('Alice in Wonderland')[0], 20)
# The above example examine how bad review are different from good

# Function 2-3 Natural Lanaguage Processing
from tkinter import W
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.downloader.download('vader_lexicon')

def NLP_score(a):
    """This function takes a string and return its nltk polarity scores"""
    return SentimentIntensityAnalyzer().polarity_scores(a)
# NLP_score(imdb_review_string('Alice in Wonderland')[0]) # Polarity Score for good review
# NLP_score(imdb_review_string('Alice in Wonderland')[1]) # Polarity Score for bad review
# NLP_score(wiki_data('Alice in Wonderland')) # Polarity Test for Wikipedia

def obtain_compound_movie(a):
    """This function require 1 paramter, a, a string, the name of the movie
    The function then returns its first five reviews' compound polarity scores"""
    d = imdb_review(a)
    list_com = list()
    for key in d:
        com = NLP_score(d[key])
        list_com.append(com['compound'])
    return list_com
# obtain_compound('Alice in Wonderland')

def obtain_rating(a):
    """This function require 1 paramter, a, a string, the name of the movie
    The function then returns its first five ratings"""
    d = imdb_review(a)
    return list(d.keys())
# obtain_rating('Alice in Wonderland')

# Function 2-4 Scatter Plot
def Scatter_plot_review(x,x_name,y,y_name,colo):
    import matplotlib.pyplot as plt
    """This function takes 5 paramter to create a scatter plot:
    x, the x-axis values, a list; y, the y-axis values, a list
    x_name, y_name, strings, are the x and y axies names
    colo, strings to specify which marker to spot the data """
    plt.scatter(x, y, label= type, color = colo)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()
# Scatter_plot_review([1,2],'x-axis',[1,2],'y-axis','green')

def Scatter_plot_movies(a):
    """This function takes 1 paramter, a list of 5 strings, 5 movie names.
    The function will create a plot to map the 5 movies' good reviews' neutral scores and positive scores,
    The same step will be repeated for bad reviews and wikipedia content
    The purpose of this plot is to explore whether the good reviews, bad reviews, and wiki page are positive/negative/neutral across movies"""
    import matplotlib.pyplot as plt
    wiki_pos = list()
    wiki_neu = list()
    good_pos = list()
    good_neu = list()
    bad_pos = list()
    bad_neu = list()
    for movie in a:
        wiki = (wiki_data(movie))
        good = (imdb_review_string(movie)[0])
        bad = (imdb_review_string(movie)[1])
        wiki_pos.append(NLP_score(wiki)['pos'])
        good_pos.append(NLP_score(good)['pos'])
        bad_pos.append(NLP_score(bad)['pos'])
        wiki_neu.append(NLP_score(wiki)['neu'])
        good_neu.append(NLP_score(wiki)['neu'])
        bad_neu.append(NLP_score(wiki)['neu'])
    plt.scatter(wiki_pos, wiki_neu, color = 'black')
    plt.scatter(good_pos,good_neu,color = 'green')
    plt.scatter(bad_pos,bad_neu,color = 'red')
    plt.xlabel('positive score')
    plt.ylabel('neutral score')
    plt.show()
# Scatter_plot_movies(['The Batman','Alice in Wonderland','The Adam Project'])

# Section 3. Example Analysis
def main():
    """These parts of the function provides insights into a specified movie"""
    ### Part 1. This part of the analysis provides you basic information about the movie
    m_name = input('Please enter the name of the movie:')
    imdb_info(m_name)
    print(f'\nThe imdb_rating for this movie is:{imdb_rating(m_name)}.')
    print(f'\nIts wikipedia page identify the following 10 keywords:')
    top_word_print(wiki_data(m_name),10)
    
    ### Part 2. This part of the analysis provides you insights behind its ratings
    print(f'\nIts good reviews all mentions the following unique words:')
    word_different(imdb_review_string(m_name)[0], imdb_review_string(m_name)[1], 20)
    print(f'\nIts bad reviews all mentions the following unique words:')
    word_different(imdb_review_string(m_name)[1], imdb_review_string(m_name)[0], 20)

    """This part of the function explores the relationship b/w rating and its comment"""
    print(f'\n We use the movie <{m_name}> to examine if there is an association relationship between rating and compound score.')
    Scatter_plot_review(obtain_compound_movie(m_name),'compound score',obtain_rating(m_name),'rating','black')
    
    raw_input = input("Please Enter anything to continue: ")
    movie_list = ['The Batman','Alice in Wonderland','Charlie and the Chocolate Factory','Uncharted','The Adam Project']
    print(f'\n We then uses the following 5 movies to examine if the relationship between compound score and neutural score are different for good reviews, bad reviews, and wikipedia for {movie_list}')
    Scatter_plot_movies(movie_list)
    print('Red represents bad review, green represents good review, black represents wiki content')

if __name__ == "__main__":
    main()