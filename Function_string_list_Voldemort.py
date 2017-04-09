def get_sentence():
    '''Convert sentence to string list'''
    sentence = input('Enter freely long sentence: ')
    sentence_list = sentence.split()
    return sentence_list

def sentence_title(sentence_list):
    '''Convert word in sentence list to upper'''
    for word in sentence_list:
        if word == 'Voldemort'.lower():
            print('Sam wiesz kto')
        else:
            print(word.title())

data = get_sentence()
sentence_title(data)
