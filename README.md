# Pointing System Example 
This is an example to test different techniques to normalize and calculate students' scores from peer surveys. 

## Files
- `data{num}.csv` contains data of student and their grading for diffrerent surveys.
- `ipsatization.py` and `z-trans.py` contains code to perform ipsatization/z-transformation on `data{num}.csv`

## Running the example
To perform ipsatization, run
```
python ipsatization.py data{num}.csv
```
e.g. python ipsazation.py data1.csv

To perform z-transformation, run
```
python z-trans.py data{num}.csv
```
e.g. python z-trans.py data1.csv