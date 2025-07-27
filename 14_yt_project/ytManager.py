import json




def loadYoutubeVideos():
    try:
        file=open("yt_videos.txt","r")
        return json.load(file)
        # return file.read()
    except FileNotFoundError:
        print("no file present",FileNotFoundError)
        return []


def saveVideos(videos):
    with open("yt_videos.txt","w") as file:
        json.dump(videos,file)
        # file.write(videos)
   
def main():
    youtubeVideos=loadYoutubeVideos()
    print(youtubeVideos)
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
                for video in enumerate(youtubeVideos):
                    print(video)
            case "2":
                video=input("\nPlease enter video name")
                if video==" ":
                    print("\nenter vailed video name it can not be empty")
                    continue
                youtubeVideos.append(video)
                saveVideos(youtubeVideos)
            case "3":
                videoToUpdate=input("\nEnter No of video you want to update.")
                
                if videoToUpdate==" ":
                    print("\nenter vailed video number it can not be empty")
                    continue
                try:
                    videoNumber=int(videoToUpdate)
                    if videoNumber>=len(youtubeVideos):
                        print("\nPlease enter valid number")
                        continue
                    newContentToAdd=input("\nEnter No of content.")
                    if newContentToAdd==" ":
                        print("\nplease some thing.")
                        continue
                    youtubeVideos[videoNumber]=newContentToAdd
                    saveVideos(youtubeVideos)     
                except ValueError:
                    print("\nplease enter a valid number",ValueError)
            
            case "4":
                videoToDelete=input("\nEnter No of video you want to delete.")
                if videoToDelete==" ":
                    print("\nenter vailed video number it can not be empty")
                    continue
                try:
                    videoNumber=int(videoToDelete)
                    if videoNumber>=len(youtubeVideos):
                        print("\nPlease enter valid number")
                        continue
                    youtubeVideos.pop(videoNumber)
                    saveVideos(youtubeVideos)    
                except ValueError:
                    print("\nplease enter a valid number",ValueError)
            case "5":
                print("\nExiting the App")    
                break
            case _:
                print("\nYou chose wrong option")    
                print("\nExiting the App")    
                break

main()

    