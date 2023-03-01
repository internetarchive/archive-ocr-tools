from iso639 import languages

AUTOUSE_DETECTED_SCRIPTS = ('Fraktur', 'Kannada', 'Telugu', 'Tamil')

# XXX: osd and equ are removed
TESSERACT_LANGUAGE_CODES = {
    'afr', 'amh', 'ara', 'asm', 'aze', 'aze_cyrl', 'bel', 'ben', 'bod', 'bos',
    'bre', 'bul', 'cat', 'ceb', 'ces', 'chi_sim', 'chi_sim_vert', 'chi_tra',
    'chi_tra_vert', 'chr', 'cos', 'cym', 'dan', 'deu', 'div', 'dzo', 'ell',
    'eng', 'enm', 'epo', 'est', 'eus', 'fas', 'fao', 'fil', 'fin', 'fra',
    'frk', 'frm', 'fry', 'gla', 'gle', 'glg', 'grc', 'guj', 'hat', 'heb',
    'hin', 'hrv', 'hun', 'hye', 'iku', 'ind', 'isl', 'ita', 'ita_old', 'jav',
    'jpn', 'kan', 'kat', 'kat_old', 'kaz', 'khm', 'kir', 'kmr', 'kor',
    'kor_vert', 'lao', 'lat', 'lav', 'lit', 'ltz', 'mal', 'mar', 'mkd', 'mlt',
    'mon', 'mri', 'msa', 'mya', 'nep', 'nld', 'nor', 'oci', 'ori', 'pan',
    'pol', 'por', 'pus', 'que', 'ron', 'rus', 'san', 'sin', 'slk', 'slv',
    'snd', 'spa', 'spa_old', 'sqi', 'srp', 'srp_latn', 'sun', 'swa', 'swe',
    'syr', 'tam', 'tat', 'tel', 'tgk', 'tha', 'tir', 'ton', 'tur', 'uig',
    'ukr', 'urd', 'uzb', 'uzb_cyrl', 'vie', 'yid', 'yor',
    }

TESSERACT_SCRIPT_CODES = {
    'Arabic', 'Armenian', 'Bengali', 'Canadian_Aboriginal', 'Cherokee',
    'Cyrillic', 'Devanagari', 'Ethiopic', 'Fraktur', 'Georgian', 'Greek',
    'Gujarati', 'Gurmukhi', 'HanS', 'HanS_vert', 'HanT', 'HanT_vert', 'Hangul',
    'Hangul_vert', 'Hebrew', 'Japanese', 'Japanese_vert', 'Kannada', 'Khmer',
    'Lao', 'Latin', 'Malayalam', 'Myanmar', 'Oriya', 'Sinhala', 'Syriac',
    'Tamil', 'Telugu', 'Thaana', 'Thai', 'Tibetan', 'Vietnamese',
}

TESSERACT_SCRIPT_CODES_L = set([x.lower() for x in TESSERACT_SCRIPT_CODES])

# Mapping of lower-case language names to ISO639-3 codes.
LANGNAME_ALPHA3_MAP = {k.lower(): v.part3.lower() for k,v in languages.name.items()}
for lang in languages.languages:
    if lang.inverted and lang.inverted != lang.name:
        LANGNAME_ALPHA3_MAP[lang.inverted.lower()] = lang.part3.lower()
    if lang.names and isinstance(lang.names, list):
        # lang.names is a list of tuples containing language name variants and
        # their formatted versions, e.g. [('Low Saxon', 'Saxon, Low'), ...].
        for variant in lang.names:
            for v in variant:
                LANGNAME_ALPHA3_MAP[v.lower()] = lang.part3.lower()

