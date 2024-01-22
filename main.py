import selenium

def getSchoolChoice():
  print('Welcome to the CSU Cancelled Class spammer')
  print('Currently we have these schools available: ')
  print('San Bernardino (0)')
  availableChoices = ['0']
  choice = ''
  while choice not in availableChoices:
    choice = input('Please input the number of the school you would like to spam (ex for CSUSB pick 0): ')
    if choice not in availableChoices:
      print('Invalid entry, please choose from the available list of universities\n')
  return choice

if __name__ == '__main__':
  schoolChoice = getSchoolChoice()