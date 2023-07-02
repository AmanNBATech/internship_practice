
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

print(quiz1['question'])
for option in quiz1['options']:
    print(quiz1['options'][option])

ans = input('Enter the letter corresponding to your answer: ')
if ans.lower() == quiz1['answer']:
    print('Correct')
else:
    print('Wrong')

print(quiz2['question'])
for option in quiz2['options']:
    print(quiz2['options'][option])

ans = input('Enter the letter corresponding to your answer: ')
if ans.lower() == quiz2['answer']:
    print('Correct')
else:
    print('Wrong')
