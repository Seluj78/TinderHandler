from tinderhandler import Tinder
from tinderhandler._sms_auth import get_token_sms
import urllib3

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    answer = int(input("Press 1 if you want login auth or 2 if you want sms auth:\n"))
    answer = int(answer)
    if answer != 1 and answer != 2:
        raise ValueError("Input must be 1 or 2.")
    else:
        if answer == 1:
            fb_email = input("Enter your facebook email:\n")
            fb_password = input("Enter your facebook password:\n")
            t = Tinder(fb_email=fb_email, fb_password=fb_password)
            print(t.tinder_token)
            t.like_batch()
        elif answer == 2:
            token = get_token_sms()
            print(token)
            t = Tinder(token=token)
            t.like_batch()