# Map of special-case values to Tesseract language codes.
"""
TODO:
    - Tesseract makes the distinction between ancient Greek ('grc') and
      modern Greek ('ell'). IA uses 'grc' for some Greek texts, and 'gre' for
      others.
    - Tesseract makes the distinction between Traditional Chinese (chi_tra) and
      Simplified Chinese (chi_sim). IA uses 'chi'.
"""
SPECIAL_CASE_MAP = {
    'chi': 'chi_sim',   # Chinese (simplified)
    'zho': 'chi_sim',   # Chinese (simplified)
    'chinese (simplified)': 'chi_sim',  # Chinese (simplified); from Google language-detect
    'chinese (traditional)': 'chi_tra', # Chinese (traditional); from Google language-detect
    'chinese (china)': 'chi_sim',       # Chinese (simplified); from Library Genesis
    'chinese (prc)': 'chi_sim',         # Chinese (simplified); from Library Genesis
    'chinese (taiwan)': 'chi_tra',      # Chinese (traditional); from Library Genesis
    'fre': 'fra',       # French
    'tib': 'bod',       # Tibetan
    'dut': 'nld',       # Dutch
    'dum': 'nld',       # Dutch
    'gre': 'ell',       # Greek
    'greek': 'ell',     # Greek
    'baq': 'eus',       # Basque
    'nob': 'nor',       # Norwegian (Bokmal)
    'nno': 'nor',       # Norwegian (Nynorsk)
    'cze': 'ces',       # Czech
    'rum': 'ron',       # Romanian; Moldavian; Moldovan
    'mol': 'ron',       # Romanian; Moldavian; Moldovan
    'moldavian': 'ron', # Romanian; Moldavian; Moldovan
    'sco': 'eng',       # Scots; use English
    'wel': 'cym',       # Welsh
    'slo': 'slk',       # Slovak
    'sla': 'slk',       # Slovak
    'per': 'fas',       # Persian
    'gsw': 'deu',       # Swiss German; use German
    'ger': 'deu',       # German
    'kur': 'kmr',       # Tesseract language code for kur is 'kmr' (at least the
                        # Latin version, Arabic is missing atm)
    'tag': 'fil',       # Tagalog; use Filipino
    'tgl': 'fil',       # Tagalog; use Filipino
    'alb': 'sqi',       # Albanian
    'cor': 'bre',       # Cornish; Breton is closest option
    'chu': 'bul',       # Church Slavic; Bulgarian is closest option
    'scr': 'hrv',       # Croatian
    'lim': 'nld',       # Limburgish; Dutch is closest option
    'cpe': 'eng',       # Creoles and Pidgins, English-based; English is closest option
    'esp': 'epo',       # Esperanto
    'far': 'fao',       # Faroese
    'cpf': 'fra',       # Creoles and Pidgins, French-based; French is closest option
    'français': 'fra',  # French
    'fri': 'fry',       # West Frisian
    'frr': 'fry',       # North Frisian; West Frisian is closest option
    'gae': 'gla',       # Scottish Gaelic
    'glv': 'gla',       # Manx; Scottish Gaelic is closest option
    'max': 'gla',       # Manx; Scottish Gaelic is closest option
    'gag': 'glg',       # Galician
    'gem': 'deu',       # Collective code for Germanic (Other); German is closest option
    'gmh': 'deu',       # Middle High German; German is closest option
    'nds': 'deu',       # Low German; German is closest option
    'ελληνικά': 'ell',  # Greek
    'ice': 'isl',       # Icelandic
    'non': 'isl',       # Old Norse; Icelandic is closest option
    'mga': 'gle',       # Middle Irish; Irish is closest option
    'sga': 'gle',       # Old Irish; Irish is closest option
    'iri': 'gle',       # Irish
    'nap': 'ita',       # Neapolitan; Italian is closest option
    'mac': 'mkd',       # Macedonian
    'may': 'msa',       # Malay
    'mao': 'mri',       # Maori
    'ang': 'enm',       # Old English; Middle English is closest option
    'old english': 'enm',        # Middle English (closest)
    'middle english': 'enm',     # Middle English
    'fro': 'fra',       # Old French; French is closest option
    'goh': 'deu',       # Old High German; German is closest option
    'cpp': 'por',       # Creoles and Pidgins, Portuguese-based; Portuguese is closest option
    'brazilian portuguese': 'por', # Brazilian Portuguese; Portuguese is closest option
    'русский': 'rus',       # Russian
    'russian old': 'rus',   # Old Russian, Russian is closest option
    'russian (old)': 'rus', # Old Russian, Russian is closest option
    'scc': 'srp',       # Serbian
    'español': 'spa',   # Spanish
    'arg': 'spa',       # Aragonese; Spanish is closest option
    'pam': 'fil',       # Pampanga; Filipino is closest option
    'pag': 'fil',       # Pangasinan; Filipino is closest option
    'taj': 'tgk',       # Tajik
    'tar': 'tat',       # Tatar
    'عربى': 'ara',      # Arabic
    'العربية': 'ara',   # Arabic
    'bur': 'mya',       # Burmese
    'eth': 'Ethiopic',      # Ethiopic (script)
    'ethiopic': 'Ethiopic', # Ethiopic (script)
    'gez': 'Ethiopic',      # Ethiopic (script)
    'geo': 'kat',       # Georgian
    'ira': 'fas',       # Persian
    'syc': 'syr',       # Classical Syriac; use Syriac
    'en_us': 'eng',     # Some partners use en_US for English
    'arm': 'hye',       # Alternative for hye (Armenian)
}

# Map of Tesseract language codes to Tesseract script values.

