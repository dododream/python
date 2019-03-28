# pip install js2py
import js2py
js_str = "console.log('Hello World')"
js2py.eval_js(js_str)
js_str2 = "var num_array = [10, 20, 30, 40]"
js2py.eval_js(js_str2)
type(js2py.eval_js(js_str2))
js2py.eval_js(js_str2)[1]
js2py.eval_js(js_str2)[2]
js2py.eval_js(js_str2)[3]
## 创建一个JavaScript 运行环境
## 创建一个JavaScript 运行环境
context = js2py.EvalJs()
context.execute("var num1 = 100")
context.num1
context.execute("var num2 = 200")
context.num2
pwd
ls
context.execute(open("lol.js", "r").read())
context.LOLherojs
context.LOLherojs.data
context.LOLherojs.champion
context.LOLherojs.champion.data
context.LOLherojs.champion.data.Akali
context.LOLherojs.champion.data.Akali.image
context.LOLherojs.champion.data.Akali.image.full
js2py.eval_js
js2py.EvalJs()
%hist -f js2py使用.py
