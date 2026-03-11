import requests
import img2pdf


def get_data():
    for i in range(1,49):
        url = f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url)
        res = req.content
        with open(f'media/{i}.jpg', 'wb') as file:
            file.write(res)

# get_data()

def write_pdf():
    img_list = [f"media/{i}.jpg" for i in range(1,49)]
    with open('res.pdf', 'wb') as f:
        f.write(img2pdf.convert(img_list))
    
write_pdf()