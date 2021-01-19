import glob 
import numpy as np

def BAM_number_list():
    elements = np.arange(1, 128, 1)
    #study 56 
    elements = elements[(elements<56)|(elements>57)] 
    elements = elements[(elements<74)|(elements>87)] # very high unf
    elements = elements[(elements<91)|(elements>91)] # precessing
    elements = elements[(elements<93)|(elements>94)] # precessing
    elements = elements[(elements<110)|(elements>119)] # very high unf
    return elements

def BAM_number_conversion(i):
    if i==0:
        i=i+1
    if i < 10:
        BAM_number = "000"+str(i)
    elif i<100:
        BAM_number = "00"+str(i)
    else:
        BAM_number = "0"+str(i) 
    return BAM_number



html_template = """
<body>
    <h1>Hello, {first_header:}!</h1>
    <p>{p2:}, {p1:}!</p>
</body>
"""
html_head= """
<html>
<head>
<style>
	.autoResizeImage {
		max-width: 100%;
		max-height: 100%;
	}
</style>
</head>
<body>
<title></title>

<div>
<table border=1 width=80%>
<tr>
	<th>BAM number</th>
	<th>delta amplitude</th>
	<th>delta phase</th>
</tr>
"""

html_loop = """
<tr>
	<td>BAM:{}</td>
	<td><img class="autoResizeImage" src="{}"\></td>
	<td><img class="autoResizeImage" src="{}"\></td>
</tr>
"""
html_end = """
</table>

</div>
</body>
</html>
"""
path_amp = "/home/luca/Documents/Nextcloud/AEI/Projects/webpage_waveforms/FD/amp/"
path_deltaamp = "/home/luca/Documents/Nextcloud/AEI/Projects/webpage_waveforms/FD/deltaamp/"
elements = BAM_number_list()
html_image_blocks = ""
for BAM in elements:
    BAM_element = BAM_number_conversion(BAM)
    print(BAM_element)
    html_image_blocks += html_loop.format(BAM_element, path_amp+BAM_element+".png", path_deltaamp+BAM_element+".png")


index = html_head+html_image_blocks+html_end
f = open('index.html', 'w')
f.write(index)
f.close()
