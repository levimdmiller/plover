import subprocess

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 1

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(key):
  assert len(key) <= LONGEST_KEY
  if key[0] == 'TPH-FRP':
    set_output('ODAC-revB USB DAC')
    return '{#}'
  if key[0] == 'TP-FRP':
    set_output('Realtek USB2.0 Audio')
    return '{#}'
  raise KeyError

# Optional: return an array of stroke tuples that would translate back
# to <text> (an empty array if not possible).
def reverse_lookup(text):
  return []

def set_output(name):
    subprocess.run('SwitchAudioSource -t output -s \'{}\''.format(name), shell=True)
