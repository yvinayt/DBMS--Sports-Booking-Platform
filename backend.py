from flask import Flask, render_template, request, redirect,session
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
# Database connection
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('database.db')
    except Error as e:
        print(e)

    return conn

import sqlite3

def create_connection():
    conn = sqlite3.connect('database.db')
    return conn

def create_data_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS data
                      (sport TEXT NOT NULL,
                       location TEXT NOT NULL,
                       day TEXT NOT NULL,
                       time TEXT NOT NULL,
                       available_vacancies INTEGER NOT NULL)''')

    cursor.execute("SELECT COUNT(*) FROM data")
    result = cursor.fetchone()[0]
    if result == 0:
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround1","Sunday","09:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround1","Sunday","10:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround1","Sunday","05:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround1","Sunday","06:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround1","Sunday","07:00 PM" , 22))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround2","Sunday","09:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround2","Sunday","10:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround2","Sunday","05:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround2","Sunday","06:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround2","Sunday","07:00 PM" , 22))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround3","Sunday","09:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround3","Sunday","10:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround3","Sunday","05:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround3","Sunday","06:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("FootBall", "FootBallGround3","Sunday","07:00 PM" , 22))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt1","Sunday","09:00 AM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt1","Sunday","10:00 AM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt1","Sunday","05:00 PM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt1","Sunday","06:00 PM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt1","Sunday","07:00 PM" , 10))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt2","Sunday","09:00 AM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt2","Sunday","10:00 AM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt2","Sunday","05:00 PM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt2","Sunday","06:00 PM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt2","Sunday","07:00 PM" , 10))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt3","Sunday","09:00 AM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt3","Sunday","10:00 AM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt3","Sunday","05:00 PM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt3","Sunday","06:00 PM" , 10))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("BasketBall", "BasketBallCourt3","Sunday","07:00 PM" , 10))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround1","Sunday","09:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround1","Sunday","10:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround1","Sunday","05:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround1","Sunday","06:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround1","Sunday","07:00 PM" , 22))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround2","Sunday","09:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround2","Sunday","10:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround2","Sunday","05:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround2","Sunday","06:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround2","Sunday","07:00 PM" , 22))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround3","Sunday","09:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround3","Sunday","10:00 AM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround3","Sunday","05:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround3","Sunday","06:00 PM" , 22))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Cricket", "CricketGround3","Sunday","07:00 PM" , 22))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt1","Sunday","09:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt1","Sunday","10:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt1","Sunday","05:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt1","Sunday","06:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt1","Sunday","07:00 PM" , 4))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt2","Sunday","09:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt2","Sunday","10:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt2","Sunday","05:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt2","Sunday","06:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt2","Sunday","07:00 PM" , 4))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt3","Sunday","09:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt3","Sunday","10:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt3","Sunday","05:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt3","Sunday","06:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Tennis", "TennisCourt3","Sunday","07:00 PM" , 4))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt1","Sunday","09:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt1","Sunday","10:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt1","Sunday","05:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt1","Sunday","06:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt1","Sunday","07:00 PM" , 4))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt2","Sunday","09:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt2","Sunday","10:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt2","Sunday","05:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt2","Sunday","06:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt2","Sunday","07:00 PM" , 4))
        
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt3","Sunday","09:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt3","Sunday","10:00 AM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt3","Sunday","05:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt3","Sunday","06:00 PM" , 4))
        cursor.execute("INSERT INTO data ( sport, location,day, time, available_vacancies) VALUES (?, ?, ?, ?, ?)",
                                    ("Badminton", "BadmintonCourt3","Sunday","07:00 PM" , 4))



    conn.commit()
    cursor.close()
    conn.close()

conn = create_connection()
create_data_table()
conn.close()
    
def create_bookings_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT NOT NULL,
                       sport TEXT NOT NULL,
                       num_players INTEGER NOT NULL,
                       available_vacancies INTEGER NOT NULL,
                       day TEXT NOT NULL,
                       time TEXT NOT NULL,
                       location TEXT NOT NULL)''')

    conn.commit()
    cursor.close()
    conn.close()
    
# Create "users" table
def create_users_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        password = request.form['password']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return redirect('/bookings')
        else:
            return "Invalid username or password. Please try again."
    return render_template('login.html')

# Signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            cursor.close()
            conn.close()
            return 'Username already taken. Please choose a different username.'
        
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return 'Signup successfull!'
    return render_template('signup.html')

