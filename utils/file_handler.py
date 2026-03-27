import aiofiles
import json
import os

def write_to_file(filename, data):
    try:
        data_file = get_data_from_file(filename)
        lst = []
        if data_file:
            lst.append(data_file)

        with open(filename, 'w') as file:
            lst.append(data)
            json.dump(lst, file)
            # file.write(str(data) + '\n')
            print("Data written to file successfully")
    except Exception as e:
        print(e)





async def write_to_file_async(filename, data):
    try:
        if os.path.exists(filename):
            async with aiofiles.open(filename, "r", encoding = "utf-8") as file:
                content = await file.read()
                data_list = json.loads(content) if content else []
        else:
            data_list = []

        data_list.append(data)

        async with aiofiles.open(filename, "w", encoding = "utf-8") as file:
            await file.write(json.dumps(data_list, ensure_ascii = False, indent = 4))

    except Exception as e:
        print(f"Ошибка записи: {e}")



def get_data_from_file(filename):
    try:
        with open(filename) as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(e)


def get_user_from_file(filename, id) -> bool | dict:
    try:
        with open(filename) as file:
            data = json.load(file)
            for user in data:
                if user.get('id') == id:
                    return user
            return False
        # with open(filename, 'r') as file:
        #     data = file.read()
        #     for user in data:
        #         if user.get('id') == id:
        #             return user
        # return False
    except Exception as e:
        print(e)
        return False