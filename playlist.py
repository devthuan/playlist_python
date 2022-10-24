
from turtle import title


class Video():
    def __init__(self, title, link):
        self.title = title
        self.link = link

class Playlist():
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

def read_video():
    title = input("Enter title of video: " )
    link = input("Enter link of video: " )
    video = Video(title, link)
    return video

def read_videos():
    videos = []
    total = int(input("Enter total video: " + "\n"))
    for i in range(total):
        vid = read_video()
        videos.append(vid)
    return videos

def print_video(video):
    print("---------------\n" )
    print(" video title: ", video.title )
    print(" video link: ", video.link )

def print_videos(videos):
    for i in range(len(videos)):
        print_video(videos[i])

def write_video_txt(videos, file):
    file.write((videos.title) + "\n")
    file.write(videos.link + "\n")

def write_to_txt(videos, file):
    total = len(videos)
    # with open("data.txt", "w") as file:
    file.write(str(total) + "\n")
    for i in range(total):
        write_video_txt(videos[i], file)

def read_playlist():
    name = input("Enter name video: ")
    description = input("Enter description video: ")
    rating = input("rating video (1-5) star: ")
    videos = read_videos()
    playlist = Playlist(name, description, rating, videos)
    return playlist

def print_playlist(list):
    print("name video: ", list.name)
    print("description video: ", list.description)
    print("rating video: ", list.rating)

def write_playlist_txt(playlist):
    with open("data.txt", "w") as file:
        file.write((playlist.name)+ "\n")
        file.write((playlist.description)+ "\n")
        file.write((playlist.rating)+ "\n")
        write_to_txt(playlist.videos, file)
    print("Successfully write playlist to txt")

# def read_playlist_from_txt(playlist):
#     pass


def main():
    # videos= read_videos()
    # write_to_txt(videos)
    # print_videos(videos)
    playlist = read_playlist()
    write_playlist_txt(playlist)
    # playlist = read_playlist_from_txt()
    # print_playlist(playlist)

main()