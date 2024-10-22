import requests   

response = requests.get('https://finance.naver.com/marketindex/?tabSel=materials#tab_section')

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')

material_prices = soup.select( 'div.section_material table.tbl_exchange tr.up td.tit' )
type(material_prices)

for material in material_prices:
    #print(f'Tag : {material}, material_price : {material.text}')
    print(material.text)
    pass

pass