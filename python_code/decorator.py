"""
The decorator function will update a function without changing source function.
"""

def add(a,b):
  """
  This function return the values after addition of a and b
  """
  return a+b

#Now writing decorator function which will update the add funcyion
def update(func):
  """This function will update old function into desired new_func."""
  def new_func(*args, **kwargs):
    """
    This function will return the old result along with some additional data
    """
    print("Old function:", func.__name__)
    print("Positional arguments:",args)
    print("Keyword arguments:",kwargs)
    
    result = func(*args,**kwargs)
    print("The old function result:",result)
    return result
  return new_func

#creating a updated function from add function
updated_add = update(add)
#now print the result from old function
print(add(5,6))
#now print the result from updated_add function
print(updated_add(5,6))
