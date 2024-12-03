# Proposal

## What will (likely) be the title of your project?

Using Sentiment Analysis to Determine Tones of New York Times Columnists

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

This project will use sentiment analysis to create a database of NYT writers' tones.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

The project will take in a NYT article as a .txt file, and then use the NLTK Sentiment Analysis library in Python to give each article a value for tone. The article will be chopped into individual sentences and processed like that. While this may present some flaws by removing context, it provides a simpler and more standardized way of digesting the article for our purposes. Using 1 for positive and 0 for negative, we can assign each article a value.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

n/a

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

n/a

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

Given an article, the project can determine and assign a value for the tone of the piece (positive or negative).

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

The project can do the above and then take input from multiple articles of a single author.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

The project can do all of the above, but can randomly select articles from several authors, creating a file containing data of authors chosen prior.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

The main skills I will need to learn are the methods for sentiment analysis using NTLK. The process of taking in the article itself should not be an issue, as it should be relatively simple to chop up the article into sentences and then assign the sentence values. I will need research methods for sentiment analysis through NTLK. 
