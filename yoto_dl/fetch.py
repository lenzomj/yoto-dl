import yt_dlp

def default_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
    elif d['status'] == 'error':
        print('Error downloading, please check the URL or your internet connection.')
    elif d['status'] == 'downloading':
        if d['downloaded_bytes'] > 0:
            percent = d['downloaded_bytes'] / d['total_bytes'] * 100
            print(f'Downloading: {percent:.2f}%')
        else:
            print('Starting download...')

class Fetch():
    class Logger(object):
        """
        Logger class for yt-dlp.
        """
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)
    """
    Downloads audio from YouTube media sources.
    """
    def __init__(self, options=None):
        self.options = options if options else {
            'format': 'bestaudio[ext=m4a]',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '192',
            }],
            'logger': self.Logger(),
            'outtmpl': '%(title)s.%(ext)s',
        }
        self.ytdl = yt_dlp.YoutubeDL(self.options)
        self.queue = []

    def add_progress_hook(self, hook: callable = default_hook) -> None:
        """
        Adds a progress hook to the downloader.
        """
        if 'progress_hooks' not in self.options:
            self.options['progress_hooks'] = []
        self.options['progress_hooks'].append(hook)

    def queue(self, title: str, url: str) -> None:
        """
        Queues a media URL for downloading.
        """
        self.queue.append((title, url))

    def download(self) -> None:
        """
        Downloads all queued media URLs.
        """
        for title, url in self.queue:
            self.options['outtmpl'] = f"{title}.%(ext)s"
            with yt_dlp.YoutubeDL(self.options) as ydl:
                ydl.download([url])
