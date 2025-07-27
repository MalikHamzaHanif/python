import sqlite3
con = sqlite3.connect("youtube_manager.db")
cur = con.cursor()
cur.execute('''
            CREATE TABLE IF NOT EXISTS videos 
            (id INTEGER PRIMARY KEY , 
            name TEXT NOT NULL, 
            time TEXT NOT NULL)
            ''')
def main():
    while True:
        
        print("\n Youtube Manager choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        userInput=input("")
        match userInput:
        
            case "1":
                print("\n")
                res = cur.execute("SELECT * FROM videos")
                for video in res.fetchall():
                    print(video)
            case "2":
                video=input("\nPlease enter video name")
                if video==" ":
                    print("\nenter vailed video name it can not be empty")
                    continue
                cur.execute('''
                            INSERT INTO videos 
                            (name , time)
                            VALUES 
                            (?,?)
                            ''',
                            (video, "15 min")
                            )
                con.commit()
            case "3":
                videoToUpdate=input("\nEnter No of video you want to update.")
                newContentToAdd=input("\nEnter new content.")
                if newContentToAdd==" ":
                    print("\nplease some thing.")
                    continue
                cur.execute("""
                            UPDATE videos set name=? 
                            WHERE id=?
                            """,
                            (newContentToAdd, videoToUpdate)
                            )
                con.commit()
            case "4":
                videoToDelete=input("\nEnter No of video you want to delete.")
                
                cur.execute("""
                            DELETE FROM videos 
                            WHERE id=?
                            """,
                            (videoToDelete)
                            )
                con.commit()
            case "5":
                print("\nExiting the App")    
                break
            case _:
                print("\nYou chose wrong option")    
                print("\nExiting the App")    
                break

if __name__ =="__main__":
    main()
    con.close()

    