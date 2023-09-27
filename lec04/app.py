from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
posts = [
    {
        'author': {
            'username': 'test-user'
        },
        'title': '첫 번째 포스트',
        'content': '첫 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-01', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'test-user'
        },
        'title': '두 번째 포스트',
        'content': '두 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-03', '%Y-%m-%d')
    },
]

# posts = []

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    # return render_template('blog_content.html', posts=posts)
    return render_template('blog_list.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about_me.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()