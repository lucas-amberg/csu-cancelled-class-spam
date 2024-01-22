from selenium import webdriver
import names

# This function returns the choice of school that the user selects
def getSchoolChoice():
  print('Welcome to the CSU Cancelled Class spammer')
  print('Currently we have these schools available: ')
  print('San Bernardino (0)')
  availableChoices = ['0'] # Array of correct options
  choice = ''

  # While loop ensures valid selection
  while choice not in availableChoices:
    choice = input('Please input the number of the school you would like to spam (ex for CSUSB pick 0): ')
    if choice not in availableChoices:
      print('Invalid entry, please choose from the available list of universities\n')
  return int(choice)

# This function spams the form from the selected choice
def spamForm(schoolChoice):
  if schoolChoice == 0:
    url = 'https://app.smartsheet.com/b/form/2945d82fd2bc46668b724f4f2e5d87e3'
  
  numOfEntries = input('Please enter the number of entries you would like to do: ')
  driver = webdriver.Chrome()
  driver.get(url)
  for i in range(numOfEntries):
    fakeName = names.get_full_name() # Generates a fake name


if __name__ == '__main__':
  schoolChoice = getSchoolChoice()
  spamForm(schoolChoice)
