from urllib import request
import nltk
import numpy as np
#nltk.download('punkt') - uncomment this if 'punkt doesn't exist' error, usually necessary if it's your first exposure to toolkit


class ScrapeAndAnalyze(object):


    def url(self):
        """
        :return: targetUrl - full url location of text to be mined
        """
        targetUrl = input("Enter Address")
        return targetUrl


    def accessUrl(self, url):
        """
        :param url: full url of location of text to be mined
        :return response
        """
        #try url
        #if url is good
        response = request.urlopen(url)
        return response


    def contentUrl(self, response):
        """
        :param response: request(urlopen)
        :return fullText: raw text from website
        """
        fullText = response.read().decode('utf8')
        return fullText


    def tokenIzer(self, fullText):
        """
        :param fullText: raw text from website
        :return tokens: tokenized version of raw text
        """
        tokens = nltk.word_tokenize(fullText)
        return tokens


    def uniqueTokens(self, tokens):
        """
        :param tokens: raw list of tokens
        :return unique_tokens: filtered set of unique tokens
        """
        unique_tokens = list(set(tokens))
        print(unique_tokens)
        return unique_tokens


    def topTenTokens(self, tokens):
        """
        :param tokens: list of tokens
        :return topTokens: list of top ten tokens
        """
        tokenCounts = nltk.FreqDist(each.lower() for each in tokens if each.isalpha())
        topTokens = tokenCounts.most_common(10)
        return topTokens

    def topAnyTokens(self, tokens, range):
        """
        :param tokens: list of tokens
        :param range:  range of "top" results, i.e., 5 for top 5 tokens
        :return: topTokens - list of tops tokens
        """
        tokenCounts = nltk.FreqDist(each.lower() for each in tokens if each.isalpha())
        topTokens = tokenCounts.most_common(range)
        return topTokens


    def averageLen(self, tokens):
        """
        :param tokens: raw list of tokens
        :return avg: float of average length of word on page
        """
        lens = [len(x) for x in tokens if x.isalpha()]
        avg = np.mean(lens)
        print(avg)
        return avg

    def wordExist(self, uniques, word):
        """
        :param word: Desired word to check if it exists in the text file
        :return: Boolean if word exists in set
        """
        if word in uniques:
            return True
        else:
            return False
