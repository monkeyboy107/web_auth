import web

app = web.app

port = 5000
debug = True

if __name__ == '__main__':
    app.run(port=port, debug=debug)