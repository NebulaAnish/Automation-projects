def get_clinic(clinic_id):
    
    url = "https://12695.portal.athenahealth.com/"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    h1_list = soup.find_all('h1')
    clinic_name= h1_list[-1].text.strip()
    return clinic_name
