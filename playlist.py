import csv


class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_total_duration(self):
        total = 0
        for song in self.songs:
            total += song.duration
        minutes = total // 60
        seconds = total % 60
        print(f"{minutes:02d}:{seconds:02d}")

    def find_by_artist(self, artist_name):
        matches = []
        for song in self.songs:
            if song.artist == artist_name:
                matches.append(song)
        if not matches:
            print(f"No songs by {artist_name} in the playlist.")
            return
        print(f"SONGS BY {artist_name.upper()}")
        print("-----------------------")
        for song in matches:
            print(f"{song.title},{song.artist}")

    def print_playlist(self):
        print(self.name.upper())
        print("-----------------")
        for song in self.songs:
            print(f"{song.title},{song.artist}")

    def load_songs(self, filename):
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_song(Song(row["Title"], row["Artist"], int(row["Duration"])))


def main():
    playlist = Playlist("My Playlist")
    playlist.load_songs("songs.csv")
    playlist.add_song(Song("My Fav Song", "Megabytes", 250))
    playlist.print_playlist()
    playlist.get_total_duration()
    playlist.find_by_artist("Null Pointer")


if __name__ == "__main__":
    main()
