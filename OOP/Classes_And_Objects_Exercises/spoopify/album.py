from spoopify.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs: list[Song] = [el for el in args]
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        try:
            song = [s for s in self.songs if s == song_name][0]
            if self.published:
                return "Cannot remove songs. Album is published."
            self.songs.remove(song)
            return f"Removed song {song.name} from album {self.name}"
        except IndexError:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        formatted_song = [f"== {s.get_info()}" for s in self.songs]
        result += "\n".join(formatted_song) + "\n"
        return result

