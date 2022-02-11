import pandas as pd
import requests
import time
import pickle
import re
from bs4 import BeautifulSoup
from urllib.parse import unquote_plus
import datetime
import os
# import shutil

path = 'C:\\Python\\kimchitv'
save_path = '\\\\KDS\\docker\\code_server\\kimchitv\\movies'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
# =======================================================
#               여기 입력
# =======================================================
# pickle_name = 'kimchitv_고딩자위.pickle'    # 여기 바꿀거
# pickle_name = 'kimchitv_출사.pickle'
# pickle_name = 'kimchitv_국산모음.pickle'
# pickle_name = 'kimchitv_섹스.pickle'
# pickle_name = 'kimchitv_good.pickle'
# pickle_name = 'kimchitv_165.pickle'
# pickle_name = 'kimchitv_kor-sg.pickle'
# pickle_name = 'kimchitv_11.pickle'
# pickle_name = 'kimchitv_커플-폰.pickle'
# pickle_name = 'kimchitv_레전.pickle'
# =======================================================


def boil_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def make_df(site, soup):
    lis = soup.select('ul.videos > li')
    data = []
    # print(lis)
    for li in lis:
        try:
            mov_link = li.select_one('a').attrs['href']
            # print(mov_link)
            mov_title = li.select_one('a').attrs['title']
            mov_title = re.sub('[\/:*?"<>|]', '', mov_title)
            id = li.attrs['id']
            n = re.findall('\d{1,10}', id)
            content = f'https://kimchi.tv/video/download/{n[0]}/{str(int(n[0])+1)}/480p/'
            data.append([mov_title, site + mov_link, content])
        except:
            pass
    df = pd.DataFrame(data=data, columns=['title', 'link', 'content'])
    # print(df)
    return df

def save_df_pickle(df, play_list_url, pickle_path):
    now = datetime.datetime.now()
    now_date = datetime.datetime.strftime(now, '%y%m%d%H%M')
    pickle_name = now_date
    # print(pickle_path)
    # print(pickle_name)
    pickle_path = pickle_path + '\\' + 'kimchitv_' + pickle_name + '.pickle'
    df.to_pickle(pickle_path,)
    # # print(pickle_path)
    # print(pickle_name, ' pickle saved')
    return f'kimchitv_{pickle_name}.pickle'



def read_drive_files():
    drv_files = load_dncomplete_files()
    # print(drv_files)
    return drv_files

def read_df_pickle(pickle_path, pickle_name):
    print(pickle_path + '\\' + pickle_name)
    df = pd.read_pickle(pickle_path + '\\' + pickle_name)
    
    return df

def save_mov(df, drv_files, pn):
    del_temp_file()
    for i in list(range(df.shape[0])):
        title = df.loc[i,'title']
        if title not in drv_files:
            if len(re.findall('.+?[가-힣].+?', title)) != 0:
                if ('Korean Bj' not in title)&('KBJ' not in title)&('Mosaic Removed' not in title):
                    referer = df.loc[i, 'link']
                    link = df.loc[i,'content']
                    file_name = save_path + '\\temp\\' + title + '.mp4'
                    print('{}/{}'.format(i,df.shape[0]), title, link)
                    start = time.time()
                    download_file(link, title, referer, start, pn[:6])
                else:
                    print(title, ': 취소')  
        else:
            print(title, ' : ',save_path,'있음' )
def download_chunk(res, file_name, destination_file_name, title, start):
    with res as r:
        r.raise_for_status()
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    file_size = os.path.getsize(file_name)
    os.replace(file_name, destination_file_name)
    dncomplete_files = load_dncomplete_files()
    dncomplete_files.append(title)
    save_dncomplete_files(dncomplete_files)
    t_m = (time.time() - start) // 60
    t_s = round((time.time() - start) % 60)
    print('{}분 {}초 {:.2f} Mbyte'.format(t_m, t_s, file_size/1000000), '완료')

