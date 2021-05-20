import requests
from bs4 import BeautifulSoup
import os
import json
import csv
import re
from tqdm import tqdm
from avlist import brands_code_list
from Classes.AVparser import AVparser

for k, v in brands_code_list.items():
    print(k)
    carslinks = {} 
    finalcars = []
    car_id = 0

    for x in tqdm(range(1,10)):

        headers = {
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
            'Accept-Encoding: gzip, deflate, br'
            'Accept-Language: en-US,en;q=0.9,ru;q=0.8'
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

        }

        r = requests.get(f'https://cars.av.by/filter?brands[0][brand]={v}&price_currency=2&page={x}')

        soup = BeautifulSoup(r.content, 'html.parser')
        carslist = soup.find_all('div', class_='listing-item')

        for item in carslist:

            parser = AVparser(item)

            title = parser.get_title()
            image = parser.get_image()
            year = parser.get_year()
            volume = parser.get_volume()
            engine = parser.get_engine()
            transmision = parser.get_transmission()
            miles = parser.get_miles()
            link = parser.get_link()
            price_ru = parser.get_price_ru()
            price_usd = parser.get_price_usd()


            # print(fmiles)       
 
            car_id += 1
        
            carslinks = {
                "id": car_id,
                'image': image,
                'title': title,
                'year': year,
                'volume': volume,
                'engine': engine,
                'transmision': transmision,
                'miles': miles,
                'link': link,
                'price_ru': price_ru,
                'price_usd': price_usd
            }

            finalcars.append(carslinks)

    print(len(finalcars))

    file_name = f'{k}.json'
 
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(finalcars, json_file, ensure_ascii = False, indent =4)
         
    # cars = "acura.csv"
    # with open(cars, mode='w') as employee_file:
    #     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    print('file dumped')