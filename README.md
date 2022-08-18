# simple-sha256
I recently had to fix a sha256 function and, to better understand how hashing works, wrote this simple Python implementation.  
It's meant to be clean, not to be fast. Input can be UTF-8 or hexadecimal.
  
Usage example:
```
$ ./main.py anything
ee0874170b7f6f32b8c2ac9573c428d35b575270a66b757c2c0185d2bd09718d

$ ./main.py deadbeef hex
5f78c33274e43fa9de5659265c1d917e25c03722dcb0b8d27db8d5feaa813953
```
  
Running tests:
```
$ ./test.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.100s

OK
```
