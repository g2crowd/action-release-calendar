from datetime import date, datetime
from pytz import timezone
from github import Github
import datetime as date_time
import yaml
import argparse
import sys
import calendar
import pytz
import os
import urllib

def load_config(filename):
    git = Github(os.environ['GITHUB_TOKEN'])
    repo = git.get_repo(os.environ['GITHUB_REPOSITORY'])
    contents = repo.get_contents(filename, ref=repo.default_branch)
    config = contents.decoded_content.decode()
    return yaml.safe_load(config)

def validate_config(config):
    if not 'working_days' in config:
        sys.exit('Error: working_days missing in calendar config!')
    if not 'working_time' in config:
        sys.exit('Error: working_time missing in calendar config!')
    if not 'start' in config['working_time']:
        sys.exit('Error: working_time.start missing in calendar config!')
    if not 'end' in config['working_time']:
        sys.exit('Error: working_time.end missing in calendar config!')

def current_datetime(zone):
    today = date_time.date.today()
    now_date = "{:%Y/%m/%d}".format(today)
    now_day = datetime.today().strftime('%A')
    time_format = "%H:%M"
    now_utc = datetime.now(timezone('UTC'))
    now_zone = now_utc.astimezone(timezone(zone))
    now_time = now_zone.strftime(time_format)

    return now_day, now_date, now_time

def is_working_day(config, day):
    if day in config['working_days']:
        return True
    else:
        return False

def is_working_time(config, time):
    start_time = str(config['working_time']['start']).split('.')
    end_time = str(config['working_time']['end']).split('.')
    now_time = time.split(':')
    start = date_time.time(int(start_time[0]), int(start_time[1]), 0)
    end = date_time.time(int(end_time[0]), int(end_time[1]), 0)
    now = date_time.time(int(now_time[0]), int(now_time[1]), 0)

    if start <= end:
        return start < now < end
    else:
        return start < now or now < end

def is_holiday(config, date):
    if date in config['holidays']:
        return True
    else:
        return False

def main():
    parser = argparse.ArgumentParser(description='Check whether release allowed or not')
    parser.add_argument('-c','--config', default='.github/release_calendar.yml')
    parser.add_argument('-t','--timezone', default='Asia/Kolkata')
    args = parser.parse_args()

    config = load_config(args.config)
    validate_config(config)
    day, date, time = current_datetime(args.timezone)
    if is_working_day(config, day) and is_working_time(config, time) and not is_holiday(config, date):
        sys.exit(0)
    else:
        sys.exit('Release freezed!')

if __name__ == "__main__":
    main()
