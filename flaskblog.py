from flask import Flask, render_template
import datetime
app = Flask(__name__)

posts = [
    {
        'author' : 'Rohit Shivapur',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : str(datetime.datetime.now())
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : str(datetime.datetime.now())
    }

]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True) 
