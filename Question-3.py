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

sentences = ["My name is Ram", "He is a good person", "You should be careful while coding",
              "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]

print('\nsentences', sentences, end='\n')

word_list=[]    
    
for sentence in sentences:
    sentence = sentence.split(' ')
    word_list.append(sentence)
print('\n\nword_list', word_list, '\n\n')

word_tree = {}

for lst in word_list:
    for word in lst:
        if word not in word_tree:
            word_tree[word] = 1
        else:
            word_tree[word] += 1

print ('word_tree:', word_tree )