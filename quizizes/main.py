import eel
from urllib3 import Retry

questions = [
    [
        'what is this',
        [
            'were',
            'were',
            'were',
            'were'
        ]
    ],

    [
        'what is this',
        [
            'were',
            'were',
            'were',
            'were'
        ]
    ],

    [
        'what is this',
        [
            'were',
            'were',
            'were',
            'were'
        ]
    ]
]


eel.init('web')


@eel.expose
def question():
    return questions[0]


index = 0
@eel.expose
def increaseIndex():
    global index
    index += 1
    print(index)
    return index


eel.start('index.html', size=(1000, 1000))
