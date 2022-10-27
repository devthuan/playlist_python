# Group class
class Video():
    def __init__(self, video_title, video_link):
        self.video_title = video_title
        self.video_link = video_link

# Group get data from user
def get_data_from_user():
    title = input("Enter title video: ")
    link = input("Enter link video: ")
    video = Video(title, link)
    return video

def get_many_data_form_user():
    videos = []
    total = int(input("Enter total video: "))
    for i in range(total):
       video = get_data_from_user()
       videos.append(video)
    return videos

# Group print info to screen
def print_info(data):
    print("Title video: ", data.video_title)
    print("link video: ", data.video_link)

def print_many_info(data):
    print("------------ \n")
    for i in range(len(data)):
        print_info(data[i])

# Group write data to file txt
def write_data_to_txt(video, file):
        file.write(video.video_title + "\n")
        file.write(video.video_link + "\n")

def write_many_data_to_txt(data):
    with open("playlist.txt", "w") as file:
        for i in range(len(data)):
            write_data_to_txt(data[i], file)

# Group read data in file txt
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

def main():
    videos = get_many_data_form_user()
    write_many_data_to_txt(videos)
    videos = read_many_data_in_txt()
    print_many_info(videos)
    

main()