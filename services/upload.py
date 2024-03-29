from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from utils.upload import save_file, allowed_file

blueprint = Blueprint("upload", __name__, url_prefix="/upload")


@blueprint.route("", methods=["POST"])
@jwt_optional
def upload():
    image = request.files.get("file")
    if image and allowed_file(image.filename):
        url = save_file(image)
        return jsonify({"url": url})
    else:
        return jsonify({"error": "400 Bad Request"}), 400
