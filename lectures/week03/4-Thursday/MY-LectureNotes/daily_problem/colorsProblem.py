
import color_data 

#? Loop through the colors data and display each color on an html page. 
#* to run the file:  python3 colorsProblem.py > index.html

color_data = color_data.colors

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
            height: 50px;
        }
    </style>
</head>
<body>
"""
hex = ''
for i in color_data:
    for j in i:
       if j == "hex_value":
           html+=f'<div style ="background-color :{i[j]} "></div>\n'
(i[j])
html += """

</body>
</html>

"""

print(html)