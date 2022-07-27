import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///tables.db")

@app.route("/")
@login_required
def homepage():
    #Show a table with all the matches this user has played. It would be a table with: name of rival, Date, and who won
    id = session["user_id"]
    rival_id1 = db.execute("SELECT rival_id FROM game WHERE user_id = ? AND status = ?", id, "Finished") #You challenged
    rival_id2 = db.execute("SELECT user_id FROM game WHERE rival_id = ? AND status = ?", id, "Finished") #Someone challenged you
    rival1_name = []
    rival2_name =[]
    winners1 = []
    winners2 = []
    somelength = len(rival_id2)
    youlength = len(rival_id1)
    if youlength == 0 and somelength == 0:
        return render_template("no_homepage.html")
    elif len(rival_id1) == 0:
        rival_id2 = rival_id2[0]['user_id']
        rival_name2 = db.execute("SELECT name FROM users WHERE user_id = ?", rival_id2)
        for name2 in rival_name2:
            rival2_name.append(name2)
        winner2 = db.execute("SELECT winner_id FROM game WHERE user_id = ? AND rival_id =?", rival_id2, id)
        winner2 = winner2[0]['winner_id']
        winner2_name = db.execute("SELECT name FROM users WHERE user_id = ?", winner2)
        for win2 in winner2_name:
            winners2.append(win2)
        length2 = len(rival2_name)
        return render_template("someone_homepage.html", rival2_name = rival2_name, winners2 = winners2, length2 = length2)
    elif len(rival_id2) == 0:
        rival_id1 = rival_id1[0]['rival_id']
        rival_name1 = db.execute("SELECT name FROM users WHERE user_id = ?", rival_id1)
        for name1 in rival_name1:
            rival1_name.append(name1)
        winner1 = db.execute("SELECT winner_id FROM game WHERE user_id = ? AND rival_id =?", id, rival_id1)
        winner1 = winner1[0]['winner_id']
        winner1_name = db.execute("SELECT name FROM users WHERE user_id = ?", winner1)
        for win1 in winner1_name:
            winners1.append(win1)
        length1 = len(rival1_name)
        return render_template("you_homepage.html", rival1_name = rival1_name, winners1 = winners1, length1 = length1)
    else:
        #Games the user challenged someone else
        for id1 in rival_id1:
            #rival_name1 = db.execute("SELECT name FROM users WHERE user_id = ?", rival_id1)
            id1 = id1['rival_id']
            rival_name1 = db.execute("SELECT name FROM users WHERE user_id = ?", id1)
            for name1 in rival_name1:
                rival1_name.append(name1)
            #for name1 in rival_name1:
            #    rival1_name.append(name1)
            winner1 = db.execute("SELECT winner_id FROM game WHERE user_id = ? AND rival_id =?", id, id1) #Antes id1 era rival_id1
            winner1 = winner1[0]['winner_id']
            winner1_name = db.execute("SELECT name FROM users WHERE user_id = ?", winner1)
            for win1 in winner1_name:
                winners1.append(win1)
        length1 = len(rival1_name)
        #Games someone challenged you
        for id2 in rival_id2:
            id2 = id2['user_id']
            #rival_name2 = db.execute("SELECT name FROM users WHERE user_id = ?", rival_id2)
            rival_name2 = db.execute("SELECT name FROM users WHERE user_id = ?", id2)
            for name2 in rival_name2:
                rival2_name.append(name2)
            winner2 = db.execute("SELECT winner_id FROM game WHERE user_id = ? AND rival_id =?", id2, id) #Antes id2 era rival_id2
            winner2 = winner2[0]['winner_id']
            winner2_name = db.execute("SELECT name FROM users WHERE user_id = ?", winner2)
            for win2 in winner2_name:
                winners2.append(win2)
        length2 = len(rival2_name)
        return render_template("homepage.html", rival1_name = rival1_name, winners1 = winners1, rival2_name = rival2_name, winners2 = winners2, length1 = length1,  length2 =  length2)
        return apology("TODO")

@app.route("/Ranking")
@login_required
def ranking():
    #There will be a table with a list of all the players in the system (if man or woman)
    mi_sexo = db.execute("SELECT sexo FROM users WHERE user_id = ?", session["user_id"])
    mi_sexo = mi_sexo[0]['sexo']
    table = db.execute("SELECT user_id FROM ranking WHERE sexo = ? ORDER BY ranking DESC", mi_sexo)
    ranking = db.execute("SELECT ranking FROM ranking WHERE sexo = ? ORDER BY ranking DESC", mi_sexo)
    names = []
    for t in table:
        t = t['user_id']
        name = db.execute("SELECT name FROM users WHERE user_id = ?", t)
        name = name[0]
        names.append(name)
    length = len(table)
    return render_template("ranking.html", ranking = ranking, names = names, lenght = length)
    return apology("TODO")

