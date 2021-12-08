
def list_comprehension_exercise_1():
    return [i for i in range(11)]

def list_comprehension_exercise_2():
    return [i for i in range(22) if i % 2 == 0 or i % 3 == 0]

def list_comprehension_exercise_3():
    return [i for i in range(-5, 32) if i % 2 != 0 and i % 5 != 0]

def list_comprehension_exercise_4():
    return [i*i for i in range(11)]

def list_comprehension_exercise_5(sentence):
    sentence = list(sentence)
    return[word for word in sentence if word[0].isupper()]
def list_comprehension_exercise_6(sentence):
    sentence = sentence.split()
    return[word for word in sentence if word[0]=='r' and len(word) >=4]
    
