## Flask

#### Flask 简略运行过程

- flask 应用实例会启动一个微型服务器
- 微型服务器收集用户请求用 `Werkzeug` 做路由分发
- 根据路由找到对应的路由函数，返回数据给用户
- 返回的数据可以是字符串和 html 模板



#### 创建 `app` 实例，并启动微型服务器

```python
from flask import Flask

# create app
app = Flask(__name__)

@app.route("/")
def index():
    return "this is a route function"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
```