LANGCODE_SCRIPT_MAP = {
    'afr': 'Latin',                 # Afrikaans: Latin
    'amh': 'Ethiopic',              # Ahmaric: Ethiopic (Ge'ez)
    'ara': 'Arabic',                # Arabic: Arabic
    'asm': 'Bengali',               # Assamese: Bengali TODO: Latin?
    'aze': ('Latin', 'Cyrillic'),   # Azerbaijani: Latin, Cyrillic TODO: Should this be latin only?
    'aze_cyrl': 'Cyrillic',         # Azerbaijani (Cyrillic): Cyrillic
    'bel': 'Cyrillic',              # Belarusian: Cyrillic TODO: Latin?
    'ben': 'Bengali',               # Bengali: Bengali
    'bod': 'Tibetan',               # Tibetan: Tibetan
    'bos': ('Latin', 'Cyrillic'),   # Bosnian: Latin, Cyrillic
    'bre': 'Latin',                 # Breton: Latin
    'bul': ('Latin', 'Cyrillic'),   # Bulgarian: Latin, Cyrillic
    'cat': 'Latin',                 # Catalan: Latin
    'ceb': 'Latin',                 # Cebuano: Latin
    'ces': 'Latin',                 # Czech: Latin
    'chi_sim': 'HanS',              # Chinese (simplified): HanS
    'chi_sim_vert': 'HanS_vert',    # Chinese (simplified, vertical): HanS_vert
    'chi_tra': 'HanT',              # Chinese (traditional): HanT
    'chi_tra_vert': 'HanT_vert',    # Chinese (traditional, vertical): HanT_vert
    'chr': ('Cherokee', 'Latin'),   # Cherokee: Cherokee, Latin
    'cos': 'Latin',                 # Corsican: Latin
    'cym': 'Latin',                 # Welsh: Latin
    'dan': ('Latin', 'Fraktur'),    # Danish: Latin + Fraktur
    'deu': ('Latin', 'Fraktur'),    # German: Latin + Fraktur
    'div': 'Thaana',                # Dhivehi/Maldivian: Thaana
    'dzo': 'Tibetan',               # Dzongkha: Tibetan
    'ell': 'Greek',                 # Greek (modern): Greek
    'eng': ('Latin', 'Fraktur'),    # English: Latin + Fraktur
    'enm': ('Latin', 'Fraktur'),    # Middle English: Latin
    'epo': 'Latin',                 # Esperanto: Latin
    #'equ': None,                    # Math equation: TODO how to handle this case?
    'est': ('Latin', 'Fraktur'),    # Estonian: Latin + Fraktur
    'eus': 'Latin',                 # Basque: Latin
    'fas': 'Arabic',                # Persian: Arabic TODO is this correct?
    'fao': 'Latin',                 # Faroese: Latin
    'fil': 'Latin',                 # Tagalog: Latin
    'fin': ('Latin', 'Fraktur'),    # Finnish: Latin
    'fra': 'Latin',                 # French: Latin
    'frk': 'Latin',                 # Frankish: Latin
    'frm': 'Latin',                 # Middle French: Latin
    'fry': 'Latin',                 # Western Frisian
    'gla': 'Latin',                 # Scottish Gaelic: Latin
    'gle': 'Latin',                 # Irish: Latin
    'glg': 'Latin',                 # Galician: Latin
    'grc': 'Greek',                 # Greek (ancient): Greek
    'guj': 'Gujarati',              # Gujarati: Gujarati TODO also Devanagari?
    'hat': 'Latin',                 # Haitian: Latin
    'heb': 'Hebrew',                # Hebrew: Hebrew
    'hin': 'Devanagari',            # Hindi: Devanagari
    'hrv': 'Latin',                 # Croatian: Latin
    'hun': 'Latin',                 # Hungarian: Latin
    'hye': 'Armenian',              # Armenian: Armenian
    'iku': 'Canadian_Aboriginal',   # Inuktitut: Canadian_Aboriginal TODO: correct?
    'ind': 'Latin',                 # Indonesian: Latin
    'isl': 'Latin',                 # Icelandic: Latin
    'ita': 'Latin',                 # Italian: Latin
    'ita_old': 'Latin',             # Old Italian: Latin
    'jav': 'Latin',                 # Javanese: Latin TODO: also Arabic?
    'jpn': 'Japanese',              # Japanese: Japanese TODO also Japanese_vert?
    'kan': 'Kannada',               # Kannada: Kannada
    'kat': 'Georgian',              # Georgian: Georgian
    'kat_old': 'Georgian',          # Georgian (old): Georgian
    'kaz': ('Latin', 'Cyrillic', 'Arabic'), # Kazakh: Latin, Cyrillic, Arabic
    'khm': 'Khmer',                 # Khmer: Khmer
    'kir': ('Latin', 'Cyrillic', 'Arabic'), # Kyrgyz: Latin, Cyrillic, Arabic
    'kmr': ('Latin'),               # Kurdish Kurmanji: Latin
    'kor': 'Hangul',                # Korean: Hangul
    'kor_vert': 'Hangul_vert',      # Korean (vertical): Hangul_vert
    'lao': 'Lao',                   # Lao: Lao
    'lat': 'Latin',                 # Latin: Latin
    'lav': ('Latin', 'Fraktur'),    # Latvian: Latin + Fraktur
    'lit': 'Latin',                 # Lithuanian: Latin
    'ltz': 'Latin',                 # Luxembourgish: Latin
    'mal': 'Malayalam',             # Malayalam: Malayalam
    'mar': 'Devanagari',            # Marathi: Devanagari
    'mkd': 'Cyrillic',              # Macdeonian: Cyrillic
    'mlt': 'Latin',                 # Maltese: Latin
    'mon': 'Cyrillic',              # Mongolian: Cyrillic
    'mri': 'Latin',                 # Maori: Latin
    'msa': 'Latin',                 # Malay: Latin
    'mya': 'Myanmar',               # Burmese: Myanmar
    'nep': 'Devanagari',            # Nepali: Devanagari
    'nld': 'Latin',                 # Dutch: Latin
    'nor': ('Latin', 'Fraktur'),    # Norwegian: Latin + Fraktur
    'oci': 'Latin',                 # Occitan: Latin
    'ori': 'Oriya',                 # Oriya: Oriya
    #'osd': None,                    # Orientation and Script Detection
    'pan': 'Gurmukhi',              # Panjabi: Gurmukhi
    'pol': 'Latin',                 # Polish: Latin
    'por': 'Latin',                 # Portuguese: Latin
    'pus': 'Arabic',                # Pushto: Arabic
    'que': 'Latin',                 # Quechua: Latin
    'ron': 'Latin',                 # Romanian, Moldovan: Latin
    'rus': 'Cyrillic',              # Russian: Cyrillic
    'san': ('Devanagari',
            'Kannada',
            'Telugu',
            'Tamil',),              # Sanskrit: Devanagari, Kannada, Telugu, Tamil
    'sin': 'Sinhala',               # Sinhala: Sinhala
    'slk': 'Latin',                 # Slovak: Latin
    'slv': 'Latin',                 # Slovene: Latin
    'snd': ('Arabic', 'Devanagari'),# Sindhi: Arabic, Devanagari TODO correct?
    'spa': 'Latin',                 # Spanish: Latin
    'spa_old': 'Latin',             # Spanish (old): Latin
    'sqi': 'Latin',                 # Albanian: Latin
    'srp': ('Cyrillic', 'Latin'),   # Serbian: Cyrillic, Latin
    'srp_latn': ('Latin'),          # Serbian: Latin only
    'sun': 'Latin',                 # Sundanese: Latin
    'swa': 'Latin',                 # Swahili: Latin
    'swe': ('Latin', 'Fraktur'),    # Swedish: Latin + Fraktur
    'syr': 'Syriac',                # Syriac: Syriac
    'tam': 'Tamil',                 # Tamil: Tamil
    'tat': ('Latin', 'Cyrillic', 'Arabic'), # Tatar: Latin, Cyrillic, Arabic
    'tel': 'Telugu',                # Telugu: Telugu
    'tgk': ('Latin', 'Cyrillic', 'Arabic'), # Tajik: Latin, Cyrillic, Arabic
    'tha': 'Thai',                  # Thai: Thai
    'tir': 'Ethiopic',              # Tigrinya: Ethiopic (Ge'ez)
    'ton': 'Latin',                 # Tonga: Latin
    'tur': 'Latin',                 # Turkish: Latin
    'uig': ('Latin', 'Cyrillic', 'Arabic'), # Uighur: Latin, Cyrillic, Arabic
    'ukr': 'Cyrillic',              # Ukranian: Cyrillic
    'urd': 'Arabic',                # Urdu: Arabic
    'uzb': 'Latin',                 # Uzbek: Latin
    'uzb_cyrl': 'Cyrillic',         # Uzbek (Cyrillic): Cyrillic
    'vie': 'Vietnamese',            # Vietnamese: Vietnamese
    'yid': 'Hebrew',                # Yiddish: Hebrew
    'yor': 'Latin'                  # Yoruba: Latin
    }


