#Extracting links from the relevants tweets
#Now that we extracted the relevant tweets, we want to retrieve links to programming tutorials. 
#We will start by creating a function that uses regular expressions for retrieving link that start 
#This function will return the url if found, 
#otherwise it returns an empty string.


def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


#Next, we will add a column called link to our tweets DataFrame. This column will contain the urls information.

tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

#Next we will create a new DataFrame called tweets_relevant_with_link. 
#This DataFrame is a subset of tweets DataFrame and contains all relevant tweets that have a link.

tweets_relevant = tweets[tweets['relevant'] == True]
tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

#We can now print out all links for python, javascript, and ruby by executing the commands below:

print tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link']
