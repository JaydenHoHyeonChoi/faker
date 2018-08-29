from flask import Flask, render_template, request
import random
import csv
from faker import Faker

names = []

app = Flask(__name__)
fake = Faker()

@app.route("/")
def index():
    return render_template('index.html')
    
    
@app.route("/result")
def result():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    match = random.randrange(50, 101)
    
    # names라는 배열에 입력된 두 이름을 넣는다. 
    # names.append(name1)
    # names.append(name2)
    
    # 'names.csv' 파일을 만들어서 저장한다.
    f = open('names.csv', 'a+', encoding='utf-8')
    a = csv.writer(f)
    a.writerow([name1, name2])
    f.close()
    
    return render_template('result.html', human1=name1, human2=name2, match=match)
    
    
@app.route("/admin")    
def admin():
    # names에 들어가 있는 모든 이름을 출력한다. 
    f = open('names.csv', 'r')
    rr = csv.reader(f)
    names = rr
    return render_template('admin.html', names=names)
    
    
@app.route("/ffaker")
def ffaker():
    name = fake.name()
    return render_template('ffaker.html', name=name)
    
# app.run(host='0.0.0.0', port='8080', debug=True)