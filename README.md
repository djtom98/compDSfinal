# compDSfinal
This is our final project for Computing for Data Science course for 2022-2023 BSE Data Science for Decision Making Master Program.


## First steps
### Instalation

The source code is currently hosted on GitHub at:
https://github.com/djtom98/compDSfinal


How install the library
```sh
pip install .
```

### Dependencies

(We need to specify the dependencies)

### Conecting to SQL

Our library uses the MySQL Connector to connect the database in the SQL and load it on Python.
Before run the code you need to edit the `config.ini` file with your `port`, `user` and `password` with your credentials to your SQL server.


## Functions
### Data Processing Functions
+ drop_nan - used to drop rows that contain NaN in a given column;
+ fill_nan - fill the NaN of a given column with the mean of values that are not NaN;
+ gen_ohe - generate dummies for the columns selected using one-hot encoding;
+ gen_binary - generate binary dummies for the columns selected (need to add something more);

## License
...
