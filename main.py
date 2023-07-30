
from flask import Flask, render_template , request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from pathlib import Path
import tempfile
import cv2


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
# @app.route('/home', methods=['GET',"POST"])
def home():
   form = UploadFileForm()
   if form.validate_on_submit():
       file = form.file.data # First grab the file
       file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
   return render_template('index.html', form=form)

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method=='POST':
        uploaded_file = request.files['file']
        with tempfile.TemporaryDirectory() as td:
            temp_filename = Path(td) / 'uploaded_video'
            uploaded_file.save(temp_filename)
            vidcap = cv2.VideoCapture(str(temp_filename))
    result_get="resultlicense"
    return render_template('result.html' , result_get=result_get)

def process():
    vidcap = cv2.VideoCapture(file)
    return vidcap;
    return jpeg.tobytes()

if __name__ == '__main__':
    app.run(debug=True)
