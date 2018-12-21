from tinderhandler import Tinder
from tinderhandler._sms_auth import get_token_sms
import urllib3

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    token = get_token_sms()
    print(token)
    t = Tinder(token=token)
    t.like_batch()
    t.like_batch()
    t.like_batch()
    t.like_batch()
    t.like_batch()
    t.like_batch()
    t.like_batch()
    t.like_batch()
    t.like_batch()
    t.like_batch()
    t.like_batch()
    t.like_batch()
