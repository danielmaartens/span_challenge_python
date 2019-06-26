# span_challenge_python #

### League Rank Calculator

This is a command-line application written in `python` that will calculate the ranking table for a
soccer league.

### Requirements

- Python 3

### NOTE:
- Results of your soccer league must be in a file with the following structure
- Please make sure the file ends with the last line of match outcomes, i.e. do not leave any empty lines in the file.

```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```

- You need to know the absolute file path to copy and paste it into the terminal

#### NB:
- This program CANNOT handle tildes (`~`) at the start of the file path. 

### Test and Run 
Before completing the following steps, please make sure you are in the root directory.
``` 
cd path/to/span_challenge_python
```

### Programmatic Execution

Scripts have been provided so that you do not have to focus on any initial setup, besides making sure you have `python 3` installed.

All you have to do is run the following from the project `root`:

##### Options

1 - test and run
``` 
sh test_and_run
```
2 - test
``` 
sh test
```
3 - run
``` 
sh run
```

### Manual Execution
If you rather manually execute in the command line, then run the following commands:


#### run tests
``` 
python3 challenge/tests.py -v
```

#### run program
```
python3 challenge/main.py
```

