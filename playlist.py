
from turtle import title


class Video():
    def __init__(self, title, link):
        self.title = title
        self.link = link

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

def write_to_txt(videos):
    total = len(videos)
    with open("data.txt", "w") as file:
        file.write(str(total) + "\n")
        for i in range(total):
           write_video_txt(videos[i], file)

def main():
    videos= read_videos()
    write_to_txt(videos)
    print_videos(videos)

main()