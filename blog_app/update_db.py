from blog_app import create_app
from blog_app import db
app = create_app()
app.app_context().push()
db.create_all()
