import scrapetube

# Get all videos in channel
def scrape_channel(channelId:str)-> list:
    channel_vids = scrapetube.get_channel(channelId)

    videos = []

    for video in channel_vids:
        one_vid = {}
        one_vid['video_id'] = video['videoId']
        one_vid['title'] = video['title']['runs'][0]['text']
        # one_vid['description'] = split_sentences(video['descriptionSnippet'])
        videos.append(one_vid)

    return videos
