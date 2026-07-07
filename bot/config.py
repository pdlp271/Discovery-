import os
from pydrive2.auth import GoogleAuth


currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)

class TG_CONFIG:
    api_id = "28269435"

    api_hash = "839f282133fe8ee79b4a946095cf4360"

    bot_token = ""

    #DEVS or #OWNERS
    sudo_users = [add]

    # Has access to gdrive config and gdrive session
    dev_users = [add]

    session = ""

    bot_creater = "ӇƤ Ʀƛʆ"  # Don't Remove if you Respect the DEV

    bot_creater_id = "@HP_Raj_Support_bot"  # Don't Remove if you Respect the DEV

class GDRIVE_CONFIG:
    #for Gdrive (Leave it as Empty String if not Gdrive Upload is turned ON)
    root_folder_id = ""

    #don't touch or add yours
    indexlink_format = "https://example.google.workers.dev/0:/{}/{}"

    is_making_drive_files_public = True

class UPLOAD_CONFIG:
    upload_to = "tg" #tg, gdrive
    
    

class GD_SHARER_CONFIG:

    gd_sharer = [
        {
            "name" : "filepress",
            "base_url" : "https://filebee.xyz",
            "method" : "to_filepress()",
            "to_upload" : False,
            "headers" : {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en,en-US;q=0.9,en-IN;q=0.8',
                'content-type': 'application/json',
                'origin': "https://filebee.xyz",
                'referer': f'https://filebee.xyz/add-file',
                'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            },
            "cookies" : {
                "connect.sid": "",
            }
        }
    ]
    

class FILENAME_CONFIG:

    filename_format = "p2p"  # p2p or non-p2p

    p2p_audio_bitrate = "K"

    non_p2p_audio_bitrate = "Kbps"

    underscore_before_after_group_tag = "__"

    language_order = ['kn', 'ta', 'te', 'bn', 'gu', 'pa', 'as', 'or',
                    'ml', 'mr', 'hi', 'th', 'ja', 'th', 'id', 'ms', 'ko', 'bho', 'bh', 'en']

    default_group_tag = "HP_Raj_MOVIES" # Don't change it if you Respect the DEV


class PROXY_CONFIG:
    #Keep it as a empty string if you don't have proxy
    proxy_url = "http://rcbforever2036:gqoagZF2Vt@103.235.64.207:50100"
    USE_PROXY_WHILE_DOWNLOADING = True

proxies = {
    "http" : PROXY_CONFIG.proxy_url,
    "https" : PROXY_CONFIG.proxy_url,
}

START_MSG = """
<b>Hello <code>@{}</code>,
A TG WEB-DL Bot</b>

> <code>{}</code>

<b>Made by @{}</b>
"""


DRIVE_DL_DONE_MSG = """
✅ <b> Task Completed In </b> <code>{}</code>

<b>FileName : </b> <code>{}</code>
<b>OTT : </b> <code>{}</code>
<b>Size : </b> <code>{}</code>
"""

LOG_MESSAGE = "<code>[+]</code> <b>{title}</b>\n<b><code>[+]</code> <b>{left_text} : </b><code>{right_text}</code>"

AUDIO_DOWNLOAD_LOG_MESSAGE = """<code>[+]</code> <b>Downloading Audio</b>  
<code> └─ [=>] | {title}</code>
<code> └─ [{codec}] | {language} | {channel} | {bitrate} kb/s</code>"""

VIDEO_DOWNLOAD_LOG_MESSAGE = """<code>[+]</code> <b>Downloading Video</b>  
<code> └─ [=>] | {title}</code>
<code> └─ [{codec}, {range}] | {langauge} | {width}x{height} @Kushi_Yarige_bedda {bitrate} kb/s, {fps} FPS</code>"""

languages_info_file_path = os.path.join(dirPath, "static", "languages_info.json")
dl_folder = os.path.join(dirPath, "downloads")  
client_secrets_json = os.path.join(dirPath, "static", "client_secrets.json")
wvd_file_path = os.path.join(
    dirPath, "static", "google_sdk_google_atv_x86_15.0.0_27cfa318_8162_l3.wvd")

token_file = os.path.join(dirPath, "static", "session_conan76")

def setup_downloads_folder(dl_folder):
    os.makedirs(dl_folder) if not os.path.exists(dl_folder) else None

def setup_binaries():
    iswin = 1 if os.name == "nt" else 0

    if iswin == 0:
        aria2c = os.path.join(dirPath, "binaries", "aria2c")
        mp4decrypt = os.path.join(dirPath, "binaries", "mp4decrypt")
        ytdlp = os.path.join(dirPath, "binaries", "yt-dlp")

        os.system(f"chmod 777 {aria2c} {mp4decrypt} {ytdlp}")
    else:
        aria2c = os.path.join(dirPath, "binaries", "aria2c.exe")
        mp4decrypt = os.path.join(dirPath, "binaries", "mp4decrypt.exe")
        ytdlp = os.path.join(dirPath, "binaries", "yt-dlp.exe")

    return aria2c, mp4decrypt, ytdlp

setup_downloads_folder(dl_folder)
aria2c, mp4decrypt, ytdlp = setup_binaries()

gauth = GoogleAuth()
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = client_secrets_json

