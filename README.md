# JCOtimer ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

JCOtimer is a Python library package for measuring the time spent for a function to run.

## Installation

### Requirements
* Windows/Linux/OSX
* Python 3.x

`$ pip install JCOtimer`

## Usage

```python
from JCOtimer.timer import timer

@timer #use as decorator
def foo():
   pass

foo() # returns 'Time it took to run the function: 0.3 secs'

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
[Jan Carlo E. Once](https://www.facebook.com/jancarlo.once)