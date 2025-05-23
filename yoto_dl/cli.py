import yt_dlp
from textual.app import App, ComposeResult

class Yoto(App):

    def compose(self) -> ComposeResult:
        #yield Markdown(MARKDOWN)

def main():
    app = Yoto()
    app.run()

if __name__ == "__main__":
    main()

