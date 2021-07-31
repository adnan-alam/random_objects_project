from flask import request, jsonify, make_response, send_from_directory
from app import app

from app.main.services import (
    RandomObjectsFileGenerator,
    get_random_objects_file_report,
    MEDIA_DIR_PATH,
)


@app.route("/api/v1/random-objects/generate", methods=["POST"])
def generate_random_objects_file():
    max_file_size = 2 * 1024 * 1024  # 2 MB
    file_name = "random_objects.txt"
    random_obj_file_generator = RandomObjectsFileGenerator(max_file_size, file_name)
    output_file = random_obj_file_generator.generate_file()
    url = f"/api/v1/download/{output_file}"
    status_code = 201
    return make_response(jsonify({"url": url}), status_code)


@app.route("/api/v1/download/<path:file_name>", methods=["GET"])
def download_random_objects_file(file_name):
    return send_from_directory(MEDIA_DIR_PATH, file_name, as_attachment=True)


@app.route("/api/v1/random-objects/report", methods=["GET"])
def get_random_objects_report():
    file_name = "random_objects.txt"
    report, file_not_found = get_random_objects_file_report(file_name)

    if file_not_found:
        error_msg = "File not found! Generate one first"
        status_code = 400
        return make_response(jsonify({"message": error_msg}), status_code)
    else:
        status_code = 200
        return make_response(jsonify(report), status_code)
