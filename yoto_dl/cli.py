import yt_dlp
import click
import pathlib
from progress.bar import Bar
from .mixtape import Mixtape, Track
from .fetch import Fetch

@click.command()
@click.argument('mixtape', type=click.Path(exists=True))
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose output')
@click.option('-d', '--display', is_flag=True, help='Display tracklist information')
@click.option('-x', '--exclude', help='Exclude tracks (multiple indices)')
def cli(mixtape, verbose, display, exclude):
    """
    A command-line interface for downloading and managing yoto mixtapes.
    """
    if verbose:
        yt_dlp.utils.std_headers['User-Agent'] = 'yt-dlp/2023.10.01'

    # Load the mixtape from the provided file
    try:
        with open(mixtape, 'r') as f:
            mixtape_data = f.read()
            mixtape_obj = Mixtape.load(mixtape_data)
    except Exception as e:
        click.echo(f'Error loading mixtape: {e}')
        return

    if exclude:
        exclude_indices = [(int(i) - 1) for i in exclude.split(',')]
        mixtape_obj.remove_tracks(exclude_indices)
    if display:
        mixtape_obj.list_tracks()

    # Download the tracks
    fetch = Fetch()
    for track in mixtape_obj.tracks:
        bar = Bar(f"{track.title} by {track.artist}", max=100)
        def progress_hook(d):
            if d['status'] == 'downloading':
                if d['downloaded_bytes'] > 0:
                    percent = d['downloaded_bytes'] / d['total_bytes'] * 100
                    bar.goto(int(percent))
                else:
                    bar.next()
        fetch.add_progress_hook(progress_hook)
        # Check if the track file is already downloaded
        if not pathlib.Path(f"{track.title}.m4a").exists():
            fetch.download(track)
        else:
            click.echo(f"Track '{track.title}' already downloaded, skipping.")
        bar.finish()

def main():
    cli()

if __name__ == "__main__":
    main()
