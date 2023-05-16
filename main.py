import sqlite3 

with sqlite3.connect("filmflix.db") as db:
    cursor = db.cursor()
   
    #CRUD
    #Show all rows
    print("All Database Files")
    quiry1= cursor.execute("select * from tblFilms")
    for row in quiry1:
        print(row)
    
    #add data
    print("\nAdd Data")
    filmID = int(input("ID number is unique. Cant enter the same ID number twice:  "))
    title = input("Enter tile of film: ")
    yearReleased = int(input("Year released: "))
    rating = int(input("Rating: "))
    duration = int(input("Lenght in mins: "))
    genre = input("Genre: ")
  
    quiry2 = cursor.execute(f"insert into tblFilms(filmID, title, yearReleased, rating, duration, genre) values ({filmID}, '{title}', {yearReleased},{rating}, {duration}, '{genre}')")
    db.commit
    
    #update data
    print("\nUpdate Records")
    updateid = input("Enter Film ID to update: ")
    change_genre = input("Change genre to: ")
    quiry4 = cursor.execute(f"update tblFilms SET genre='{change_genre}' where filmID = {updateid};")
    
    #delet data
    print("\nDelete record")
    delete_record = input("Enter the films Film ID here to delete it:  ")
    quiry3 = cursor.execute(f"delete from tblFilms where filmID = {delete_record}")
    
    #Report
    #1. Print details of all films
    print("\nShows all films")
    for row in cursor.execute("select * from tblFilms"):
        print(row)
    
    #2. Print all films of a particular genre
    print("\nPrinting out films of genre Action")
    for row in cursor.execute("select * from tblFilms where genre = 'Action'"):
        print(row)
    
    #3. Print all films of a particular year
    print("\nPrinting out films released in the year 2014")
    for row in cursor.execute("select yearReleased,title from tblFilms where yearReleased = 2014"):
        print(row)
    
    #4. Print all films of a particular rating
    print("\nPrinting out films of a rating of PG")
    for row in cursor.execute("select rating, genre, title from tblFilms where rating ='PG';"):
        print(row)

    

        
        
        