#%%
def stemload():
    import os
    # os.chdir(os.path.dirname(os.path.realpath(__file__)))
    #getting the required config details
    import configparser
    import pandas as pd
    configs = configparser.ConfigParser()
    configs.read('config.ini')
    configs.sections()

    #pip install mysql-connector-python

    # Assign it to variable
    user = configs['mysql']['user']
    pw=configs['mysql']['passwd']
    port=configs['mysql']['PORT']
    host=configs['DEFAULT']['host']
    pathcsv=configs['DEFAULT']['filepath']
    print(user) # returns: 'peter'

    # configs['MySQL'].get_boolean('log') # returns: True
    # configs['MySQL'].get_int('port') # returns: 4000
    # configs['MySQL'].get_float('port') # returns: 4000.0

    # # Assign the values you want 
    # configs['MySQL']['user']='sam'

    # # Or you can use the `set` method
    # configs.set(section='Postgresql', option='log', value='False')

    # # Write it to the file
    # with open('configurations.ini', 'w') as configfile:
    #     configs.write(configfile)

    import mysql.connector
    from mysql.connector import errorcode

    # try:
    cnx = mysql.connector.connect(user=user,password=pw,host=host,port=port,
                                    database='mysql')
    # except mysql.connector.Error as err:
    #   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #     print("Something is wrong with your user name or password")
    #   elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #     print("Database does not exist")
    #   else:
    #     print(err)
    # else:
    #   cnx.close()

    cursor = cnx.cursor()
    #%%
    query = ("SELECT AlbumId , Title FROM Album "
            "LIMIT 3")

    # cursor.execute(query)
    cursor.execute("CREATE DATABASE IF NOT EXISTS DS_STEM;")
    cnx.reconnect() 
    cursor.execute("USE DS_STEM;")
    cursor.execute("DROP TABLE IF EXISTS salaries ;")
    cursor.execute("CREATE TABLE IF NOT EXISTS `salaries` ( \
    `timestamp` NVARCHAR(40), \
    `company` NVARCHAR(40), \
    `level` NVARCHAR(100), \
    `title` NVARCHAR(40), \
    `totalyearlycompensation` NVARCHAR(40) DEFAULT NULL, \
    `location` text, \
    `yearsofexperience` NVARCHAR(40) DEFAULT NULL, \
    `yearsatcompany` NVARCHAR(40) DEFAULT NULL, \
    `tag` NVARCHAR(100), \
    `basesalary` NVARCHAR(40) DEFAULT NULL, \
    `stockgrantvalue` NVARCHAR(40) DEFAULT NULL, \
    `bonus` NVARCHAR(40) DEFAULT NULL, \
    `gender` NVARCHAR(40), \
    `otherdetails` text, \
    `cityid` NVARCHAR(40) DEFAULT NULL, \
    `dmaid` NVARCHAR(40) DEFAULT NULL, \
    `rowNumber` NVARCHAR(40) DEFAULT NULL, \
    `Masters_Degree` NVARCHAR(40) DEFAULT NULL, \
    `Bachelors_Degree` NVARCHAR(40) DEFAULT NULL, \
    `Doctorate_Degree` NVARCHAR(40) DEFAULT NULL, \
    `Highschool` NVARCHAR(40) DEFAULT NULL, \
    `Some_College` NVARCHAR(40) DEFAULT NULL, \
    `Race_Asian` NVARCHAR(40) DEFAULT NULL, \
    `Race_White` NVARCHAR(40) DEFAULT NULL, \
    `Race_Two_Or_More` NVARCHAR(40) DEFAULT NULL, \
    `Race_Black` NVARCHAR(40) DEFAULT NULL, \
    `Race_Hispanic` NVARCHAR(40) DEFAULT NULL, \
    `Race` NVARCHAR(40), \
    `Education` NVARCHAR(40) \
    ) ")
    #%%
    # for (albumid,title) in cursor:
    #   print(albumid,title)
    cnx.commit()
    # try:
    query = "Select * from salaries;"
    result_dataFrame = pd.read_sql(query,cnx)
    # cnx.close() #close the connection
    # except Exception as e:
        # mydb.close()
        # print(str(e))
    print(result_dataFrame)

    cursor.close()
    cursor=cnx.cursor()
    import csv
    with open(pathcsv,'r',newline='') as csvfile:
        csv_data = csv.reader(csvfile,delimiter=',',quotechar='"')
        next(csv_data)
    # csv_data = csv.reader(file(pathcsv))
        i=0
        for row in csv_data:
            # print(row)
            # i+=1
            # if i==3:
            #     break
            cursor.execute('''INSERT INTO salaries VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', tuple(row))
    #close the connection to the database.
    cnx.commit()
    cursor.close()
    print( "Done")


    try:
        # mydb = connection.connect(host="localhost", database = 'Student',user="root", passwd="root",use_pure=True)
        query = "Select * from salaries;"
        df= pd.read_sql(query,cnx)
        # mydb.close() #close the connection
    except Exception as e:
        # mydb.close()
        print(str(e))
    # print(df.head(10))
    
    cnx.close()
    return df
# %%
