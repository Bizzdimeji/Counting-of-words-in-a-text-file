# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as file:
        contents = file.read()
    return contents


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text= text.lower()
    text = text.split()
    text= [word.strip(".,?") for word in text]

    new_words= []
    for word in text:
        if word not in new_words:
            new_words.append(word)

    dic= {}
    for word in new_words:
        count= text.count(word)
        dic.update({word:count})
    return dic

print(count_words())