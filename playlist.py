import webbrowser

 # Group class  ==>
class Video():
    def __init__(self, video_title, video_link):
        self.video_title = video_title
        self.video_link = video_link
        self.seen = False

    def open(self):
        # webbrowser.open() : open link on website
        webbrowser.open(self.video_link)
        self.seen = True

class Playlist():
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

# Group get data from user ==>
def get_data_from_user():
    title = input("Enter title video: ") + "\n"
    link = input("Enter link video: ")+ "\n"
    video = Video(title, link)
    return video

def get_many_data_form_user():
    videos = []
    total = int(input("Enter total video: "))
    for i in range(total):
        # print("video ", i+1)
        video = get_data_from_user()
        videos.append(video)
    return videos

def get_data_of_playlist():
    playlist_name = input("Enter name playlist: ") + "\n"
    playlist_description = input("Enter description playlist: ") + "\n"
    playlist_rating = input("Enter rating (1-5) playlist: ") + "\n"
    playlist_video = get_many_data_form_user()
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_video)
    return playlist

# Group print info to screen ==>
def print_info(data):
    print("Title video: "+ data.video_title, end="")
    print("link video: "+ data.video_link, end="")

def print_many_info(data):
    for i in range(len(data)):
        print("video ", i+1)
        print_info(data[i])

def print_info_playlist(playlist):
    print("-----------")
    print("name playlist: " + playlist.name, end="" )
    print("name description: "+ playlist.description  , end="")
    print("name rating: "+ playlist.rating , end="" )
    print_many_info(playlist.videos)

# Group write data to file txt ==>
def write_data_to_txt(video, file):
        file.write(video.video_title )
        file.write(video.video_link )

def write_many_data_to_txt(data, file):
    total = len(data)
    # with open("playlist.txt", "w") as file:
    file.write(str(total) + "\n")
    for i in range(int(total)):
        write_data_to_txt(data[i], file)

def write_data_playlist_to_txt(playlist):
    with open("playlist.txt", "w") as file:
        file.write(playlist.name)
        file.write(playlist.description)
        file.write(playlist.rating)
        write_many_data_to_txt(playlist.videos, file)
    print("Successfully write playlist to file txt")


# Group read data in file txt ==>
def read_data_in_txt(file):
    title = file.readline()
    link = file.readline()
    video = Video(title, link)
    return video

def read_many_data_in_txt(file):
    videos = []
    # with open("playlist.txt", "r") as file:
    total = file.readline()
    for i in range(int(total)):
        video = read_data_in_txt(file)
        videos.append(video)
    return videos

def read_data_playlist_in_txt():
    with open("playlist.txt", "r") as file:
        name = file.readline()
        description = file.readline()
        rating = file.readline()
        videos = read_many_data_in_txt(file)
    playlist = Playlist(name, description, rating, videos)
    return playlist

# notification
def show_menu():
    print("*********** MENU ************")
    print("| Option 1: Create playlist |")
    print("| Option 2: Show playlist   |")
    print("| Option 3: Play a video    |")
    print("| Option 4: Add a video     |")
    print("| Option 5: Update playlist |")
    print("| Option 6: Delete video    |")
    print("| Option 7: Save and Exit   |")
    print("----------------------------")

# Group function option menu
def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max :
        choice = input(prompt)
    choice = int(choice)
    return choice

def play_video(playlist):
    print_many_info(playlist.videos)
    total = len(playlist.videos)
    choice = select_in_range("Select a video (1-" + str(total) + "): " , 1, total)
    print("Open video: " + playlist.videos[choice-1].video_title + " - " + playlist.videos[choice-1].video_link)
    playlist.videos[choice-1].open()

def add_video(playlist):
    print("Enter new video information:")
    new_title = input("Enter new video title: ") + "\n"
    new_link = input("Enter new video link: ")   + "\n"
    new_video = Video(new_title, new_link)
    playlist.videos.append(new_video)
    return playlist

def update_playlist(playlist):
    print("Update playlist?")
    print("1. Name")
    print("2. Description")
    print("3. Rating")
    choice = select_in_range("Enter what you want to update (1-3): ", 1,3)
    if choice == 1:
        new_playlist_name = input("Enter new name for playlist: ") + "\n"
        playlist.name = new_playlist_name
        print("Update successfully!")
        return playlist
    elif choice == 2:
        new_playlist_description = input("Enter new description for playlist: ") + "\n"
        playlist.description = new_playlist_description
        print("Update successfully!")
        return playlist
    elif choice == 3:
        new_playlist_rating = input("Enter new rating for playlist: ") + "\n"
        playlist.rating = new_playlist_rating
        print("Update successfully!")
        return playlist

def remove_video(playlist):
    print_many_info(playlist.videos)
    choice = select_in_range("Enter you want to delete video: ", 1, len(playlist.videos))
    del playlist.videos[choice-1]
    # or
    # new_video_list = []
    # for i in range(len(playlist.videos)):
    #     if i == choice-1:
    #         continue
    #     new_video_list.append(playlist.video[i])
    # playlist.videos = new_video_list
    # return playlist
    print("Delete successfully!")


def main():
    # playlist = get_data_of_playlist()
    # write_data_playlist_to_txt(playlist)
    # playlist = read_data_playlist_in_txt()
    # print_info_playlist(playlist)

    try:
        playlist = read_data_playlist_in_txt()
        print("loaded data Successfully!")
    except:
        print("Welcome !!!")

    while True:
        show_menu()
        choice = select_in_range("Select an option (1-7): " ,1 ,7)
        if choice == 1:
            playlist = get_data_of_playlist()
            input("Press Enter to continue ")

        elif choice == 2:
            print_info_playlist(playlist)
            input("Press Enter to continue ")

        elif choice == 3:
            play_video(playlist)
            input("Press Enter to continue ")

        elif choice == 4:
            playlist  = add_video(playlist)
            input("Press Enter to continue ")

        elif choice == 5:
            playlist  = update_playlist(playlist)
            input("Press Enter to continue ")
        
        elif choice == 6:
            playlist  = remove_video(playlist)
            input("Press Enter to continue ")

        elif choice == 7:
            write_data_playlist_to_txt(playlist)
            input("Press Enter to continue ")
            break
        else:
            input("Wrong input, Exist.")

   


main()