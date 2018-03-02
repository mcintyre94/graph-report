# graph-report

A script for rewriting RAGE brief reports to contain the graph that they link to. 

## Prerequisites: Firefox, Geckodriver
This script uses [ragelib](https://code.citrite.net/users/callumiandam/repos/ragelib), which uses Selenium to fetch and render RAGE pages. Communication between Selenium and Firefox is performed using geckodriver. You must have Firefox installed, and a release of geckodriver for your platform downloaded from https://github.com/mozilla/geckodriver/releases.

Recommended locations for the geckodriver binary are `C:\dev\geckodriver.exe` on Windows or `/usr/local/bin/geckodriver` on Linux/OS X.

## Installation
The suggested installation method is using pip/pipenv to handle this.

You need Python 3.6+ with pip installed.

### System wide
```
pip install -r requirements.txt
pip install .
```

### In a virtual env
The suggested approach is using pipenv (`pip install pipenv`):
```
pipenv install
pipenv shell
pip install .
```

## Usage
```
$ graph-report --help
usage: graph-report [-h] [--geckodriver-path GECKODRIVER_PATH]
                    [--outfile OUTFILE] [-v] [-d]
                    file

Extract graphs from a RAGE brief report using headless firefox (geckodriver).
You should get the latest geckodriver release from
https://github.com/mozilla/geckodriver/releases.

positional arguments:
  file                  A report file to extract graphs for

optional arguments:
  -h, --help            show this help message and exit
  --geckodriver-path GECKODRIVER_PATH
                        The geckodriver path to use (default:
                        C:\dev\geckodriver.exe, or /usr/local/bin/geckodriver)
  --outfile OUTFILE     File to write the results to (default: output.html)
  -v, --verbose         Enable verbose logging
  -d, --debug           Enable debug logging
```

If your `geckodriver` is in one of the recommended paths, simply running `graph-report my-report.html` will generate `output.html` containing the data rows and rendered graphs.

Use `--geckodriver-path` if your `geckodriver` is in a different location, and `--outfile` to save the rewritten report to a different location.