import curses, locale, sys, traceback

# Gets system's default encoding for non-ASCII chars; "code" is then used for str.encode() calls
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

"""
This is a documentation comment.
"""


# -- Key Bindings --
#
# Enter = switch between command/edit mode
# CTRL-D = quit
#
#  - Command Mode -
# 
# l = new line
# p = paragraph break
# q = quote
# s = save (prompt for directory and file to output if no file argv given at runtime)
# T = title (center, bold, increase font-size)
# t = subtitle
#
# - Editing Mode -
#
# Tab = Indent four spaces
# 

# curses.textpad()
# User enters command mode; make this toggleable at a later point?
# User 

# if 