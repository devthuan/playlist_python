 # Group class  ==>
class Video():
    def __init__(self, video_title, video_link):
        self.video_title = video_title
        self.video_link = video_link

class Playlist():
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

# Group get data from user ==>
def get_data_from_user():
    title = input("Enter title video: ")
    link = input("Enter link video: ")
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
    playlist_name = input("Enter name playlist: ")
    playlist_description = input("Enter description playlist: ")
    playlist_rating = input("Enter rating (1-5) playlist: ")
    playlist_video = get_many_data_form_user()
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_video)
    return playlist

# Group print info to screen ==>
def print_info(data):
    print("Title video: "+ data.video_title, end="")
    print("link video: "+ data.video_link, end="")

def print_many_info(data):
    for i in range(len(data)):
        print_info(data[i])

def print_info_playlist(playlist):
    print("----------- \n")
    print("name playlist: ",playlist.name )
    print("name description: ", playlist.description )
    print("name rating: ", playlist.rating )
    print_many_info(playlist.videos)

# Group write data to file txt ==>
def write_data_to_txt(video, file):
        file.write(video.video_title + "\n")
        file.write(video.video_link + "\n")

def write_many_data_to_txt(data, file):
    total = len(data)
    # with open("playlist.txt", "w") as file:
    file.write(str(total) + "\n")
    for i in range(int(total)):
        write_data_to_txt(data[i], file)

def write_data_playlist_to_txt(playlist):
    with open("playlist.txt", "w") as file:
        file.write(playlist.name + "\n")
        file.write(playlist.description + "\n")
        file.write(playlist.rating + "\n")
        write_many_data_to_txt(playlist.videos, file)


# Group read data in file txt ==>
def read_data_in_txt(file):
    title = file.readline()
    link = file.readline()
    video = Video(title, link)
    return video

def read_many_data_in_txt():
    videos = []
    with open("playlist.txt", "r") as file:
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
        videos = read_many_data_in_txt()
    playlist = Playlist(name, description, rating, videos)
    return playlist

def main():
    # videos = get_many_data_form_user()
    # write_many_data_to_txt(videos)
    # videos = read_many_data_in_txt()
    # print_many_info(videos)
    playlist = get_data_of_playlist()
    write_data_playlist_to_txt(playlist)
    playlist = read_data_playlist_in_txt()
    print_info_playlist(playlist)

main()