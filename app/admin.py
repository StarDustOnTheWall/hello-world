from sanic import Blueprint, response
from fun import fun

homepage = Blueprint(name="admin")


@homepage.route("/", methods=['GET'])
async def index(request):
    return response.text("This is admin index page.")


@homepage.route("/test", methods=['GET'])
async def test_input(request):
    return response.html('''<form action="/test" method="post">
              <p><input name="things1" type="text"></p>
              <p><input name="things2" type="text"></p>
              <p><input name="things3" type="text"></p>
              <p><input name="things4" type="text"></p>
              <p><input name="things5" type="text"></p>
              <p><input name="things6" type="text"></p>
              <p><input name="things7" type="text"></p>
              <p><input name="things8" type="text"></p>
              <p><button type="submit">Sign In</button></p></form>''')


@homepage.route("/test", methods=['POST'])
async def test_output(request):
    return response.json(fun(int(request.form['things1'][0]), int(request.form['things2'][0]), int(request.form['things3'][0]),
                             int(request.form['things4'][0]), int(request.form['things5'][0]), int(request.form['things6'][0]),
                             int(request.form['things7'][0]), int(request.form['things8'][0])))