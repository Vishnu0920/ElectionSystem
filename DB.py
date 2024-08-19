import mysql.connector
import tkinter.messagebox

global dbname
global dbuser
global dbpassword

#Change these values as per the mysql details in the machine where it is executed
dbname = "elections"
dbuser = "root"
dbpassword = "a1s2d#"

def CreateTables(db):
    
    ##VOTER DETAILS
    vdetails = "CREATE TABLE v_details ( v_name VARCHAR(100) NOT NULL,\
            v_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY)"

    ##CANDIDATE DETAILS
    cdetails = "CREATE TABLE c_details (\
            c_name VARCHAR(100) NOT NULL,\
            c_post ENUM('HP','SC') NOT NULL,\
            c_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY)"


    ##VOTER RECORDS
    vrec= "CREATE TABLE v_rec ( v_id INT UNSIGNED NOT NULL,\
    HP_id INT UNSIGNED NOT NULL,\
    SC_id INT UNSIGNED NOT NULL)"

    ##SPORTS CAPTAIN'S VOTE COUNT
    scount= "CREATE TABLE s_count (s_cand VARCHAR(100) NOT NULL,\
    votes_sn INT NOT NULL,\
    s_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY)"

    ##HEAD PREFECT VOTE COUNT
    hcount="CREATE TABLE h_count (h_cand VARCHAR(100) NOT NULL,\
    votes_hn INT NOT NULL,\
    h_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY)"

    ##Create all Tables
    mycursor=mydb.cursor()

    mycursor.execute(vdetails) 
    mycursor.execute(cdetails)
    mycursor.execute(vrec)
    mycursor.execute(scount)
    mycursor.execute(hcount)
    print("All Tables Created..")


mydb = mysql.connector.connect(
  host="localhost",
  user=dbuser,
  password=dbpassword
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

dbPresent = False

for x in mycursor:
    if x[0] == dbname :
        dbPresent = True

if dbPresent == False :
    print("DB not prsent, creating new one..")
    mycursor.execute("CREATE DATABASE elections")

    mydb = mysql.connector.connect(
    host="localhost",
    user=dbuser,
    password=dbpassword,
    database=dbname
    )
    
    CreateTables(mydb)
else:
    print("DB already exists")




