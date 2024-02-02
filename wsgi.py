# from blog_app import create_app

# app = create_app()
from blog_app.admin import app
if __name__ == '__main__':
    app.run(debug=True)
