from main import *
import time


def get_posts(wall_id):
    data = session.method("wall.get", {"owner_id": wall_id, "count": 1, "offset": 1})  # 1
    return data


def get_group_id(name):
    tmp1 = session.method("utils.resolveScreenName", {"screen_name": name})
    wall_id = tmp1['object_id'] * (-1)
    return wall_id


def add_post_photos_on_wall(owner_id, text, photo):
    session.method("wall.post", {"owner_id": owner_id, "from_group": 1, "message": text, "attachments": photo})


def add_video_on_wall(owner_id, text, info):
    session.method("wall.post", {"owner_id": owner_id, "from_group": 1, "message": text,
                                 "attachments": f"video{info[0]['video']['owner_id']}_{info[0]['video']['id']}"})


def add_text_on_wall(owner_id, text):
    session.method("wall.post", {"owner_id": owner_id, "from_group": 1, "message": text})


def get_string_parameters(wall_id, num_photos):
    i = 0
    photo = ''
    data1 = get_posts(wall_id)
    type_data = data1['items'][0]['attachments'][i]['type']
    while i < num_photos:
        photo = photo + f"{type_data}{data1['items'][0]['attachments'][i][type_data]['owner_id']}_{data1['items'][0]['attachments'][i][type_data]['id']}"
        if i + 1 != num_photos:
            photo = photo + ','
            i = i + 1
            type_data = data1['items'][0]['attachments'][i]['type']
        elif i + 1 == num_photos:
            break
    return photo


def parser(group_name, owner_id, date, post_counter, timing, end_time):
    print("thief of pretty cats or whatever kind of posts you want")
    wall_id = get_group_id(group_name)
    data = get_posts(wall_id)
    date_of_post = data['items'][0]['date']

    if date_of_post > date:
        if post_counter[0] < 50:
            flag = 0
            text = data['items'][0]['text']
            try:
                info = data['items'][0]['attachments']
            except KeyError:
                flag = 1
            post_counter[0] += 1
            if flag == 0:
                if info[0]['type'] == 'photo':
                    num_photos = len(data['items'][0]['attachments'])
                    if num_photos > 6:
                        num_photos = 5
                    photo = get_string_parameters(wall_id, num_photos)
                    add_post_photos_on_wall(owner_id, text, photo)

                    return date_of_post
                elif info[0]['type'] == 'video':
                    add_video_on_wall(owner_id, text, info)
                    return date_of_post
                else:
                    return date_of_post
            elif flag == 1:
                add_text_on_wall(owner_id, text)
                return date_of_post
        elif post_counter[0] >= 50:
            post_counter[0] = 0
            deactivate = end_time[0] - time.time() + 60 * 30
            time.sleep(deactivate)
            timing[0] = time.time()
            end_time[0] = 60 * 60 * 24 + time.time()
            return date
    elif date_of_post <= date:
        return date
