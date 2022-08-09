import requests
import json

url = "https://randomuser.me/api"


def get_user_by(users_data: dict) -> dict:
    '''
    get user from response.

    Args:
        users_data (dict): response user

    Return:
        dict: user object
    '''

    user = dict()

    user['first_name'] = users_data['name']['first']
    user['last_name']  = users_data['name']['last']
    user['gender']     = users_data['gender']
    user['city']       = users_data['location']['city']
    user['age']        = users_data['dob']['age']

    return user


def main(n: int, url: str) -> None:
    '''
    main function.

    Args:
        n (int): users count

    Returns:
        None: create json file
    '''

    users = list()

    while len(users) <= n:
        response = requests.get(url=url)

        if response.status_code == 200:
            users_data = response.json()['results'][0]

            if users_data['gender'] == 'male':
                user = get_user_by(users_data)
                print("done")
                users.append(user)

    
    results = {
        'results': users
    }
    users_json = json.dumps(results, indent=4)

    f = open("users_data.json", "w")
    f.write(users_json)
    f.close()

main(10, url)



