# Length of the longest supported key (number of strokes).
LONGEST_KEY = 1

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(key):
  assert len(key) <= LONGEST_KEY
  if key[0] == 'TKPW*EURBT':
    return 'git push --set-upstream origin PAT-3478-leave-site-dialog-exceptions'
  raise KeyError

# Optional: return an array of stroke tuples that would translate back
# to <text> (an empty array if not possible).
def reverse_lookup(text):
  return []
