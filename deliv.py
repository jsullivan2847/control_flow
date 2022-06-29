# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 


# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':


# 1 & 2 below 

# vowels = ['a','e','i','o','u']
# letter = ''
# while letter != 'quit':
#   letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
#   if letter in vowels:
#     print(f'You entered {letter}, which IS a vowel')
#   elif letter == 'quit':
#     print('game over')
#   elif letter not in vowels:
#     print(f'You entered {letter} which is NOT a vowel')















# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

# word = ''
# while word != 'quit':
#   word = input('Enter a 3 letter word: ').lower()
#   if(word == 'quit'):
#     print('game over')
#   elif(len(word) == 3):
#     print(f'You entered "{word}" a {len(word)} letter word. Nice!')
#   elif(len(word) > 3):
#     difference = len(word) - 3
#     print(f'''
#     You entered "{word}", a {len(word)} letter word. 
#     It was {difference} characters too long. :((''')












# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

# years = int(input('Enter your dog''s age: '))
# each_year = list(range(years))
# for year in each_year:
#   if(each_year[year] < 2):
#     each_year[year] = 10
#   elif(each_year[year] <= len(each_year)):
#     each_year[year] = 7
# dog_years = sum(each_year)

# print(dog_years)










# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle




# print('Enter 3 lengths for the three sides of a triangle, seperated by commas: ')
# a = int(input('side A: '))
# b = int(input('side B: '))
# c = int(input('side C: '))

# if a == b and b == c:
#   print('equalateral')
# elif a!=b and a!=c and b!=c:
#   print('scalene')
# else: 
#   print('isosceles')






















# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it




# term = 0
# number = 0
# a = 0
# b = 1

# while term < 50:
#   if term < 1:
#     print(term, number)
#   else: 
#     number = a + b
#     print(term,number)
#     a = b 
#     b = number
#   term += 1






# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 


from virtualenv import session_via_cli


month = input('Enter the month in three characters (Jan, Feb, Mar, ect...)').lower()
day = int(input('Enter the day as a number 1-31 (Mon, Tue, Wed, ect...)'))

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
winter = ['jan', 'feb', 'mar']
spring = ['apr', 'may', 'june']
summer = ['july', 'aug', 'sep']

if(month in months and day < 32):
  if month in winter:
    season = 'Winter'
  elif month in spring:
    season = 'Spring'
  elif month in summer:
    season = 'Summer'
  else:
    season = 'Fall'
  if month == 'dec' and day > 20:
    season = 'Winter'
  elif month == 'mar' and day > 19:
    season = 'Spring'
  elif month == 'jun' and day > 20:
    season = 'Summer'
  elif month == 'sep' and day > 20:
    season = 'Fall'
  if day < 10:
    day = f'0{day}'
  month = month[0].upper() + month[1] + month[2]
  print(f'{month} {day} is in {season}')

 



# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.




















# color = ''
# while color != 'quit':
#     color = input('Enter "green", "yellow", "red": ').lower()
#     print(f'The user entered {color}')
#     if color == 'green':
#         print('Go!')
#     elif color == 'yellow':
#         print('Slow Down!')
#     elif color == 'red':
#         print('Stop!')
#     elif color == "quit":
#         print('ok you''re done')



# nums = list(range(10))
# print(nums)
# odds = tuple(range(1, 10, 2))
# print(odds)




#in python an array is called a list 

# names = ["Tom", "Deborah", "Murray", "Axel"]

# age = 53

# while age < 60:
#     age += 1
#     print(age)

# # name refers to each individual name in the list 
# for name in names:
#   print(name)



