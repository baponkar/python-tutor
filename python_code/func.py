'''
Developing Date: 15/05/2024
Developer : Bapon Kar
License : GNU GPL v3.0
Function is defining some process which will return the result with pre defined rules. First 
define it then call it.
There are multiple type functions and they will take multiple input.The function can use as 
many as possible local or global variables.
The function may have another function or it can use another outside function.
In here I also have written the output result side of calling function
'''

#function without any input and without any return value
def func():
  print("This function will just print this line")
  
#call the above function
func() #This function will just print this line
  
#The next function will return default value 'True' without accepting any input
def true_func():
  return True

#call the above function
print(true_func()) #True

#The next function will return either True or False on based of pre defined rule of adult
def adult_func(age):
  '''This function will take age input and return the age is either adult or not'''
  if age >= 18:
    return True
  else:
    return False
  
#call the above function
print(adult_func(37)) #True

  
#The next function will return addition of two numbers
def add_func(a,b):
  return a+b

#call the above function
print(add_func(3,6)) #9

#The next function will create another function and use the function inside of the function
def func_with_func(a,b,c):
  '''This function will return the sum of three numbers if they are in the range between 0 
to 20 otherwise return 0'''
  #inner function
  def check(m):
    '''This function will check if m is in the range 0-20 or not'''
    if m >= 0 and m <= 20:
      return True
    else:
      return False
    
  is_all_input_ok = check(a) and check(b) and check(c)
  
  if is_all_input_ok:
    return add_func(add_func(a,b),c) #using  external add function
  else:
    print("Please check the input")
    return 0
  
#call the above function
print(func_with_func(3,6,4)) #13
  
#function with default input value
def def_inp_func(a=2):
  '''If we call this function then it will take default value of 2 otherwise we can use 
custom value'''
  return a**2
  
#call the above function
print(def_inp_func()) #4
print(def_inp_func(3)) #9
  
#Poositional Arguments
def pos_arg_func(*args):
  print("Positional arguments tuple:", args)
  return None

pos_arg_func(12,"gg",True,54.8) #Positional arguments tuple: (12, 'gg', True, 54.8)

  
#Gather Keyword Arguments with **
def print_kwargs(**kwargs):
  print("Keyword arguments:", kwargs)
  return None

print(print_kwargs(age=24,value=54,string="Kate")) #Keyword arguments: {'age': 24, 'value': 54, 'string': 'Kate'} None
  
#Lambda function
#Lambda function are simple one line function

my_lambda_func = lambda x:x**3+2 #one variable x
lambda_func = lambda x,y:x+y #two variables x,y

print(my_lambda_func(3)) #29
print(lambda_func(2,3)) #5
    
    
    
  
  
