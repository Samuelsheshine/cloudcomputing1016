from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬資料庫，用 list 暫存
posts = [
    {
        'id': 1,
        'title': '我的第一篇文章',
        'author': '小明',
        'content': '這是我用 Flask 寫的第一篇部落格文章！'
    },
    {
        'id': 2,
        'title': 'Flask 模板教學',
        'author': '小華',
        'content': 'Flask 的 templates 功能讓前後端分離更方便。'
    }
]

@app.route('/')
def index():
    """首頁：列出所有文章"""
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    """顯示單篇文章"""
    article = next((p for p in posts if p['id'] == post_id), None)
    if article:
        return render_template('post.html', post=article)
    else:
        return "找不到這篇文章", 404

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    """新增文章"""
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        new_id = len(posts) + 1
        posts.append({'id': new_id, 'title': title, 'author': author, 'content': content})
        return redirect(url_for('index'))
    return '''
        <h2>新增文章</h2>
        <form method="post">
            標題: <input name="title"><br><br>
            作者: <input name="author"><br><br>
            內容:<br>
            <textarea name="content" rows="5" cols="40"></textarea><br><br>
            <input type="submit" value="新增">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
