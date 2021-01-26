#Imports
import math
#Imports
print("Calculator is working")

#Calculator Functions

def Add(x,y):
  sum = x+y
  return sum

def Subtract(x,y):
  difference = x-y
  return difference

def Multiplication(x,y):
  product = x*y
  return product

def Division(x,y):
  try:
    divide = x/y
    return divide
  except Exception as e:
    print(e)

def Sine(angle):
  try:
    sin = math.sin(math.radians(angle))
    return sin
  except Exception as e:
    print(e)

def Cosine(angle):
  try:
    cosine = math.cos(math.radians(angle))
    return cosine
  except Exception as e:
    print(e)

def Tangent(angle):
  try:
    tangent = math.tan(math.radians(angle))
    return tangent
  except Exception as e:
    print(e)

def Log(a,base):
  try:
    log = math.log(a,base)
    return log
  except Exception as e:
    print(e)

def nthTermsAP(startingTerm, numberOfTheTerm, commonDifference):
  try:
    term = startingTerm + (numberOfTheTerm - 1)*commonDifference
    return term
  except Exception as e:
    print(e)

def SumofAP(numberOfTheTerm, startingTerm, commonDifference):
  try:
    sum = numberOfTheTerm/2*(2*startingTerm + (numberOfTheTerm - 1)*commonDifference)

    return sum
  except Exception as e:
    print(e)

def Permutation(n,r):
  try:
    permute = math.factorial(n)/math.factorial(n-r)
    return permute
  except Exception as e:
    print(e)

def Combination(n,r):
  try:
    combinate = math.factorial(n)/math.factorial(r)*math.factorial(n-r)
    return combinate
  except Exception as e:
    print(e)

def PowerRaised(number, power):
  try:
    product = number**power
    return product
  except Exception as e:
    print(e)

def Root(number):
  try:
    root = math.sqrt(number)
    return root
  except Exception as e:
    print(e)

def Percentage(number, percent):
  try:
    percent1 = (number * percent)/100
    return percent1
  except Exception as e:
    print(e)

def Factorial(number):
  try:
    fact = math.factorial(number)
    return fact
  except Exception as e:
    print(e)

def SinInverse(number):
  try:
    inverse = math.asin(number)
    return inverse
  except Exception as e:
    print(e)

def CosInverse(number):
  try:
    inverse = math.acos(number)
    return inverse
  except Exception as e:
    print(e)

def TanInverse(number):
  try:
    inverse = math.atan(number)
    return inverse
  except Exception as e:
    print(e)

#Calculator Functions


#Commands

userInput = int(input('''Input 1 for addition
Input 2 for subtraction
Input 3 for multiplication
Input 4 for division
Input 5 for finding Sin of an angle
Input 6 for finding Cos of an angle
Input 7 for finding Tan of an angle
Input 8 for finding Log
Input 9 for finding the nth term of an AP
Input 10 for finding the sum of an AP
Input 11 for Permutation
Input 12 for Combination
Input 13 for finding the power of a number
Input 14 for finding root of a number
Input 15 for finding the percentage of a number
Input 16 for finding the factorial of a number
Input 17 for finding the sin inverse of a number
Input 18 for finding the cos inverse of a number
input 19 for finding the tan inverse of a number'''))

#Commands

# Input from the user

if(userInput == 1 or userInput == 2 or userInput == 3 or userInput == 4):
  x = int(input("Enter number 1: "))
  y = int(input("Enter number 2: "))

if(userInput == 5 or userInput == 6 or userInput == 7):
  angle = int(input("Enter the value for which you want to find the sin for: "))

if(userInput == 8):
  a = int(input("Tell the number for log"))
  base = int(input("Tell the base to which the logarithm has to be computed"))

if(userInput == 9 or userInput == 10):
  firstTerm = int(input("Enter the first term of the AP"))
  commonDifference = int(input("Enter the common difference of the AP"))
  nthTerm = int(input("Enter the number of the term you are finding"))

if(userInput == 11 or userInput == 12):
  n = int(input("Enter n "))
  r = int(input("Enter r "))

if(userInput == 13):
  number = int(input("Enter the number whom you want to raise"))

  power = int(input("Enter the power to which you want to raise the number to"))

if(userInput == 14):
  number = int(input("Enter the number whom you want to root"))

if(userInput == 15):
  number = int(input("Enter the number"))
  percentage = int(input("Enter the percentage"))

if(userInput == 16 or userInput == 17 or userInput == 18 or userInput == 19):
  number2 = int(input("Enter the number"))
else:
  print("Please enter a valid input")

# Input for the user

# The return statements

if(userInput == 1):
  print("The sum is", Add(x,y))
if(userInput == 2):
  print("The difference is", Subtract(x,y))
if(userInput == 3):
  print("The product is",Multiplication(x,y))
if(userInput == 4):
  print("The answer is", Division(x,y))
if(userInput == 5):
  print("The value is", Sine(angle))
if(userInput == 6):
  print("The value is", Cosine(angle))
if(userInput == 7):
  print("The value is", Tangent(angle))
if(userInput == 8):
  print("The value is", Log(a,base))
if(userInput == 9):
  print("The nth term is", nthTermsAP(firstTerm, nthTerm, commonDifference))
if(userInput == 10):
  print("The sum is", SumofAP(nthTerm, firstTerm, commonDifference))
if(userInput == 11):
  print("The answer is", Permutation(n,r))
if(userInput == 12):
  print("The answer is", Combination(n,r))
if(userInput == 13):
  print("The answer is", PowerRaised(number, power))
if(userInput == 14):
  print("The answer is", Root(number))
if(userInput == 15):
  print("The answer is", Percentage(number,percentage))
if(userInput == 16):
  print("The factorial is", Factorial(number2))
if(userInput == 17):
  print("The sin inverse is", SinInverse(number2))
if(userInput == 18):
  print("The cos inverse is",CosInverse(number2))
if(userInput == 19):
  print("The of tan inverse is", TanInverse(number2))
# The return statements
