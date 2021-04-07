import requests


# 我这里是将经纬度转换为地址，所以选用的是逆地理编码的接口。
# https://restapi.amap.com/v3/geocode/regeo?
# output=xml&location=116.310003,39.991957&key=<用户的key>&radius=1000&extensions=all

# 高德地图
def regeocode(location):
    parameters = {'output': 'json', 'location': location, 'key': 'b65ac7bac54ed07220e8d05ab93ad469',
                  'extensions': 'all'}
    base = 'https://restapi.amap.com/v3/geocode/regeo'
    response = requests.get(base, parameters)
    answer = response.json()
    print('url:' + response.url)
    print(answer)
    '''return answer['regeocode']['formatted_address'], answer['regeocode']['roads'][0]['id'], \
           answer['regeocode']['roads'][0]['name']'''


def geocode(address, city):
    '''
    :param address:地址串
    :param city: 城市名
    :return: street:四级地址
             label:标签
    '''
    url = 'http://restapi.amap.com/v3/geocode/geo'

    parameters = {
        'address': address,
        'key': 'b65ac7bac54ed07220e8d05ab93ad469',
        'city': city
    }
    try:
        res = requests.get(url, parameters)
        street = res.json()['geocodes'][0]['street']
        if street != []:
            return street
        else:
            return street, 0
    except :
        return "", -1


# 处理正常地址
    print(street)

# 百度地图
def geocodebaidu(location):
    parameters = {'location': location, 'output': 'json', 'coordtype': 'gcj02ll',
                  'pois': '0', 'latest_admin': '1', 'ak': 'FUu6OTikvprEEwd1qL9X23a9PGq05efW', 'extensions_road': 'true'}
    base = 'http://api.map.baidu.com/geocoder/v2/'
    response = requests.get(base, parameters)
    # response=requests.get('http://api.map.baidu.com/geocoder/v2/?location=30.48686,104.07649&output=json&pois=1&latest_admin=1&ak=U1ck8zXZpoWGYqv2ozr8Xa3IraDfy4Vw')
    print('url:' + response.url)
    answer = response.json()
    print(answer)
    return answer['result']['formatted_address'], answer['result']['addressComponent']['adcode'], \
           answer['result']['addressComponent']['street']

def route_planning(start,end):
    base = 'https://restapi.amap.com/v3/direction/walking?parameters'
    parameters = {
        'key': '5b075bd243a18155fbc164db0c3e426b',
        'origin': str(start),
        'destination': str(end)
    }

    response = requests.get(base, parameters)
    answer = response.json()
    print(answer)


xtmp = 104.07649
ytmp = 30.48686
locations = str(ytmp) + ',' + str(xtmp)
regeocode(locations)
'''detail, id, name = regeocode(locations)
print(detail)
print(id)
print(name)
geocode('上海市浦东区世纪大道1号', '上海')'''
