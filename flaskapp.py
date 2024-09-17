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
        months = request.form.get('months')
        check123 = request.form.get('check123')
        option2 = request.form.get('option2')
        budgethold = request.form.get('budget')
        pans1 = request.form.get('pans1')
        cups1 = request.form.get('cups1')
        budget = request.form.get('budget')
        custbudget = request.form.get('custbudget')

        filter1 = request.form.get('filter1')
        shower1 = request.form.get('shower1')
        bottle1 = request.form.get('bottle1')



        #budget
        if budget =="1":
            budgethold = "50"
        elif budget =="2":
            budgethold = "100"
        elif budget =="3":
            budgethold = "250"
        elif budget =="4":
            budgethold = "500"
        elif budget =="5":
            budgethold = "1500"

            #budgethold = str(int(budgethold)*3) + " Months"

        #custbudget
        if custbudget == "":
            custbudget = "50"
        elif int(custbudget) > int(budget)*100:
            budgethold = str(int(custbudget))

        ######################################################################### PRODUCTS #######################################################

        #filter1
        if filter1 == "1" or filter1 == "4":
            if int(budgethold) > 249:    #budgethold == "1" or budgethold == "2" or budgethold == "3":
                filter1 = '<br><i> Recommended Drinking Water Filter (based on Budget): </i><br><br> <img src="static/simp1x.png" style="width:400px; height:300px; border: solid 1px #CCC"</img>' + '<br><br><a href="simpurereview.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>'
            else:
                filter1 = '<br><i> Recommended Drinking Water Filter (based on Budget): </i><br><br> <img src="static/sp1x.png" style="width:400px; height:300px; border: solid 1px #CCC"</img><br>'+ '<br> <a href="epicpure.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>'

        #shower
        if shower1 is None:
            shower1 = ''
        else:
            shower1 = '<br><i> Recommended Shower Filter: </i> <br><br> <img src="static/aqy1x.png" style="width:400px; height:300px; border: solid 1px #CCC"</img>' + '<br><br><a href="aquayouth.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br><br>'

        #shower
        if bottle1 is None:
            bottle1 = ''
        else:
            bottle1 = '<br><i> Recommended Water Bottle: </i> <br><br> <img src="static/EV1x.png" style="width:400px; height:300px; border: solid 1px #CCC"</img>' + '<br><br><a href="vostok.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br><br>'


        #cups
        if cups1 is None:
            cups1 = ''
        else:
            cups1 = '<br><i> Recommended Drinkware Set: </i> <br><br> <img src="static/scott1x.png" style="width:400px; height:300px; border: solid 1px #CCC"</img> ' + '<br><br> <a href="SchottReview.html"> <img src="static/preview.png" style="width:200px">  </a><br><br>'


        #pans
        if pans1 is None:
            pans1 = ''

        else:
            if budget == "1" or budget == "2" or budget == "3":
                tc += 199
                pans1 = '<br> <i>Recommended Cookware Set (based on Budget):</i> <br><br>' + ' <img src="static/treviso1x.png" style="width:400px; height:300px; border: solid 1px #CCC"</img>'+ '<br><br><a href="greenpan.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>'
                
            else:
                pans1 = '<br><i> Recommended Cookware Set (based on Budget): </i> <br><br>' + '<img src="static/carawayprodfin.png" style="width:400px; height:300px; border: solid 1px #CCC"</img>' + '<br><br><a href="carawayreview.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>'


        # Set default values for option2 and message
        if option2 is None:
            option2 = ''
            message = 'Not Enough Information Entered <br><br>'

        # Check if months is 2 and option2 is not empty
        #if months == '2' and option2 != '':
        if months == '2':
            tupperhold = 'Tupperware'
            message = '<br> Month 1: Purchase ' +  tupperhold
        
        # Check if check123 is None (i.e., not checked)
        if check123 is None:
            check123 = ''
        else:
            check123 = '<br><i> Recommended Food Storage Set: </i> <br><br> <img src="static/verel1x.png" style="width:400px; height:300px; border: solid 1px #CCC"</img>' + '<br><br><a href="glassstorage.html"> <img src="static/preview.png" style="width:200px">  </a><br><br><br>'


        if pans1 != '' or check123 != '' or cups1 != '':
            kitchen1 = '<img src="static/kitchencookingheader.png" style="width:500px"</img><br>'
        else:
            kitchen1 = ''

        # Create output string
        output = '<br>' \
               + '<center><a href="/"><img src="static/deleteplastic2.png" style="width:350px"></a></center><br>' \
               + kitchen1 \
               + pans1 \
               + check123 \
               + cups1 \
               + '<br><img src="static/waterfiltheader.png" style="width:500px"</img><br>' \
               + filter1 \
               + "<br>" \
               + shower1 \
               + "<br>" \
               + bottle1 \
               + '<br><br>' \
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
            <br><i>[Answer a few questions and enter your budget - the app will recommend products that have been reviewed by the team] </i></center><br><br><br><br><br>
            <label><img src="static/appmealprep.png" style="width:270px"><br></label>
          
            <br><br>
            <label>Alternate: Enter a custom budget: $</label>
            <input type="text" name="custbudget"><br><br>
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
