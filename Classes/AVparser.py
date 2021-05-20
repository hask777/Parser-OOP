import re

class AVparser:

    def __init__(self, item):
        self.item = item
        self.params = item.find('div', class_='listing-item__params').text

    def get_title(self):
        ''' Find car title '''
        title = self.item.find('span', class_='link-text').text

        return title

    def get_image(self):
        ''' Find car image '''
        photo = self.item.find('div', class_='listing-item__photo')
        try:
            image = photo.find('img')['data-src']
        except:
            image = "none"

        return image

    def get_year(self):
        ''' Year '''
        year_param = re.compile(r"(\d{4})")
        year =  year_param.search(self.params)
        try:
            fyear = year.group()
            # print(type(fyear))
        except:
            fyear = ''

        return fyear

    def get_volume(self):
        ''' Volume '''
        volume_param = re.compile(r"(\d{1}[.]\d{1})")
        volume = volume_param.search(self.params)
        try:
            fvolume = volume.group()
            fvolume = float(fvolume)
        except:
            fvolume = 0.0

        return fvolume

    def get_engine(self):
        ''' Engine '''
        engine_param = re.compile(r"(бензин|дизель)")
        engine = engine_param.search(self.params)
        # print(engine.group())
        try:
            fengine = engine.group()
        except:
            fengine = ''
        
        return fengine

    def get_transmission(self):
        ''' Transmision '''
        transmision_param = re.compile(r"(автомат|механика)")
        transmision = transmision_param.search(self.params)
        try:
            ftransmision = transmision.group()
        except:
            ftransmision = ''

        return ftransmision

    def get_miles(self):
        ''' Miles '''
        mile_param = re.compile(r"(\d{1}\s\d{3})|(\d{2}\s\d{3})|(\d{3}\s\d{3})")
        miles = mile_param.search(self.params)

        try:
            fmiles = miles.group()
            fmiles = fmiles.split()
                    
            for x in fmiles:
                x = int(x)

            fmiles = fmiles[0] + fmiles[1]
            fmiles = int(fmiles)
                # print(type(fmiles))
        except:
            fmiles = 0 

        return fmiles    

    def get_price_ru(self):
        ''' Find car price '''
        price_ru = self.item.find('div', class_='listing-item__price').text
        price_ru = price_ru.replace('р.', ' ').strip()
        price_ru = price_ru.split()

        try:
            for x in price_ru:
                x = int(x)

            price_ru = price_ru[0] + price_ru[1]
            price_ru = int(price_ru)
                # print(type(price_ru))
        except:
                price_ru = 0

        return price_ru

    def get_price_usd(self):
        ''' Find car price by usd '''
        price_usd = self.item.find('div', class_='listing-item__priceusd').text
        price_usd = price_usd.replace('≈', ' ')
        price_usd = price_usd.replace('$', ' ').strip()
        price_usd = price_usd.split()
                
        try:
            for x in price_usd:
                x = int(x)
            price_usd = price_usd[0] + price_usd[1]
            price_usd = int(price_usd)
        except:
                price_usd = 0

        return price_usd

    def get_link(self):
        ''' Find car link '''
        link = self.item.find('a', href=True)['href']

        return link