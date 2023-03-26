import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    data = []
    path = './1'
    for path, dir, file in sorted(os.walk(path)):
        if path:
            data.append(path)
        if file:
            for file in sorted(file):
                data.append(f' --  {file}')
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
