from flask import Flask, jsonify, request



app = Flask(__name__)

@app.route('/model/fill',methods=['POST'])
def fileupload():
    
    resp={}
    
    data=request.args.get('date')
    if not date:
        resp['status']=400
        resp['msg']="fail"
        return jsonify(resp),400
    """
    try:
        model
    except:
        pass
    else:
        resp['status']=200
        resp['msg']='yesyesy'
    return jsonify(resp)

    """
    
@app.route('/nst_post', methods=['GET','POST'])
def nst_post():
    if request.method == 'POST':
        # Reference Image
        refer_img = request.form['refer_img']
        refer_img_path = 'static/images/'+str(refer_img)
 
        # User Image (target image)
        user_img = request.files['user_img']
        user_img.save('./flask_deep/static/images/'+str(user_img.filename))
        user_img_path = './static/images/'+str(user_img.filename)
 
        # Neural Style Transfer 
        transfer_img = modelname.main(refer_img_path, user_img_path)
        transfer_img_path = './static/images/'+str(transfer_img.split('/')[-1])
 
    return render_template('nst_post.html', 
                    refer_img=refer_img_path, user_img=user_img_path, transfer_img=transfer_img_path)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

