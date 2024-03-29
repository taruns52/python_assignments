# 3. You are given a list of sentences. 
# Create a word tree from each sentence and 
# find how many times the word is appeared in other word trees.

# * Input:
# sentences = [“My name is Ram”, “”He is a good person”, “You should be careful while coding”,
#               “He can do better”, “The person is mysterious”, “Jay Shree Ram”, “It is my pen.”]

# * Output:
# word_trees = [[“My”, “name”, “is”, “Ram”],
#                [“He”, “is”, “a”, “good”, “person”], 
#                 [“You”, “should”, “be”, “careful”, “while”, “coding”], 
#                  [“He”, “can”, “do”, “better”], 
#                   [“The”, “person”, “is”, “mysterious”], 
#                    [“Jay”, “Shree”, “Ram”], 
#                     [“It”, “is”, “my”, “pen”]]

# Number of time each word appears:
# {“My”: 1, “name”: 1, “is”: 4, “Ram”: 2, “He”: 2, “good”: 1, “person”: 2, “You”: 1 ......} Likewise all word should be covered.

import collections


sentences = ["My name is Ram", "He is a good person", "You should be careful while coding",
              "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]

print('\nsentences', sentences, end='\n')

 
# word_list=[ sentence.split(' ') for sentence in sentences]

sentences = " ".join(sentences)
print(sentences)
word_list = sentences.split(" ")
print('\n\nword_list', word_list, '\n\n')

# The argument of counter should be a list but word_list is a list of list , hence used list comprehension to flatten the list 
word_tree = dict(collections.Counter(word_list))


print('Number of time each word appears: \n')
print ('word_tree:', word_tree )