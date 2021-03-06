import os
import random
import string


PROJECT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

MEDIA_DIR = "media"

MEDIA_DIR_PATH = os.path.join(PROJECT_DIR, MEDIA_DIR)


class RandomObjectsFileGenerator:
    def __init__(self, max_file_size, file_name):
        self.max_file_size = max_file_size
        self.file_name = file_name

    def _random_alphanumerics(self):
        size = random.randint(5, 20)
        obj = "".join(
            random.choice(string.ascii_lowercase + string.digits) for _ in range(size)
        )
        return obj

    def _random_string(self):
        size = random.randint(5, 20)
        obj = "".join(random.choice(string.ascii_lowercase) for x in range(size))
        return obj

    def _random_integer(self):
        obj = random.randint(1, 99999)
        return obj

    def _random_real_number(self):
        decimal_places_len = random.randint(1, 5)
        obj = round(random.uniform(-99999, 99999), decimal_places_len)
        return obj

    def generate_file(self):
        # create media dir if not exists
        if not os.path.exists(MEDIA_DIR_PATH):
            os.mkdir(MEDIA_DIR_PATH)

        file_path = os.path.join(MEDIA_DIR_PATH, self.file_name)

        # initial file size
        file_size = 0

        with open(file_path, "w") as f_obj:
            random_methods_list = [
                self._random_alphanumerics,
                self._random_string,
                self._random_integer,
                self._random_real_number,
            ]

            while file_size < self.max_file_size:
                random_method = random.choice(random_methods_list)
                obj = str(random_method())
                f_obj.write(obj + ",")
                file_size = os.path.getsize(file_path)

        return self.file_name


def get_random_objects_file_report(file_name):
    file_path = os.path.join(MEDIA_DIR_PATH, file_name)

    file_not_found = False
    (
        total_alphabetical_strings,
        total_integers,
        total_real_numbers,
        total_alphanumerics,
    ) = [0] * 4

    if os.path.exists(file_path):
        with open(file_path, "r") as f_obj:
            file_content = f_obj.read().strip(",")
            objects_list = file_content.split(",")

            for obj in objects_list:
                if obj.isalpha():
                    total_alphabetical_strings += 1
                elif obj.isdigit():
                    total_integers += 1
                elif obj.isalnum():
                    total_alphanumerics += 1
                else:
                    total_real_numbers += 1
    else:
        file_not_found = True

    report = {
        "total_alphabetical_strings": total_alphabetical_strings,
        "total_integers": total_integers,
        "total_real_numbers": total_real_numbers,
        "total_alphanumerics": total_alphanumerics,
    }
    return (report, file_not_found)
