import numpy as np
from flask import Flask, request, jsonify, render_template
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
application = Flask(__name__) #Initialize the flask App
import torch
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder() 
# Load the saved DistilBERT model and tokenizer
import nltk
from nltk.corpus import stopwords
save_directory="content/drive/MyDrive/saved_file"
model_fine_tuned = TFDistilBertForSequenceClassification.from_pretrained('C:\\Users\\Inspiron\\Downloads\\saved_file')
tokenizer_fine_tuned = DistilBertTokenizer.from_pretrained('C:\\Users\\Inspiron\\Downloads\\saved_file')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import string
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')
import tensorflow as tf
def predictionresult(textinput):
    
    def remove_stopwords_and_punctuations(text):
        stop_words = set(stopwords.words('english'))
        translator = str.maketrans('', '', string.punctuation)
        lemmatizer = WordNetLemmatizer()

        words = nltk.word_tokenize(text)
        words = [word for word in words if word.lower() not in stop_words]

        # Lemmatize the words
        lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

        words_without_punctuations = [word.translate(translator) for word in lemmatized_words]
        return ' '.join(words_without_punctuations)
    textinput=remove_stopwords_and_punctuations(textinput)
    predict_input = tokenizer_fine_tuned.encode(
        textinput,
        truncation = True,
        padding = True,
        return_tensors = 'tf'    
    )
    
    output = model_fine_tuned(predict_input)[0]
    print(output)
    prediction_value = tf.argmax(output, axis = 1).numpy()[0]

    return prediction_value
@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    title= features[0]
    paragraph=features[1]
    text= title+ " " +paragraph
    prediction_value = predictionresult(text)
    dict={0:"Commodities", 1:"Compliance", 2:"Delays", 3:"Environmental", 4: "Financial Health", 5: "Supplier Market"}
    return render_template('index.html', prediction_text='New Category Should Be {}'.format(dict[prediction_value]))

if __name__ == "__main__":
    application.run(debug=True)