import base64
import requests
import time


source_paths = ['./images/hou-1.jpg', './images/hou-2.jpg', './images/hou-3.jpg']
target_path = './images/test-2.mp4'


def image_to_base64_str(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')


def request(source_paths, target_path):
    sources = []
    for source_path in source_paths:
        sources.append(image_to_base64_str(source_path))
    target = image_to_base64_str(target_path)
    params = {
        'sources': sources,
        'target': target,
        'target_extension': '.mp4'
    }
    url = 'http://0.0.0.0:8000/'
    response = requests.post(url, json=params)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        output_data = base64.b64decode(response.json()['output'])
        with open(f'output/{int(time.time())}.mp4', 'wb') as f:
            f.write(output_data)
    else:
        print("Error: The request did not succeed.")


request(source_paths, target_path)