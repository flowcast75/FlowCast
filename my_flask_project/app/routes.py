from flask import render_template, request
from .models import User,db

def register_routes(app):
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == "GET":
            return render_template('signup.html')
        else:
            # Get the form data
            username = request.form.get('name')
            password = request.form.get('password')
            email = request.form.get('email')
            dob = request.form.get('dob')
            print(username, password, email)
            try:
                user = User(
                    username = username,
                    password = password,
                    email = email,
                    dob = dob
                    )
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                print(e)
                return render_template('signup.html')
    
            return render_template('index.html',msg="Profile created successfully")
            
    

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return render_template('login.html')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/cycle')
    def cycle():
        return render_template('cycle.html')

    @app.route('/calendar')
    def calendar():
        # Render the calendar page
        return render_template('calendar.html')

    @app.route('/profile')
    def profile():
        return render_template('profile.html')

    @app.route('/health_library')
    def health_library():
        # Render the health library page
        return render_template('health_library.html')
