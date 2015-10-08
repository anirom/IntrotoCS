from ps5 import *

#
# Test code
#

def testLoadWords():
    wordlist = loadWords()
    print("Cargando las palabras del archivo...")
    print("  ", len(wordlist), "words loaded.")

def testGetWordScore():
    """
    Unit test for getWordScore
    """
    failure = False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):2, ("was", 7):6, ("love",7):7,("scored", 7):9, ("waybill", 7):65, ("outgnaw", 7):61, ("outgnawn", 8):62}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print("FAILURE: testGetWordScore()")
            print("\tSe esperaban", words[(word, n)], "puntos, pero se obtuvo '" + str(score) + "' para la palabra '" + word + "', n=" + str(n))
            failure = True
    if not failure:
        print("SUCCESS: testGetWordScore()")

testLoadWords()
testGetWordScore()

