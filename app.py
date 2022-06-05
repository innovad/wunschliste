from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'marlen_nhl'

@app.route('/test')
def test():  # put application's code here
    return 'Pittsburgh Penguins!'

@app.route('/')
def hello_world():  # put application's code here
    if not 'wishes' in session:
        session['wishes'] = []
    return render_template('index.html', wishes=session['wishes'])

@app.route('/', methods=['POST'])
def nach_eingabe():
    session['wishes'].append(request.form['wish'])
    session.modified = True
    print(session['wishes'])
    return render_template('index.html', wishes=session['wishes'])

@app.route('/delete', methods=['POST'])
def löschen():
    session['wishes'] = []
    return render_template('index.html', wishes=session['wishes'])

if __name__ == '__main__':
    app.run()
