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

## Setup and Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setting Up a Virtual Environment
It's recommended to use a virtual environment to avoid conflicts with other Python projects. Follow these steps:

1. **Create a Virtual Environment**:
   Navigate to the project's root directory in your terminal and run:
   ```bash
   python -m venv venv
   ```
   Activate the Virtual Environment
   ```bash
   source venv/bin/activate
   ```

2. **Installing Dependencies
    With the virtual environment activated, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    
