from flask import Flask

app = Flask(__name__)

def multi():
    res = []
    for i in range(1,11):
        r = 1 * i
        res.append(r)
    return res

@app.route('/table_1')
def table_1():
    res=multi()
    resultat=""
    for i in range(0,len(res)):
        resultat += " - 1 * {} = {} - ".format(i,res[i])
    return resultat


#def table(a):
    #for i in range(1,11):
        #print("la table de multiplication de ",i)
        #for j in range(1,11):
            #a = i *j
            #print(i, "*", j, "=",a)

app.run()