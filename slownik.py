information = {
  'jakubmanczak': {
    'name': 'Jakub',
    'surname': 'Mańczak',
    'status': 0,
    'age': 17,
    'birthdate': '2004-08-28'
  },
  'wilhelmzwei': {
    'name': 'Wilhelm',
    'surname': 'Hohenzollern',
    'status': 1,
    'age': 82,
    'birthdate': '1859-01-27',
    'title': 'Kaiser',
    'occupation': 'Royalty'
  },
  'booth': {
    'name': 'John',
    'surname': 'Wilkes-Booth',
    'status': 1,
    'age': 26,
    'birthdate': '1838-05-10',
    'occupation': 'Actor',
  },
  'jaruzel': {
    'name': 'Wojciech',
    'surname': 'Jaruzelski',
    'status': 2,
    'age': 90,
    'birthdate': '1923-07-06',
    'title': 'Generał',
    'occupation': 'General'
  }
}

statusDict = {
  0: 'alive',
  1: 'dead',
  2: 'recently deceased'
}

for key, value in information.items():
  print('username: ', key)
  print('-------------')
  for itemkey, itemvalue in value.items():
    if(itemkey != 'status'):
      print(itemkey, ': ', itemvalue)
    else:
      if itemvalue == 1:
        print(itemkey, ': ', 'dead')
      elif itemvalue == 2:
        print(itemkey, ': ', 'recently deceased')
      else:
        print(itemkey, ': ', 'alive')
  print()
  print()