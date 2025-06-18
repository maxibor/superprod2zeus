# superprod2zeus

Convert [Super Productivity](https://super-productivity.com) Worklog Export to Percentage per Project for [Zeus time tracking](https://www.isgus.de/en/time-attendance/) 

> Make sure to "Group by worklog" when exporting the worklog from [Super Productivity](https://super-productivity.com)

## Install

```bash
pip install git+https://github.com/maxibor/superprod2zeus
```

## Help

```bash
$ superprod2zeus --help
usage: superprod2zeus [-h] [--output OUTPUT] worklog

Convert Superprod worklog file for Zeus input.

positional arguments:
  worklog          Path to the Superprod worklog file

options:
  -h, --help       show this help message and exit
  --output OUTPUT  Path to save the output TSV file
```

## Demo

```bash
$ superprod2zeus --output tests/data/percentage_worklog.tsv tests/data/superprod_worklog.csv 
Output saved to tests/data/percentage_worklog.tsv
```