from flask import Flask,jsonify,request
app=Flask(__name__)
app.id_count=1
app.users={}
app.tweets=[]

@app.route("/ping",methods=['GET'])
def ping():
    return "pong"

@app.route("/sign-up",methods=['POST'])
def sign_up():
    new_user=request.json
    new_user["id"]=app.id_count
    app.users[app.id_count]=new_user
    app.id_count=app.id_count+1

    return jsonify(new_user)

@app.route("/tweet",methods=['POST'])
def tweet():
    upload_info=request.json
    user_id=int(upload_info['id'])
    tweet=upload_info["tweet"]

    if len(tweet)>300:
        return "300자 초과",400
    app.tweets.append({'user_id':user_id,'tweet':tweet})
    return '',200