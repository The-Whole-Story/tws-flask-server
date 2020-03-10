from flask import Flask, jsonify, request

import spacy
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)


#NOTE: getTitleFromEntities currently returns whatever entity had the highest number of occurences accross all article titles passed
def getTitleFromEntities(titles):
    titleEntities = {}
    for title in titles:
        titleToAnalyze = nlp(title)
        for entity in titleToAnalyze.ents:
            if(entity.label_ != 'DATE'):
                if(entity.text not in titleEntities):
                    titleEntities[entity.text] = 1
                else:
                    titleEntities[entity.text]+=1
    maxTitleEntity = (max(titleEntities, key=titleEntities.get))
    return maxTitleEntity



@app.route('/title')
def title():
    return jsonify(getTitleFromEntities(request.get_json()))