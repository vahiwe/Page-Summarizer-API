from flask import url_for,request,Flask,render_template,jsonify
import pickle
from sklearn.externals import joblib




app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/summarize',methods=['POST'])
def summarize():

    if model:
        try:
            if request.method == 'POST':
                text = request.form['text']
                text = [text]
                summarized_text = None
                summarized_text_json = jsonify({'summarized_text': str(summarized_text)})
        except:
            return jsonify({'trace': traceback.format_exc()})
        else:
            return render_template('result.html',summarized_text = summarized_text)

    else:
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) 
    except:
        port = 12345 

    model = joblib.load('page summarizer model goes here') 
    print ('Model loaded')

    app.run(port=port, debug=True)
