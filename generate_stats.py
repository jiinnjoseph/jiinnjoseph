import datetime
from dateutil import relativedelta
import requests
import os
from lxml import etree
import time
import hashlib
import xml.sax.saxutils as saxutils
from PIL import Image
import re

TOKEN = os.environ.get('ACCESS_TOKEN') or os.environ.get('GITHUB_TOKEN')
HEADERS = {'authorization': 'token ' + TOKEN} if TOKEN else {}
USER_NAME = os.environ.get('USER_NAME', 'Heyjithin')
QUERY_COUNT = {'user_getter': 0, 'follower_getter': 0, 'graph_repos_stars': 0, 'recursive_loc': 0, 'graph_commits': 0, 'loc_query': 0}

def daily_readme(birthday):
    diff = relativedelta.relativedelta(datetime.datetime.today(), birthday)
    return '{} {}, {} {}, {} {}{}'.format(
        diff.years, 'year' + format_plural(diff.years), 
        diff.months, 'month' + format_plural(diff.months), 
        diff.days, 'day' + format_plural(diff.days),
        ' 🎂' if (diff.months == 0 and diff.days == 0) else '')

def format_plural(unit):
    return 's' if unit != 1 else ''

def simple_request(func_name, query, variables):
    if not TOKEN:
        raise Exception("No ACCESS_TOKEN provided for GraphQL query")
    request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables}, headers=HEADERS)
    if request.status_code == 200:
        return request
    raise Exception(func_name, ' has failed with code ', request.status_code, request.text, QUERY_COUNT)

def user_getter(username):
    query_count('user_getter')
    if TOKEN:
        try:
            query = '''
            query($login: String!){
                user(login: $login) {
                    id
                    createdAt
                }
            }'''
            request = simple_request('user_getter', query, {'login': username})
            return {'id': request.json()['data']['user']['id']}, request.json()['data']['user']['createdAt']
        except Exception:
            pass
    r = requests.get(f'https://api.github.com/users/{username}', headers=HEADERS).json()
    return {'id': r.get('id', 0)}, r.get('created_at', '2026-03-14T06:16:21Z')

def follower_getter(username):
    query_count('follower_getter')
    if TOKEN:
        try:
            query = '''
            query($login: String!){
                user(login: $login) {
                    followers {
                        totalCount
                    }
                }
            }'''
            request = simple_request('follower_getter', query, {'login': username})
            return int(request.json()['data']['user']['followers']['totalCount'])
        except Exception:
            pass
    r = requests.get(f'https://api.github.com/users/{username}', headers=HEADERS).json()
    return int(r.get('followers', 2))

def graph_repos_stars(count_type, owner_affiliation, cursor=None):
    query_count('graph_repos_stars')
    if TOKEN:
        try:
            query = '''
            query ($owner_affiliation: [RepositoryAffiliation], $login: String!, $cursor: String) {
                user(login: $login) {
                    repositories(first: 100, after: $cursor, ownerAffiliations: $owner_affiliation) {
                        totalCount
                        edges {
                            node {
                                ... on Repository {
                                    nameWithOwner
                                    stargazers {
                                        totalCount
                                    }
                                }
                            }
                        }
                    }
                }
            }'''
            request = simple_request('graph_repos_stars', query, {'owner_affiliation': owner_affiliation, 'login': USER_NAME, 'cursor': cursor})
            if count_type == 'repos':
                return request.json()['data']['user']['repositories']['totalCount']
            elif count_type == 'stars':
                return stars_counter(request.json()['data']['user']['repositories']['edges'])
        except Exception:
            pass
    
    r = requests.get(f'https://api.github.com/users/{USER_NAME}/repos?per_page=100', headers=HEADERS).json()
    if isinstance(r, list):
        if count_type == 'repos':
            return len(r)
        elif count_type == 'stars':
            return sum(repo.get('stargazers_count', 0) for repo in r)
    return 9 if count_type == 'repos' else 0

def stars_counter(data):
    total_stars = 0
    for node in data:
        total_stars += node['node']['stargazers']['totalCount']
    return total_stars

def commit_counter():
    try:
        r = requests.get(f'https://api.github.com/search/commits?q=author:{USER_NAME}', headers=HEADERS)
        if r.status_code == 200:
            return r.json().get('total_count', 26)
    except Exception:
        pass
    return 26

def query_count(funct_id):
    global QUERY_COUNT
    QUERY_COUNT[funct_id] += 1

def perf_counter(funct, *args):
    start = time.perf_counter()
    funct_return = funct(*args)
    return funct_return, time.perf_counter() - start

