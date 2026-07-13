from app import app, db, Category, Item

MASSIVE_SEED_DATA = {
    ("House and kitchen cleaning supplies", "Limpieza casa y cocina"): [
        ("Bleach", "Lejía"),
        ("Ammonia", "Amoníaco"),
        ("Muriate (hydrochloric acid)", "Salfumán"),
        ("Floor cleaner", "Friegasuelos"),
        ("Forniture cleaner", "Pronto"),
        ("Glass cleaner", "Limpiacristales"),
        ("Ceramic hob cleaner", "Limpia vitrocerámica"),
        ("Broom", "Escoba"),
        ("Mop", "Fregona"),
        ("Mop handle", "Palo esoba/fregona"),
        ("Dustpan", "Recogedor"),
        ("Dish soap", "Lavavajillas"),
        ("Scouring pad", "Estropajo"),
        ("Inox Scouring pad", "Nanas"),
        ("Cloth", "Bayeta"),
        ("Garbage bags", "Bolsas de basura"),
        ("Poop bags", "Bolsas de cacas"),
        ("Dog treats", "Premio perro"),
        ("Detergent", "Detergente"),
        ("Fabric softener", "Suavizante"),
        ("Laundry bleach", "Lejía ropa"),
        ("Stain remover", "Quitamanchas"),
        ("Bleach with detergent", "Lejía con detergente"),
        ("Tupperware containers", "Tuppers"),
        ("Paper plates", "Platos papel"),
        ("Paper cups", "Vasos papel"),
        ("Paper cutlery", "Cubiertos papel"),
        ("Matches", "Cerillas"),
        ("Aluminum foil", "Papel plata"),
        ("Baking paper", "Papel horno"),
        ("Absorbent paper towels", "Papel cocina absorbente"),
        ("Cling film", "Film"),
        ("Dog canned food", "Comida perro lata"),
        ("Dog kibble", "Comida perro pienso"),
        ("Mosquito repellent", "Repelente mosquitos"),
        ("Insecticide", "Insecticida"),
    ],
    ("Personal hygiene supplies", "Limpieza personal"): [
        ("Toilet paper", "Papel wc"),
        ("Roll-on deodorant", "Desodorante rollon"),
        ("Deodorant gel", "Desodorante “gel”"),
        ("Shower gel", "Gel"),
        ("Shampoo", "Champú"),
        ("Hair conditioner", "Suavizante pelo"),
        ("Moisturizer", "Crema hidratante"),
        ("Sunscreen", "Crema solar"),
        ("After-sun lotion", "Aftersun"),
        ("Lotion Anti-aging", "Crema antiedad"),
        ("Cologne", "Colonia"),
        ("Mouthwash", "Enjuague bucal"),
        ("Toothpaste", "Pasta de dientes"),
        ("Toothbrush", "Cepillo de dientes"),
        ("Dental floss", "Hilo dental"),
        ("Toilet wipes", "Toallitas wc"),
        ("Cotton sticks", "Palillos oídos"),
        ("Tissues", "Clinex"),
    ],
    ("Bakery", "Panadería"): [
        ("Chocolate", "Chocolate"),
        ("Maria biscuits", "Galletas maría"),
        ("Croissants", "Croissants"),
        ("Chocolate cookies", "Galletas choco"),
        ("Digestive biscuits", "Galletas digestive"),
        ("Bread", "Pan"),
        ("Muffins", "Magdalenas"),
        ("Sponge cakes", "Bizcochos soletilla"),
        ("Empanadas (Mexican pastries)", "Empanadas"),
        ("Coffee", "Café"),
        ("Instant coffee", "Café soluble"),
        ("Tea", "Te"),
        ("Herbal teas", "Infusiones"),
        ("Breadsticks", "Picos"),
        ("Bread with tomato", "Pan con tomate"),
        ("Sugar", "Azúcar"),
        ("Sweetener", "Edulcorante"),
        ("Cereal", "Cereales"),
        ("Breadcrumbs", "Pan rayado"),
    ],
    ("Refrigerated desserts", "Postres refrigerados"): [
        ("Yogurt", "Yogur"),
        ("Custard", "Natillas"),
        ("Flan", "Flan"),
        ("Chocolate mousse", "Copa chocolate"),
        ("Rice pudding", "Arroz con leche"),
    ],
    ("Cured meats", "Embutidos"): [
        ("Fuet (Catalan sausage)", "Fuet"),
        ("Chorizo ​​(Spanish sausage)", "Chorizo"),
        ("Eggs", "Huevos"),
        ("Cheese", "Queso"),
        ("York ham", "Jamón york"),
        ("Serrano ham", "Jamón serrano"),
        ("Cream cheese", "Queso untar"),
        ("Plastic sausages", "Salchichas plástico"),
		("Mascarpone", "Mascarpone"),
    ],
    ("Meat and fish", "Carne y pescado"): [
        ("Ground beef", "Carne picada"),
        ("Country sausages", "Salchichas país"),
        ("Chicken", "Pollo"),
        ("Pork", "Cerdo"),
        ("Beef", "Ternera"),
        ("Fish", "Pescado"),
    ],
    ("Legumes", "Legumbres"): [
        ("Dried Chickpeas", "Garbanzos secos"),
        ("Canned Chickpeas", "Garbanzos bote"),
        ("Dried Lentils", "Lentejas secas"),
        ("Canned Lentils", "Lentejas bote"),
        ("Dried Beans", "Judias secas"),
        ("Canned Beans", "Judías bote"),
        ("Pasta", "Pasta"),
        ("Stuffed Pasta", "Pasta rellena"),
        ("Rice", "Arroz"),
        ("Couscous", "Cuscus"),
        ("Quinoa", "Quinoa"),
        ("Textured Soy Protein", "Soja texturizada"),
    ],
    ("Canned Goods", "Conservas"): [
        ("Canned Mushrooms", "Champis lata"),
        ("Canned Corn", "Maíz lata"),
        ("Canned Sardines", "Sardinas lata"),
        ("Canned Mussels", "Mejillones lata"),
        ("Canned Peppers", "Pimiento lata"),
        ("Crushed Tomatoes", "Tomate triturado"),
        ("Fried Tomatoes", "Tomate frito"),
        ("Coconut Milk", "Leche coco"),
        ("Pepper", "Pimienta"),
        ("Oregano", "Orégano"),
        ("Paprika", "Pimentón"),
        ("Tuna", "Atún"),
        ("Soup", "Sopa"),
        ("Ball Stock", "Avecrem"),
        ("Cinnamon", "Canela"),
    ],
    ("Snacks", "Aperitivos"): [
        ("Olives", "Aceitunas"),
        ("Pithless Olives", "Aceitunas sin hueso"),
        ("Potato Chips", "Patatas fritas"),
        ("Nachos", "Nachos"),
        ("Corn Tortilla Chips", "Tortitas maíz"),
        ("Popcorn", "Palomitas maíz"),
        ("Oil", "Aceite"),
        ("Vinegar", "Vinagre"),
        ("Salt", "Sal"),
        ("Mayonnaise", "Mahonesa"),
        ("Pesto", "Pesto"),
        ("Nuts", "Frutos secos"),
        ("Soy Sauce", "Salsa soja"),
        ("Hot Sauce", "Salsa picante"),
        ("Cream", "Nata"),
        ("Chewing Gum", "Chicles"),
    ],
    ("Drinks", "Bebidas"): [
        ("Vermouth", "Vermut"),
        ("Beer", "Cerveza"),
        ("Cava", "Cava"),
        ("Wine", "Vino"),
        ("Lambrusco", "Lambrusco"),
        ("Red Wine Summer", "Tinto de verano"),
        ("Soda", "Gaseosa"),
        ("Coca-Cola", "Cocacola"),
        ("Milk", "Leche"),
        ("Soy Milk", "Leche soja"),
        ("Horchata", "Horchata"),
        ("Juice", "Zumo"),
        ("Cacaolat", "Cacaolat"),
        ("Water", "Agua"),
        ("Liqueur Cream", "Crema de licor"),
    ],
    ("Frozen Foods", "Congelados"): [
        ("Pizza", "Pizza"),
        ("Croquettes", "Croquetas"),
        ("Ice Cream", "Helado"),
        ("Peas", "Guisantes"),
        ("Spinach", "Espinacas"),
        ("Cannelloni", "Canelones"),
        ("Polines", "Polines"),
    ],
    ("Prepared Foods", "Comida preparada"): [
        ("Hummus", "Hummus"),
        ("Chicken", "Pollo"),
        ("Omelette", "Tortilla"),
        ("Avocado", "Aguacate"),
        ("Canned Foods", "Comida lata"),
        ("Salmorejo", "Salmorejo"),
        ("Gazpacho", "Gazpacho"),
        ("Guacamole", "Guacamole"),
    ],
    ("Fruit and Vegetables", "Frutería"): [
        ("Tomatoes", "Tomates"),
        ("Green Peppers", "Pimientos verdes"),
        ("Red Peppers", "Pimientos rojos"),
        ("Fruit", "Fruta"),
        ("Eggplants", "Berenjenas"),
        ("Onions", "Cebollas"),
        ("Potatoes", "Patatas"),
        ("Zucchini", "Calabacín"),
        ("Pumpkin", "Calabaza"),
        ("Sweet Potatoes", "Boniatos"),
        ("Carrots", "Zanahoria"),
        ("Lettuce", "Lechuga"),
    ],
}

def seed_massive_data():
    with app.app_context():
        added_categories = 0
        added_items = 0

        for (cat_en, cat_es), items in MASSIVE_SEED_DATA.items():
            category = Category.query.filter_by(name_en=cat_en, user_id=None).first()

            if not category:
                category = Category(name_en=cat_en, name_es=cat_es, user_id=None)
                db.session.add(category)
                db.session.commit()
                added_categories += 1

            for item_en, item_es in items:
                item = Item.query.filter_by(name_en=item_en, category_id=category.id, user_id=None).first()

                if not item:
                    new_item = Item(category_id=category.id, name_en=item_en, name_es=item_es, user_id=None)
                    db.session.add(new_item)
                    added_items += 1

            db.session.commit()

        print("=========================================")
        print("✅ Database successfully updated!")
        print(f"📁 Categories added: {added_categories}")
        print(f"📝 Items added: {added_items}")
        print("=========================================")

if __name__ == '__main__':
    seed_massive_data()
