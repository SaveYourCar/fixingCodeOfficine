import re

def get_link_id(link): 

    youtube_link = re.search(r"(youtube.com|youtu.be)", link)

    if youtube_link:
        start_id = re.search(r"(v=|.be/)", link).end()
        return link[start_id :]
    else:
        return "not a youtube link"

print(get_link_id(input()))
