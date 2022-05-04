import requests
import json
from main import *


# Function of adding posts on my wall (from pc). This func isn't used in main.
def get_data_photo(owner_id):
    photo_data = session.method("photos.getWallUploadServer", {"owner_id": owner_id*(-1)})
    print("Msg1", photo_data["upload_url"])
    return photo_data


# Makes request to post (from pc). This func isn't used in main.
def my_request(owner_id):
    # Get URL address
    upload_url = get_data_photo(owner_id)["upload_url"]
    # Working with request
    img1 = {'file1': ('img.jpg', open(r'/home/tim/python/vkBot/cat_bot/spike1.jpg', 'rb')), 'file2':
            ('img.jpg', open(r'/home/tim/python/vkBot/cat_bot/spike2.jpg', 'rb'))}
    response = requests.post(upload_url, files=img1)
    result = json.loads(response.text)
    print("Msg2", result)
    # Save wall photo
    save_data = session.method("photos.saveWallPhoto", result)
    session.method("wall.post", {"owner_id": owner_id, "from_group": 1, "message": "Two pics",
                                 "attachments": f"photo{save_data[0]['owner_id']}_{save_data[0]['id']},"
                                                f"photo{save_data[1]['owner_id']}_{save_data[1]['id']}"})