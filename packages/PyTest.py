def test(func,value):
  try:
    val = func()
    if val == value:
      return "Test completed. Success"
    else:
      return "Test completed. Failure." + val + " != " + value
  except:
    return "Failed to test"
def testTrue(func):
  try:
    if func == "True" or True:
      return "Test completed. Success"
    else:
      return "Test completed. Failed"
  except:
    return "Failed to test"

def testFalse(func):
  try:
    if func == "False" or False:
      return "Test completed. Success"
    else:
      return "Test completed. Failed"
  except:
    return "Failed to test"
 
