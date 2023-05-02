### flask 基本结束

Flask是一个轻量级的可定制框架，使用Python语言编写，较其他同类型框架更为灵活、轻便、安全且容易上手。它可以很好地结合[MVC模式](https://baike.baidu.com/item/MVC模式/713147)进行开发，开发人员分工合作，小型团队在短时间内就可以完成功能丰富的中小型网站或[Web服务](https://baike.baidu.com/item/Web服务/2837593)的实现。另外，Flask还有很强的定制性，用户可以根据自己的需求来添加相应的功能，在保持核心功能简单的同时实现功能的丰富与扩展，其强大的插件库可以让用户实现个性化的网站定制，开发出功能强大的网站。

### flask基本使用

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```

这些都不是我们要说的重点，重点是一下的部分

### [学会flask了解python上下文](学会flask了解python上下文.md)

### [学会flask了解python线程隔离](学会flask了解python线程隔离.md)

### [学会flask了解序列化](学会flask了解序列化.md)

### [学会flask了解代理模式](学会flask了解代理模式.md)

### [学会flask了解装饰器](学会flask了解装饰器.md)
