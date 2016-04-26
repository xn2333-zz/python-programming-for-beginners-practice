interestings = {'Jeff': 'Is afraid of clowns.', 'David': 'Plays the piano.', 'Jason': 'Can fly an airplane.'
            }
for interesting in interestings:
    print('{0}: {1}'.format(interesting, interestings[interesting]))

interestings['Jeff'] = 'Is afraid of heights.'
interestings['Jill'] = 'Can hula dance.'

for interesting in interestings:
    print('{0}: {1}'.format(interesting, interestings[interesting]))
