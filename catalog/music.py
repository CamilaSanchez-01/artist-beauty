import zlib

PRODUCT_AUDIO_MAP = {
    'rare-beauty-soft-pinch-liquid-blush': {
        'title': 'Lose You To Love Me — Selena Gomez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/2b/d3/53/2bd3533f-9fd5-f845-5525-fbdca63f8e4e/mzaf_2903374598480765315.plus.aac.p.m4a',
    },
    'rare-beauty-positive-light-tinted-moisturizer': {
        'title': 'Back To You — Selena Gomez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/58/36/67/58366770-6541-57a3-fa58-8f7ad0b1cb8e/mzaf_11238694758091585166.plus.aac.p.m4a',
    },
    'rare-beauty-lip-souffle-matte-cream-lipstick': {
        'title': 'Hands To Myself — Selena Gomez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/5e/ab/68/5eab6888-aec7-a73f-2cdf-d2dd6b62c2b9/mzaf_10827919152868106610.plus.aac.p.m4a',
    },
    'rare-beauty-kind-words-matte-lipstick': {
        'title': 'Who Says — Selena Gomez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/cf/86/08/cf860812-6b7e-4e0c-a6b3-fa8feef8ea4e/mzaf_11448972915342822579.plus.aac.p.m4a',
    },
    'rare-beauty-always-an-optimist-4-in-1-mist': {
        'title': 'Look At Her Now — Selena Gomez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/e6/8f/9e/e68f9e3a-1797-d00f-cc01-a3c534b24756/mzaf_1814467481890963067.plus.aac.p.m4a',
    },
    'rare-beauty-find-comfort-body-cream': {
        'title': 'Good For You — Selena Gomez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/b1/ee/49/b1ee499c-ee5e-10a3-dc21-0ff3a8f30c14/mzaf_18076546371493502114.plus.aac.p.m4a',
    },
    'fenty-beauty-pro-filtr-soft-matte-foundation': {
        'title': 'Diamonds — Rihanna',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/26/97/fb/2697fb36-8ef2-9d18-0a2e-6545947b4445/mzaf_9032202105098805603.plus.aac.p.m4a',
    },
    'fenty-beauty-gloss-bomb-universal-lip-luminizer': {
        'title': 'Work — Rihanna',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/f7/8d/12/f78d1232-043f-3573-22a9-d65edd474f93/mzaf_8658533347319025740.plus.aac.p.m4a',
    },
    'fenty-beauty-killawatt-freestyle-highlighter': {
        'title': 'Umbrella — Rihanna',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/7b/45/22/7b452241-882c-409b-3a9b-23306b14286a/mzaf_8588243939716013218.plus.aac.p.m4a',
    },
    'fenty-beauty-eaze-drop-blurring-skin-tint': {
        'title': 'We Found Love — Rihanna',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/81/4e/9f/814e9f54-e7f8-3ab1-d92e-c7869efbd376/mzaf_9149255715038044431.plus.aac.p.m4a',
    },
    'fenty-beauty-fenty-eau-de-parfum': {
        'title': 'Only Girl (In The World) — Rihanna',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/58/bd/6f/58bd6f05-45d7-76d7-bae3-6d453e00b5cc/mzaf_1937910784700207272.plus.aac.p.m4a',
    },
    'rem-beauty-at-the-borderline-lip-liner': {
        'title': '7 rings — Ariana Grande',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/d5/c8/f3/d5c8f31b-1c8f-93ed-e78b-8c0bce3e8b66/mzaf_14456154925680073521.plus.aac.p.m4a',
    },
    'rem-beauty-on-your-collar-plumping-lip-gloss': {
        'title': 'thank u, next — Ariana Grande',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/89/96/16/8996169e-2309-a298-f6f0-e7c52fe8e176/mzaf_590631660224715451.plus.aac.p.m4a',
    },
    'rem-beauty-midnight-shadows-eyeshadow-palette': {
        'title': 'positions — Ariana Grande',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/46/cd/b2/46cdb240-11e4-4aed-31bd-6fb953752580/mzaf_15823372495978399916.plus.aac.p.m4a',
    },
    'rem-beauty-practically-permanent-lip-stain': {
        'title': 'No Tears Left To Cry — Ariana Grande',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/8b/a8/85/8ba88586-341e-0bb9-6e49-1f67f7edcd4d/mzaf_16866815274086216089.plus.aac.p.m4a',
    },
    'rem-beauty-flare-the-liner-felt-tip-eyeliner': {
        'title': 'Dangerous Woman — Ariana Grande',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/37/c9/91/37c99147-526e-138d-af0c-8ebb4d1c540b/mzaf_2834228674136291006.plus.aac.p.m4a',
    },
    'pleasing-the-pearlescent-illuminating-serum': {
        'title': 'As It Was — Harry Styles',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/67/10/16/67101606-3869-ca44-6c03-e13d6322cb51/mzaf_1135399237022217274.plus.aac.p.m4a',
    },
    'pleasing-pleasing-pen': {
        'title': 'Watermelon Sugar — Harry Styles',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview116/v4/16/86/f5/1686f50d-8b77-7e32-85f7-5f0e804d68fe/mzaf_14195633304344507287.plus.aac.p.m4a',
    },
    'pleasing-shroom-bloom-eye-gel': {
        'title': 'Adore You — Harry Styles',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview126/v4/1b/59/1f/1b591fec-7157-f069-02fd-46a77c8638af/mzaf_2481090751237982049.plus.aac.p.m4a',
    },
    'pleasing-posie-plumping-lip-oil': {
        'title': 'Golden — Harry Styles',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/50/8f/f7/508ff714-12ac-6b8b-9e48-871ec5da8ed1/mzaf_782156429997343495.plus.aac.p.m4a',
    },
    'pleasing-the-glow-lotion': {
        'title': 'Sign of the Times — Harry Styles',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/19/f7/99/19f799a3-4638-f354-8713-f5ac076f328e/mzaf_2398941441794619302.plus.aac.p.m4a',
    },
    'florence-by-mills-get-that-grime-face-wash': {
        'title': 'Running Up That Hill — Kate Bush',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview126/v4/e5/ba/20/e5ba201c-8940-86d1-0541-520079b6c916/mzaf_13026886145802029834.plus.aac.p.m4a',
    },
    'florence-by-mills-zero-chill-face-cream': {
        'title': 'Stranger Things — Michael Stein',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/98/00/7a/98007a61-5912-d8e6-2d05-0a8378611124/mzaf_5025701178983290939.plus.aac.p.m4a',
    },
    'florence-by-mills-eye-candy-cooling-eye-gel': {
        'title': 'Jealousy — Labrinth',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/a5/ed/74/a5ed7400-0651-6593-a1f3-2976ac6e3749/mzaf_460901585079471463.plus.aac.p.m4a',
    },
    'florence-by-mills-look-alive-eye-balm': {
        'title': 'Should I Stay or Should I Go — The Clash',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/2a/81/23/2a8123dd-9b78-cd6e-c802-a8ccc2d7fbad/mzaf_17446670162302022873.plus.aac.p.m4a',
    },
    'florence-by-mills-oh-whale-lip-duo': {
        'title': 'Atmosphere — Joy Division',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/8b/14/b0/8b14b02e-690f-4b7f-79b8-c35c69cacdb5/mzaf_10831524843963161836.plus.aac.p.m4a',
    },
     # =========================
    # LADY GAGA
    # =========================
    
    'lady-gaga-haus-labs-foundation': {
        'title': 'Bad Romance — Lady Gaga',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/1b/54/f0/1b54f0b7-db6a-1a40-6af8-4ae4650d8d6d/mzaf_2782647211171496826.plus.aac.p.m4a',
    },
    
    'lady-gaga-haus-labs-lip-oil': {
        'title': 'Poker Face — Lady Gaga',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/7b/d4/b9/7bd4b972-99ea-4ce7-9042-615a894173a4/mzaf_17216069970734143078.plus.aac.p.m4a',
    },
    
    'lady-gaga-haus-labs-blush': {
        'title': 'Rain On Me — Lady Gaga',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/47/3b/65/473b6523-131c-4c73-f774-158c1abbc3eb/mzaf_16291488932735455549.plus.aac.p.m4a',
    },
    
    'lady-gaga-haus-labs-eyeliner': {
        'title': 'Born This Way — Lady Gaga',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/9c/7a/54/9c7a54a6-f2a7-8d8e-1d13-4fe110fddf38/mzaf_3987088489827294384.plus.aac.p.m4a',
    },
    
    'lady-gaga-haus-labs-highlighter': {
        'title': 'Applause — Lady Gaga',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/5e/d7/a2/5ed7a263-1691-2010-da59-1f4ec093b90a/mzaf_6117100412983656708.plus.aac.p.m4a',
    },
    
    'lady-gaga-haus-labs-mascara': {
        'title': 'Shallow — Lady Gaga',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/77/41/4c/77414c83-2297-fb9f-7d38-47a03ab56d8f/mzaf_17756500385136857934.plus.aac.p.m4a',
    },
    # =========================
    # HALSEY
    # =========================
    
    'halsey-about-face-foundation': {
        'title': 'Without Me — Halsey',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/a1/96/ee/a196ee27-727a-7911-6207-8d2904aac4c1/mzaf_5972923977565050863.plus.aac.p.m4a',
    },
    
    'halsey-about-face-lip-color': {
        'title': 'Colors — Halsey',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/bd/f9/b9/bdf9b9b2-eaa4-4461-6079-aaacc6df7316/mzaf_17327312786932455493.plus.aac.p.m4a',
    },
    
    'halsey-about-face-eye-paint': {
        'title': 'Nightmare — Halsey',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/3e/d8/06/3ed8065d-1a50-625b-b995-3e653b32701f/mzaf_6014038911874968955.plus.aac.p.m4a',
    },
    
    'halsey-about-face-cheek-freak': {
        'title': 'Graveyard — Halsey',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/47/f7/a3/47f7a342-7a2e-9005-9605-cb6275d8bcc0/mzaf_8698601067572093492.plus.aac.p.m4a',
    },
    
    'halsey-about-face-matte-fix': {
        'title': 'Bad At Love — Halsey',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/5b/58/a4/5b58a42c-8bd2-343b-902f-0ff2eef75782/mzaf_4415174550656631789.plus.aac.p.m4a',
    },
    
    'halsey-about-face-fractal-glitter': {
        'title': 'You should be sad — Halsey',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/38/eb/a2/38eba210-a804-0534-20f4-a3435093f0b4/mzaf_13239253188955232407.plus.aac.p.m4a',
    },
    # =========================
    # JENNIFER LOPEZ
    # =========================
    
    'jlo-beauty-that-hit-single-gel-cream': {
        'title': 'On The Floor — Jennifer Lopez',
        'url': 'https://audio-ssl.itunes.apple.com/apple-assets-us-std-000001/Music/76/f5/46/mzm.fgyrzuwc.aac.p.m4a',
    },
    
    'jlo-beauty-glow-serum': {
        'title': 'Jenny From The Block — Jennifer Lopez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/b2/a3/42/b2a342b3-47a3-7d5c-c6b0-2b288f1cf091/mzaf_17014161434593598911.plus.aac.p.m4a',
    },
    
    'jlo-beauty-firming-body-butter': {
        'title': 'Love Don’t Cost a Thing — Jennifer Lopez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/54/00/1b/54001bea-2f7a-65db-b5b0-62a56ca69447/mzaf_16533168308152363902.plus.aac.p.m4a',
    },
    
    'jlo-beauty-bronzing-glow': {
        'title': 'Waiting for Tonight — Jennifer Lopez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/73/f1/59/73f1599f-b20e-4bda-9d24-167a55edb9b1/mzaf_16279959302221601258.plus.aac.p.m4a',
    },
    
    'jlo-beauty-radiance-mask': {
        'title': 'Dance Again — Jennifer Lopez',
        'url': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/d1/26/7f/d1267f37-ae4b-8176-7066-67787afd4195/mzaf_16242458862458331824.plus.aac.p.m4a',
    },
}

SAMPLE_PRODUCT_AUDIOS = [
    {
        'title': 'Ritmo Soothing',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3',
    },
    {
        'title': 'Dream Pop',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3',
    },
    {
        'title': 'Soft Vibes',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3',
    },
    {
        'title': 'Glow Beat',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3',
    },
    {
        'title': 'Late Night Groove',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3',
    },
]


def get_product_audio(product):
    """Devuelve una pista consistente por producto."""
    slug = getattr(product, 'slug', '')
    if slug and slug in PRODUCT_AUDIO_MAP:
        song = PRODUCT_AUDIO_MAP[slug]
        return song['url'], song['title']

    idx = zlib.crc32(product.slug.encode('utf-8')) % len(SAMPLE_PRODUCT_AUDIOS)
    song = SAMPLE_PRODUCT_AUDIOS[idx]
    return song['url'], f"{song['title']} · {product.artist.name}"

