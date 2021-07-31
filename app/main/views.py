from flask import request, jsonify, make_response, send_from_directory
from app import app

from app.main.services import (
    RandomObjectsFileGenerator,
    get_random_objects_file_report,
    MEDIA_DIR_PATH,
)


@app.route("/random-objects/generate", methods=["POST"])
def generate_random_objects_file():
    max_file_size = 2 * 1024 * 1024  # 2 MB
    file_name = "random_objects.txt"
    random_obj_file_generator = RandomObjectsFileGenerator(max_file_size, file_name)
    output_file = random_obj_file_generator.generate_file()
    url = f"/download/{output_file}"
    status_code = 201
    return make_response(jsonify({"url": url}), status_code)
