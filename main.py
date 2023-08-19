from data_collection import scrape_channel
from data_cleaning import add_transcript, cleanup
from saving import save_with_pkl, check_exists
import pprint

channelId = 'UCbojg-FJgI1L6iLWUzgcsww'
printer = pprint.PrettyPrinter()

if __name__ == '__main__':
    if not check_exists("videos.pkl"):
        videos = scrape_channel(channelId)
        add_transcript(videos)
        cleanup(videos)
        save_with_pkl(videos)

    # <- path already exists, build model in here







