class Video():
    def __init__(self, video_title, video_link):
        self.video_title = video_title
        self.video_link  = video_link

class Playlist():
    def __init__(self, playlist_name, playlist_description, playlist_rating, videos):
        self.playlist_name = playlist_name
        self.playlist_description = playlist_description
        self.playlist_rating = playlist_rating
        self.videos = videos

def get_data():
    video_title = input("Enter title video: " )
    video_link = input("Enter link video: ")
    video = Video(video_title, video_link)
    return video

# read videos
def get_many_data():
    videos = []
    total_video = int(input("Enter total video:  \n"))
    for i in range(total_video):
        print("Enter video ", i+1)
        get_function = get_data()
        videos.append(get_function)
    return videos

# get data of playlist video
def get_data_playlist():
    playlist_name = input("Enter name playlist video: ")
    playlist_description = input("Enter description playlist video: ")
    playlist_rating = input("Enter name rating video: ")
    videos = get_many_data()
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, videos)
    return playlist

def print_data(data):
    print("Title video: ", data.video_title)
    print("Title link video: ", data.video_link)

# print videos
def print_many_data(videos):
    for i in range(len(videos)):
        print_data(videos[i])

# print data playlist video
def print_data_playlist(playlist):
    print("------------- print  ==> \n")
    print("Enter name playlist: ", playlist.playlist_name)
    print("Enter description playlist: ", playlist.playlist_description)
    print("Enter rating playlist: ", playlist.playlist_rating)
    print_many_data(playlist.videos)

def write_data(videos, file):
    file.write(videos.video_title + "\n")
    file.write(videos.video_link + "\n")

def write_to_txt(videos, file):
    total = len(videos)
    # with open("data_task2.txt", "w") as file:
    file.write(str(total) + "\n")
    for i in range(total):
        write_data(videos[i], file)
            # file.write(videos[i].video_title + "\n")
            # file.write(videos[i].video_link + "\n")

# write data to file data_task2
def write_playlist__to_txt(playlist):
    with open("data_task2.txt", "w") as file:
        file.write((playlist.playlist_name + "\n"))
        file.write((playlist.playlist_description + "\n"))
        file.write((playlist.playlist_rating + "\n"))
        write_to_txt(playlist.videos, file)
    print("Successfully write playlist to file txt")


def main():
    # video = get_many_data()
    # write_to_txt(video)
    # print_many_data(video)
    playlist = get_data_playlist()
    write_playlist__to_txt(playlist)
    print_data_playlist(playlist)
main()