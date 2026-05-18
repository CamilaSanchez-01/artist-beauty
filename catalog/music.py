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
        'url': 'https://aod-ssl.itunes.apple.com/itunes-assets/Music211/v4/4e/c4/cb/4ec4cba8-0447-e07d-7b4a-fec980606dea/mzaf_A1476727864.rmhq.aac.wa.mp4',
    },

    'lady-gaga-haus-labs-lip-oil': {
        'title': 'Poker Face — Lady Gaga',
        'url': 'https://aod-ssl.itunes.apple.com/itunes-assets/Music211/v4/30/84/c7/3084c70f-61b6-d7d6-e3e2-b1289324a4b7/mzaf_A1476727861.rmhq.aac.wa.mp4',
    },

    # =========================
    # HALSEY
    # =========================

    'halsey-about-face-foundation': {
        'title': 'Without Me — Halsey',
        'url': 'https://aod-ssl.itunes.apple.com/itunes-assets/Music211/v4/12/76/cc/1276ccc6-00e0-0dc3-a819-4d9690c47253/mzaf_A1170699703.rmhq.aac.wa.mp4',
    },

    'halsey-about-face-lip-color': {
        'title': 'Colors — Halsey',
        'url': 'https://aod-ssl.itunes.apple.com/itunes-assets/Music211/v4/12/76/cc/1276ccc6-00e0-0dc3-a819-4d9690c47253/mzaf_A1170699703.rmhq.aac.wa.mp4',
    },

    # =========================
    # GWEN STEFANI
    # =========================

    'gwen-stefani-gxve-lipstick': {
        'title': 'Hollaback Girl — Gwen Stefani',
        'url': 'https://aod-ssl.itunes.apple.com/itunes-assets/Music221/v4/2e/3f/a0/2e3fa0ac-350e-8ff8-d2ac-d2cab1d0178b/mzaf_A1452870036.rmhq.aac.wa.mp4',
    },

    'gwen-stefani-gxve-eyeliner': {
        'title': 'The Sweet Escape — Gwen Stefani',
        'url': 'https://aod-ssl.itunes.apple.com/itunes-assets/Music221/v4/67/07/52/67075233-8ad5-752f-168c-98a09bddc92e/mzaf_A1452870050.rmhq.aac.wa.mp4',
    },

    # =========================
    # JENNIFER LOPEZ
    # =========================

    'jlo-beauty-that-hit-single-gel-cream': {
        'title': 'On The Floor — Jennifer Lopez',
        'url': 'https://aod-ssl.itunes.apple.com/itunes-assets/Music211/v4/fe/dd/84/fedd84fe-7053-4c9e-0a29-3705735066dc/mzaf_A1440622264.rmhq.aac.wa.mp4',
    },

    'jlo-beauty-glow-serum': {
        'title': 'Jenny From The Block — Jennifer Lopez',
        'url': 'https://aod-ssl.itunes.apple.com/itunes-assets/Music221/v4/f8/b1/ca/f8b1ca91-e4c5-b9f0-9c4a-acd3654d776f/mzaf_A265144078.rmhq.aac.wa.mp4',
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

