###########################
# Steps to Completion:
# 1. Get password from user
# 2. Check what characters are in password
# 3. Return the number of combinations from log2(n^m) calculation
###########################
def main():
  # Get password from user
  password = input("Please enter the password: ")
  # Pass the password to the alphabet_analyzer function
  size = alphabet_analyzer(password)
  print("Alphabet size:", size)
 
# Check what kinds of characters are in the password
def alphabet_analyzer(password):
  # Set all allowed characters for examination
  all_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  lowercase = 'abcdefghijklmnopqrstuvwxyz'
  numbers = '0123456789'
  special_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
  # Set Booleans to determine if allowed characters are found
  contains_all_caps = False
  contains_lowercase = False
  contains_numbers = False
  contains_special_chars = False
  # Set initial count of possible characters
  size = 0
  # TODO: Compare password to all allowed characters
  
  # Return number of matches
  return size

# Run the program
if __name__ == "__main__":
  main()
