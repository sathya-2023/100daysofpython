# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
  # +++your code here+++
    if len(s) >= 3:
        if s.endswith('ing'):
            return s + 'ly'
    return s + 'ing'

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

s = 'This dinner is not that bad!'
def not_bad(s):
    # +++your code here+++
    not_ = s.find('not')
    bad_ = s.find('bad')

    if not_ != -1 and bad_ != -1 and bad_ > not_:
        s = s[:not_] + 'good' + s[bad_ + 3:]
    print(s)
    return s

