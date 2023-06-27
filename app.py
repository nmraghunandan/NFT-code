from flask import Flask, render_template, redirect, url_for,flash,request,session
import sqlite3
import os

app = Flask(__name__)
app.secret_key="123"
app.config['UPLOAD_FOLDER'] = 'C:/Projects/NFT/static/images'

con = sqlite3.connect('main.db')
con.execute("""create table if not exists users(
    pid integer primary key,
    name text,
    phone integer,
    email text,
    password text,
    address text,
    coupon_code text
)
"""
)
con.execute("create table if not exists datafiles (box_id integer, image BLOB, link text)")
con.close()

@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
    i=6
    j=15
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY,box_id INTEGER,filename TEXT,data BLOB)')
    cur.execute("select box_id, filename, data from files")
    images = cur.fetchall()
    
    for image in images:
        box_id, name, data = image
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f'box{box_id}.jpeg')
        with open(file_path, 'wb') as f:
            f.write(data)
    con.close()
    images = os.listdir('C:/Projects/NFT/static/images')
    return render_template('index.html',i=i,j=j,str=str,images=images)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/referral')
def referral():
    return render_template('referral.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/widget')
def widget():
    return render_template('widget.html')
@app.route('/manage')
def manage():
    return render_template('manage.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        try:
            name = request.form['name']
            phone = request.form['phone']
            email = request.form['email']
            password = request.form['password']
            address = request.form['address']
            con = sqlite3.connect("main.db")
            cur = con.cursor()
            coupon_code = name[:3] + phone[-3:]  #Generate coupon code
            coupon_code = coupon_code.upper()
            cur.execute("insert into users(name,phone,email,password,address,coupon_code)values(?,?,?,?,?,?)",(name,phone,email,password,address,coupon_code,))
            con.commit()
            con.close()
            flash("Record Added  Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for('login')) 
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['email'] == 'admin@admin' and request.form['password'] == 'admin':
            return redirect(url_for('admin'))
        else:
            email=request.form['email']
            password=request.form['password']
            con=sqlite3.connect("main.db")
            con.row_factory=sqlite3.Row
            cur=con.cursor()
            cur.execute("select * from users where email=? and password=?",(email,password))
            data=cur.fetchone()

            if data:
                session["email"]=data["email"]
                session["password"]=data["password"]
                flash("logged in successfully")
                return redirect(url_for('home'))
            else:    
                flash("Username and Password Mismatch","danger")   
    return render_template('login.html')

@app.route('/go_to_cart', methods=['POST','GET'])
def go_to_cart():
    selected_box_ids = request.form['cart'].split(',')  # get the selected box IDs from the cart form
    #if request.method == 'POST':
    for box_id in selected_box_ids:
        print(box_id)
    
    if request.method == 'POST':
        con = sqlite3.connect('main.db')
        cur = con.cursor()
        for box_id in selected_box_ids:
            images = request.files.getlist(f'product-image-{box_id}')
            links = request.form.getlist(f'product-link-{box_id}')
            for i in range(len(images)):
                image = image[i].filename
                link = links[i]        
                cur.execute("insert into products (box_id, image, link) values (?, ?, ?)",(box_id, image, link,)) 
        con.commit()
        con.close()
        return render_template('cart.html', selected_box_ids=selected_box_ids)
    else:
        return render_template('cart.html', selected_box_ids=selected_box_ids)



@app.route('/vendorprofile', methods=['GET', 'POST'])
def vendorprofile():
    box_id = request.args.get('boxId')
    con=sqlite3.connect('main.db')
    cur=con.cursor()
    cur.execute('select * from users')
    rows=cur.fetchall()
    print(box_id)  
    return render_template('vendorprofile.html',rows=rows)

@app.route('/activity')
def activity():
    return render_template('activity.html')