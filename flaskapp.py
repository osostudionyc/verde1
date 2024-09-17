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
            '<center><img src="https://raw.githubusercontent.com/osostudionyc/verde1/Pictures/verde.png" alt="Logo" style="width:350px"> <br><br><p> Welcome to <b>Verde.io</b> - The Ultimate Resource for Renovations that Save Money and Save the Planet



<br><br><br><br><b>

<img src="https://raw.githubusercontent.com/osostudionyc/verde1/main/DPdescripupdate.png" style="width:1000px">
       
</center>
 </p>
            <br><br><center>
             <a href="/webapp"> <img src="https://raw.githubusercontent.com/osostudionyc/verde1/Pictures/freeport.png" style="width:300px" > <br>
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

@app.route('/webapp', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':


        #OS: General Variables Here


        hold1 = ""
        message = ""
        tc = 0

        # Get form data
        
        custbudget = request.form.get('custbudget')
        state = request.form.get('state')

   




        #custbudget
        if custbudget == "":
            custbudget = "50"
        elif int(custbudget) > int(custbudget)*100:
            budgethold = str(int(custbudget))

        ######################################################################### PRODUCTS #######################################################

        #filter1
        if state = "NY":
            if int(budgethold) > 249:    #budgethold == "1" or budgethold == "2" or budgethold == "3":
                filter1 = '<br><i> Recommended Drinking Water Filter (based on Budget): </i><br><br> <img src="static/simp1x.png" style="width:400px; height:300px; border: solid 1px #CCC"</img>' + '<br><br><a href="simpurereview.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>'
            else:
                filter1 = '<br><i> Recommended Drinking Water Filter (based on Budget): </i><br><br> <img src="static/sp1x.png" style="width:400px; height:300px; border: solid 1px #CCC"</img><br>'+ '<br> <a href="epicpure.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>'
                

        # Create output string
        output = '<br>' \
               + '<center><a href="/"><img src="static/deleteplastic2.png" style="width:350px"></a></center><br>' \
               + custbudget \
               + '<br><br>' \
               + 'State' \
               + state \
               + '<a href="https://deleteplastic.io/webapp"> <b><p <p style="color:green;"><img src="static/restart2.png" style="width:250px; border: solid 0px #CCC"</p></b> </a>'
               

        return output
    
    # Generate HTML form
    return '''
        <form method="POST">
            <br><br>
            <head>
<style>
  body {
    font-family: 'Source Code Pro', monospace;
    font-size: 13px;
  }
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap">
</head>
            <center><a href='/' ><img src="/static/DP.png" width="350"></a>
            <br><i>[Enter some basic information about your proeprty and our proprietary database will create a custiome report with the best ROI renovation projects] </i></center><br><br><br><br><br>
            <label><img src="static/appmealprep.png" style="width:270px"><br></label>
          
            <br><br>
            <label>Alternate: Enter a custom budget: $</label>
            <input type="text" name="custbudget"><br><br>
            <br><br>
            <label>State</label>
            <input type="text" name="state"><br><br>
            <br><br>
            <i> The app will rank products by health impact and create a custom priority list based on your desired spend </p>
            <br>
            <br>
            <input type="submit" value="Submit">
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
