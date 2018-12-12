from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route('/soccermm')
def index():
    return render_template('soccermm.html',list=list)
@app.route('/soccerdetail=<int:id>')
def detail(id):
    return render_template('soccerdetail.html',list=list, id=id)

class HostForm(Form):
    field = SelectField(u'Soccer Field', choices=[('Kovan SC', 'Kovan SC'), ('Ang mo kio Secondary School', 'Ang mo kio Secondary School'), ('Safra Tampines', 'Safra Tampines')])
    playersize = SelectField(u'Player Size', choices=[('8', '8'), ('16', '16'), ('24', '24')])
    privacy = SelectField(u'Match Privacy', choices=[('Public', 'Public'), ('Private', 'Private')])
    price = SelectField(u'Entry Price', choices=[('Free', 'Free'),('$6.00/player', '$6.00/player'), ('$48.00/team', '$48.00/team')])
    date = StringField('',[validators.Length(min=5,max=5)], render_kw={"placeholder": "dd/mm"})
    time1 = StringField('',[validators.Length(min=7,max=7)], render_kw={"placeholder": "00:00am"})
    age1 = StringField('',[validators.Length(min=1,max=2)], render_kw={"placeholder": "01"})
    time2 = StringField('',[validators.Length(min=7,max=7)], render_kw={"placeholder": "00:00pm"})
    age2 = StringField('',[validators.Length(min=1,max=2)], render_kw={"placeholder": "99"})
    gender = SelectField(u'Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Mixed', 'Mixed')])
    description = TextAreaField("Game Description", default="Game Rule: \n1) Friendly and Safe game!\n2) Winner stay, loser out.\n3) 3 Streak Winning team exits.\nSafety Rules:\n1) Watch your tackles\n3) No sliding")

list=[]
fieldimg= {'Kovan SC': 'https://s3-media4.fl.yelpcdn.com/bphoto/K33Qd__MXsQUSNYgNWjWHw/ls.jpg', 'Ang mo kio Secondary School':'https://www.myactivesg.com/~/media/Consumer/Images/Facilities/DUS%20and%20FTP/Ang%20Mo%20Kio%20Secondary%20School/AMKSSField.jpg', 'Safra Tampines': 'https://www.safra.sg/~/media/Images/Enjoy/Sports-Outdoor/soccer_pitches.ashx'}
fieldimgs=''
fieldlocations=''
fieldlocation= {'Kovan SC':'https://maps.google.com/maps?q=kovan%20sport%20centre&t=&z=13&ie=UTF8&iwloc=&output=embed',
                'Ang mo kio Secondary School':'https://maps.google.com/maps?q=ang%20mo%20kio%20seconday%20school&t=&z=13&ie=UTF8&iwloc=&output=embed',
                'Safra Tampines':'https://maps.google.com/maps?q=safra%20tampines&t=&z=13&ie=UTF8&iwloc=&output=embed'}
@app.route('/soccerhost', methods=['GET','POST'])
def host():
    form = HostForm(request.form)
    if request.method == 'POST' and form.validate():
        field=form.field.data
        playersize=form.playersize.data
        privacy=form.privacy.data
        price=form.price.data
        date=form.date.data
        time1=form.time1.data
        age1=form.age1.data
        time2=form.time2.data
        age2=form.age2.data
        gender=form.gender.data
        description=form.description.data
        for key,value in fieldimg.items():
            if key == field:
                fieldimgs=value
        for key,value in fieldlocation.items():
            if key == field:
                fieldlocations=value
        list.append(match(field,playersize,privacy,price,date,time1,time2,age1,age2,gender,description,fieldimgs,fieldlocations))
        flash('You has successfully hosted a match','success')
        return redirect('/soccermm')
    return render_template('soccerhost.html', form=form)
class match():
    def __init__(self,field,playersize,privacy,price,date,time1,time2,age1,age2,gender,description,fieldimg,location):
        self.__field=field
        self.__playersize=playersize
        self.__privacy=privacy
        self.__price=price
        self.__date=date
        self.__time1=time1
        self.__age1=age1
        self.__time2=time2
        self.__age2=age2
        self.__gender=gender
        self.__description=description
        self.__fieldimg=fieldimg
        self.__fieldlocation=location

    def get_field(self):
        return self.__field
    def get_playersize(self):
        return self.__playersize
    def get_privacy(self):
        return self.__privacy
    def get_price(self):
        return self.__price
    def get_date(self):
        return self.__date
    def get_gender(self):
        return self.__gender
    def get_time1(self):
        return self.__time1
    def get_time2(self):
        return self.__time2
    def get_age1(self):
        return self.__age1
    def get_age2(self):
        return self.__age2
    def get_description(self):
        return self.__description
    def get_fieldimg(self):
        return self.__fieldimg
    def get_location(self):
        return self.__fieldlocation

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
