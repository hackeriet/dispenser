
# Accouting software for the soda dispenser

This project is work-in-progress. Its goal is to allow Hackeriet members to use their NFC cards to dispense soda from the dispenser, and pay for the dispensed consumables from a pre-paid account associated with their card.

### Setting up for development

You need python 3.x installed, preferrably 3.4 or later

After checking out the dispenser software into the directory `dispenser`, you should run
```sh
$ virtualenv -p python3 venv
$ . venv/bin/activate
$ python setup.py develop
```

After that, you can take the implementation for a spin by running `dispensertool`.
```sh
$ python hackeriet/tools/dispensertool.py
```

Testing and smoke-testing will certainly change soon.

