from datetime import datetime

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 2

TEST_EMAIL_KEY = 'TO*EUPL'

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(key):
  assert len(key) <= LONGEST_KEY
  if TEST_EMAIL_KEY != key[0]:
    raise KeyError
  if len(key) > 1:
    number = key[1].removesuffix('-D')
    double = key[1].endswith('-D')
    

  emailBase = f"dev+levi.{datetime.today().strftime('%Y-%m-%d')}"
  return f"{emailBase}{get_number(key)}@qhrtest.com"

def get_number(key):
  if len(key) != 2:
    return '';
  number = key[1].removesuffix('-D')

  if not number.isnumeric():
    raise KeyError
  
  if key[1].endswith('-D'):
    return f'.{number}{number}'
  return f'.{number}'
  

# Optional: return an array of stroke tuples that would translate back
# to <text> (an empty array if not possible).
def reverse_lookup(text):
  return []
