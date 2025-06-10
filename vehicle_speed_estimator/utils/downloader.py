import gdown
import os
from config.settings import VIDEO_URL, VIDEO_NAME

def download_video_if_needed(path="assets"):
    os.makedirs(path, exist_ok=True)
    local_path = os.path.join(path, VIDEO_NAME)
    return gdown.cached_download(VIDEO_URL, local_path)
