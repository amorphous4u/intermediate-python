__author__ = 'Amit Verma'

import re

str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et ' \
      'dolore magna aliqua. Dolor sed viverra ipsum nunc aliquet bibendum enim. joradan@test.com ' \
      'In massa tempor nec feugiat. Nunc aliquet bibendum enim facilisis gravida. ' \
      'Nisl nunc mi ipsum faucibus chase@yahoo vitae aliquet nec ullamcorper. Amet luctus venenatis lectus magna fringilla. ' \
      'Volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in. ' \
      'Egestas egestas fringilla phasellus faucibus scelerisque eleifend. tiffany@example.com Sagittis orci a scelerisque purus semper eget duis. ' \
      'Nulla pharetra diam sit amet nisl suscipit. Sed adipiscing diam donec adipiscing tristique risus nec feugiat in. ' \
      'Fusce ut placerat orci nulla. Pharetra vel turpis nunc eget lorem dolor. Tristique senectus et netus et malesuada.'

# match = re.search(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z]+', str)
# if match:
#     print(match.group())

matches = re.findall(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\ .[a-zA-Z]+', str)
for match in matches:
    print(match)