@app.route("/Desafiar", methods=["GET", "POST"])
@login_required
def challenge():
    #There will be a form for you to pick a rival, and what day and time to play. And send email to whom you challenge
    if request.method == "POST":
        challenger = session["user_id"]
        challenged = request.form['name']
        challenged = challenged[:-1] #To eliminate the extra space after the name
        challenged_id = db.execute("SELECT user_id FROM users WHERE name = ?", challenged)
        challenged_id = challenged_id[0]['user_id']
        #email = db.execute("SELECT email FROM users WHERE id = ?", challenged_id)
        # send email
        date = request.form.get("date")
        date = date.split("-")
        month = int(date[1])
        day = int(date[2])
        hour = request.form.get("hour")
        db.execute("INSERT INTO game (user_id, rival_id, month, day, hour) VALUES (?, ?, ?, ?, ?)", challenger, challenged_id, month, day, hour)
        return homepage()
    else:
        sexo =  db.execute("SELECT sexo FROM users WHERE user_id = ?", session["user_id"])
        sexo = sexo[0]['sexo']
        name = db.execute("SELECT name FROM users WHERE sexo = ?  ORDER BY name ASC", sexo) # I need to add for it to be the same sex
        name_len = len(name)
        return render_template("challenge.html", name = name, name_len = name_len)
        return apology("TODO")

@app.route("/Desafios", methods=["GET", "POST"])
@login_required
def challenges():
    #There will be 2 things here: Information of who challenged you, when and accept or decline button and email saying if you accept or decline;
    if request.method == "POST":
        id = session["user_id"]
        wait_id = db.execute("SELECT user_id FROM game WHERE rival_id = ? AND status = ?", id, "Waiting")
        wait_id = wait_id[0]['user_id']
        if request.form.get("answer") == "Accept":
            db.execute("UPDATE game SET status = 'Accepted' WHERE user_id = ? AND rival_id = ?", wait_id, id )
        else:
            db.execute("UPDATE game SET status = 'Declined' WHERE user_id = ? AND rival_id = ?", wait_id, id)
        return homepage()

    else:
        #I need to make sure the user has a game to play
        my_id = session["user_id"]
        w_id = db.execute("SELECT user_id FROM game WHERE rival_id = ? AND status = ?", my_id, "Waiting")
        if len(w_id) == 0:
            return render_template("no_challenges.html")
        else:
            # If we are waiting response
            w_id = w_id[0]['user_id']
            w_name = db.execute("SELECT name FROM users WHERE user_id = ?", w_id)
            w_month = db.execute("SELECT month FROM game WHERE user_id = ? AND rival_id = ? AND status = ?", w_id, my_id, "Waiting")
            w_day = db.execute("SELECT day FROM game WHERE user_id = ? AND rival_id = ? AND status = ?", w_id, my_id, "Waiting")
            w_hour = db.execute("SELECT hour FROM game WHERE user_id = ? AND rival_id = ? AND status = ?", w_id, my_id, "Waiting")
            w_length = len(w_name)
            return render_template("challenges.html", w_name = w_name, w_month = w_month, w_day = w_day, w_hour = w_hour, w_length = w_length)
            return apology("TODO")

