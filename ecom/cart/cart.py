from store.models import Product
class Cart():
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        #Make sure the session Cart is available on all pages of site    
        self.cart = cart

    def add(self, product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        #Logic

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id]= {' price ': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def cart_total(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)
        quantites = self.cart
        total=0
        for key, value in quantites.items():
            Key =int(key)
            for product in products:
                if product.id == Key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:    
                         total = total + (product.price * value)
        return total            

    def __len__(self):
        return len(self.cart)


    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)   
        return products     

    def get_quants(self):
        quantites =self.cart
        return quantites  

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        
        ourcart[product_id]=product_qty
        self.session.modified = True
        thing = self.cart
        return thing 


    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True