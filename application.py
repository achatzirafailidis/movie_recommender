from flask import Flask
from recommender import recommend_random
from flask import render_template
from flask import request
from utils import movies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Alex', movies=movies.title.to_list())
    
@app.route('/recommend')
def recommendations():
    if request.args['algo']=='Random':
        recs = recommend_random()
        print(request.args)        
        titles = request.args.getlist('title')
        ratings = request.args.getlist('Ratings')
        user_input = dict(zip(titles,ratings))        
        print(user_input)        
        for keys in user_input:
            user_input[keys] = int(user_input[keys])        
        return render_template('recommendations.html',recs =recs)
    else:
        return f"Function not defined"
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)
