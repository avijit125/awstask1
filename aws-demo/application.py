import mysql.connector
from flask import Flask,render_template,request,jsonify

conn=mysql.connector.connect(host="database-1.ct06rowu6gza.us-east-2.rds.amazonaws.com",user="admin",password="avijit123",database="moviedb")

mycursor = conn.cursor()






application=Flask(__name__)

#mycursor.execute("DELETE FROM movies WHERE id = 13")

#conn.commit()

@application.route('/')
def index():
	mycursor.execute("SELECT * FROM movies")
	data=mycursor.fetchall()
	return render_template('index.html', data=data)

@application.route('/add')
def add():
	return render_template('addmovie.html')

@application.route('/insert', methods=['POST'])
def insert():
	name=request.form.get('name')
	actor=request.form.get('actor')
	year=request.form.get('year')
	poster=request.form.get('poster')

	mycursor.execute("INSERT INTO movies (user_id,name,actor,year,poster) VALUES (NULL,'{}','{}','{}','{}')".format(name,actor,year,poster))

	conn.commit()

	return render_template('addmovie.html')

@application.route('/view/<movie>',methods=['GET'])
def view_movie(movie):

	# d={'response':200,'text':movie}

	mycursor.execute("SELECT * FROM movies WHERE name LIKE '{}'".format(movie))

	data=mycursor.fetchall()

	if(len(data)!=0):
		response={'response':200, 'data':{'name':data[0][1],'actor':data[0][2],'year':data[0][3],'poster':data[0][4]}}
	else:
		response={'response':404}

	return jsonify(response)

if __name__=="__main__":
	application.run(debug=True)

