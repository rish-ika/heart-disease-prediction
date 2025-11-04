import pickle
from flask import Flask,render_template,request
app=Flask(__name__)
load=pickle.load(open('heart_model.pkl','rb'))
@app.route('/')

def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    if request.method=="POST":
        Age=int(request.form['Age'])
        Sex=int(request.form['Sex'])
        ChestPainType=int(request.form['ChestPainType'])
        RestingBP=int(request.form['RestingBP'])
        Cholesterol	=int(request.form['Cholesterol'])
        RestingECG=int(request.form['RestingECG'])
        MaxHR=int(request.form['MaxHR'])
        Oldpeak	=int(request.form['Oldpeak'])
        ST_Slope=int(request.form['ST_Slope'])
        prediction= load.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,RestingECG,MaxHR,Oldpeak,ST_Slope]])
        if prediction==1:
            result="You have Heart Disease"
        else:
            result="You are Healthy"
        return render_template("index.html",prediction_text="{}".format(result))
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)