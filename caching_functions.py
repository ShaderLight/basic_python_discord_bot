import jsonpickle

import json

def find_cache(keyword, filename):
    assert type(keyword) == str and type(filename) == str
    
    try:
        with open(filename + '_cache.json', 'r') as file:
            data = json.load(file)
    except:
        with open(filename + '_cache.json', 'w') as file:
            json.dump({}, file, indent=4)
            return None
    
    for cached_keyword, cached_response in data.items():
        if cached_keyword == keyword:
            encoded_list = cached_response
            decoded_list = decode_list(encoded_list)
            return decoded_list

    return None


def cache_response(keyword, response, filename):
    cache_dict = {}
    cache_dict[keyword] = encode_list(response)

    with open(filename + '_cache.json','r') as file:
        data = json.load(file)
        data.update(cache_dict)

    with open(filename + '_cache.json', 'w') as file:
        json.dump(data, file, indent=4)


def encode_list(object_list):
    output_list = []
    for obj in object_list:
        output_list.append(jsonpickle.encode(obj))
    return output_list


def decode_list(object_list):
    output_list = []
    for obj in object_list:
        output_list.append(jsonpickle.decode(obj))
    return output_list