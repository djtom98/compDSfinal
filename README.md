
# compDSfinal
This is our final project for Computing for Data Science course for 2022-2023 BSE Data Science for Decision Making Master Program.


## First steps
### Installation

The source code is currently hosted on GitHub at:
https://github.com/djtom98/compDSfinal


How to install the library
```sh
pip install .
```

### Dependencies

(We need to specify the dependencies)

### Connecting to SQL

Our library uses the MySQL Connector to connect the database in the SQL and load it on Python.
Before run the code you need to edit the `config.ini` file with your `port`, `user` and `password` with your credentials to your SQL server.


## Functions
### Data Processing Functions
+ drop_nan - used to drop rows that contain NaN in a given column;
+ fill_nan_unavailable - fill the NaN of a given column with the value 'Unavailable;

### Feature Creation functions
+ get_dummies - get dummy columns for the values in a specified column
+ time -splits datetime type columns into day, month and year columns
+ cluster - group by specified column to get the median of a target column

### Model Elements
These consist of the model class which takes as input the splitted x and y train datasets, and also incorporates a method to predict the y values based on x_test.

To contribute to your library, please recognize that our main library functions are within the src/learnlibs, and sql database interactions are organized in src/sqldb . Please raise a pull request with your changes, and the developers will review your changes before adding them to the library.
Ensure that any functions you add satisfy the tests we have already built, and if needed, add more tests to the test/ folder to analyse if your particular requirements are met.

## License
...

