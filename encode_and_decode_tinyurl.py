#!/usr/bin/python
#Benjamin Wiens
#Encode and Decode Tinyurl
#TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = alphabet.lower()
numbers = "0123456789"
pool = alphabet + alphabet2 + numbers

longurl = "benjaminwiens.com"
shorturl = retrieve = ''
#use inverted dict for better lookup (otherwise loop over entire hashtable)
map = {}
inverted_map = {}

class Codec:
    def encode(self, longurl):
        """

        :param longurl: str
        :return: str
        """
        #get random tinyurl and convert to string
        shorturl = "".join(random.sample(pool, 7))
        #add to dict if we haven't encoded this url yet:
        if longurl not in map:
            map[longurl] = shorturl
            inverted_map[shorturl] = longurl
        #sep req. python 3
        print("Encoded URL is: http://tinyurl.com/",shorturl, sep="")
        return shorturl
    def decode(self, shorturl):
        """

        :param shorturl: str
        :return: str
        """
        retrieve = inverted_map.get(shorturl)
        print("Decoded URL is:", retrieve)
        return retrieve

codec = Codec()
print(codec.decode(codec.encode("reddit.com")))

