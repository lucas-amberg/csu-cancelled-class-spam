from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import names
import time

fake_class_codes = [
    'CIS317', 'MTH424', 'MTH397', 'BIO155', 'ENG285', 'HIS310', 'MTH471', 'PSY456', 
    'ENG270', 'MTH165', 'HIS167', 'ENG451', 'PSY316', 'CIS348', 'ENG180', 'MTH257', 
    'CIS446', 'BIO200', 'CIS306', 'MTH234', 'HIS367', 'ENG370', 'MTH302', 'BIO178', 
    'CIS445', 'PSY204', 'MTH442', 'ENG281', 'BIO185', 'CIS402', 'ENG199', 'PSY395', 
    'ENG256', 'PSY429', 'ENG158', 'MTH129', 'BIO166', 'ENG289', 'CIS319', 'ENG155', 
    'PSY324', 'HIS120', 'PSY231', 'MTH404', 'HIS431', 'BIO194', 'CIS371', 'ENG338', 
    'PSY371', 'ENG476', 'CIS398', 'MTH170', 'ENG445', 'CIS214', 'ENG153', 'BIO463', 
    'PSY141', 'ENG278', 'HIS353', 'MTH381', 'ENG268', 'PSY268', 'CIS200', 'MTH114', 
    'CIS479', 'ENG127', 'ENG302', 'PSY131', 'CIS149', 'BIO282', 'PSY443', 'HIS377', 
    'ENG246', 'CIS156', 'PSY318', 'MTH197', 'ENG130', 'MTH448', 'ENG306', 'PSY117', 
    'HIS230', 'MTH119', 'PSY423', 'ENG418', 'HIS146', 'CIS305', 'CIS490', 'MTH363', 
    'BIO361', 'PSY150', 'HIS163', 'ENG232', 'ENG136', 'ENG476', 'CIS360', 'MTH214', 
    'PSY457', 'ENG275', 'PSY282', 'CIS403', 'BIO358', 'ENG109', 'ENG485', 'MTH421'
]

fake_time_minutes = ['00', '15', '30', '45']
email_sites = ['gmail', 'yahoo', 'msn', 'aol']
key_choice = ['.', '', '_']

# This function returns the choice of school that the user selects
def get_school_choice():
  print('Welcome to the CSU Cancelled Class spammer')
  print('Currently we have these schools available: ')
  print('San Bernardino (0)')
  print('Fullerton (1)')
  available_choices = ['0', '1'] # Array of correct options
  choice = ''

  # While loop ensures valid selection
  while choice not in available_choices:
    choice = input('Please input the number of the school you would like to spam (ex for CSUSB pick 0): ')
    if choice not in available_choices:
      print('Invalid entry, please choose from the available list of universities\n')
  return int(choice)

# This function spams the form from the selected choice
def spam_form(school_choice):
  if school_choice == 0: # CSUSB
    url = 'https://app.smartsheet.com/b/form/2945d82fd2bc46668b724f4f2e5d87e3'
  elif school_choice == 1: # CSUF
    url = 'https://app.smartsheet.com/b/form/758f260d8d114de5bb2ba5877dfe2042'
  
  num_of_entries = input('Please enter the number of entries you would like to do: ')
  driver = webdriver.Chrome()
  
  for i in range(int(num_of_entries)):
    driver.get(url)
    fake_name = names.get_full_name() # Generates a fake name
    name_box = driver.find_element(By.ID, 'text_box_Instructor/Coach/Counselor/Librarian')
    name_box.send_keys(fake_name) # Sends fake name to form

    random_key = random.randint(0, 99)
    fake_class = fake_class_codes[random_key] # Selects a random fake class name to submit
    class_box = driver.find_element(By.ID, 'text_box_Class/Student Service')
    class_box.send_keys(fake_class)

    fake_date = '01/' + str(random.randint(22,26)) + '/24' # Creates a fake date between the days of the strike
    date_box = driver.find_element(By.ID, 'date_Date of Class or Service')
    date_box.send_keys(fake_date)

    fake_time = str(random.randint(1,12)) + ':' + fake_time_minutes[random.randint(0,3)] # Creates a random time
    time_box = driver.find_element(By.ID, 'text_box_Time of Class or Service')
    time_box.send_keys(fake_time)

    # Create a fake alias for the form submission
    user_first_name = names.get_first_name()
    user_last_name = names.get_last_name()

    # Create a fake name and email
    full_name = user_first_name + ' ' + user_last_name
    email = str(random.randint(0,99)) + user_first_name + key_choice[random.randint(0,2)] + user_last_name + str(random.randint(0,2324)) + '@' + email_sites[random.randint(0,3)] + '.com'
    
    # Append the fake name and email to the bottom of the form
    submitter_name_box = driver.find_element(By.ID, 'text_box_Submitter\'s Name')
    submitter_name_box.send_keys(full_name)
    submitter_email_box = driver.find_element(By.ID, 'text_box_Submitter\'s Email')
    submitter_email_box.send_keys(email)

    time.sleep(1)

    form_element = driver.find_element(By.CSS_SELECTOR, 'form')
    form_element.submit()

    print(f'Completed Submission #{i+1} with Name: {fake_name} and Class: {fake_class}')
    time.sleep(3)

  input('Press enter to continue...')


if __name__ == '__main__':
  school_choice = get_school_choice()
  spam_form(school_choice)
