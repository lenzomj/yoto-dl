from ..mixtape import Mixtape, Track


def test_add_track():
    mixtape = Mixtape("My Mixtape")
    track = Track("Song Title", "Artist Name", "http://example.com")
    mixtape.add_track(track)
    assert len(mixtape.tracks) == 1
    assert mixtape.tracks[0].title == "Song Title"
    assert mixtape.tracks[0].artist == "Artist Name"
    assert mixtape.tracks[0].link == "http://example.com"


def test_save_load_mixtape():
    mixtape = Mixtape("My Mixtape")
    track1 = Track("Song Title 1", "Artist Name 1", "http://example.com/1")
    track2 = Track("Song Title 2", "Artist Name 2", "http://example.com/2")
    mixtape.add_track(track1)
    mixtape.add_track(track2)

    # Save the mixtape
    saved = mixtape.save()

    # Load the mixtape
    loaded_mixtape = Mixtape.load(saved)

    assert len(loaded_mixtape.tracks) == 2
    assert loaded_mixtape.name == "My Mixtape"
    assert loaded_mixtape.tracks[0].title == "Song Title 1"
    assert loaded_mixtape.tracks[1].title == "Song Title 2"
