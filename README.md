# CalCorrupt

## To install and run:
**You must have Python 3.**
You can get it from [python.org](https://www.python.org/)

**You must have the Tkinter library installed.**
Many Linux distributions offer it as a package. For more details, see [http://www.tkdocs.com/tutorial/install.html](http://www.tkdocs.com/tutorial/install.html)

**Running:**
Simply run calcorrupt.py

This can be done with the command *python3*.
eg. 
"cd /path/to/script"
"python3 calcorrupt.py"

CalCorrupt is distributed under the GNU GPL-3.0-or-later.

**Features:**
* Choose which bytes to corrupt on an interval.
* Choose starting and ending byte.
* Choose chance of corruption occuring on a byte
* Different types of corruption:
  * Byte increment
  * Bitshift
  * Multiply
  * Power (x to the a)
  * Exponent (a to the x)
  * Log
  * Invert (255-a)
  * Byteshift (shifting byte order)
  * Randomize
* Length of file in bytes is shown