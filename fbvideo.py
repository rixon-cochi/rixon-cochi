from datetime import datetime
from tqdm import tqdm
import requests
import re
import os

banner = r'''


    __________     _    __________  __________ 
   / ____/ __ )   | |  / /  _/ __ \/ ____/ __ \
  / /_  / __  |   | | / // // / / / __/ / / / /
 / __/ / /_/ /    | |/ // // /_/ / /___/ /_/ / 
/_/   /_____/     |___/___/_____/_____/\____/  
                                  [TECH-COCHI] 2020              

  '''

print(banner)



def main():
    try:
        if len(list) == 2:
            if 0 in list and 1 in list:
                _input_1 = str(input("\nPress 'H' to download the video in HD quality.\nPress 'S' to download the video in SD quality.\n: ")).upper()
                if _input_1 == 'H':
                    download_video("HD")

                if _input_1 == 'S':
                    download_video("SD")

        if len(list) == 2:
            if 1 in list and 2 in list:
                _input_2 = str(input("\nOops! The video is not available in HD quality. Would you like to download it? ('Y' or 'N'): ")).upper()
                if _input_2 == 'Y':
                    download_video("SD")
                if _input_2 == 'N':
                    exit()

        if len(list) == 2:
            if 0 in list and 3 in list:
                _input_2 = str(input("\nOops! The video is not available in SD quality. Would you like to download it? ('Y' or 'N'): \n")).upper()
                if _input_2 == 'Y':
                    download_video("HD")
                if _input_2 == 'N':
                    exit()
    except(KeyboardInterrupt):
        print("\nProgramme Interrupted")


def download_video(quality):
    """Download the video in HD or SD quality"""
    print(f"\nDownloading the video in {quality} quality... \n")
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    with open(filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    print("\nVideo downloaded successfully.")


try:
    while True:
        url = input("\nEnter the URL of Facebook video: ")
        x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)

        if x:
            html = requests.get(url).content.decode('utf-8')
        else:
            print("\nNot related with Facebook domain.")
            exit()

        _qualityhd = re.search('hd_src:"https', html)
        _qualitysd = re.search('sd_src:"https', html)
        _hd = re.search('hd_src:null', html)
        _sd = re.search('sd_src:null', html)

        list = []
        _thelist = [_qualityhd, _qualitysd, _hd, _sd]
        for id,val in enumerate(_thelist):
            if val != None:
                list.append(id)

        main()
        again = input("\nWanna download another video? (Y or N): ").upper()
        if again == str("Y"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner)
            continue
        else:
            break

except KeyboardInterrupt:
    print("\nProgramme Interrupted")
    
