import pymongo

client = pymongo.MongoClient("mongodb+srv://Preeti:ineuron@cluster0.snwbf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d= {
    "name":"preeti" ,
    "email": "preetijainamb123@gmail.com" ,
    "surname" : "jain"
}
d= {
    "name":"preeti" ,
    "email": "preetijainamb123@gmail.com" ,
    "surname" : "jain"
}
d= {
    "name":"preeti" ,
    "email": "preetijainamb123@gmail.com" ,
    "surname" : "jain"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)