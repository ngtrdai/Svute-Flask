from os import environ
from Svute_Flask import Create_App
app = Create_App()


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5901'))
    except ValueError:
        PORT = 5901
    app.run(HOST, PORT,debug=True)
    # app.run(debug=True)