from datetime import datetime

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 1

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(key):
  assert len(key) <= LONGEST_KEY
  if key[0] == 'TPHOUD':
    return datetime.today().strftime('%Y-%m-%d')
  if key[0] == 'TPHOUT':
    return datetime.today().strftime('%H:%M')
  if key[0] == 'TPHOUTD':
    return datetime.today().strftime('%Y-%m-%d-%H:%M')
  raise KeyError

# Optional: return an array of stroke tuples that would translate back
# to <text> (an empty array if not possible).
def reverse_lookup(text):
  return []
