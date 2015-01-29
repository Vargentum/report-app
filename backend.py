from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def entries():
  if request.method == 'GET':
    show_entries()


def show_entries():
  #entries = Flask.request.get_json() 

  return render_template('app.html', entries=entries)



def render_app():
  return render_template('app.html')




if __name__ == '__main__':
  app.run()

app.debug = True
app.run(host='0.0.0.0')
