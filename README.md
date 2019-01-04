# CalCorrupt

## To install and run:
**You must have Python 3.**
You can get it from [python.org](https://www.python.org/)

**You must have [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5) installed.**

Most Linux distributions offer it as a package. It can be installed on Windows and Mac via PIP.

**Running:**

Simply run calcorrupt.py

This can be done with the command *python3*.
For example:

"cd /path/to/script"

"python3 calcorrupt.py"

CalCorrupt is distributed under the GNU GPL-3.0-or-later.

**Features:**
* Choose which bytes to corrupt on an interval.
* Choose starting and ending byte.
* Choose chance of corruption occuring on a byte
* Different types of corruption:
  * Increment
  * Multiply
  * Power (x to the v)
  * Exponent (v to the x)
  * Log
  * Invert (v - x)
  * Bitshift
  * Byteshift (shifting byte order)
  * Randomize
* Length of file in bytes is shown
* Toggle whether corruptions stack (applied successively as opposed to replacing each other)
* Random fuzz value can be added to corruption value