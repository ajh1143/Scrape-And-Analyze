# Scrape And Analyze
Class of tools for language analysis of URL content
________________________________________________________________________________________________________________________________________
## Imports
```Python3
from urllib import request
import nltk
import numpy as np
#nltk.download('punkt')
```

________________________________________________________________________________________________________________________________________
## Class

```Python3
class ScrapeAndAnalyze(object):
```

________________________________________________________________________________________________________________________________________
## Get URL - Location of text file / page to be scraped

```Python3
    def url(self):
        """
        :return: targetUrl - full url location of text to be mined
        """
        targetUrl = input("Enter Address")
        return targetUrl
```

________________________________________________________________________________________________________________________________________
## Make Request to URL

```Python3
    def accessUrl(self, url):
        """
        :param url: full url of location of text to be mined
        :return response
        """
        #try url
        #if url is good
        response = request.urlopen(url)
        return response
```

________________________________________________________________________________________________________________________________________
## Get Content From URL

```Python3
    def contentUrl(self, response):
        """
        :param response: request(urlopen)
        :return fullText: raw text from website
        """
        fullText = response.read().decode('utf8')
        return fullText
```

________________________________________________________________________________________________________________________________________
## Tokenize Requested Content

```Python3
    def tokenIzer(self, fullText):
        """
        :param fullText: raw text from website
        :return tokens: tokenized version of raw text
        """
        tokens = nltk.word_tokenize(fullText)
        return tokens
```
________________________________________________________________________________________________________________________________________

## Generate List of Unique Tokens

```Python3
    def uniqueTokens(self, tokens):
        """
        :param tokens: raw list of tokens
        :return unique_tokens: filtered set of unique tokens
        """
        unique_tokens = list(set(tokens))
        print(unique_tokens)
        return unique_tokens
```

________________________________________________________________________________________________________________________________________
## Generate List Of Top 10 Most Frequent Words

```Python3
    def topTenTokens(self, tokens):
        """
        :param tokens: list of tokens
        :return topTokens: list of top ten tokens
        """
        tokenCounts = nltk.FreqDist(each.lower() for each in tokens if each.isalpha())
        topTokens = tokenCounts.most_common(10)
        return topTokens
```

________________________________________________________________________________________________________________________________________

## Generate List of Top N Most Frequent Words

```Python3
    def topAnyTokens(self, tokens, range):
        """
        :param tokens: list of tokens
        :param range:  range of "top" results, i.e., 5 for top 5 tokens
        :return: topTokens - list of tops tokens
        """
        tokenCounts = nltk.FreqDist(each.lower() for each in tokens if each.isalpha())
        topTokens = tokenCounts.most_common(range)
        return topTokens
```


## Generate List of 10 Least Frequent Words
```Python3
    def lowTenTokens(self, tokens):
        """
        :param tokens: list of tokens
        :return topTokens: list of 10 least common tokens
        """
        tokenCounts = nltk.FreqDist(each.lower() for each in tokens if each.isalpha())
        lowTokens = tokenCounts.most_common()[-10:]
        return lowTokens
```

________________________________________________________________________________________________________________________________________

## Find Average Length of Words in Content

```Python3
    def averageLen(self, tokens):
        """
        :param tokens: raw list of tokens
        :return avg: float of average length of word on page
        """
        lens = [len(x) for x in tokens if x.isalpha()]
        avg = np.mean(lens)
        print(avg)
        return avg
```
________________________________________________________________________________________________________________________________________

## Check If Specific Word Exists 

```Python3
    def wordExist(self, uniques, word):
        """
        :param word: Desired word to check if it exists in the text file
        :return: Boolean if word exists in set
        """
        if word in uniques:
            return True
        else:
            return False
```
