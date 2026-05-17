"""
Carga datos de ejemplo: 5 marcas de belleza de artistas reales + productos.

Uso:
    python manage.py seed_data

Las URLs de audio son a previews de SoundHelix (libres de derechos)
para evitar problemas de copyright en la demo académica.
Puedes reemplazarlas por previews de Spotify, archivos en Cloudinary,
o cualquier URL de mp3 pública.
"""
from decimal import Decimal
from urllib.parse import quote_plus
from django.core.management.base import BaseCommand
from catalog.models import Artist, Category, Product


def img(text, color='D97A93', w=400, h=500, font='playfair-display'):
    """Genera URL de placehold.co con color de marca y nombre del producto."""
    return (f'https://placehold.co/{w}x{h}/{color}/FFFFFF'
            f'?text={quote_plus(text)}&font={font}')


def artist_img(brand, color):
    """Imagen cuadrada grande para foto de artista."""
    return img(brand, color, w=600, h=600)


CATEGORIES = [
    ('Skincare', 'Cuidado de la piel: serums, cremas, limpiadores'),
    ('Makeup', 'Maquillaje: labial, base, sombras, rubor'),
    ('Fragrance', 'Perfumes y body mists'),
    ('Body Care', 'Cuidado corporal: lociones, exfoliantes'),
    ('Tools', 'Brochas, esponjas y herramientas'),
]


# URLs de audio libres de derechos (SoundHelix) para la demo
SAMPLE_AUDIO = [
    'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3',
    'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3',
    'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3',
    'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3',
    'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3',
]


# Colores de cada marca
RARE = 'E8A2B8'      # rosa empolvado - Rare Beauty
FENTY = 'B83D5C'     # carmín profundo - Fenty Beauty
REM = '6B5B95'       # morado espacial - R.E.M Beauty
PLEASING = '9CAF88'  # verde sage - Pleasing
FLORENCE = 'D4A8C9'  # lila pastel - Florence by Mills


