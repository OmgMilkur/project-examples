import requests
import img2pdf


def main():
    img_list = []

    for i in range(1, 25):
        if i < 10:
            i = '0' + str(i)
        url = f'https://d3euuwqpqlzvic.cloudfront.net/60048/img-fb211824-000{i}.jpg'

        req = requests.get(url=url)
        response = req.content

        with open(f'media/{i}.jpg', 'wb') as file:
            file.write(response)
            img_list.append(f'media/{i}.jpg')
            print('Downloads..')


    with open('result.pdf', 'wb') as file:
        file.write(img2pdf.convert(img_list))


if __name__ == '__main__':
    main()
