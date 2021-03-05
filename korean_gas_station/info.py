def get_brand(page):
    return [each.img['alt'] for each in page]
def get_isself(page):
    gas_self=[]
    for each in page:
        if each.span is None:
            gas_self.append('N')
        else:
            gas_self.append('Y')
    return gas_self

def get_name(page):
    name=[]
    for each in page:
        candi = each.a.string
        candi = candi.replace('\n','')
        candi = candi.replace('\t','')
        candi = candi.replace('.','')
        name.append(candi)
    return name

def gas_price(price):
    gas_price=[]
    for i in range(0, len(price)):
        if i%2 !=0:
            gas_price.append(price[i])
    return gas_price

def diesel_price(price):
    diesel_price=[]
    for i in range(0, len(price)):
        if i%2 ==0:
            diesel_price.append(price[i])
    return diesel_price