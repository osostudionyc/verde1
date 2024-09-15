from app import app
from flask import Flask,jsonify
from flask import request

import importlib
#####
#import pandas as pd <-- this will crash websited due to libffi.6 --> 7 conversion issue
from collections import Counter
from geopy.geocoders import Nominatim

#######


######
####
@app.route('/', methods=['GET', 'POST'])
def mainindexcopy():


    if request.method == 'POST':
        output301 = '<br>' \
                + '<br>' \
                + '<a href="/webapp"> PRODUCT APP <br><br>' \
                + '<a href="/hello"> TREE SCAN APP ' \
                + '<br><br>' 
        return output301
    return '''
    <form method="POST">
            <br><br>
            '<center><img src="static/deleteplastic2.png" alt="Logo" style="width:350px"> <br><br><p><i>🌿 Welcome to <b></i>DeletePlastic.io<i></b> - Eliminate Plastic from Your Life! 🌎</i>



<br><br><br><br><b>

<img src="static/DPdescripupdate.png" style="width:1000px">
       
</center>
 </p>'
            <br><br><center>
             <a href="/webapp"> <img src="static/tquiz.png" style="width:300px" > <br>
            <a href="/reviews"> <img src="static/PRZ.png" style="width:300px"></center>
            <br><br><br><br>
            <center><a href = "mailto: hello@deleteplastic.io"><img src="static/contact.png" style="width:300px"</img></a></center>
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








@app.route('/test1', methods=['GET', 'POST'])
def mainindex():


    if request.method == 'POST':
        output3 = '<br>' \
                + '<br>' \
                + '<a href="/webapp"> PRODUCT APP <br><br>' \
                + '<a href="/hello"> TREE SCAN APP ' \
                + '<br><br>' 
        return output3
    return '''
    <form method="POST">
            <br><br>
            <a href="/webapp"> PRODUCT APP >
            <br><br>
            <a href="/hello"> TREE SCAN APP >
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
            <label> How often do you usually cook?</label>
            <select name="option2">
                <option value="1">Daily</option>
                <option value="2">Every Other Day</option>
                <option value="3">2-3 Times / Week</option>
                <option value="4">Monthly</option>
                <option value="5">1 Never</option>
            </select>
            <br><br>
            <label> Do you use plastic tupperware?</label>
            <input type="checkbox" name="check123" value="Y">
            <br><br>
            <label> Are you not currently using a safe and chemical free pan to cook with? (Example: Ceramic, Stainless Steel, Cast Iron) </label>
            <input type="checkbox" name="pans1" value="Y">
             <br><br>
            <label> Do you use a plastic based cups / drinkware? </label>
            <input type="checkbox" name="cups1" value="Y">
            <br><br><br>


            <img src="static/appwater.png" style="width:350px"><br>
            <label> Do you use a drinking water filtration system? </label>
            <select name="filter1">
                <option value="1">None</option>
                <option value="2">NSF Certified Reverse Osmisis Filter </option>
                <option value="3">NSF Certified Carbon Filter</option>
                <option value="4">Other</option>
            </select>
            <br><br>
            <label> Are you not currently using a shower filter? </label>
            <input type="checkbox" name="shower1" value="Y">
            <br><br>
            <label> Do you use a plastic water bottle? </label>
            <input type="checkbox" name="bottle1" value="Y">


            <br><br><br>
            <img src="static/appbudget.png" style="width:270px"><br>
            <label> What is your budget? (The app will rank products by health impact and create a custom priority list based on your desired spend) </label>
            <select name="budget">
                <option value="1">$50</option>
                <option value="2">$100</option>
                <option value="3">$250</option>
                <option value="4">$500</option>
                <option value="5">$1k+</option>
            </select>
            <br><br>
            <label>Alternate: Enter a custom budget: $</label>
            <input type="text" name="custbudget"><br><br>
            <i> The app will rank products by health impact and create a custom priority list based on your desired spend </p>
            <br>
            <br>
            <input type="submit" value="Submit">
        </form>
    '''



@app.route('/hello', methods=['GET', 'POST'])
def helloIndex():
    df = pd.read_csv('./app/static/2015StreetTreesCensus_TREES.csv')#, encoding = 'unicode_escape') #dtype = 'unicode')
    x = df.loc[1][25]


    if request.method == 'POST':

        boro = request.form.get('boro')
        address = request.form.get('address')
        street = request.form.get('street')
        zip1 = request.form.get('zip1')
        #input_1 = float(request.form.get('input_1'))
        #input_2 = float(request.form.get('input_2'))

        combined = address + ' ' + street + ', ' + boro + ', ' + 'New York' + ', ' + str(zip1) + ', ' + 'USA'
        
        #address we need to geocode
        loc = combined
 
        #making an instance of Nominatim class
        geolocator = Nominatim(user_agent="my_request_os2")
 
        #applying geocode method to get the location
        location = geolocator.geocode(loc)
 
        #printing address and coordinates
        #print(location.address)
        testcord1 = location.latitude
        testcord2 = location.longitude

        loctest = location
        
        input_1 = location.latitude
        input_2 = location.longitude
        
        list1 = []
        list2 = []
        i = 0
        z = len(df)
 
        while i < 40000: #len(df):
            if abs((float(df.loc[i][38]) - input_1)) <= 0.002 and abs((float(df.loc[i][39]) - input_2)) <= 0.002:
                list1.append(df.loc[i][25])
                list2.append(df.loc[i][10])
            i += 1
    

        list2_nodup = list(set(list2))


        counter = Counter(list2)

        sorted_items = sorted(list2_nodup, key=lambda item: counter[item], reverse=True)

        str1 = ''
 
        for item in sorted_items:
            count = counter[item]
            str1 += f"{item}: {count} Tree(s)  "
        
        #hold = ''
        #for item in sorted_items:
         #   count = counter[item]
         #   hold += str(item)

        output2 = '<br>' \
                + '<br>' \
                + '<img src="/static/Allergyscan.png" width="300" height="30"><br><br><br>' \
                + '<br><br>' \
                + '<b>Data Entered:</b> ' \
                + combined \
                + '<br><br>' \
                + '<i><b><u>GPS DATA:</u></b></i>' \
                + '<br>' \
                + '<i><b>Address Returned by App: </i></b>' \
                + str(loctest) \
                + '<br>' \
                + '<i><b>Latitude:</i></b>' \
                + str(testcord1) \
                + '<br>' \
                + '<i><b>Longitude: </i></b>' \
                + str(testcord2) \
                + '<br>' \
                + '<i><b># of Trees Scanned: </b></i>' \
                + str(z) \
                + '<br>' \
                + '<br>' \
                + '<b><u>Allergy Causing Trees [located within 2 blocks]:</u></b>' \
                + '<br><br>' \
                + str1 \
                + '<br><br>' \
                + '<a href="https://deleteplastic.io/hello"> <b><p <p style="color:green;"><img src="static/restart.png" style="width:100px; height:25px; border: solid 0px #CCC"</p></b> </a>'
        return output2
    return '''
    <form method="POST">
            <br><br>
            <img src="/static/Allergyscan.png" width="300" height="30"><br><br><br>
            <label> Borough:  </label>
            <select name="boro">
                <option value="Brooklyn">Brooklyn</option>
                <option value="Queens">Queens</option>
                <option value="New York">Manhattan</option>
                <option value="Bronx">Bronx</option>
                <option value="Staten Island">Staten Island</option>
            </select>
            <br><br>
            <label>Address: </label>
            <input type="text" name="address"><br><br>
            <label>Street: </label>
            <input type="text" name="street"><br><br>
            <label>ZIP Code: </label>
            <input type="text" name="zip1"><br><br><br><br>

            <input type="submit" value="Submit">
    </form>
    '''

    
#jsonify(df.to_dict(orient='records'))
#testcsv = pd.read_csv('2015StreetTreesCensus_TREES.csv', dtype = 'unicode')
#######################