@app.route("/Resultados", methods=["GET", "POST"])
@login_required
def results():
    #Form for you to insert the winner of match (Possible after match was played)
    if request.method == "POST":
        id = session["user_id"]
        other_id = db.execute("SELECT user_id FROM game WHERE rival_id = ? AND status = ?", id, "Accepted")
        other_id = other_id[0]['user_id']
        winner = request.form.get("ganador")
        #winner_id = db.execute("SELECT name FROM users WHERE user_id = ?", winner)
        #winner_id = winner_id[0]['name']
        db.execute("UPDATE game SET winner_id = ? WHERE user_id = ? AND rival_id = ?", winner, other_id, id)
        db.execute("UPDATE game SET status = ? WHERE user_id = ? AND rival_id = ?", "Finished", other_id, id)
        #Implementing ELO ranking now
        ROH = db.execute("SELECT ranking FROM ranking WHERE user_id = ?", id) #User ranking.
        ROH = ROH[0]['ranking']
        ROH_id = id
        ROL = db.execute("SELECT ranking FROM ranking WHERE user_id = ?", other_id) #Other players ranking.
        ROL = ROL[0]['ranking']
        ROL_id = other_id
        mi_sexo = db.execute("SELECT sexo FROM users WHERE user_id = ?", session["user_id"])
        mi_sexo = mi_sexo[0]['sexo']
        order = db.execute("SELECT ranking FROM ranking WHERE sexo = ? ORDER BY ranking DESC", mi_sexo)
        length = len(order)
        RH = None
        RL = None
        for l in range(length):
            if order[l]['ranking'] == ROH:
                RH = l
        for l in range(length):
            if order[l]['ranking'] == ROL:
                RL = l
        dif = RL - RH
        Probh = 1/(1+10**(-(dif/400))) #Probability for each player to win. ** is ^
        Probl = 1 - Probh
        print("winner")
        print(winner)
        print(ROH_id)
        ROH_id = int(ROH_id)
        winner = int(winner)
        if ROH_id == winner :  #The winner is H 
            new_ROH = ROH + 40 * (1 - Probh)
            new_ROL = ROL + 40 * (0 - Probl)
            db.execute("UPDATE ranking SET ranking = ? WHERE user_id = ?", new_ROH, ROH_id) #Players new ranking
            db.execute("UPDATE ranking SET ranking = ? WHERE user_id = ?", new_ROL, ROL_id)
        else:
            new_ROH = ROH + 40 * (0 - Probh)
            new_ROL = ROL + 40 * (1 - Probl)
            db.execute("UPDATE ranking SET ranking = ? WHERE user_id = ?", new_ROH, ROH_id)
            db.execute("UPDATE ranking SET ranking = ? WHERE user_id = ?", new_ROL, ROL_id)
        return ranking()
    else:
        my_id = session["user_id"]
        check = db.execute("SELECT user_id FROM game WHERE rival_id = ? AND status = ?", my_id, "Accepted")
        if len(check) == 0:
            return render_template("no_results.html")
        else:
            a_id = db.execute("SELECT user_id FROM game WHERE rival_id = ? AND status = ?", my_id, "Accepted")
            a_id = a_id[0]['user_id']
            a_name = db.execute("SELECT name FROM users WHERE user_id = ?", a_id)
            a_month = db.execute("SELECT month FROM game WHERE user_id = ? AND rival_id = ?", a_id, my_id)
            a_day = db.execute("SELECT day FROM game WHERE user_id = ? AND rival_id = ?", a_id, my_id)
            a_length = len(a_name)
            name = db.execute("SELECT name FROM users WHERE user_id = ?", my_id)
            name = name[0]['name']
            return render_template("results.html", a_name = a_name, a_month = a_month, a_day = a_day, a_length = a_length, my_id = my_id, a_id = a_id, name = name)
#Only the player challenged can insert the result
    return apology("TODO")

@app.route("/login", methods=["GET", "POST"]) #Copied this from finace, changing username for email
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("email"):
            return apology("must provide email", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("invalid email and/or password", 403)
        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]
        # Redirect user to home page
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout") #Copied this function from week 9 finance
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # My work
    if request.method == "POST":
        email = request.form.get("email")
        Password = request.form.get("password")
        Confirm = request.form.get("confirm_password")
        name = request.form.get("name")
        #middle = request.form.get("second_name")
        #last = request.form.get("last_name")
        sexo = request.form.get("sexo")
        if not email:
            return apology("Insertar e-mail")
        elif len(db.execute("SELECT * FROM users WHERE email = ?", email)) != 0:
            return apology("Este e-mail ya esta en uso")
        elif not Password:
            return apology("Insertar contraseña")
        elif Password != Confirm:
            return apology("Contraseñas no coinciden")
        elif not name:
            return apology("Insertar Nombre Completo")
        #elif not last:
        #    return apology("Insertar Apellido")
        elif not sexo:
            return apology("Insertar sexo")
        else:
            Save_password = generate_password_hash(Password)
            db.execute("INSERT INTO users (name, password, sexo, email) VALUES (?, ?, ?, ?)", name, Save_password, sexo, email)
            new_id = db.execute("SELECT user_id FROM users WHERE email = ?", email)
            new_id = new_id[0]['user_id']
            new_id = int(new_id)
            sexo = str(sexo)
            db.execute("INSERT INTO ranking (user_id, sexo) VALUES (?, ?)", new_id, sexo)
            #db.execute("INSERT INTO ranking (sexo) VALUES (?)", sexo)
            return redirect ("/login")

    else:
        return render_template("register.html")