def formatter(query_type, difference, funct_return=False):
    print('{:<23}'.format('   ' + query_type + ':'), end='')
    print('{:>12}'.format('%.4f' % difference + ' s ')) if difference > 1 else print('{:>12}'.format('%.4f' % (difference * 1000) + ' ms'))
    return funct_return

def update_avatar_ascii():
    url = f"https://avatars.githubusercontent.com/u/268110323?v=4"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            with open("avatar.png", "wb") as f:
                f.write(r.content)
    except Exception:
        pass
    
    if not os.path.exists("avatar.png"):
        return

    def image_to_ascii(img_path, width, height, invert=False):
        img = Image.open(img_path).convert('L')
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        chars = [' ', '.', ':', '-', '=', '+', '*', '%', '#', '@']
        if invert:
            chars = chars[::-1]
        lines = []
        for y in range(height):
            line = ''
            for x in range(width):
                p = img.getpixel((x, y))
                idx = int(p / 256 * len(chars))
                idx = min(idx, len(chars) - 1)
                line += chars[idx]
            lines.append(line)
        return lines

    def inject_ascii(svg_path, width, height, invert, fill_color):
        ascii_lines = image_to_ascii('avatar.png', width, height, invert=invert)
        with open(svg_path, 'r', encoding='utf-8') as f:
            file_lines = f.readlines()
        
        ascii_idx = 0
        new_file_lines = []
        for line in file_lines:
            match = re.search(r'<text x="28" y="([^"]+)" fill="[^"]+" font-family="[^"]+" xml:space="preserve" font-size="8">(.*?)</text>', line)
            if match:
                y_val = match.group(1)
                if ascii_idx < len(ascii_lines):
                    escaped_text = saxutils.escape(ascii_lines[ascii_idx])
                    new_line = f'  <text x="28" y="{y_val}" fill="{fill_color}" font-family="\'Consolas\', \'Menlo\', \'DejaVu Sans Mono\', monospace" xml:space="preserve" font-size="8">{escaped_text}</text>\n'
                    new_file_lines.append(new_line)
                    ascii_idx += 1
                else:
                    new_file_lines.append(line)
            else:
                new_file_lines.append(line)

        with open(svg_path, 'w', encoding='utf-8') as f:
            f.writelines(new_file_lines)

    inject_ascii('dark_mode.svg', 65, 37, False, '#c9d1d9')
    inject_ascii('light_mode.svg', 96, 50, True, '#24292f')

def svg_overwrite(filename, age_data, commit_data, star_data, repo_data, follower_data):
    if not os.path.exists(filename):
        return
    tree = etree.parse(filename)
    root = tree.getroot()
    justify_format(root, 'commit_data', commit_data, 12)
    justify_format(root, 'star_data', star_data, 14)
    justify_format(root, 'repo_data', repo_data, 6)
    justify_format(root, 'follower_data', follower_data, 10)
    justify_format(root, 'age_data', age_data, 20)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def justify_format(root, element_id, new_text, length=0):
    if isinstance(new_text, int):
        new_text = f"{'{:,}'.format(new_text)}"
    new_text = str(new_text)
    find_and_replace(root, element_id, new_text)
    just_len = max(0, length - len(new_text))
    if just_len <= 2:
        dot_map = {0: '', 1: ' ', 2: '. '}
        dot_string = dot_map[just_len]
    else:
        dot_string = ' ' + ('.' * just_len) + ' '
    find_and_replace(root, f"{element_id}_dots", dot_string)

def find_and_replace(root, element_id, new_text):
    element = root.find(f".//*[@id='{element_id}']")
    if element is not None:
        element.text = new_text

if __name__ == '__main__':
    print('Calculation times:')
    user_data, user_time = perf_counter(user_getter, USER_NAME)
    OWNER_ID, acc_date = user_data
    formatter('account data', user_time)
    
    created_dt = datetime.datetime.strptime(acc_date[:10], '%Y-%m-%d')
    age_data, age_time = perf_counter(daily_readme, created_dt)
    formatter('uptime calculation', age_time)
    
    commit_data, commit_time = perf_counter(commit_counter)
    star_data, star_time = perf_counter(graph_repos_stars, 'stars', ['OWNER'])
    repo_data, repo_time = perf_counter(graph_repos_stars, 'repos', ['OWNER'])
    follower_data, follower_time = perf_counter(follower_getter, USER_NAME)

    update_avatar_ascii()

    svg_overwrite('dark_mode.svg', age_data, commit_data, star_data, repo_data, follower_data)
    svg_overwrite('light_mode.svg', age_data, commit_data, star_data, repo_data, follower_data)

    print('Profile card stats successfully updated!')
