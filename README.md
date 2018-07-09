# Foobar ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

JCOtimer is a Python library package for measuring the time spent for a function to run.

## Installation

### Requirements
* Linux
* Python 3.x

`$ pip install JCOtimer`

## Usage

```python
from JCOtimer.timer import timer

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Development
```
$ virtualenv foobar
$ . foobar/bin/activate
$ pip install -e .
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)