from datetime import datetime
import pytz
from bs4 import BeautifulSoup
import requests
import csv
import re
with open('schoolsorg.csv', "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Berlin time','URL','Name','State','District','Block','Cluster','About','Rating','UDISE Code','Building','Class Rooms','Boys Toilet','Girls Toilet',
                     'Computer Aided Learning','Electricity','Wall','Library','Village / Town','Playground','Books in Library','Drinking Water','Ramps for Disable',
                     'Computers','Academic','Instruction Medium','Male Teachers','Pre Primary Sectin Avilable','Board for Class 10th','School Type','Classes',
                     'Female Teacher','Pre Primary Teachers','Board for Class 10+2','Meal','Establishment','School Area','School Shifted to New Place','Head Teachers',
                     'Head Teacher','Is School Residential','Residential Type','Total Teachers','Contract Teachers','Management','Google maps link'])
    roi = 'no info on the website'
    response = requests.get('https://schools.org.in/schools-in-india.html', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, "html.parser")
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    for v in soup.select('.table.table-striped tr')[1:]:
        lnk = 'https://schools.org.in/' + v.find('a')['href']
        state = v.find('a').text.replace('Schools in','').strip()
        respons = s.get(lnk)
        print(f'\nPAGE 1: {lnk}\n')
        sorpa = BeautifulSoup(respons.content, "html.parser")   
        for v in sorpa.select('.table.table-striped tr')[1:]:
            page = 'https://schools.org.in/' + v.find('a')['href']
            district = v.find('a').text.replace('Schools in','').strip()
            respon = s.get(page)
            print(f'\nPAGE 2: {page}\n')
            sorp = BeautifulSoup(respon.content, "html.parser")         
            for v in sorp.select('.table.table-striped tr')[1:]:
                pag = 'https://schools.org.in/' + v.find('a')['href']
                block = v.find('a').text.replace('Schools in','').strip()
                respo = s.get(pag)
                print(f'\nPAGE 3: {pag}\n')
                sor = BeautifulSoup(respo.content, "html.parser")             
                for v in sor.select('.table.table-striped tr')[1:]:
                    pa = 'https://schools.org.in/' + v.find('a')['href']
                    cluster = v.find('a').text.replace('Schools in','').strip()
                    resp = s.get(pa)
                    print(f'\nPAGE 4: {pa}\n')
                    sorr = BeautifulSoup(resp.content, "html.parser")
                    for v in sorr.select('.table.table-striped tr')[1:]:
                        url = 'https://schools.org.in/' + v.find('a')['href']
                        name = v.find('a').text.replace('Schools in','').strip()
                        res = s.get(url)
                        print(url)
                        soupa = BeautifulSoup(res.content, "html.parser")
                        about = soupa.find(class_='my-3 p-3 bg-white border border-muted').text.strip() if soupa.find(class_='my-3 p-3 bg-white border border-muted') else roi
                        rating = soupa.find(style='margin:5px 0px; font-size:16px; text-align:center').text.strip() if soupa.find(style='margin:5px 0px; font-size:16px; text-align:center') else roi
                        udise = soupa.find(string=re.compile(r'UDISE Code')).find_next().text.strip() if soupa.find(string=re.compile(r'UDISE Code')) else roi
                        building = soupa.find(string=re.compile(r'Building:')).find_next().text.strip() if soupa.find(string=re.compile(r'Building:')) else roi
                        rooms = soupa.find(string=re.compile(r'Class Rooms:')).find_next().text.strip() if soupa.find(string=re.compile(r'Class Rooms:')) else roi
                        btoilet = soupa.find(string=re.compile(r'Boys Toilet:')).find_next().text.strip() if soupa.find(string=re.compile(r'Boys Toilet:')) else roi
                        gtoilet = soupa.find(string=re.compile(r'Girls Toilet:')).find_next().text.strip() if soupa.find(string=re.compile(r'Girls Toilet:')) else roi
                        aid = soupa.find(string=re.compile(r'Computer Aided Learning:')).find_next().text.strip() if soupa.find(string=re.compile(r'Computer Aided Learning:')) else roi
                        electr = soupa.find(string=re.compile(r'Electricity:')).find_next().text.strip() if soupa.find(string=re.compile(r'Electricity:')) else roi
                        wall = soupa.find(string=re.compile(r'Wall:')).find_next().text.strip() if soupa.find(string=re.compile(r'Wall:')) else roi
                        library = soupa.find(string=re.compile(r'Library:')).find_next().text.strip() if soupa.find(string=re.compile(r'Library:')) else roi
                        town = soupa.find(string=re.compile(r'Village / Town:')).find_next().text.strip() if soupa.find(string=re.compile(r'Village / Town:')) else roi
                        playg = soupa.find(string=re.compile(r'Playground:')).find_next().text.strip() if soupa.find(string=re.compile(r'Playground:')) else roi
                        nbooks = soupa.find(string=re.compile(r'Books in Library:')).find_next().text.strip() if soupa.find(string=re.compile(r'Books in Library:')) else roi
                        water = soupa.find(string=re.compile(r'Drinking Water:')).find_next().text.strip() if soupa.find(string=re.compile(r'Drinking Water:')) else roi
                        ramps = soupa.find(string=re.compile(r'Ramps for Disable:')).find_next().text.strip() if soupa.find(string=re.compile(r'Ramps for Disable:')) else roi
                        computers = soupa.find(string=re.compile(r'Computers:')).find_next().text.strip() if soupa.find(string=re.compile(r'Computers:')) else roi
                        academic = soupa.find(class_='mt-3 p-3 bg-white border border-muted').text.replace(':','').replace('✔ Academic -','').strip() if soupa.find(class_='mt-3 p-3 bg-white border border-muted') else roi
                        instr = soupa.find(string=re.compile(r'Instruction Medium:')).find_next().text.strip() if soupa.find(string=re.compile(r'Instruction Medium:')) else roi
                        malet = soupa.find(string=re.compile(r'Male Teachers:')).find_next().text.strip() if soupa.find(string=re.compile(r'Male Teachers:')) else roi
                        preprimary = soupa.find(string=re.compile(r'Pre Primary Sectin Avilable:')).find_next().text.strip() if soupa.find(string=re.compile(r'Pre Primary Sectin Avilable:')) else roi
                        board = soupa.find('sup',string='th').find_next().text.strip() if soupa.find('sup',string='th') else roi
                        tyype = soupa.find(string=re.compile(r'School Type:')).find_next().text.strip() if soupa.find(string=re.compile(r'School Type:')) else roi
                        classes = soupa.find(string=re.compile(r'Classes:')).find_next().text.strip() if soupa.find(string=re.compile(r'Classes:')) else roi
                        femalet = soupa.find(string=re.compile(r'Female Teacher:')).find_next().text.strip() if soupa.find(string=re.compile(r'Female Teacher:')) else roi
                        preprim = soupa.find(string=re.compile(r'Pre Primary Teachers:')).find_next().text.strip() if soupa.find(string=re.compile(r'Pre Primary Teachers:')) else roi
                        board2 = soupa.find(string=' Board for Class 10+2 ').find_next().text.strip() if soupa.find(string=' Board for Class 10+2 ') else roi
                        meal = soupa.find(string=re.compile(r'Meal')).next_element.strip() if soupa.find(string=re.compile(r'Meal')) else roi
                        estab = soupa.find(string=re.compile(r'Establishment:')).find_next().text.strip() if soupa.find(string=re.compile(r'Establishment:')) else roi
                        area = soupa.find(string=re.compile(r'School Area:')).find_next().text.strip() if soupa.find(string=re.compile(r'School Area:')) else roi
                        shift = soupa.find(string=re.compile(r'School Shifted to New Place:')).find_next().text.strip() if soupa.find(string=re.compile(r'School Shifted to New Place:')) else roi
                        head = soupa.find(string=re.compile(r'Head Teachers:')).find_next().text.strip() if soupa.find(string=re.compile(r'Head Teachers:')) else roi
                        headt = soupa.find(string=re.compile(r'Head Teacher:')).find_next().text.strip() if soupa.find(string=re.compile(r'Head Teacher:')) else roi
                        residental = soupa.find(string=re.compile(r'Is School Residential:')).find_next().text.strip() if soupa.find(string=re.compile(r'Is School Residential:')) else roi
                        restype = soupa.find(string=re.compile(r'Residential Type:')).find_next().text.strip() if soupa.find(string=re.compile(r'Residential Type:')) else roi
                        totalte = soupa.find(string=re.compile(r'Total Teachers:')).find_next().text.strip() if soupa.find(string=re.compile(r'Total Teachers:')) else roi
                        contractt = soupa.find(string=re.compile(r'Contract Teachers:')).find_next().text.strip() if soupa.find(string=re.compile(r'Contract Teachers:')) else roi
                        manage = soupa.find(string=re.compile(r'Management:')).find_next().text.strip() if soupa.find(string=re.compile(r'Management:')) else roi
                        if soupa.find(string=re.compile(r'lat:')):
                            match = re.search(r'lat:([^,]+), lng:([^}]+)', soupa.find(string=re.compile(r'lat:')))
                            gmap = f"https://maps.google.com/maps?ll={match.group(1)},{match.group(2)}" if match else roi
                        else:
                            gmap = roi
                        berlin = datetime.now(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%d %H:%M:%S %Z')
                        writer.writerow([berlin,url,name,state,district,block,cluster,about,rating,udise,building,rooms,btoilet,gtoilet,aid,electr,wall,library,town,
                                         playg,nbooks,water,ramps,computers,academic,instr,malet,preprimary,board,tyype,classes,femalet,preprim,board2,meal,estab,area,
                                         shift,head,headt,residental,restype,totalte,contractt,manage,gmap])