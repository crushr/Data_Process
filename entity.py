import requests
import base64
import pickle

val = pickle.load(open('/Users/zhongshannan/Documents/fakenews_detection/dataset/weiboA/validate.pickle', 'rb'))
val_id = pickle.load(open('/Users/zhongshannan/Documents/fakenews_detection/dataset/weiboA/validate_id.pickle', 'rb'))
print(val.keys())

val['event'] = []
for id_ in val['id']:
    val['event'].append(val_id[id_])
print(val.keys())

root = '/Users/zhongshannan/Documents/fakenews_detection/dataset/weibo/all_images/'
val['image_entity'] = []
for image in val['image']:
    image_path = root + image[0]

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    # 二进制方式打开图片文件
    f = open(image_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = '24.4620f18817784443a7d292f169bed9b0.2592000.1652362821.282335-25954805'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    image_entity = response.json
    
    val['image_entity'].append(image_entity)
    print(image[0])








# temp = pd.read_csv('/Users/zhongshannan/Documents/fakenews_detection/dataset/weibo/weibo_train.csv')
# temp_arr = np.array(temp)
# root = '/Users/zhongshannan/Documents/fakenews_detection/dataset/weibo/all_images/'

# new = []

# for i in range(len(temp_arr)):
#     image_path = root + temp_arr[i][1]

#     request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"

#     # 二进制方式打开图片文件
#     f = open(image_path, 'rb')
#     img = base64.b64encode(f.read())

#     params = {"image":img}
#     access_token = '24.fb8b685b4483a724e3e1cb21399f8818.2592000.1652409489.282335-25956725'
#     request_url = request_url + "?access_token=" + access_token
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.post(request_url, data=params, headers=headers)

#     str_ = ''
#     for k in range(len(response.json()['result'])):
#         str_ += response.json()['result'][k]['keyword'] + ' '

#     print(str_)
#     list_ = list(temp_arr[i])
#     list_.append(str_)
#     new.append(list_)

# new_arr = np.asarray(new)

# file_ = pd.DataFrame(new_arr, columns=['text','image','label','event_label', 'image_entity'])
# file_.to_csv('/Users/zhongshannan/Documents/fakenews_detection/dataset/weibo/weibo_train_entity.csv',encoding='utf-8',index=False)