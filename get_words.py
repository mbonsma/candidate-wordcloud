def get_words(url, min_len=3, max_len=30):
    """
    This function scrapes the text from a url and returns a list of words without punctuation.
    Words that don't contain any ascii letters are also removed (for example, this removes 
    words written in Inuktitut that are not rendered properly by the WordCloud package).
    
    Inputs:
    url : the url for a website to be scraped
    min_len : the minimum length for words to be included (default 3)
    max_len : the maximum length for words to be included (default 30)
    
    Returns:
    words : a single string with each extracted word separated by a space. This is the format  
        used by the WordCloud package.
    wordlist : a list of extracted words (same as `words`, just different format)
    all_words : every word, including words removed for punctuation and length.
    """
    page = requests.get(url)
    # parse 
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.get_text()
    words = ""
    wordlist = []
    all_words = []
    punctuation = list(string.punctuation)
    punctuation.append('’') # special apostrophe from websites
    punctuation.append('…') # special ellipses from websites
    
    # iterate through the text and extract words
    for line in text.split('\n'):
        if len(line) < 2:
            continue
        for word in line.split(' '):
            #print(word)
            #word = word.strip()
            if word == "":
                continue
            all_words.append(word)
            #print(word)
            if len(word) > max_len:
                continue
            if len(word) < min_len:
                continue
            # get words with an apostrophe, period, or comma
            if "'" in word:
                word_apostrophe = word.split("'")
                word = word_apostrophe[0]
            elif "’" in word:
                word_apostrophe = word.split("’") # fun apostrophe
                word = word_apostrophe[0]
            elif "." in word:
                word_period = word.split(".")
                word = word_period[0]
            elif "," in word:
                word_comma = word.split(",")
                word = word_comma[0]
            # skip words with punctuation
            check = False
            for p in punctuation:
                if p in word:
                    check = True
            if check == True:
                continue
            # skip words that don't have an ascii letter in them
            letter_check = False
            for l in string.ascii_letters:
                if l in word:
                    letter_check = True
                    break
            if letter_check == False:
                continue

            words += " "
            words += word
            wordlist.append(word)
    
    return words, wordlist, all_words