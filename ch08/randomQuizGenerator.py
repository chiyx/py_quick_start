#! python3

import random

# The quiz data. Keys are states and value are their captitals

captitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahasse',
    'Georgia': 'Altanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Marylan': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing'
}

cLen = len(captitals)
for quizNum in range(cLen):
    # Create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('captitalsquiz_awsers%s.txt' % (quizNum + 1), 'w')
    # Write out the header for the quiz.
    quizFile.write('Name:\n\nData:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (From %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    # Shuffle the order of the states
    states = list(captitals.keys())
    random.shuffle(states)

    