# LearningDutch

Vocabulary learning on apps like duolingo is highly inefficient and impractical for beginners, yet usage by beginners persists. 
Duolingo succeeds because of its User interface and marketing. Therefore, I have decided to leverage 
Quizlet's (Quizlet.com) platform to host the cards I generate, combining multiple readymade resources into a highly efficient 
and easy to use environment. On apps like Anki and Quizlet, there are no existing consistent and well-maintained 
flashcard lists that organise Dutch words by their frequency of usage, therefore I used the information gathered here to
identify the most common words (https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Dutch_wordlist). 

The scripts here can be used to generate quizlet ready CSV's for any language rapidly using only a frequency list available
for many languages on wikitionary.

This is an ongoing project, initially to create CSVs to be used with a 3rd party flashcard application (Quizlet), 
and eventually to develop a tailor made set of applications for learning Dutch that cater to the needs of those wanting 
to rapidly acquire Dutch (or any other language)

The scripts output a CSV that displays in Quizlet as in the images below. For each Dutch word, on the reverse of the 
Flashcard is given:
1. a translation
2. alternative parses for the part-of-speech and their (up to 3) respective translations
3. an example of the sentence

The sentences are generated by OpenAI's GPT-4. Each sentence is formed from using both the study word and 2 words from 
the same study set. In this case I organise study sets into groups of 100, but this is variable in the code.

[![Screenshot-2023-02-06-at-13-31-09.png](https://i.postimg.cc/W3FL2rYp/Screenshot-2023-02-06-at-13-31-09.png)](https://postimg.cc/sQr0mBRb)
[![Screenshot-2023-02-06-at-13-31-02.png](https://i.postimg.cc/hG3RWMr3/Screenshot-2023-02-06-at-13-31-02.png)](https://postimg.cc/mcM57YKQ)
