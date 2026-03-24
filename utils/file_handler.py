def write_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(str(data) + '\n')
            print("Data written to file successfully")
    except Exception as e:
        print(e)


def get_user_from_file(filename, id) -> bool | dict:
    try:
        with open(filename, 'r') as file:
            data = file.read()
            for user in data:
                if user.get('id') == id:
                    return user
        return False
    except Exception as e:
        print(e)
        return False