#! /usr/bin/env python

import sys
from sha256 import sha256

if len(sys.argv) < 2:
  print(f"Usage: {sys.argv[0]} <input> [hex]", file=sys.stderr)
  sys.exit(1)
  
input = sys.argv[1]

is_hex = False
if len(sys.argv) >= 3:
	is_hex = sys.argv[2].lower() == "hex"
 
result = sha256(input, is_hex)
print(result)