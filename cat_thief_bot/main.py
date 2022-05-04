import vk_api
import time
from my_token import *
from functions import *
session = vk_api.VkApi(token=my_token)


def main():
    owner_id = my_owner_id
    name = ['ave_catt', 'meowkyit', '40cats', 'kotyambusi']
    date = [0]*len(name)
    while True:
        for i in range(len(name)):
            date[i] = parser(name[i], owner_id, date[i])
        time.sleep(30)


if __name__ == "__main__":
    main()













