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
            '<center><img src="https://raw.githubusercontent.com/osostudionyc/verde1/Pictures/verde.png" alt="Logo" style="width:350px"> <br><br><p><i>🌿 Welcome to <b></i>DeletePlastic.io<i></b> - Eliminate Plastic from Your Life! 🌎</i>



<br><br><br><br><b>

<img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/DPdescripupdate.png" style="width:1000px">
       
</center>
 </p>
            <br><br><center>
             <a href="/webapp"> <img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/tquiz.png" style="width:300px" > <br>
            <a href="/reviews"> <img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/PRZ.png" style="width:300px"></center>
            <br><br><br><br>
            <center><a href = "mailto: hello@deleteplastic.io"><img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/contact.png" style="width:300px"</img></a></center>
            <p>
    </form>
    '''

@app.route('/reviews', methods=['GET', 'POST'])
def mainindexcopy2():


    if request.method == 'POST':
        output3 = '<br>' \
                + '<br>' \
                + '<a href="/webapp"> PRODUCT APP <br><br>' \
                + '<a href="/hello"> TREE SCANz APP ' \
                + '<br><br>' 
        return output3
    return '''
    <form method="POST">
            <center><a href="/"><img src="static/deleteplastic2.png" style="width:350px"></a><br><br>
            <img src="static/productrev1.png" style="width:300px"></center><br><br>
            <img src="static/waterfilt2.png" style="width:300px">
            <br><br><img src="static/simp1x.png" style="width:350px"</img><br><br><a href="simpurereview.html"> <img src="static/preview.png" style="width:200px"> </a><br><br><br>
            <br><img src="static/sp1x.png" style="width:350px"</img><br><br> <a href="epicpure.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>
            <img src="static/aqy1x.png" style="width:350px; border: solid 0px #006400"</img><br><br><a href="aquayouth.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>
            
            <br><br><br><img src="static/cookware2.png" style="width:300px"><br><br><br>
            <img src="static/treviso1x.png" style="width:350px"</img><br><br><a href="greenpan.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>
            <img src="static/carawayprodfin.png" style="width:350px; height:300px; border: solid 1px #CCC"</img><br><br><a href="carawayreview.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>
            <img src="static/verel1x.png" style="width:350px"</img><br><br><a href="glassstorage.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>


            <br><img src="static/drinkware2.png" style="width:300px"><br><br><br>
            <img src="static/scott1x.png" style="width:350px;border: solid 1px #CCC"</img><br><br> <a href="SchottReview.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>
            <img src="static/EV1x.png" style="width:350px;border: solid 1px #CCC"</img><br><br><a href="vostok.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>
            <center><a href = "mailto: hello@deleteplastic.io"><img src="static/contact.png" style="width:300px"</img></a></center>
            
            

    </form>
    '''
'''
@app.route("/")
def hello_world():
    return 'Hello World Again TEST'
'''
#main driver function 


@app.route('/dp', methods=['GET', 'POST'])
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

<img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/DPdescripupdate.png" style="width:1000px">
       
</center>
 </p>
            <br><br><center>
             <a href="/webapp"> <img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/tquiz.png" style="width:300px" > <br>
            <a href="/reviews"> <img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/PRZ.png" style="width:300px"></center>
            <br><br><br><br>
            <center><a href = "mailto: hello@deleteplastic.io"><img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/contact.png" style="width:300px"</img></a></center>
            <p>
    </form>
    '''

@app.route('/reviews', methods=['GET', 'POST'])
def mainindexcopy2():


    if request.method == 'POST':
        output3 = '<br>' \
                + '<br>' \
                + '<a href="/webapp"> PRODUCT APP <br><br>' \
                + '<a href="/hello"> TREE SCANz APP ' \
                + '<br><br>' 
        return output3
    return '''
    <form method="POST">
            <center><a href="/"><img src="static/deleteplastic2.png" style="width:350px"></a><br><br>
            <img src="static/productrev1.png" style="width:300px"></center><br><br>
            <img src="static/waterfilt2.png" style="width:300px">
            <br><br><img src="static/simp1x.png" style="width:350px"</img><br><br><a href="simpurereview.html"> <img src="static/preview.png" style="width:200px"> </a><br><br><br>
            <br><img src="static/sp1x.png" style="width:350px"</img><br><br> <a href="epicpure.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>
            <img src="static/aqy1x.png" style="width:350px; border: solid 0px #006400"</img><br><br><a href="aquayouth.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>
            
            <br><br><br><img src="static/cookware2.png" style="width:300px"><br><br><br>
            <img src="static/treviso1x.png" style="width:350px"</img><br><br><a href="greenpan.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>
            <img src="static/carawayprodfin.png" style="width:350px; height:300px; border: solid 1px #CCC"</img><br><br><a href="carawayreview.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>
            <img src="static/verel1x.png" style="width:350px"</img><br><br><a href="glassstorage.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>


            <br><img src="static/drinkware2.png" style="width:300px"><br><br><br>
            <img src="static/scott1x.png" style="width:350px;border: solid 1px #CCC"</img><br><br> <a href="SchottReview.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>
            <img src="static/EV1x.png" style="width:350px;border: solid 1px #CCC"</img><br><br><a href="vostok.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>
            <center><a href = "mailto: hello@deleteplastic.io"><img src="static/contact.png" style="width:300px"</img></a></center>
            
            

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
