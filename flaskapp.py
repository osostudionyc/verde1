from flask import Flask

from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mainindexcopy():


    if request.method == 'POST':
        output301 = '<br>' \
                + '<br>' \
                + '<a href="/"> PRODUCT APP <br><br>' \
                + '<a href="/"> TREE SCAN APP ' \
                + '<br><br>' 
        return output301
    return '''
    <form method="POST">
            <br><br>
            '<center><img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/deleteplastic2.png" alt="Logo" style="width:350px"> <br><br><p><i>🌿 Welcome to <b></i>DeletePlastic.io<i></b> - Eliminate Plastic from Your Life! 🌎</i>



<br><br><br><br><b>

<img src="static/DPdescripupdate.png" style="width:1000px">
       
</center>
 </p>'
            <br><br><center>
             <a href="/webapp"> <img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/tquiz.png" style="width:300px" > <br>
            <a href="/reviews"> <img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/PRZ.png" style="width:300px"></center>
            <br><br><br><br>
            <center><a href = "mailto: hello@deleteplastic.io"><img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/contact.png" style="width:300px"</img></a></center>
            <p>
    </form>
    '''



'''
@app.route("/")
def hello_world():
    return 'Hello World Again TEST'
'''
#main driver function 

if __name__ == '__main__':
    app.run()
