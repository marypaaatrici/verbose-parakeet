from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from tmdbv3api import TMDb
from tmdbv3api import Movie
import time
import csv
import json
import pyperclip
import random
import string

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "movie"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

email ='sigasaina@gmail.com'
password='sigasaina@gmail.com40z'


def web_driver():
     options = webdriver.ChromeOptions()
     options.add_argument("--verbose")
     # options.add_argument('--no-sandbox')
     # options.add_argument('--headless')
     options.add_argument('--disable-gpu')
     # options.add_argument("--window-size=1920, 1200")
     options.add_argument('--disable-dev-shm-usage')
     driver = webdriver.Chrome(options=options)
     return driver
        


driver = web_driver()
driver.maximize_window()



driver.get('https://knowt.com/')
time.sleep(5)

driver.find_element(By.CSS_SELECTOR,'.MuiBox-root.mui-qkvqai').click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'#Email').send_keys(email)
time.sleep(2)




driver.find_element(By.CSS_SELECTOR,'#Password').send_keys(password,Keys.ENTER)
time.sleep(10)


with open('id.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        tmdb = TMDb()
        tmdb.api_key = 'ce7dc231f477c13ba0789c8de9268db4'
        tmdb.language = 'en-EN'
        movie = Movie()
        

        
        m = movie.details(line[0])
        # poster_path = m.poster_path

        
        year = m.release_date[0:4]
        # poster = 'https://image.tmdb.org/t/p/w185/'+poster_path
        link   ='https://app.geoflix.me/movie/'+line[0]+'?ref=fb-es'
        title  =m.title
        original = m.original_title


        judul = f"++TOP! [PELISPLUS] ～  VER!! {title} Película Completa en Español Y Latino"
            


        # POSTING AND LOOP

        driver.get("https://knowt.com/")
        time.sleep(10)

        driver.find_element(By.CSS_SELECTOR,'.MuiBox-root.mui-1dk0m5b').click()
        time.sleep(2)


        driver.find_element(By.XPATH,"//span[text()='Notes']").click()
        time.sleep(8)


        driver.find_element(By.CSS_SELECTOR,"textarea[placeholder='Untitled']").send_keys(judul)
        time.sleep(2)

        konten =f'''

𝚑𝚊𝚌𝚎 𝟶9 𝚖𝚒𝚗𝚞𝚝𝚘𝚜 — 𝙿𝚎𝚕𝚒𝚜𝚙𝚕𝚞𝚜 𝚅𝚎𝚛 {title} 𝚙𝚎𝚕í𝚌𝚞𝚕𝚊 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚊 𝚎𝚗 𝚕𝚒𝚗𝚎𝚊 𝚎𝚗 𝚎𝚜𝚙𝚊ñ𝚘𝚕. 𝚟𝚎𝚛 𝚐𝚛𝚊𝚝𝚒𝚜 𝚎𝚗 𝚕í𝚗𝚎𝚊 [𝚅𝚎𝚛 {title}] {year} 𝚎𝚗 𝚎𝚜𝚙𝚊ñ𝚘𝚕 𝚕𝚊𝚝𝚒𝚗𝚘 | 𝙳𝚒𝚜𝚏𝚛𝚞𝚝𝚊 𝚍𝚎 𝚕𝚊 𝙿𝚎𝚕í𝚌𝚞𝚕𝚊 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚊 𝚍𝚎 {title} 𝚎𝚗 𝙷𝙳 𝚌𝚘𝚗 𝙰𝚞𝚍𝚒𝚘 𝙴𝚜𝚙𝚊ñ𝚘𝚕 𝚢 𝙻𝚊𝚝𝚒𝚗𝚘 𝚂𝚞𝚋𝚝𝚒𝚝𝚞𝚕𝚊𝚍𝚘.<br>
<br>
<br>
<a href="{link}">➤ ►🌍📺📱👉 𝚅𝙴𝚁 𝙰𝙷𝙾𝚁𝙰 ➤► {title} ({year}) 𝙿𝚎𝚕𝚒𝚌𝚞𝚕𝚊 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚊 𝙾𝚗𝚕𝚒𝚗𝚎 𝚎𝚗 𝙴𝚜𝚙𝚊ñ𝚘𝚕 </a><br>
<br>
<a href="{link}">➤ ►🌍📺📱👉𝙳𝙴𝚂𝙲𝙰𝚁𝙶𝙰𝚁 ➤► {title} ({year}) 𝙿𝚎𝚕𝚒𝚌𝚞𝚕𝚊 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚊 𝙾𝚗𝚕𝚒𝚗𝚎 𝚎𝚗 𝙴𝚜𝚙𝚊ñ𝚘𝚕 </a><br>
<br>
¿Dónde puedo ver la serie {title}?<br>
<br>
Estreno de {title} en Prime Video.<br>
<br>
¿Dónde puedes ver {title}?<br>
<br>
Cuándo y dónde ver {title}. La película {title} estará disponible exclusivamente en Amazon Prime Video a partir del viernes 27 de diciembre. La película se puede ver en streaming de forma gratuita para cualquier persona con una suscripción a Amazon Prime.<br>
<br>
¿Cuándo sale {title} 2 la película?<br>
<br>
¿CÓMO VER “{title}? “{title} se estrenará el viernes 27 de diciembre de 2024 en Amazon Prime Video por lo tanto para ver la secuela de la película española solo necesitas una suscripción a dicha plataforma de streaming.<br>
<br>
¿Dónde encuentro la película {title}?<br>
<br>
La esperada película española {title} llega a Prime Video.<br>
<br>
¿Dónde puedes ver {title} 2?<br>
<br>
{title} solo se transmitirá en Amazon Prime Video para suscriptores de Amazon Prime.<br>
<br>
¿Cuándo darán {title}?<br>
<br>
Tras el éxito de la primera película no solo en España sino en el resto de territorios Prime Video no dudaría en dar luz verde a sus dos secuelas. {title} la primera secuela de Culpa mía llega a Prime Video este 27 diciembre de 2024 justo a tiempo para ser disfrutada en las vacaciones de Navidad.<br>
<br>
¿{title} está en Netflix?<br>
<br>
A finales de 2024 las películas de 20th Century Studios se dirigirán a Hulu o Disney+ una vez que salgan de los cines. ¿La película The {title} está en Netflix Crunchyroll Hulu o Amazon Prime? Netflix: The {title} actualmente no está disponible en Netflix.<br>
<br>
¿Dónde puedo ver Mi Culpa 2?<br>
<br>
Prime Video ha dado luz verde a la película original española Tu culpa y nuestra culpa tras el éxito de Mi culpa que se estrenó en Prime Video el 8 de junio.<br>
<br>
¿{title} se lanza en Prime?<br>
<br>
EXCLUSIVA: {title} se estrena en Prime Video el 27 de diciembre y el guionista y director Domingo González promete que es un paso adelante respecto de la exitosa primera película Culpa Mía.<br>
<br>
¿Cuándo sale {title} en cine?<br>
<br>
Así {title} llega a Prime Video este 27 de diciembre un esperado estreno que hará las delicias de los espectadores.<br>
<br>
{title} 𝙿𝚎𝚕𝚒𝚌𝚞𝚕𝚊 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚊 | 𝟺𝙺 [𝙱𝚕𝚞 𝚁𝚊𝚢] 𝟺𝟼𝟶𝚙 - 𝟽𝟸𝟶𝚙 - 𝟷𝟶𝟾𝟶𝚙 - 𝙵𝚕𝚟 - 𝙼𝚙𝟺<br>
<br>
𝙲𝚞𝚎𝚟𝚊𝚗𝚊 𝟹 𝚅𝚎𝚛 {title} 𝙾𝚗𝚕𝚒𝚗𝚎 𝚎𝚗 𝙴𝚜𝚙𝚊ñ𝚘𝚕 𝙻𝚊𝚝𝚒𝚗𝚘 {title} ({year}) 𝙿𝚎𝚕í𝚌𝚞𝚕𝚊 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚊 𝙾𝚗𝚕𝚒𝚗𝚎 𝚎𝚗 𝙴𝚜𝚙𝚊ñ𝚘𝚕.<br>
<br>
𝙲𝚞𝚎𝚟𝚊𝚗𝚊 | 𝙴𝚜𝚝𝚛𝚎𝚗𝚘𝚜 | 𝙿𝚎𝚕𝚒𝚜𝚙𝚎𝚍𝚒𝚊 | 𝙿𝚎𝚕𝚒𝚜𝚙𝚕𝚞𝚜 | 𝙶𝚗𝚞𝚕𝚊 | 𝚁𝚎𝚙𝚎𝚕𝚒𝚜𝚙𝚕𝚞𝚜 | 𝚁𝚎𝚙𝚎𝚕𝚒𝚜 | 𝙿𝚎𝚕𝚒𝚜 | 𝙿𝚎𝚕𝚒𝚜𝚙𝚕𝚞𝚜| | 𝙽𝚎𝚝𝚏𝚕𝚒𝚡 | 𝙲𝚒𝚗𝚎 | 𝙲𝚒𝚗𝚎𝚖𝚊 | 𝙲𝚊𝚕𝚒𝚍𝚊𝚍 | 𝙼𝚎𝚓𝚘𝚛 | 𝙲𝚑𝚒𝚕𝚎<br>
<br>
𝚂𝚒𝚗𝚘𝚙𝚜𝚒𝚜 : 𝚃𝚛𝚊𝚜 𝚝𝚛𝚊𝚝𝚊𝚛 𝚍𝚎 𝚊𝚌𝚊𝚋𝚊𝚛 𝚙𝚘𝚛 𝚝𝚘𝚍𝚘𝚜 𝚕𝚘𝚜 𝚖𝚎𝚍𝚒𝚘𝚜 𝚌𝚘𝚗 𝚕𝚊 𝚟𝚒𝚍𝚊 𝚍𝚎 𝚂𝚒𝚎𝚗𝚗𝚊 𝚢 𝚜𝚞 𝚑𝚎𝚛𝚖𝚊𝚗𝚘 𝙹𝚘𝚗𝚊𝚝𝚑𝚊𝚗 𝚍𝚞𝚛𝚊𝚗𝚝𝚎 𝚞𝚗𝚊 𝚖𝚘𝚟𝚒𝚍𝚊 𝚗𝚘𝚌𝚑𝚎 𝚝𝚑𝚎 𝙷𝚊𝚕𝚕𝚘𝚠𝚎𝚎𝚗 𝚟𝚞𝚎𝚕𝚟𝚎 𝚎𝚕 𝚜𝚒𝚗𝚒𝚎𝚜𝚝𝚛𝚘 𝚢 𝚜𝚊𝚗𝚐𝚞𝚒𝚗𝚊𝚛𝚒𝚘 𝚊𝚜𝚎𝚜𝚒𝚗𝚘 𝚖𝚞𝚍𝚘 𝙰𝚛𝚝 𝚝𝚑𝚎 𝙲𝚕𝚘𝚠𝚗. 𝚂𝚎𝚐ú𝚗 𝚜𝚞 𝚍𝚒𝚛𝚎𝚌𝚝𝚘𝚛 𝙳𝚊𝚖𝚒𝚎𝚗 𝙻𝚎𝚘𝚗𝚎 𝚜𝚎 𝚝𝚛𝚊𝚝𝚊 𝚍𝚎 𝚕𝚊 𝚎𝚗𝚝𝚛𝚎𝚐𝚊 𝚖á𝚜 𝚜𝚊𝚗𝚐𝚛𝚒𝚎𝚗𝚝𝚊 𝚍𝚎 𝚝𝚘𝚍𝚊𝚜 𝚕𝚊𝚜 𝚚𝚞𝚎 𝚑𝚊 𝚏𝚒𝚕𝚖𝚊𝚍𝚘 𝚑𝚊𝚜𝚝𝚊 𝚎𝚕 𝚖𝚘𝚖𝚎𝚗𝚝𝚘 𝚎𝚗 𝚜𝚞 𝚌𝚊𝚛𝚛𝚎𝚛𝚊.<br>
<br>
𝚅𝚎𝚛 {title} 𝚎𝚗 𝚁𝚎𝙿𝚎𝚕𝚒𝚜 𝙶𝚛𝚊𝚝𝚒𝚜 » 𝙴𝚜𝚝á𝚜 𝚙𝚘𝚛 𝚅𝚎𝚛 {title} [𝙿𝚎𝚕í𝚌𝚞𝚕𝚊 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚊 𝙶𝚛𝚊𝚝𝚒𝚜]. 𝙻𝚊 𝙿𝚎𝚕í𝚌𝚞𝚕𝚊 {title} 𝙾𝚗𝚕𝚒𝚗𝚎 𝚎𝚗 𝙴𝚜𝚙𝚊ñ𝚘𝚕 𝙷𝙳. 𝙿𝚎𝚕í𝚌𝚞𝚕𝚊 {title} 𝙴𝚜𝚝𝚛𝚎𝚗𝚘 𝚍𝚎𝚕 𝟸𝟶𝟸𝟹 𝙶𝚛𝚊𝚝𝚒𝚜. 𝙿𝚎𝚕í𝚌𝚞𝚕𝚊𝚜 𝚎𝚗 𝙰𝚞𝚍𝚒𝚘 (𝙸𝚍𝚒𝚘𝚖𝚊) 𝙴𝚜𝚙𝚊ñ𝚘𝚕 𝙻𝚊𝚝𝚒𝚗𝚘 𝚘 𝙸𝚗𝚐𝚕é𝚜 (𝚂𝚞𝚋𝚝𝚒𝚝𝚞𝚕𝚊𝚍𝚊𝚜).<br>
<br>
𝚅𝚎𝚛 {title} ({year}) : 𝙿𝚎𝚕𝚒𝚌𝚞𝚕𝚊 𝙾𝚗𝚕𝚒𝚗𝚎 𝙻𝚊𝚝𝚒𝚗𝚘 𝙳𝚎𝚜𝚙𝚞é𝚜 𝚍𝚎 𝚞𝚗𝚊 𝚝𝚛𝚊𝚐𝚎𝚍𝚒𝚊 𝚏𝚊𝚖𝚒𝚕𝚒𝚊𝚛 𝚒𝚗𝚎𝚜𝚙𝚎𝚛𝚊𝚍𝚊 𝚝𝚛𝚎𝚜 𝚐𝚎𝚗𝚎𝚛𝚊𝚌𝚒𝚘𝚗𝚎𝚜 𝚍𝚎 𝚕𝚊 𝚏𝚊𝚖𝚒𝚕𝚒𝚊 𝙳𝚎𝚎𝚝𝚣 𝚛𝚎𝚐𝚛𝚎𝚜𝚊𝚗 𝚊 𝚜𝚞 𝚑𝚘𝚐𝚊𝚛 𝚎𝚗 𝚕𝚊 𝚙𝚎𝚚𝚞𝚎ñ𝚊 𝚌𝚒𝚞𝚍𝚊𝚍 𝚍𝚎 𝚆𝚒𝚗𝚝𝚎𝚛 𝚁𝚒𝚟𝚎𝚛. 𝙻𝚊 𝚟𝚒𝚍𝚊 𝚍𝚎 𝙻𝚢𝚍𝚒𝚊 𝚚𝚞𝚎 𝚜𝚒𝚐𝚞𝚎 𝚊𝚝𝚘𝚛𝚖𝚎𝚗𝚝𝚊𝚍𝚊 𝚙𝚘𝚛 𝙱𝚒𝚝𝚎𝚕𝚌𝚑ú𝚜 𝚍𝚊 𝚞𝚗 𝚟𝚞𝚎𝚕𝚌𝚘 𝚌𝚞𝚊𝚗𝚍𝚘 𝙰𝚜𝚝𝚛𝚒𝚍 𝚜𝚞 𝚛𝚎𝚋𝚎𝚕𝚍𝚎 𝚑𝚒𝚓𝚊 𝚊𝚍𝚘𝚕𝚎𝚜𝚌𝚎𝚗𝚝𝚎 𝚍𝚎𝚜𝚌𝚞𝚋𝚛𝚎 𝚕𝚊 𝚖𝚒𝚜𝚝𝚎𝚛𝚒𝚘𝚜𝚊 𝚖𝚊𝚚𝚞𝚎𝚝𝚊 𝚍𝚎 𝚕𝚊 𝚌𝚒𝚞𝚍𝚊𝚍 𝚎𝚗 𝚎𝚕 á𝚝𝚒𝚌𝚘 𝚢 𝚎𝚕 𝚙𝚘𝚛𝚝𝚊𝚕 𝚊𝚕 𝙼á𝚜 𝙰𝚕𝚕á 𝚜𝚎 𝚊𝚋𝚛𝚎 𝚍𝚎 𝚏𝚘𝚛𝚖𝚊 𝚊𝚌𝚌𝚒𝚍𝚎𝚗𝚝𝚊𝚕. 𝙲𝚘𝚗 𝚝𝚊𝚗𝚝𝚘𝚜 𝚙𝚛𝚘𝚋𝚕𝚎𝚖𝚊𝚜 𝚎𝚗 𝚊𝚖𝚋𝚘𝚜 𝚖𝚞𝚗𝚍𝚘𝚜 𝚎𝚜 𝚜ó𝚕𝚘 𝚌𝚞𝚎𝚜𝚝𝚒ó𝚗 𝚍𝚎 𝚝𝚒𝚎𝚖𝚙𝚘 𝚚𝚞𝚎 𝚊𝚕𝚐𝚞𝚒𝚎𝚗 𝚍𝚒𝚐𝚊 𝚝𝚛𝚎𝚜 𝚟𝚎𝚌𝚎𝚜 𝚎𝚕 𝚗𝚘𝚖𝚋𝚛𝚎 𝚍𝚎 𝙱𝚒𝚝𝚎𝚕𝚌𝚑ú𝚜 𝚢 𝚎𝚕 𝚝𝚛𝚊𝚟𝚒𝚎𝚜𝚘 𝚍𝚎𝚖𝚘𝚗𝚒𝚘 𝚟𝚞𝚎𝚕𝚟𝚊 𝚊 𝚕𝚊𝚜 𝚊𝚗𝚍𝚊𝚍𝚊𝚜 𝚙𝚊𝚛𝚊 𝚍𝚎𝚜𝚊𝚝𝚊𝚛 𝚜𝚞 𝚙𝚊𝚛𝚝𝚒𝚌𝚞𝚕𝚊𝚛 𝚌𝚊𝚘𝚜.<br>
<br>
𝚎𝚛 {title} {year} 𝙾𝚗𝚕𝚒𝚗𝚎 𝙶𝚛𝚊𝚝𝚒𝚜 𝚙𝚎𝚕í𝚌𝚞𝚕𝚊 𝚌𝚘𝚖𝚙𝚕𝚎𝚝𝚊 𝚎𝚗 𝙴𝚜𝚙𝚊ñ𝚘𝚕 𝚢 𝙻𝚊𝚝𝚒𝚗𝚘 𝙷𝙳 𝚎𝚗 𝙿𝚘𝚙𝙲𝚘𝚛𝚗𝚃𝚅. 𝙳𝚒𝚜𝚏𝚛𝚞𝚝𝚊 𝚍𝚎 {title} 𝚎𝚗 𝚊𝚕𝚝𝚊 𝚌𝚊𝚕𝚒𝚍𝚊𝚍 𝙷𝙳 𝚜𝚒𝚗 𝚛𝚎𝚐𝚒𝚜𝚝𝚛𝚘.<br>
<br>
𝚁𝙴𝙿𝙴𝙻𝙸𝚂-𝚃𝚅- 𝚅𝚎𝚛 𝚙𝚎𝚕í𝚌𝚞𝚕𝚊𝚜 𝚘𝚗𝚕𝚒𝚗𝚎 𝚎𝚗 𝚎𝚜𝚙𝚊ñ𝚘𝚕 𝚕𝚊𝚝𝚒𝚗𝚘 𝚢 𝚜𝚎𝚛𝚒𝚎𝚜 𝚍𝚎 𝚎𝚜𝚝𝚛𝚎𝚗𝚘 𝚌𝚘𝚖𝚙𝚕𝚎𝚝𝚊𝚜 𝚌𝚘𝚗 𝚝𝚘𝚍𝚘𝚜 𝚜𝚞𝚜 𝚌𝚊𝚙í𝚝𝚞𝚕𝚘𝚜 𝚐𝚛𝚊𝚝𝚒𝚜. 𝙿𝚎𝚕í𝚌𝚞𝚕𝚊𝚜 𝚢 𝚜𝚎𝚛𝚒𝚎𝚜 𝚎𝚗 𝙷𝙳 𝚌𝚘𝚗 𝚕𝚊 𝚟𝚎𝚗𝚝𝚊𝚓𝚊 𝚊𝚍𝚒𝚌𝚒𝚘𝚗𝚊𝚕 𝚍𝚎 𝚙𝚘𝚍𝚎𝚛 𝚟𝚎𝚛𝚕𝚊𝚜 𝚎𝚗 𝚝𝚞 𝙿𝚘𝚙𝙲𝚘𝚛𝚗𝚃𝚅.<br>
<br>
𝙴𝚜𝚝𝚎 𝚎𝚜 𝚞𝚗 𝚜𝚒𝚝𝚒𝚘 𝚍𝚎 𝚝𝚛𝚊𝚗𝚜𝚖𝚒𝚜𝚒ó𝚗 𝚎𝚗 𝚕í𝚗𝚎𝚊 𝚍𝚘𝚗𝚍𝚎 𝚙𝚞𝚎𝚍𝚎 𝚟𝚎𝚛 𝚖𝚒𝚕𝚎𝚜 𝚍𝚎 𝚙𝚎𝚕í𝚌𝚞𝚕𝚊𝚜 𝚢 𝚙𝚛𝚘𝚐𝚛𝚊𝚖𝚊𝚜 𝚍𝚎 𝚝𝚎𝚕𝚎𝚟𝚒𝚜𝚒ó𝚗 𝚍𝚎𝚜𝚍𝚎 𝚙𝚎𝚕í𝚌𝚞𝚕𝚊𝚜 𝚍𝚎𝚜𝚝𝚊𝚌𝚊𝚍𝚊𝚜 𝚙𝚎𝚕í𝚌𝚞𝚕𝚊𝚜 𝚙𝚘𝚙𝚞𝚕𝚊𝚛𝚎𝚜 𝚢 𝚖𝚞𝚌𝚑𝚊𝚜 𝚘𝚝𝚛𝚊𝚜 𝚏𝚞𝚗𝚌𝚒𝚘𝚗𝚎𝚜 𝚌𝚘𝚗 𝚝𝚘𝚍𝚊𝚜 𝚕𝚊𝚜 𝚏𝚞𝚗𝚌𝚒𝚘𝚗𝚎𝚜.<br>
<br>
{title} {year}<br>
<br>
{title} 𝚌𝚞𝚎𝚟𝚊𝚗𝚊<br>
<br>
{title} 𝚙𝚎𝚕í𝚌𝚞𝚕𝚊 𝚌𝚘𝚖𝚙𝚕𝚎𝚝𝚊<br>
<br>
{title} 𝚘𝚗𝚕𝚒𝚗𝚎 𝚎𝚜𝚙𝚊ñ𝚘𝚕<br>
<br>
{title} 𝚛𝚎𝚙𝚎𝚕𝚒𝚜𝚙𝚕𝚞𝚜<br>
<br>
{title} 𝚌𝚘𝚖𝚙𝚕𝚎𝚝𝚊 𝚐𝚛𝚊𝚝𝚒𝚜<br>
<br>
{title} 𝚙𝚎𝚕𝚒𝚜𝚙𝚕𝚞𝚜<br>

        


        '''

        konten_bersih = konten.replace('"', '\\"').replace("'", "\\'").replace("\n", "\\n")

        driver.execute_script(f'document.querySelector("p.is-empty.is-editor-empty").innerHTML = "{konten_bersih}"  ')
        time.sleep(5)


        # SET PUBLIC
        driver.find_element(By.CSS_SELECTOR,"button > span > svg.lucide-ellipsis-vertical").click()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR,"div > svg.lucide-lock").click()
        time.sleep(2)

        driver.find_element(By.XPATH," (//div[@role='button'])[1]").click()
        time.sleep(5)

        getlink = driver.find_element(By.XPATH,"//span[contains(text(), 'knowt.com')]")

        sharelink = getlink.text
        time.sleep(3)

        response = (
                supabase.table(SUPABASE_TABLE_NAME)
                .insert({"result": sharelink})
                .execute()
            )
        time.sleep(3)



       





       








