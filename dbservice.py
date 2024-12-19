from flask import Flask, render_template, request
app = Flask(__name__)

@app.route ('/register',methods = [ 'POST'])
def register():
   if request.method=="GET":
      return render_template("register.html")
   else:
      name=request.form["fullname"]
      email=request.form["email"]
      password=request.form["password"]
      query="insert into users(name,email,password) values('{}','{}','{}')" .format(name,email,password)
      cur.execute(query)
      conn.commit()
      return redirect("/dashboard")



@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      email=request.form["email"]
      password=request.form["password"]
      cur.execute("select id from users where email='{}' and password='{}'").format(email,password)
      row=cur.fetchone()
      if row==none:
         return"invalid credentials"
      else:
         return redirect('/dashboard')
    else:
      return render-render_template("login.html")
   


#       return render_template("login.html")
#    if request.method == 'POST':
#       pass

# if __name__ == '__main__':
#    app.run()