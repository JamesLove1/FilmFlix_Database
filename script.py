import sqlite3 

with sqlite3.connect("filmflix.db") as db:
    cursor = db.cursor()
   
    #CRUD
    #Show all rows
    quiry1= cursor.execute("select * from tblFilms")
    for row in quiry1:
        print(row)
    
    #add data
    quiry2 = cursor.execute("insert into tblFilms(filmID, title, yearReleased, rating, duration, genre) values (40, '007 - James Bond', 2023,16, 180, 'Action') ")
    
    #update data
    quiry4 = cursor.execute("update tblFilms SET filmID=39 where filmID = 1;")
    
    #delet data
    quiry3 = cursor.execute("delete from tblFilms where filmID = 39")
    
    #Report
    #1. Print details of all films
    for row in cursor.execute("select * from tblFilms"):
        print(row)
    
    #2. Print all films of a particular genre
    for row in cursor.execute("select * from tblFilms where genre = 'Action'"):
        print(row)
    
    #3. Print all films of a particular year
    for row in cursor.execute("select yearReleased,title from tblFilms where yearReleased = 2014"):
        print(row)
    
    #4. Print all films of a particular rating
    for row in cursor.execute("select rating, genre, title from tblFilms where rating ='PG';"):
        print(row)

    

        
        
        