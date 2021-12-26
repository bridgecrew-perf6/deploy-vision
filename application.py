
from flask import Flask, render_template, request, redirect, url_for

import os
import config
import face_exp2
application = Flask(__name__)

#save images to static/images folder
application.config['IMAGE_UPLOADS'] = f'static/Images'

#importing images with greater security.
#prevent hacking/phishing
from werkzeug.utils import secure_filename



@application.route('/img/<filename>/<age>/<gender>/<mood>')
def img(filename,age, gender, mood):

    return render_template("img.html",filename=filename ,age=age, gender=gender, mood=mood)
@application.route('/',methods=['POST', "GET"])
def upload_image():
    if request.method == "POST":
   
        #capture file name
    
        image = request.files['file-upload-field']
    
        #if file has no name
        if image.filename == '':
          
            
            return redirect(request.url)
      
        filename = secure_filename(image.filename)
   
        #access directory of folder to upload our file.
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir, application.config['IMAGE_UPLOADS'], filename))
     
        #predict mood
        mood = face_exp2.face_exp(f'static/Images/{filename}')
        mood[0].upper()
      
        age, gender = face_exp2.gender_age(f'static/Images/{filename}')
     
        return redirect(url_for('img', filename=filename, age=age, gender=gender, mood=mood))
    return render_template("main.html")


#route to display the image
@application.route('/display/<filename>')
def display_image(filename):
    
    return redirect(url_for('static', filename='/Images/'+filename), code=301) #code=301 for security




if __name__ == '__main__':
    application.run()