def download_file(link, title, referer, start, pn):
    file_name = save_path + '\\temp\\' + title + '.mp4'
    # pn = pickle_name[pickle_name.find('_')+1:pickle_name.rfind('.')]
    os.makedirs(save_path + '\\' + pn, exist_ok=True)
    destination_file_name = save_path + '\\'+ pn +'\\' + title + '.mp4'
    # destination_file_name = save_path + '\\' + title + '.mp4'
    headers = {'Referer':referer,
            'User-Agent':user_agent}
    res = requests.get(link, headers=headers, stream=True)
    if res.status_code != 404:
        download_chunk(res, file_name, destination_file_name, title, start)
    elif res.status_code == 404:
        link = link.replace('480p', '720p')
        # print(link)
        res = requests.get(link, headers=headers, stream=True)
        if res.status_code != 404:
            download_chunk(res, file_name, destination_file_name, title, start)
        elif res.status_code == 404:
            u = link[:link.rfind('download/')+9]
            n = link[link.rfind('download/')+9:][:link[link.rfind('download/')+9:].find('/')]
            link = u + n + '/' + n + '/720p/'
            res = requests.get(link, headers=headers, stream=True)
            if res.status_code != 404:
                download_chunk(res, file_name, destination_file_name, title, start)
            elif res.status_code == 404:
                u = link[:link.rfind('download/')+9]
                n = link[link.rfind('download/')+9:][:link[link.rfind('download/')+9:].find('/')]
                link = u + n + '/' + n + '/480p/'
                # print(link)
                # print(d,'파일없음')
                res = requests.get(link, headers=headers, stream=True)
                if res.status_code != 404:
                    download_chunk(res, file_name, destination_file_name, title, start)
                else:
                    print(f'HTTPError: 404 Client Error: Not Found for url: {link}')
                    pass
    # ==============================================================


def load_dncomplete_files():
    pickle_file = save_path + '\\' + 'download_complete.pickle'
    with open(pickle_file, 'rb') as f:
        dncomplete_files = pickle.load(f)
        # pickle.dump(files0, f, pickle.HIGHEST_PROTOCOL)
        return dncomplete_files

def save_dncomplete_files(data):
    pickle_file = save_path + '\\' + 'download_complete.pickle'
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def del_temp_file():
    # files = os.listdir(save_path)
    # # print(files)
    # for f in files:
    #     print(f)
    #     f_size = os.path.getsize(save_path + '\\' + f)
    #     if f_size == 0:
    #         os.remove(save_path + '\\' + f)
    temp_dr = save_path + '\\temp'
    temp_files = os.listdir(temp_dr)
    for f in temp_files:
        os.remove(temp_dr + '\\' + f)


# ==========================================================
#                   여기 url 입력
# url = 'https://kimchi.tv/playlist/1584/%EB%A0%88%EC%A0%84/'
# url = 'https://kimchi.tv/playlist/132/ko/'
# url = 'https://kimchi.tv/playlist/6796/xx/'
# url = 'https://kimchi.tv/playlist/8094/gooooooood/'
# url = 'https://kimchi.tv/playlist/4592/%EA%BC%B4%EB%A6%AC%EB%8A%94-%EA%B1%B0/'
# url = 'https://kimchi.tv/playlist/7968/sl/'
# url = 'https://kimchi.tv/playlist/10806/%EC%98%A8%ED%8C%AC/'
# url = 'https://kimchi.tv/playlist/4662/%EC%9A%95%EA%B3%A0%EB%94%A9/'
# url = 'https://kimchi.tv/playlist/1233/%EA%B1%B8%EB%A0%88%EB%85%84%EB%93%A4/'
# url = 'https://kimchi.tv/playlist/8763/me-only/'
# url = 'https://kimchi.tv/playlist/1921/%EC%96%BC%EA%B5%B4/'
url = 'https://kimchi.tv/'
# url = 
# url = 
# url = 
# ==========================================================
pickle_path = 'C:\\Python\\kimchitv'
site = 'https://kimchi.tv'
soup = boil_soup(url)
df = make_df(site, soup)
pickle_name = save_df_pickle(df, url, pickle_path)
pn = pickle_name[pickle_name.find('_')+1:pickle_name.rfind('.')]
print(pn)
df = read_df_pickle(pickle_path, pickle_name)
drv_files = read_drive_files()
save_mov(df, drv_files, pn)