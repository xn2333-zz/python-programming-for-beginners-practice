def display_interestings(interestings):
    for interesting in interestings:
        print('{}: {}'.format(interesting, interestings[interesting]))
    print()

interestings = {
    'Jason': 'Can fly an airplane.',
    'Jeff': 'Is afraid of clowns.',
    'Davis': 'Plays the piano.'
}

display_interestings(interestings)

interestings['Jeff'] = 'Is afraid of heights.'
interestings['Jill'] = 'Can hula dance.'

display_interestings(interestings)


    
    
    
