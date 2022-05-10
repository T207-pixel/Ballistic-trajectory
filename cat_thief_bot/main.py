import vk_api
import time
from my_token import *
from functions import *
session = vk_api.VkApi(token=my_token)


def main():
    owner_id = my_owner_id
    post_counter = [0]
    name = ['ave_catt', 'meowkyit', '40cats', 'kotyambusi']
    date = [0]*len(name)
    timing = [time.time()]
    end_time = [60 * 60 * 24 + time.time()]
    while True:
        if time.time() - timing[0] >= 60 * 60 * 24:  # 24h
            timing[0] = time.time()
            end_time[0] = 60 * 60 * 24 + time.time()
        elif time.time() - timing[0] < 60 * 60 * 24:  # 24h
            for i in range(len(name)):
                date[i] = parser(name[i], owner_id, date[i], post_counter, timing, end_time)
            time.sleep(60*30)



if __name__ == "__main__":
    main()













