import sys
import re
from collections import Counter
file_name = sys.argv[1]  # Get the file name
with open(file_name, 'r') as f:  # Open the file using the context manager
	file_text = f.read()  # Store file text
list_of_words = re.findall('\w+', file_text)  # Find the list of words using appropriate regex
list_of_words = [word.lower() for word in list_of_words]  # Convert words to one case
word_counts = Counter(list_of_words)  # Counter Dictionary containing counts of each word
most_frequent_word = word_counts.most_common(1)  # Find most frequent word
print "Most Frequent Word - %s, Count - %s" %(most_frequent_word[0][0], most_frequent_word[0][1])