ARTISTS_DATA = [
    {
        'name': 'Selena Gomez',
        'brand_name': 'Rare Beauty',
        'color': RARE,
        'bio': 'Marca de belleza que celebra la individualidad y promueve la salud mental. Fundada en 2020 por Selena Gomez.',
        'image_url': 'https://juicyskinmx.com/cdn/shop/files/IMG-1071.webp?v=1711643257',
        'iconic_song_title': 'Lose You To Love Me',
        'iconic_song_url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/2b/d3/53/2bd3533f-9fd5-f845-5525-fbdca63f8e4e/mzaf_2903374598480765315.plus.aac.p.m4a',
        'lyrics': (
            'You promised the world and I fell for it\n'
            'I put you first and you adored it\n'
            'Set fires to my forest\n'
            'And you let it burn\n'
            '\n'
            'I needed to lose you to find me\n'
            'This dancing was killing me softly\n'
            'I needed to hate you to love me, yeah\n'
            'To love, love, yeah\n'
            '\n'
            'I needed to lose you to love me…'
        ),
        'products': [
            ('Soft Pinch Liquid Blush', 'Makeup', '23.00', 4.8, True,
             'Rubor líquido de larga duración y acabado natural.',
             'https://cdn.shopify.com/s/files/1/0314/1143/7703/files/ECOMM-SP-LIQUID-BLUSH-DEWY-HOPE.jpg?v=1762200490&width=1024'),
            ('Positive Light Tinted Moisturizer', 'Makeup', '30.00', 4.7, True,
             'Hidratante con color y SPF 20.',
             'https://blushbox.store/wp-content/uploads/2024/01/download-2024-01-24T080535.990.png'),
            ('Lip Soufflé Matte Cream Lipstick', 'Makeup', '20.00', 4.6, True,
             'Labial cremoso de acabado mate ultra suave.',
             'https://www.sephora.com.mx/on/demandware.static/-/Sites-masterCatalog_Sephora/es_MX/dw807c8059/images/hi-res/boletos/Karla%20Nieto/RARE%20BEAUTY/840122905315_6.jpg'),
            ('Kind Words Matte Lipstick', 'Makeup', '22.00', 4.5, True,
             'Labial mate con mensajes positivos grabados.',
             'https://www.rarebeauty.com/cdn/shop/products/kind-words-matte-lipstick-talented.jpg?v=1762280633&width=1024'),
            ('Always an Optimist 4-in-1 Mist', 'Skincare', '26.00', 4.7, True,
             'Spray fijador, hidratante y prep en uno.',
             'https://beautyessentials.hn/cdn/shop/products/image_943062be-fd54-4732-8f30-0b7b6952671c.jpg?v=1662144603&width=990'),
            ('Find Comfort Body Cream', 'Body Care', '38.00', 4.6, False,
             'Crema corporal hidratante con aromas relajantes.',
             'https://cdn.shopify.com/s/files/1/0314/1143/7703/files/share-image.jpg?format=pjpg&v=1613733998&width=1202'),
        ],
    },
    {
        'name': 'Rihanna',
        'brand_name': 'Fenty Beauty',
        'color': FENTY,
        'bio': 'Marca inclusiva con 50 tonos de base. Fundada en 2017 por Rihanna, revolucionó la industria al priorizar todos los tonos de piel.',
        'image_url': 'https://cdn.shopify.com/s/files/1/0341/3458/9485/products/2000X2000_300DPI10_1200x1500_1_5790edfd-2654-4d89-ae52-5d726f5b84fb_600x.jpg?v=1713575214',
        'iconic_song_title': 'Diamonds',
        'iconic_song_url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/26/97/fb/2697fb36-8ef2-9d18-0a2e-6545947b4445/mzaf_9032202105098805603.plus.aac.p.m4a',
        'lyrics': (
            'Shine bright like a diamond\n'
            'Shine bright like a diamond\n'
            'Find light in the beautiful sea\n'
            'I choose to be happy\n'
            'You and I, you and I\n'
            'We\'re like diamonds in the sky\n'
            '\n'
            'You\'re a shooting star I see\n'
            'A vision of ecstasy\n'
            'When you hold me, I\'m alive\n'
            'We\'re like diamonds in the sky…'
        ),
        'products': [
            ('Pro Filt\'r Soft Matte Foundation', 'Makeup', '40.00', 4.8, True,
             'Base de larga duración en 50 tonos.',
             ''),
            ('Gloss Bomb Universal Lip Luminizer', 'Makeup', '21.00', 4.9, True,
             'Brillo labial universal súper brillante.',
             ''),
            ('Killawatt Freestyle Highlighter', 'Makeup', '38.00', 4.7, True,
             'Iluminador en dúo con acabado metálico.',
             ''),
            ('Eaze Drop Blurring Skin Tint', 'Makeup', '32.00', 4.6, True,
             'Tinte ligero estilo "tu piel pero mejor".',
             ''),
            ('Fenty Eau de Parfum', 'Fragrance', '140.00', 4.8, True,
             'Perfume con notas de magnolia, almizcle y pachulí.',
             ''),
        ],
    },
    {
        'name': 'Ariana Grande',
        'brand_name': 'R.E.M Beauty',
        'color': REM,
        'bio': 'Marca cosmética inspirada en el espacio y los sueños. Lanzada en 2021 por Ariana Grande con estética futurista.',
        'image_url': 'https://www.revistadeck.com/wp-content/uploads/r.e.m.-beauty-1.jpg',
        'iconic_song_title': '7 rings',
        'iconic_song_url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/d5/c8/f3/d5c8f31b-1c8f-93ed-e78b-8c0bce3e8b66/mzaf_14456154925680073521.plus.aac.p.m4a',
        'lyrics': (
            'I want it, I got it\n'
            'I want it, I got it\n'
            'I want it, I got it\n'
            'I want it, I got it\n'
            '\n'
            'You like my hair? Gee, thanks, just bought it\n'
            'I see it, I like it, I want it, I got it (Yeah)\n'
            'I want it, I got it, I want it, I got it\n'
            'I want it, I got it, I want it, I got it…'
        ),
        'products': [
            ('At The Borderline Lip Liner', 'Makeup', '18.00', 4.6, True,
             'Delineador labial cremoso de larga duración.',
             ''),
            ('On Your Collar Plumping Lip Gloss', 'Makeup', '20.00', 4.7, True,
             'Brillo con efecto volumen.',
             ''),
            ('Midnight Shadows Eyeshadow Palette', 'Makeup', '34.00', 4.5, True,
             'Paleta de 12 sombras tonos noche estrellada.',
             ''),
            ('Practically Permanent Lip Stain', 'Makeup', '22.00', 4.6, True,
             'Tinte labial de larga duración.',
             ''),
            ('Flare The Liner Felt Tip Eyeliner', 'Makeup', '24.00', 4.7, True,
             'Delineador líquido de punta fina.',
             ''),
        ],
    },
    {
        'name': 'Harry Styles',
        'brand_name': 'Pleasing',
        'color': PLEASING,
        'bio': 'Marca de belleza y bienestar lanzada en 2021 por Harry Styles. Productos sin género, formulados de manera limpia.',
        'image_url': 'https://media.glamour.mx/photos/6190546da6e030d6480f5212/1:1/w_972,h_972,c_limit/259141.jpg',
        'iconic_song_title': 'As It Was',
        'iconic_song_url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/67/10/16/67101606-3869-ca44-6c03-e13d6322cb51/mzaf_1135399237022217274.plus.aac.p.m4a',
        'lyrics': (
            'Holdin\' me back\n'
            'Gravity\'s holdin\' me back\n'
            'I want you to hold out the palm of your hand\n'
            'Why don\'t we leave it at that?\n'
            '\n'
            'Nothin\' to say\n'
            'When everything gets in the way\n'
            'Seems you cannot be replaced\n'
            'And I\'m the one who will stay, oh-oh-oh\n'
            '\n'
            'In this world, it\'s just us\n'
            'You know it\'s not the same as it was…'
        ),
        'products': [
            ('The Pearlescent Illuminating Serum', 'Skincare', '38.00', 4.7, True,
             'Serum iluminador con efecto perla.',
             ''),
            ('Pleasing Pen', 'Makeup', '20.00', 4.5, True,
             'Pluma multiusos para ojos y labios.',
             ''),
            ('Shroom Bloom Eye Gel', 'Skincare', '35.00', 4.6, True,
             'Gel de ojos con hongos adaptógenos.',
             ''),
            ('Posie Plumping Lip Oil', 'Makeup', '24.00', 4.8, True,
             'Aceite labial con efecto volumen.',
             ''),
            ('The Glow Lotion', 'Body Care', '32.00', 4.5, True,
             'Loción corporal con brillo dorado.',
             ''),
        ],
    },
    {
        'name': 'Millie Bobby Brown',
        'brand_name': 'Florence by Mills',
        'color': FLORENCE,
        'bio': 'Marca de skincare y makeup para gen Z fundada en 2019 por Millie Bobby Brown. Vegana y cruelty-free.',
        'image_url': 'https://beautymatter.com/storage/4287/conversions/florence-by-mills-future50-2023-large@2x.jpg',
        'iconic_song_title': 'Running Up That Hill',
        'iconic_song_url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview126/v4/e5/ba/20/e5ba201c-8940-86d1-0541-520079b6c916/mzaf_13026886145802029834.plus.aac.p.m4a',
        'lyrics': (
            'It doesn\'t hurt me\n'
            'Do you want to feel how it feels?\n'
            'Do you want to know that it doesn\'t hurt me?\n'
            'Do you want to hear about the deal that I\'m making?\n'
            '\n'
            'And if I only could\n'
            'I\'d make a deal with God\n'
            'And I\'d get him to swap our places\n'
            'Be running up that road\n'
            'Be running up that hill\n'
            'Be running up that building…'
        ),
        'products': [
            ('Get That Grime Face Wash', 'Skincare', '12.00', 4.5, True,
             'Limpiador facial con activos suaves.',
             ''),
            ('Zero Chill Face Cream', 'Skincare', '20.00', 4.6, True,
             'Crema hidratante refrescante.',
             ''),
            ('Eye Candy Cooling Eye Gel', 'Skincare', '18.00', 4.7, True,
             'Gel de ojos con aplicador metálico frío.',
             ''),
            ('Look Alive Eye Balm', 'Skincare', '16.00', 4.5, True,
             'Bálsamo para ojeras y bolsas.',
             ''),
            ('Oh Whale! Lip Duo', 'Makeup', '14.00', 4.6, True,
             'Dúo de balsamo y tinte labial.',
             ''),
        ],
    },
]


