def get_sentence():
    sentence = input('Enter freely long sentence: ')
    sentence_list = sentence.split()
    return sentence_list

def sentence_title(sentence_list):
    for word in sentence_list:
        if word.lower() == 'voldemort':
            print('Sam wiesz kto')
        else:
            print(word.title())

data = get_sentence()
sentence_title(data)
