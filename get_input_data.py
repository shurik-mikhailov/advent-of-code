import requests

def get_input_data(year: int, task_number: int) -> str:
    try:
        session_cookie = open(f"../cookie.txt", 'r').read()
    except FileNotFoundError:
        raise FileNotFoundError('create cookie.txt file with session cookie')
    url = f'https://adventofcode.com/{year}/day/{task_number}/input'
    response = requests.get(url, cookies={'session': session_cookie})

    return response.text.strip()
