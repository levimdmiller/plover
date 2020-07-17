

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 1

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(key):
  assert len(key) <= LONGEST_KEY
  if 'BG' in key[0] and key[0].endswith('DZ'):
    return key[0][:-2] + '/-G'
  raise KeyError

# Optional: return an array of stroke tuples that would translate back
# to <text> (an empty array if not possible).
def reverse_lookup(text):
  return []
