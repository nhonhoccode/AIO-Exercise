import gdown


def download_file_from_google_drive(url, destination):
    link = url
    gdown.download(link, destination, quiet=False)


if __name__ == '__main__':
    url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
    destination = 'D:\AIO_2024\AIO-Exercise\mod01_w02\P1_data.txt'
    download_file_from_google_drive(url, destination)