# Undefined, No linguistic content, Multiple and no language specified enables
# autonomous mode.
AUTONOMOUS_LANGUAGE_CODES = {'und', 'zxx', 'mul', None}

# Languages codes that we want to skip
SKIP_LANGUAGES = {'None'}

def ia_language_to_tesseract_codes(languages, get_scripts=False,
                                   detected_scripts=None,
                                   filter_scripts=False):
    if languages is None:
        return None
    if not isinstance(languages, list):
        languages = [languages]
    tess_codes = [get_tesseract_language_code(lang) for lang in languages]
    tess_codes = set(c for c in tess_codes if c is not None)
    tess_codes = list(tess_codes)
    if get_scripts:
        scripts = set()
        for lang in tess_codes:
            s = LANGCODE_SCRIPT_MAP.get(lang)
            if s is None:
                continue
            if filter_scripts and detected_scripts is not None:
                if isinstance(s, str):
                    if s not in detected_scripts:
                        # Skip language if the script does not match
                        print('Not including language %s with scripts %s '
                              'because it does not match any of the '
                              'detected scripts (%s)' % (lang, s, detected_scripts))
                        continue
                else:
                    found = False

                    for l in s:
                        if l in detected_scripts:
                            found = True
                            break
                    if not found:
                        print('Not including language %s with scripts %s '
                              'because it does not match any of the '
                              'detected scripts (%s)' % (lang, s, detected_scripts))
                        continue

            if isinstance(s, str):
                if detected_scripts is not None and s in detected_scripts:
                    scripts.add(s)
            else:
                for l in s:
                    if detected_scripts is not None and l in detected_scripts:
                        scripts.add(l)
        for s in scripts:
            tess_codes.append(s)

    return tess_codes or None


