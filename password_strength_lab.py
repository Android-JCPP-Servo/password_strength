# IMPORT LIBRARIES
import math
import pandas as pd

######################################################
# Steps to Completion:
# 1. Get password from user
# 2. Check what characters are in password
# 3. Return the number of combinations from log2(n^m) calculation
######################################################
def main():
  # Get password from user
  password = input("Please enter the password: ")
  # Pass the password to the alphabet_analyzer function
  size = alphabet_analyzer(password)
  # Pass the size and password to combination_counter for number of combinations
  combinations = combination_counter(size, password)
  print("\tThere are", combinations, "combinations")
  # Pass the number of combinations to bit_counter
  bit_strength = bit_counter(combinations)
  print("\tThat is equivalent to a key of", bit_strength, "bits")
 
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
  for x in password:
    if x in all_caps:
      contains_all_caps = True
    if x in lowercase:
      contains_lowercase = True
    if x in numbers:
      contains_numbers = True
    if x in special_chars:
      contains_special_chars = True
  # If any Booleans are True, add the alphabet size to size
  if contains_all_caps == True:
    size += 26
  if contains_lowercase == True:
    size += 26
  if contains_numbers == True:
    size += 10
  if contains_special_chars == True:
    size += 33
  # Return number of matches
  return size

######################################################
# Calculate Combinations
# To calculate the number of calculations, use the formula 
# (nm), or the alphabet size (n) raised to the power of the 
# password length (m).
######################################################
def combination_counter(size, password):
  # Calculate how many combinations are possible against the password
  combinations = size ** len(password)
  # print("Combinations:", combinations)
  return combinations

######################################################
# Bit Strength
# Your program will next compute the bit strength of a password. 
# This should be accomplished by using the bit strength equation 
# presented in the textbook.
######################################################
def bit_counter(combinations):
  bit_strength = math.log(combinations, 2) # Base is base 2
  bit_strength = math.floor(bit_strength)
  return bit_strength

# Run the program
if __name__ == "__main__":
  main()
