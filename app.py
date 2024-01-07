#Implement all this concept by machine learning with flask

from flask import Flask, escape, request, render_template  #basic format for flask
import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer #to import the func so that .....conversion of text to feature vectors or numbers
# load the model in read binary mode
vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  #index as first page

@app.route('/prediction', methods=['GET', 'POST']) #on click prediction will be hitted and thus this action is performed 
def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)

        predict = model.predict(vector.transform([news]))[0]         #predict on user text by our model
        print(predict)

        return render_template("prediction.html", prediction_text="News headline is -> {}".format(predict))


    else:
        return render_template("prediction.html")


if __name__ == '__main__':
    app.debug = True
    app.run()