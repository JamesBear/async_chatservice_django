
import random

name_list = ['Noah','William','James','Logan','Benjamin','Mason','Elijah','Oliver','Jacob','Lucas','Michael',
'Alexander','Ethan','Daniel','Matthew','Aiden','Henry','Joseph','Jackson','Samuel','Sebastian','David','Carter',
'Wyatt','Jayden','John','Owen','Dylan','Luke','Gabriel','Anthony','Isaac','Grayson','Jack','Julian','Levi','Christopher',
'Joshua','Andrew','Lincoln','Mateo','Ryan','Jaxon','Nathan','Aaron','Isaiah','Thomas','Charles','Caleb','Josiah','Christian',
'Hunter','Eli','Jonathan','Connor','Landon','Adrian','Asher','Cameron','Leo','Theodore','Jeremiah','Hudson','Robert','Easton','Nolan',
'Nicholas','Ezra','Colton','Angel','Brayden','Jordan','Dominic','Austin','Ian','Adam','Elias','Jaxson','Greyson','Jose','Ezekiel','Carson',
'Evan','Maverick','Bryson','Jace','Cooper','Xavier','Parker','Roman','Jason','Santiago','Chase','Sawyer','Gavin','Leonardo','Kayden','Ayden',
'Jameson']

def _random_name_naive():
    return random.choice(name_list)

def random_name():
    return _random_name_naive()