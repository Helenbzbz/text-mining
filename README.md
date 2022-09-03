# NLP Project

## 🔑 Project Overview ##
This project aims to achieve the following functions:
* 📤 Automatically return the basic information reagrding one movie and its IMDB rating by inputting the movie name
* 🎐 Analyze the top 10 keywords appear in this movie's wikipedia content page and its frequency.
* 📈 Understand what keywords are unique in good reviews and what are unique in bad reviews
* 📋 Return the association between the NLP compound score and the actual rating -> Does the wording of the movie review associate with the rating❓
* 🗂 Figure out if different types of wording (good review, bad review, wiki content) show different neutral and positive score


## ✅ Implementation ##

I uses the IMDB Movie database and wikipedia database to fullfill the following functions </br>

* Function 1-2 and 1-3 take the name of movie as input and first search for movieID in the IMDB data base by Cinemagoer package. Then corresponding information is obtained by key search in this dictionary obatined from database. Results are formatted to print in a readable manner.

* Function 1-1, wiki data are imported by MediaWiki and only the content part is saved into a string, which is then broken into list of words in fucntion 2-1. Every word in this list is counted. I applied a stopwords list to exclude words with no attitude meaning for text-mining. I also use replace function to remove punctuations. The top 10 frequency words will be printed directly by running this function.

* Function 1-4, the first five reviews are imported and saved into a dictionary, with rating of this review as the key and the comment as the values. In function 1-5, this dictionary turns into a list with only 2 elements: all of the good ratings combined together, all of the bad ratings combined. How to set a break point for good and bad rating? I tried to set a fixed point at 7, while some movies turn out to have very high rating while some movies' ratings are extremelt low. I then turns to look at the relative measure and set the break point always equal to the avergae of all ratings. Besides, there are certain comment without an rating, I filter out rating = None. Function 2-2 is written to print only the unique words in bad or good ratings.

* Function 2-3 first write a general function that calculate NLP score. Then a function to generate compound score for each of the first five valid comments is written, this function takes the movie name, generate the review dictionary. For each item in dictionary, compound score is saved as a list. This compound score list and rating list are visualized by Function 2-4.

* A scatter plot function is written. By entering a list of movie names, it generates the positive and neutral scores for the movie's wikipedia, good review, and bad review. Then, these two scores are plotted and different text types have different colors.

## ☑️ Results ##

Use The Batman as the example, run ```main``` in https://github.com/Helenbzbz/NLP-Project/blob/master/NLP.py <br>
It will return the following texts automatically.

" The movie <The Batman (2022)> is directed by Matt Reeves. It is casted by Robert Pattinson, Zoë Kravitz, Jeffrey Wright, and Colin Farrell. It tells the story of: When the Riddler, a sadistic serial killer, begins murdering key political figures in Gotham, Batman is forced to investigate the city's hidden corruption and question his family's involvement. The imdb_rating for this movie is:8.4.

Its wikipedia page identify the following 10 keywords: 513 times, Batman, frequency:2.824890% 121 times, Bruce, frequency:0.666300% 111 times, Wayne, frequency:0.611233% 84 times, Batman's, frequency:0.462555% 74 times, DC, frequency:0.407489% 69 times, series, frequency:0.379956% 68 times, character, frequency:0.374449% 54 times, Robin, frequency:0.297357% 51 times, Comics, frequency:0.280837% 48 times, Gotham, frequency:0.264317%

Its good reviews all mentions the following unique words: story movie role movies series scene film able maybe aside seen credits people Robert Twilight Batman! looking aware DC ones copy MCU considering overall call surprised rating don't feel lot tone head

Its bad reviews all mentions the following unique words: Selina Colson Penguin murdered bomb informant Thomas City Mitchell Savage car Annika Iceberg Lounge mobster answer learns Alfred kill journalist Nashton Arkham "

* ⏭ The association relationship between rating and compound score [See Output 1 in text-mining folder] There is association between the rating and compound score. This rating seems eponential for The Batman

* 🔝 We then uses the following 5 movies to examine if the relationship between compound score and neutural score are different for good reviews, bad reviews, and wikipedia: ['The Batman', 'Alice in Wonderland', 'Charlie and the Chocolate Factory', 'Uncharted', 'The Adam Project'] [See Output 2 in text-mining folder]

* ⤴️ An interesting finding is that wiki-content has much lower positive score comparing to the bad review.

## 4. Reflection ##

I think most of my idea works out (a working code is a good code). While this code can definitely be more concise but I just don't know where I can make the code more efficient. Besides, the second graph takes 30 more seconds to process and I'm looking for a way to shorten the time. For next project, I should make a sketch first, espcially make the input and output type clear. During this HW, I return back to previous functions very frequently to fix the function thus its output data type can fit into the new functions.
