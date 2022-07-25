import data 

#? Loop through the colors data and display logo image and company name on an html page. 
#* to run the file:  python3 colorsProblem.py > index.html

companies = data.data

html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>  
    
        body{
            margin:0px;
        }
        div{
            display: flex;
            height: 50px;
            font-size: 50px;
        }
    </style>
</head>
<body>
"""

for i in companies:
    html += "<div> " + i["business_name"] + "</div>\n"
    html += "<div> <img src=\"" + i["logo"] + "\">\n"
 
html += """

</body>


</html>

"""

print(html)