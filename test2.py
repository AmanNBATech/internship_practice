def take_quiz(quiz):
    print(quiz['question'])
    for option in quiz['options'].values():
        print(option)

    ans = input('Enter the letter corresponding to your answer: ')
    if ans.lower() == quiz['answer']:
        return 'Correct'
    else:
        return 'Wrong'

quiz1 = {
    'question': 'What is the capital of Himachal Pradesh?',
    'options': {'a': 'Shimla', 'b': 'Mandi', 'c': 'Kullu', 'd': 'Kangra'},
    'answer': 'a'
}

quiz2 = {
    'question': 'How many states are there in Himachal Pradesh?',
    'options': {'a': '10', 'b': '9', 'c': '12', 'd': '14'},
    'answer': 'c'
}

print(take_quiz(quiz1))
print(take_quiz(quiz2))
