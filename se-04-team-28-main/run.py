from app.app import app


# start the server
if __name__ == '__main__':
    app.run(debug = True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
