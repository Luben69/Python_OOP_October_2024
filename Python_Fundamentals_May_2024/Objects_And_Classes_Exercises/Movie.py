class Movie:
    __watched_movies = 0

    def __init__(self, name: str, director: str, watched=False):
        self.name = name
        self.director = director
        self.watched = watched

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}." \
            f" Total watched movies: {Movie.__watched_movies}"