# Display page
@app.route('/display')
def display():
    conn = create_connection()
    cursor = conn.cursor()
    username = session.get('username')
    cursor.execute("SELECT * FROM bookings WHERE username=?", (username,))
    bookings = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('display.html', bookings=bookings)

# Bookings page
@app.route('/bookings', methods=['GET', 'POST'])
def bookings():
    if request.method == 'POST':
        username = session.get('username')
        sport = request.form['sport']
        day = request.form['day']
        time = request.form['time'] 
        num_players = int(request.form['num_players']) 
        location = request.form['location'] 
        # Define a dictionary 
        max_capacity = {
            'Cricket' : 22, 
            'FootBall': 22,
            'BasketBall': 10,
            'Tennis': 4,
            'Badminton': 4
        }

        conn = create_connection()
        cursor = conn.cursor()
        
        # Check if table exists, if not, create it
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bookings'")
        table_exists = cursor.fetchone()
        if not table_exists:
            create_bookings_table()

        # Check if slot is available based on the maximum capacity for the sport
        cursor.execute("SELECT SUM(num_players) FROM bookings WHERE day=? AND sport=? AND time=? AND location=?", (day, sport,time,location))
        row = cursor.fetchone()
        total_players = row[0] or 0
        available_vacancies= max_capacity[sport]-total_players
        if total_players + num_players > max_capacity[sport]:
            cursor.close()
            conn.close()
            s= str(available_vacancies)+' vacancies available. Please choose another slot or location.'
            return s.format(sport)
        else:  
            cursor.execute("SELECT * FROM bookings WHERE sport=? AND day=? AND time=? AND location=?",
                   (sport, day, time, location))
            existing_booking = cursor.fetchone()
            if existing_booking:
                # UPDATE the existing booking with the new num_players value
                existing_available_vacancies = existing_booking[4]
                new_available_vacancies = existing_available_vacancies - num_players
                cursor.execute("UPDATE bookings SET available_vacancies=? WHERE sport=? AND day=? AND time=? AND location=?",
                               ( new_available_vacancies, sport, day, time, location))
                cursor.execute("UPDATE data SET available_vacancies=? WHERE sport=? AND day=? AND time=? AND location=?",
                               ( new_available_vacancies, sport, day, time, location))
                conn.commit()      
                cursor.execute("INSERT INTO bookings (username, sport, num_players, available_vacancies, day, time, location) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                (username, sport, num_players, available_vacancies - num_players, day, time, location))          
            else:
                # Insert a new booking with the provided values
                cursor.execute("INSERT INTO bookings (username, sport, num_players, available_vacancies, day, time, location) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                (username, sport, num_players, available_vacancies - num_players, day, time, location))
                cursor.execute("UPDATE data SET available_vacancies=? WHERE sport=? AND day=? AND time=? AND location=?",
                               ( available_vacancies - num_players, sport, day, time, location))

            conn.commit()
            cursor.close()
            conn.close()
            return 'Booking successful!'
    return render_template('booking.html',username=session.get('username'))

@app.route('/cancel_booking/<int:booking_id>', methods=['GET', 'POST'])
def cancel_booking(booking_id):
    if request.method == 'POST':
        if request.form['submit'] == 'Yes':
            conn = create_connection()
            cursor = conn.cursor()

            # Retrieve the booking details from the database
            cursor.execute("SELECT * FROM bookings WHERE id=?", (booking_id,))
            booking = cursor.fetchone()

            # UPDATE available slots in the database
            sport = booking[2]
            num_players = booking[3]
            day = booking[5]
            location= booking[7]
            time = booking[6]
            cursor.execute("UPDATE bookings SET available_vacancies = available_vacancies + ? WHERE sport = ? AND day = ? AND time=? AND location=?", (num_players, sport, day,time,location))
            cursor.execute("UPDATE data SET available_vacancies = available_vacancies + ? WHERE sport = ? AND day = ? AND time=? AND location=?", (num_players, sport, day,time,location))
            cursor.execute("DELETE FROM bookings WHERE id=?", (booking_id,))
            
            # Commit the changes to the database
            conn.commit()
            
            cursor.close()
            conn.close()

            return 'Booking Cancelled'
        elif request.form['submit'] == 'No':
            return redirect('/My_Bookings')
    return render_template('cancel_booking.html', booking_id=booking_id)


create_data_table()
# Create users table on app startup
create_users_table()

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
