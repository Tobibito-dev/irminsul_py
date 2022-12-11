api_url = "https://api.irminsul.info"
res_url = "https://enka.network/ui"
local_url = "data"


class Url:
    API = 'api'
    RESOURCES = 'res'
    LOCAL = 'local'


def change_url(url_type: str, new_url: str):
    if url_type == 'api':
        global api_url
        api_url = new_url
    elif url_type == 'res':
        global res_url
        res_url = new_url
    elif url_type == 'local':
        global local_url
        local_url = new_url


def get_url(url_type: str):
    if url_type == 'api':
        return api_url
    elif url_type == 'res':
        return res_url
    elif url_type == 'local':
        return local_url
