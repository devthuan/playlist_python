import pygame
import webbrowser
import binascii

# Group class ==>
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


class TextButton():
    def __init__(self, text, position):
        self.text = text
        self.position = position

    def is_mouse_on_text(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (mouse_x > self.position[0] and mouse_x < self.position[0] + self.text_box[2]) and (mouse_y > self.position[1]  and mouse_y < self.position[1] + self.text_box[3]):
            return True
        else:
            return False    

    def draw(self):
        font = pygame.font.SysFont('Time new Roman', 30)
        text_render = font.render(self.text, True, (0, 0, 0))
        self.text_box = text_render.get_rect()

        if self.is_mouse_on_text():
            text_render = font.render(self.text, True, (0,0,255))
            pygame.draw.line(screen, BLUE, (self.position[0], self.position[1] + self.text_box[3]), (self.position[0] + self.text_box[2], self.position[1] + self.text_box[3]))
        else:
            text_render = font.render(self.text, True, (0, 0, 0))

        # pygame.draw.rect(screen,WHITE, (self.position[0], self.position[1], self.text_box[2], self.text_box[3]))
        screen.blit(text_render, self.position)


# Group function ==>
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

def read_data_playlist_in_txt(file):
    # with open("playlist.txt", "r") as file:
    name = file.readline()
    description = file.readline()
    rating = file.readline()
    videos = read_many_data_in_txt(file)
    playlist = Playlist(name, description, rating, videos)
    return playlist

def read_data_playlists_in_txt():
    playlists = []
    with open("playlist.txt", "r") as file:
        total = file.readline()
        for i in range(int(total)):
            playlist = read_data_playlist_in_txt(file)
            playlists.append(playlist)

    return playlists
# Default
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Playlist video Youtube")
running = True
clock = pygame.time.Clock()

# Color
GREEN = (23, 168, 60)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE =(255, 255, 255)
BLACK =  (0, 0, 0)

# Load data
playlists = read_data_playlists_in_txt()
playlist = playlists[1]
margin = 50
playlists_btn_list = []
videos_list_btn = []
for i in range(len(playlists)):
    playlist_btn = TextButton(str(i+1) + ". " + playlists[i].name.rstrip(), (30, 50+margin*i))
    playlists_btn_list.append(playlist_btn)


while running:
    clock.tick(60)
    screen.fill(WHITE)

    for playlist_button in playlists_btn_list:
        playlist_button.draw()
    for video_button in videos_list_btn:
        video_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(len(playlists_btn_list)):
                    if playlists_btn_list[i].is_mouse_on_text():
                        play_choice = i
                        videos_list_btn = []
                        playlist = playlists[i]
                        for j in range(len(playlist.videos)):
                            video_btn = TextButton(str(j+1) + ". " + playlist.videos[j].video_title.rstrip(), (230, 50+margin*j))
                            videos_list_btn.append(video_btn)
                if play_choice != None:
                    for i in range(len(videos_list_btn)):
                        if videos_list_btn[i].is_mouse_on_text():
                            playlist.videos[i].open()
                        

                

        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
    