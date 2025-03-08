from flask import Flask, request, render_template
from rembg import remove
from PIL import Image
import io
import base64
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    img_data = None
    if request.method == "POST":
        if "file" not in request.files:
            return "Không tìm thấy file!"

        file = request.files["file"]
        if file.filename == "":
            return "Chưa chọn file!"

        # Xử lý ảnh
        input_image = Image.open(file)
        output_image = remove(input_image)

        # Chuyển ảnh thành base64 để hiển thị trên web
        img_io = io.BytesIO()
        output_image.save(img_io, "PNG")
        img_io.seek(0)
        img_data = base64.b64encode(img_io.getvalue()).decode("utf-8")

    return render_template("index.html", img_data=img_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Running on port: {port}")
    app.run(host="0.0.0.0", port=port)
