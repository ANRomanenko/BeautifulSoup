import requests

img_url = 'https://online-converting.ru/wp-content/uploads/jpeg1.jpg'
video_url = 'https://my.skvot.io/uploads/media/5face974225e0_720.mp4'


def download_img(url=''):

    try:
        response = requests.get(url=url)

        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)

        return 'Img succefully downloaded'
    except Exception as _ex:
        return 'Upps... Chek the URL please'


def download_video(url=''):

    try:
        # response = requests.get(url=url)

        # with open('req_video.mp4', 'wb') as file:
        #     file.write(response.content)

        response = requests.get(url=url, stream=True)
        with open('req_video.mp4', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)


        return 'Img succefully downloaded'
    except Exception as _ex:
        return 'Upps... Chek the URL please'


def main():
    # print(download_img(url=img_url))
    print(download_video(url=video_url))


if __name__ == '__main__':
    main()