# XXX: Only call this if no language mappings were found to start with
def ia_language_requires_autonomous(languages):
    if not isinstance(languages, list):
        languages = [languages]
    for lang in languages:
        if lang in AUTONOMOUS_LANGUAGE_CODES:
            return True

    return False


def ia_language_requires_skip_ocr(languages):
    if not isinstance(languages, list):
        languages = [languages]
    for lang in languages:
        if lang and lang.endswith('-handwritten'):
            return True

        if lang in SKIP_LANGUAGES:
            return True

    return False


def language_to_alpha3lang(lang):
    lang = lang.lower()

    alpha3lang = None

    if len(lang) == 2:
        iso639lang = None

        # Convert alpha2 to alpha3
        try:
            iso639lang = languages.get(alpha2=lang)
        except KeyError:
            pass

        if iso639lang is not None:
            alpha3lang = iso639lang.part3
    elif len(lang) == 3:
        # Handle cases where IA uses a non-standard 3-letter code (e.g. 'chi')
        alpha3lang = lang
        # return SPECIAL_CASE_MAP.get(lang)
    else:
        # Attempt to map full language names to their ISO639-3 representation
        alpha3lang = LANGNAME_ALPHA3_MAP.get(lang, None)

    return alpha3lang


def get_tesseract_language_code(lang):
    lang = lang.lower()

    if lang in TESSERACT_SCRIPT_CODES_L:
        return lang.capitalize()

    if lang in TESSERACT_LANGUAGE_CODES:
        # Check the raw language value against tesseract codes
        return lang

    alpha3lang = language_to_alpha3lang(lang)

    if alpha3lang is None:
        # If no alpha3 was found for a language value, check if the raw language
        # value is special cased
        return SPECIAL_CASE_MAP.get(lang)

    if alpha3lang in TESSERACT_LANGUAGE_CODES:
        return alpha3lang

    # Check for special case values for the alpha3 value
    return SPECIAL_CASE_MAP.get(alpha3lang)

# If one language is not supported, report as unsupported
def language_invalid_iso639(languages):
    iso639_langs = [language_to_alpha3lang(lang) for lang in languages]

    for lang in iso639_langs:
        if lang is None:
            return True

    return False

# If one language is not supported, report as unsupported
def tesseract_unsupported_iso639(languages):
    iso639_langs = [language_to_alpha3lang(lang) for lang in languages]

    for lang in iso639_langs:
        if not get_tesseract_language_code(lang):
            return True

    return False

def special_case_tesseract_scripts(scripts):
    res = []
    for (script, conf) in scripts:
        if script == 'Han':
            res.append(('HanS', conf / 2.))
            res.append(('HanT', conf / 2.))
        elif script == 'Korean':
            res.append(('Hangul', conf))
        elif script == 'Katakana':
            res.append(('Japanese', conf))
        elif script == 'Hirigana':
            res.append(('Japanese', conf))
        else:
            res.append((script, conf))

    return res
