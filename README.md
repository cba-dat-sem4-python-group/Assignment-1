Link to mybinder:

https://mybinder.org/v2/gh/cba-dat-sem4-python-group/Assignment-1/master?filepath=Assignment-1.ipynb

# Assignment 1: CLI, Openpyxl and modules

This assignment will make you work with files, command-line and objects.

## How to hand in

The assignment is expected to be published on GitHub, but the actual hand-in should be a link to a MyBinder. See the notebook 12-Assignments if you don't know what that means

## Part 1: Download script

Write a program `download_script.py`, which downloads a set of files from the internet. The files to download are given as arguments to your program on the command-line as illustrated in the following:

`$ python download_script.py http://www.gutenberg.org/files/2701/2701-0.txt http://www.gutenberg.org/cache/epub/27525/pg27525.txt`
  
Downloading file to `./2701-0.txt` 
Downloading file to `./pg27525.txt` 
Reuse your `webget` module from exercises in 07-Functions and Modules.

## Part 2: Reading .xlsx files

Write a program that converts the Excel spreadsheet `./iris_data.xlsx` into a CSV file with the same data.

Start with writing a unit test against which you implement your solution. You are welcome to use a framework for this, but it can also simply be a function that you call with an expected outcome

## Part 3: Creating a module with data

Write a function that reads the `befkbhalderstatkode.csv` file from this url: 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'

The function should return the following `STATISTICS` dictionary:

``` python
STATISTICS = {
      2015: {
          1: {
              0: {
                 5100: 614,
                 5104: 2,
                 5106: 1,
                 ...
              },
              1: {
                  5100: 485,
                  5110: 1,
                  5115, 1,
                  ...
              },
              2: {
                  ...
              },
              ...
          },
          2: {
              ...
          },
          3: {
              ...
          },
          ...
      },
      2014: {
          ...
      },
      ...
  }
  ```
  
To be sure that the code is complete and correct, start with writing a unit test, which iterates over the CSV data and checks that the corresponding data exists in the dictionary. Here is an example

``` python
import kkdata

  f = './befkbhalderstatkode.csv'

  reader = csv.reader(f)
  header_row = next(reader)
  for row in reader:
      data.append(row)
      
      assert kkdata.STATISTICS[row[0]][row[1]][row[2]][row[3]] == [row[4]]
```
      
