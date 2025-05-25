import json

class Track():
    def __init__(self, title: str, artist: str, link: str):
        self.title = title
        self.artist = artist
        self.link = link

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Mixtape():
    def __init__(self, name: str):
        self.name = name
        self.tracks = []

    def add_track(self, track: Track):
        self.tracks.append(track)

    def remove_tracks(self, indices: list):
        self.tracks = [track for i, track in enumerate(self.tracks) if i not in indices]

    def list_tracks(self):
        for track in self.tracks:
            print(track)

    def save(self) -> str:
        """
        Saves the mixtape to a JSON string.
        {
            "name": "My Mixtape",
            "tracks": [
                {
                    "title": "Song Title",
                    "artist": "Artist Name",
                    "link": "http://example.com"
                },
                {
                    "title": "Another Song",
                    "artist": "Another Artist",
                    "link": "http://example.com/another"
                }
            ]
        }
        """
        mixtape_dict = {
            "name": self.name,
            "tracks": [
                {
                    "title": track.title,
                    "artist": track.artist,
                    "link": track.link
                } for track in self.tracks
            ]
        }
        return json.dumps(mixtape_dict, indent=4)

    @staticmethod
    def load(json_str: str) -> 'Mixtape':
        """
        Loads the mixtape from a JSON string.
        """
        mixtape_dict = json.loads(json_str)
        mixtape = Mixtape(mixtape_dict["name"])
        for track_dict in mixtape_dict["tracks"]:
            track = Track(
                track_dict["title"],
                track_dict["artist"],
                track_dict["link"]
            )
            mixtape.add_track(track)
        return mixtape