class Command(BaseCommand):
    help = 'Carga datos de ejemplo: artistas reales, categorías y productos.'

    def add_arguments(self, parser):
        parser.add_argument('--reset', action='store_true',
                            help='Borra todos los datos antes de cargar.')

    def handle(self, *args, **opts):
        if opts['reset']:
            self.stdout.write('Borrando datos previos…')
            Product.objects.all().delete()
            Artist.objects.all().delete()
            Category.objects.all().delete()

        # Categorías
        cats = {}
        for name, desc in CATEGORIES:
            cat, _ = Category.objects.get_or_create(
                name=name, defaults={'description': desc})
            cats[name] = cat
        self.stdout.write(self.style.SUCCESS(f'✓ {len(cats)} categorías'))

        # Artistas + productos
        total_products = 0
        for a in ARTISTS_DATA:
            artist, created = Artist.objects.update_or_create(
                name=a['name'],
                brand_name=a['brand_name'],
                defaults={
                    'bio': a['bio'],
                    'image_url': a['image_url'],
                    'iconic_song_title': a['iconic_song_title'],
                    'iconic_song_url': a['iconic_song_url'],
                    'iconic_song_lyrics': a.get('lyrics', ''),
                },
            )
            status = 'creado' if created else 'actualizado'
            self.stdout.write(f'  · {artist.brand_name} ({status})')

            color = a.get('color', 'D97A93')
            for p in a['products']:
                name, cat_name, price, rating, is_bs, desc, image_url = p
                # Auto-genera la URL de la imagen con el color de la marca,
                # pero permite imágenes reales cuando se proveen.
                product_image = image_url or img(name, color)
                Product.objects.update_or_create(
                    artist=artist, name=name,
                    defaults={
                        'category': cats.get(cat_name),
                        'description': desc,
                        'price': Decimal(price),
                        'image_url': product_image,
                        'rating': Decimal(str(rating)),
                        'is_bestseller': is_bs,
                        'stock': 25,
                    },
                )
                total_products += 1

        self.stdout.write(self.style.SUCCESS(
            f'✓ {len(ARTISTS_DATA)} artistas, {total_products} productos cargados.'))
