from flask import Flask

from flask import request


app = Flask(__name__)

# PDFMonkey API details
PDFMONKEY_API_KEY = 'mS2YudqXyK14-tw_bfVNg78PcjsrtCS-'
PDFMONKEY_DOCUMENTS_ENDPOINT = 'https://api.pdfmonkey.io/api/v1/documents'

# Headers for PDFMonkey API requests
headers = {
    'Authorization': f'Bearer {PDFMONKEY_API_KEY}',
    'Content-Type': 'application/json'
}




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
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        type = request.form.get('type')
        built = request.form.get('built')
        sqft = request.form.get('sqft')

   




        #custbudget
        if custbudget == "":
            custbudget = "50"
        

        ######################################################################### PRODUCTS #######################################################

        #filter1
       

        # Create output string
        output = '<br>' \
               + '<center><a href="/"><img src="https://raw.githubusercontent.com/osostudionyc/verde1/Pictures/verde.png" style="width:350px"></a></center><br>' \
               + custbudget \
               + '<br><br>' \
               + 'Address:<br>' \
               + address \
               + '<br><br>' \
               + 'City:<br>' \
               + city \
               + '<br><br>' \
               + 'State:<br>' \
               + state \
               + '<br><br>' \
               + 'Type:<br>' \
               + type \
               + '<br><br>' \
               + 'Year Built:<br>' \
               + built \
               + '<br><br>' \
               + 'Square Footage:<br>' \
               + sqft \
               + '<br><br>' \
               + '<a href="https://plankton-app-5raue.ondigitalocean.app/webapp"> <b><p <p style="color:green;"><img src="https://raw.githubusercontent.com/osostudionyc/verde1/Pictures/restart2.jpg" style="width:250px; border: solid 0px #CCC"</p></b> </a>'
               

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
            <center><a href='/' ><img src="https://raw.githubusercontent.com/osostudionyc/verde1/Pictures/verde.png" width="350"></a>
            <br><i>[Enter some basic information about your proeprty and our proprietary database will create a custiome report with the best ROI renovation projects] </i><br><br><br><br><br>
            <br><br>
            <label>Alternate: Enter a custom budget: $</label>
            <input type="text" name="custbudget"><br><br>
            <br><br>
            <label>Address:</label>
            <input type="text" name="address"><br><br>
            <br><br>
            <label>City</label>
            <input type="text" name="city"><br><br>
            <br><br>
            <label>State</label>
            <input type="text" name="state"><br><br>
            <br><br>
            

            <label> What Type of Property </label>
            <select name="type">
                <option value="1">Multi</option>
                <option value="2">$100</option>
                <option value="3">$250</option>
                <option value="4">$500</option>
                <option value="5">$1k+</option>
            </select>
            <br><br><br><br>
            <label>Year Built</label>
            <input type="text" name="built"><br><br>
            <br><br>
            <label>Square Footage</label>
            <input type="text" name="sqft"><br><br>
            <br><br>
            <i> The app will rank products by health impact and create a custom priority list based on your desired spend </p>
            <br>
            <br>
            <input type="submit" value="Submit"></center>
        </form>
    '''





@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    try:
        # The data we send to the PDFMonkey template
        template_data = request.json.get('data')

        # Your PDFMonkey template ID
        template_id = request.json.get('template_id')

        # Prepare the payload for the API request
        payload = {
            'document': {
                'document_template_id': template_id,
                'payload': template_data
            }
        }

        # Make the API call to PDFMonkey
        response = requests.post(PDFMONKEY_DOCUMENTS_ENDPOINT, json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 201:
            pdf_document = response.json()
            return jsonify({
                'status': 'success',
                'pdf_id': pdf_document['data']['id'],
                'pdf_url': pdf_document['data']['attributes']['download_url']
            }), 201
        else:
            return jsonify({'status': 'error', 'message': 'Failed to generate PDF'}), response.status_code

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

    curl -X POST http://127.0.0.1:5000/generate_pdf \
          -H "Content-Type: application/json" \
          -d '{
                "template_id": "B42E8ED7-A637-4073-9671-B0ABA6537858",
                "data": {
                    "name": "John Doe",
                    "date": "2024-09-16"
                }
              }'


#main driver function 

if __name__ == '__main__':
    app.run()
