from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json 

NJ_SOLD_URL = 'https://www.zillow.com/nj/sold/?searchQueryState=%7B%22usersSearchTerm%22%3A%22new%20jersey%22%2C%22mapBounds%22%3A%7B%22west%22%3A-83.19478098437499%2C%22east%22%3A-68.91255442187499%2C%22south%22%3A34.08762938075141%2C%22north%22%3A45.3200386163014%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A40%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22doz%22%3A%7B%22value%22%3A%226m%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'
def cookie_parser():
    cookie_string = 'zguid=23|%2422076a31-437d-4207-8326-1ad0598ad7da; zgsession=1|4d0f4405-af7b-4bba-a063-d60db06188f2; _ga=GA1.2.1165413865.1623343194; _pxvid=7b935055-ca0a-11eb-af86-0242ac120010; _gcl_au=1.1.1066147500.1623343194; DoubleClickSession=true; __pdst=286c1e31a02b4273b63e5655282e6068; _fbp=fb.1.1623343193835.1440686999; _pin_unauth=dWlkPVl6TXlNak5tTldVdFpUQmlZUzAwTkRFNUxUazNZVGd0WWprell6SXhNalZrWVRWbQ; KruxPixel=true; KruxAddition=true; g_state={"i_p":1623768833578,"i_l":2}; G_ENABLED_IDPS=google; userid=X|3|2201da6324e337d3%7C3%7CB7ftjC9VPdzkexG2bRdjT0tSjdOtMnJPRRKUZ-Rgl8lamen7c9qWKA%3D%3D; loginmemento=1|9195b1a922d98dedd3234291b51563447ee16d5a5d552b7f2bdef5804c45e25f; zjs_user_id=%22X1-ZUtku28039d98p_1r7ky%22; optimizelyEndUserId=oeu1623695349709r0.8247443086356552; _cs_c=1; zjs_anonymous_id=%2222076a31-437d-4207-8326-1ad0598ad7da%22; _gid=GA1.2.1839560673.1623795885; JSESSIONID=D09A65A12DD57D06E3EC2B0A8745ECC8; ZILLOW_SID=1|AAAAAVVbFRIBVVsVEgPhhCzkgdA59oIedq%2FKf6My%2BywS04coy1zCy5mRqgQ73BEb9SLrFZe6MFVhTltU8weg0skzuppf; _pxff_bsco=1; utag_main=v_id:0179f6cb5f15007b95fec94a00fc02078001707000bd0$_sn:5$_se:1$_ss:1$_st:1623869911532$dc_visit:2$ses_id:1623868111532%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:us-east-1%3Bexp-session$ttd_uuid:8c7a2fe0-9fe8-488e-a021-adb2fcaf8965%3Bexp-session; intercom-session-xby8p85u=L2puN2ROT3Jyejc2MFBBRDNZbTNmZmdCUGJ4R3FuazlLb2EyZ2dxUFhyR0l1VS93YXd0K3lxS20rVjkzdmNhYS0tWVhJeXdEYXBDbGZXb3c2T1dPdjlTQT09--28944b7416931315f677355fc020bbbe18d97f49; _uetsid=7d0b0240ce2811eb979737521e997969; _uetvid=7ba8dab0ca0a11ebb06103cac4a33064; _px3=34edbce0e250e3133b1bcaa7375931931c8a26d7618c7aa947788e539ea4c617:mkbvclm7nQ1yTq5cUCgMSJKCx0bAbUzGOkmqRhqkPjy2+nxBjExprYU97hzQpx5ABk3TFcXIwh2uD9KDUzzurQ==:1000:9o99FLReSkWJz/eJWamw0pROYHmaGGn+yRAhRWRfhQOiIvOl8cCOXC1KIPkxdQpDc7u8yixDQ1t9ws1rf/TSnLayEKYuweqO68Gj0UMyGoO1mPE0inc3wPGGNFvMSVxCZ29VqVEsgt096L3y83afMwXBgbk5FTgcuK4FSwN5vL0Pv25gCBvs5V9ZlQ0Mf4bYagJ3YVv2NcS6vqgRgRQziw==; _gat=1; AWSALB=spZW6r3LRQHPTcaF1MO8hwi75208+G5dfjJZKt5qOPJKc/zUzlT7Oykn/k2c7qNZHE4iZTfB+Za3nFBagcoXavOSALNfEib+mF8qatCSfmzeEV+D1CLN4Jf6x7vt; AWSALBCORS=spZW6r3LRQHPTcaF1MO8hwi75208+G5dfjJZKt5qOPJKc/zUzlT7Oykn/k2c7qNZHE4iZTfB+Za3nFBagcoXavOSALNfEib+mF8qatCSfmzeEV+D1CLN4Jf6x7vt; search=6|1626460170591%7Crect%3D45.3200386163014%252C-68.91255442187499%252C34.08762938075141%252C-83.19478098437499%26rid%3D40%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26sort%3Ddays%26z%3D1%26days%3D6m%26fs%3D0%26fr%3D0%26mmm%3D0%26rs%3D1%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%0940%09%09%09%09%09%09'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies = {}
    print(cookie)
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies

def parse_new_url(url,pg_num):
    url_parsed = urlparse(url)
    query_str = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_str.get('searchQueryState')[0])
    search_query_state['pagination'] = {"currentPage": pg_num}
    query_str.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_str, doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url

#print(parse_new_url(NJ_SOLD_URL, 22))


