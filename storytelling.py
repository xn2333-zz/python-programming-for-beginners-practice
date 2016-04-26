def get_word(word_type):
    if word_type.lower() == 'adjective':
        a_or_an = 'an'
    else:
        a_or_an = 'a'
    return input('Enter a word that is {0} {1}:'.format(a_or_an, word_type))

def fill_in_the_blanks(noun, verb, adjective):
    story = "In this book you will learn how to {1}. It's so easy even a {0} can do it. Trust me, it will be very {2}.".format(noun, verb, adjective)
    return story

def display_story(story):
    print()
    print('Here is the story you created. Enjoy!')
    print()
    print(story)

def create_story():
    noun = get_word('noun')
    verb = get_word('verb')
    adjective = get_word('adjective')

    the_story = fill_in_the_blanks(noun, verb, adjective)
    display_story(the_story)

create_story()

    
    
    
