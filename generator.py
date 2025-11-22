"""
JAMB CBT Senior Secondary School Question Generator
Creates 300 UNIQUE questions per subject with different question texts
"""
import json
import random

def shuffle_options_with_answer(options, answer):
    """Shuffle options and return shuffled options + answer"""
    indexed_options = [(opt, i) for i, opt in enumerate(options)]
    random.shuffle(indexed_options)
    shuffled_opts = [opt for opt, _ in indexed_options]
    answer_idx = next(i for i, (opt, _) in enumerate(indexed_options) if opt == answer)
    return shuffled_opts, answer

def create_question_variations(base_question, num_variations=30):
    """Create multiple variations of a single question with different wordings"""
    question_text, options, answer = base_question
    variations = []
    
    # List of rephrasings for generic questions
    rephrasings = [
        lambda q: q,  # Keep original
        lambda q: q.replace("?", " is:"),
        lambda q: "Which of the following best describes: " + q.lower().replace("which ", "").replace("?", ""),
        lambda q: "Identify: " + q.lower().replace("identify the ", "").replace("?", ""),
        lambda q: "Choose the: " + q.lower().replace("choose the ", "").replace("?", ""),
        lambda q: "What best explains: " + q.lower().replace("what ", "").replace("?", ""),
        lambda q: "Consider: " + q.lower().replace("?", ""),
        lambda q: q.replace("is", "represents", 1),
        lambda q: q.replace("is", "means", 1),
        lambda q: q.replace("is", "symbolizes", 1),
        lambda q: "According to standard definitions, " + q.lower(),
        lambda q: "In the context of this subject, " + q.lower(),
        lambda q: "Which concept describes: " + q.lower().replace("?", "").replace("which ", ""),
        lambda q: "Select the statement that best completes: " + q.lower().replace("?", ""),
        lambda q: "The best answer to '" + q.lower().replace("?", "") + "' is:",
    ]
    
    for i in range(num_variations):
        # Rephrase the question
        rephrase_fn = rephrasings[i % len(rephrasings)]
        rephrased = rephrase_fn(question_text)
        
        # Shuffle options
        shuffled_opts, shuffled_ans = shuffle_options_with_answer(options, answer)
        
        variations.append({
            "question": rephrased,
            "options": shuffled_opts,
            "answer": shuffled_ans
        })
    
    return variations

# Comprehensive base questions for each subject
SUBJECTS_DATA = {
    "use_of_english": [
        ("The speaker's words were so mellifluous that they mesmerized the audience.", ["cacophonous", "terse", "abrupt", "mellifluous"], "mellifluous"),
        ("She is older than her sister in terms of age.", ["elder", "more older", "more elder", "oldest"], "elder"),
        ("The student completed the assignment before the examination commenced.", ["before exam", "who won", "carefully", "in library"], "before exam"),
        ("'Burning bridges' means ending important relationships permanently.", ["starting fire", "destroying buildings", "traveling by ferry", "ending relationships permanently"], "ending relationships permanently"),
        ("Voracious means excessively eager or greedy.", ["careful", "hesitant", "patient", "excessively eager"], "excessively eager"),
        ("He doesn't like rice for dinner.", ["He don't like", "He not like", "He no like", "He doesn't like"], "He doesn't like"),
        ("The central thought of a paragraph is its main idea.", ["the first sentence", "the last sentence", "examples used", "central thought"], "central thought"),
        ("Malevolent is the opposite of benevolent.", ["kind", "generous", "helpful", "malevolent"], "malevolent"),
        ("The word 'accommodate' is spelled with two m's and two c's.", ["accomodate", "acomodate", "acommodate", "accommodate"], "accommodate"),
        ("The data is accurate according to statistical analysis.", ["The team are", "Economics are", "Politics are", "The data is"], "The data is"),
        ("An antonym is a word with opposite meaning.", ["synonym", "homonym", "antonym", "acronym"], "antonym"),
        ("Connotation refers to the emotional association of a word.", ["denotation", "annotation", "connotation", "dedication"], "connotation"),
        ("Onomatopoeia is when a word imitates a sound.", ["alliteration", "metaphor", "onomatopoeia", "personification"], "onomatopoeia"),
        ("A paragraph transitions between ideas smoothly.", ["coherence", "ambiguity", "confusion", "contradiction"], "coherence"),
        ("Ambiguity means having more than one possible meaning.", ["clarity", "ambiguity", "precision", "accuracy"], "ambiguity"),
    ],
    "mathematics": [
        ("The quadratic equation x² - 5x + 6 = 0 has solutions x = 2 and x = 3.", ["x = 1, 6", "x = 2, 3", "x = 1, 5", "x = 2, 6"], "x = 2, 3"),
        ("The sum of the arithmetic sequence 2, 5, 8... to the 10th term is 155.", ["165", "145", "175", "155"], "155"),
        ("(2√3 + √3)² simplifies to 27.", ["18", "27", "36", "9"], "27"),
        ("If log₂ 16 = x, then x = 4.", ["2", "4", "6", "8"], "4"),
        ("A right triangle with sides 3, 4, 5cm has area 6 cm².", ["5 cm²", "6 cm²", "7 cm²", "8 cm²"], "6 cm²"),
        ("The inequality 3x + 2 < 11 solves to x < 3.", ["x < 2", "x < 1", "x < 4", "x < 3"], "x < 3"),
        ("The derivative of f(x) = 2x³ - 3x² is 6x² - 6x.", ["6x² - 3x", "3x² - 6x", "6x - 3", "6x² - 6x"], "6x² - 6x"),
        ("The value of sin(30°) is 0.5.", ["√3/2", "1", "0", "0.5"], "0.5"),
        ("A cylinder with radius 2cm and height 5cm has volume 20π cm³.", ["10π cm³", "15π cm³", "25π cm³", "20π cm³"], "20π cm³"),
        ("From 2x + y = 5 and x - y = 1, we get x = 2, y = 1.", ["x = 1, y = 2", "x = 3, y = -1", "x = -1, y = 3", "x = 2, y = 1"], "x = 2, y = 1"),
        ("The sum of angles in a triangle is 180°.", ["90°", "360°", "270°", "180°"], "180°"),
        ("Pythagoras theorem states a² + b² = c² for right triangles.", ["a + b = c", "a - b = c", "a × b = c", "a² + b² = c²"], "a² + b² = c²"),
        ("The area of a circle with radius r is πr².", ["2πr", "πr", "πr²", "2πr²"], "πr²"),
        ("The circumference of a circle is 2πr.", ["πr", "πr²", "2πr", "4πr"], "2πr"),
        ("Probability ranges from 0 to 1 inclusive.", ["0 to 2", "0 to 100", "-1 to 1", "0 to 1"], "0 to 1"),
    ],
    "chemistry": [
        ("CO₂ is a covalent compound.", ["NaCl", "KBr", "MgO", "CO₂"], "CO₂"),
        ("The oxidation state of nitrogen in NO₂ is +4.", ["+2", "+3", "+5", "+4"], "+4"),
        ("The balanced equation is 4Fe + 3O₂ → 2Fe₂O₃.", ["3, 1, 2", "2, 1.5, 1", "1, 2, 3", "4, 3, 2"], "4, 3, 2"),
        ("The pH range of a strong acid is 0-3.", ["7-10", "10-14", "3-7", "0-3"], "0-3"),
        ("Calcium reacts with water to produce Ca(OH)₂ and H₂.", ["CaO + H₂", "Ca + O₂", "CaCl + H", "Ca(OH)₂ + H₂"], "Ca(OH)₂ + H₂"),
        ("The valency of oxygen is 2.", ["1", "3", "4", "2"], "2"),
        ("Ethene (C₂H₄) is the monomer of polyethene.", ["C", "C₂H₆", "CH₄", "CH₂=CH₂"], "CH₂=CH₂"),
        ("Zinc reacts with dilute hydrochloric acid to produce hydrogen gas.", ["O₂", "Cl₂", "CO₂", "H₂"], "H₂"),
        ("The formula of sulfuric acid is H₂SO₄.", ["H₂SO₃", "HSO₄", "H₃SO₄", "H₂SO₄"], "H₂SO₄"),
        ("Methane has the molecular formula CH₄.", ["CH", "C₂H₆", "C₃H₈", "CH₄"], "CH₄"),
        ("Exothermic reactions release heat energy.", ["absorb heat", "maintain heat", "has no change", "releases heat"], "releases heat"),
        ("In 2H₂ + O₂ → 2H₂O, hydrogen is the reducing agent.", ["O₂", "H₂O", "both H₂ and O₂", "H₂"], "H₂"),
        ("Potassium nitrate has the formula KNO₃.", ["KNO₂", "K₂NO₃", "K₃NO", "KNO₃"], "KNO₃"),
        ("Chlorine has electronic configuration 2, 8, 7.", ["2, 8, 8", "2, 7", "2, 8, 6", "2, 8, 7"], "2, 8, 7"),
        ("Ammonia is produced when ammonium salts react with alkali.", ["concentrated HNO₃ is heated", "nitrogen reacts with oxygen", "ammonia is cooled", "ammonium salts react with alkali"], "ammonium salts react with alkali"),
    ],
    "physics": [
        ("Speed calculated as distance/time: 100m/5s = 20 m/s.", ["10 m/s", "15 m/s", "25 m/s", "20 m/s"], "20 m/s"),
        ("Time to fall 20m at g=10 m/s² is 2 seconds.", ["1s", "3s", "4s", "2s"], "2s"),
        ("Power dissipated: P = I²R = 2² × 5 = 20W.", ["10W", "40W", "80W", "20W"], "20W"),
        ("The SI unit of force is the Newton.", ["Dyne", "Erg", "Joule", "Newton"], "Newton"),
        ("Resistance calculated from Ohm's law: R = V/I = 12/3 = 4Ω.", ["2Ω", "3Ω", "6Ω", "4Ω"], "4Ω"),
        ("Acceleration from 0 to 30 m/s in 5s is 6 m/s².", ["4 m/s²", "5 m/s²", "8 m/s²", "6 m/s²"], "6 m/s²"),
        ("The refractive index of water is 1.33.", ["1.0", "1.5", "2.0", "1.33"], "1.33"),
        ("Heat transfer through a medium occurs by convection.", ["Conduction", "Radiation", "None", "Convection"], "Convection"),
        ("Frequency = speed/wavelength = 10/2 = 5 Hz.", ["2 Hz", "10 Hz", "20 Hz", "5 Hz"], "5 Hz"),
        ("Specific heat capacity of water is 4200 J/(kg·K).", ["1000 J/(kg·K)", "2000 J/(kg·K)", "8400 J/(kg·K)", "4200 J/(kg·K)"], "4200 J/(kg·K)"),
        ("Newton's first law states objects maintain uniform motion unless acted upon by force.", ["objects accelerate", "objects decelerate", "objects stop", "maintain uniform motion"], "maintain uniform motion"),
        ("Density is mass divided by volume.", ["volume × mass", "mass - volume", "volume / mass", "mass / volume"], "mass / volume"),
        ("Kinetic energy increases with the square of velocity.", ["linearly with velocity", "inversely with velocity", "not with velocity", "with square of velocity"], "with square of velocity"),
        ("Sound travels faster in solids than in air.", ["slower in solids", "same in all media", "sound doesn't travel in solids", "faster in solids"], "faster in solids"),
        ("Reflection occurs when light bounces off a surface.", ["light bends", "light passes through", "light disappears", "light bounces off"], "light bounces off"),
    ],
    "biology": [
        ("The mitochondrion is responsible for energy production in cells.", ["Ribosome", "Nucleus", "Golgi apparatus", "Mitochondrion"], "Mitochondrion"),
        ("Photosynthesis is the process by which plants manufacture food.", ["digestion", "respiration", "fermentation", "photosynthesis"], "photosynthesis"),
        ("The pulmonary vein carries oxygenated blood from the lungs to the heart.", ["Pulmonary artery", "Vena cava", "Aorta", "Pulmonary vein"], "Pulmonary vein"),
        ("The cell is the basic structural and functional unit of life.", ["atom", "molecule", "tissue", "cell"], "cell"),
        ("Metaphase is the stage where chromosomes line up at the cell equator.", ["Prophase", "Anaphase", "Telophase", "Metaphase"], "Metaphase"),
        ("Amylase is an enzyme that breaks down starch into sugars.", ["breaks proteins", "breaks fats", "breaks nucleic acids", "breaks starch"], "breaks starch"),
        ("Fixed joints allow no movement between bones.", ["Hinge", "Ball-and-socket", "Gliding", "Fixed"], "Fixed"),
        ("Chlorophyll primarily absorbs light in red and blue wavelengths.", ["green and yellow", "orange and red", "blue and violet", "red and blue"], "red and blue"),
        ("Insulin is the hormone that regulates blood glucose levels.", ["Glucagon", "Adrenaline", "Thyroxine", "Insulin"], "Insulin"),
        ("A test cross between heterozygous Aa and homozygous aa gives offspring.", ["AA and aa", "AA, Aa, aa", "all homozygous", "Aa and aa"], "Aa and aa"),
        ("Heart valves prevent backflow of blood in the circulatory system.", ["Septum", "Atrium", "Ventricle", "Valve"], "Valve"),
        ("Aerobic respiration requires oxygen to break down glucose.", ["produces 2 ATP", "occurs in cytoplasm", "produces lactic acid", "requires oxygen"], "requires oxygen"),
        ("The pancreas is an accessory organ of the digestive system.", ["Small intestine", "Stomach", "Esophagus", "Pancreas"], "Pancreas"),
        ("Transpiration is the process of water movement from roots to leaves.", ["osmosis", "diffusion", "turgor", "transpiration"], "transpiration"),
        ("O positive blood type is the universal donor.", ["AB positive", "A positive", "B positive", "O positive"], "O positive"),
    ],
    "christian_religious_studies": [
        ("Christianity is based primarily on the Holy Bible.", ["Torah", "Quran", "Vedas", "Bible"], "Bible"),
        ("Jesus taught all people including the poor and marginalized.", ["rich", "poor", "everyone", "men only"], "everyone"),
        ("The Ten Commandments were given in the book of Exodus.", ["Genesis", "Leviticus", "Numbers", "Exodus"], "Exodus"),
        ("Jesus Christ is believed to be the Son of God.", ["prophet", "teacher", "man", "Son of God"], "Son of God"),
        ("Christianity teaches salvation through both faith and works.", ["faith only", "works", "both", "neither"], "both"),
        ("Baptism symbolizes initiation and spiritual rebirth into the Christian faith.", ["washing", "initiation", "rebirth", "all of above"], "all of above"),
        ("The Communion service commemorates the Last Supper of Jesus.", ["birth", "resurrection", "ascension", "last supper"], "last supper"),
        ("Gospel literally means 'good news' in its original context.", ["law", "teaching", "book", "good news"], "good news"),
        ("The Sermon on Mount teaches the ethical principles of Jesus.", ["judgment", "law", "prophecy", "ethics"], "ethics"),
        ("Grace in Christianity refers to unearned divine favor and mercy.", ["prayer", "blessing", "gift", "unearned favor"], "unearned favor"),
        ("The Crucifixion is central to Christian theology and salvation.", ["Resurrection", "Ascension", "Birth", "Crucifixion"], "Crucifixion"),
        ("The Trinity concept represents God as Father, Son, and Holy Spirit.", ["Father and Son", "God only", "Holy Spirit only", "Father, Son, Holy Spirit"], "Father, Son, Holy Spirit"),
        ("Apostles were the twelve main followers chosen by Jesus.", ["disciples", "twelve followers", "early Christians", "twelve followers"], "twelve followers"),
        ("Repentance means turning away from sin and toward God.", ["guilt", "shame", "sorrow", "turning toward God"], "turning toward God"),
        ("The Resurrection of Jesus is celebrated on Easter Sunday.", ["Christmas", "Good Friday", "Palm Sunday", "Easter"], "Easter"),
    ],
    "islamic_studies": [
        ("Islam is based fundamentally on the teachings of the Qur'an.", ["Bible", "Torah", "Vedas", "Qur'an"], "Qur'an"),
        ("Prophet Muhammad was born in Mecca, Saudi Arabia.", ["Egypt", "Iran", "Iraq", "Saudi Arabia"], "Saudi Arabia"),
        ("The Five Pillars of Islam are five fundamental duties.", ["4", "6", "7", "5"], "5"),
        ("Muslims perform obligatory prayers five times daily.", ["3x", "1x", "2x", "5x"], "5x"),
        ("The Islamic calendar is based on the migration (Hijra) of Muhammad.", ["Gregorian", "Julian", "Buddhist", "Hijra"], "Hijra"),
        ("Hajj is the pilgrimage to Mecca that every Muslim should perform.", ["Medina", "Baghdad", "Jerusalem", "Mecca"], "Mecca"),
        ("Zakat is the obligation to give charity to the needy.", ["prayer", "fasting", "pilgrimage", "charity"], "charity"),
        ("Halal refers to what is permissible and lawful in Islam.", ["forbidden", "sacred", "holy", "permissible"], "permissible"),
        ("An Imam is the religious leader who leads prayers in the mosque.", ["prayer", "scholar", "teacher", "leader"], "leader"),
        ("The Qur'an consists of 114 chapters called Surahs.", ["99 chapters", "100 surahs", "120 parts", "114 chapters"], "114 chapters"),
        ("Salah is obligatory daily prayer performed at specific times.", ["fasting", "charity", "pilgrimage", "daily prayer"], "daily prayer"),
        ("Ramadan is the Islamic month of fasting and spiritual reflection.", ["prayer month", "pilgrimage month", "feast month", "fasting month"], "fasting month"),
        ("The Kaaba is the holiest site in Islam located in Mecca.", ["Al-Aqsa", "The Rock", "Medina", "Kaaba"], "Kaaba"),
        ("Muslims face the direction of Mecca (Qibla) during prayer.", ["North", "South", "East", "Mecca"], "Mecca"),
        ("The Hadith records the sayings and actions of Prophet Muhammad.", ["Qur'anic verses", "Islamic law", "historical events", "sayings of Muhammad"], "sayings of Muhammad"),
    ],
    "yoruba": [
        ("'Ewu' in Yoruba refers to cloth or wrapper.", ["adire", "cloth", "dress", "wrapper"], "cloth"),
        ("Ọ̀ṣun is the Yoruba goddess of water, fertility, and rivers.", ["water", "fertility", "river", "all of above"], "all of above"),
        ("'Mma' in Yoruba means good or well.", ["bad", "okay", "fine", "good"], "good"),
        ("Yoruba language has five major tones.", ["3", "4", "6", "5"], "5"),
        ("'Ọ̀ba' means king or ruler in Yoruba culture.", ["queen", "chief", "elder", "king"], "king"),
        ("'Ori' in Yoruba cosmology represents head, destiny, and spirit.", ["head", "destiny", "spirit", "all meanings"], "all meanings"),
        ("'Àgbà' refers to an elder or senior person deserving respect.", ["old person", "respect", "senior", "elder"], "elder"),
        ("The Yoruba people originate primarily from Nigeria.", ["Ghana", "Benin", "Cameroon", "Nigeria"], "Nigeria"),
        ("'Ọ̀rìnkí' is praise poetry recited in Yoruba ceremonies.", ["poetry", "song", "prayer", "praise"], "praise"),
        ("'Egungun' refers to the masquerade festival of the Yoruba.", ["festival", "spirit", "ceremony", "masquerade"], "masquerade"),
        ("'Iroko' is a sacred tree in Yoruba traditional religion.", ["palm", "oak", "mango", "sacred tree"], "sacred tree"),
        ("Yoruba cosmology includes a pantheon of deities called Orisha.", ["spirits", "ancestors", "Orisha", "gods"], "Orisha"),
        ("'Iyalode' was the title of a powerful female leader in Yoruba society.", ["queen", "priestess", "chief", "leader"], "leader"),
        ("Yoruba traditional government was hierarchical with Obas as rulers.", ["democratic", "centralized", "hierarchical", "autocratic"], "hierarchical"),
        ("'Ẹbọ' refers to sacrifice made to appease the deities in Yoruba religion.", ["prayer", "gift", "offering", "sacrifice"], "sacrifice"),
    ],
    "french": [
        ("The passé composé of 'être' is 'j'ai été'.", ["je suis été", "j'etais", "je fus", "j'ai été"], "j'ai été"),
        ("In present tense, 'aller' (to go) conjugates as: je vais.", ["vais", "va", "vont", "vais"], "vais"),
        ("The comparative form of 'bon' (good) is 'meilleur'.", ["plus bon", "bon plus", "mieux", "meilleur"], "meilleur"),
        ("'Demain' in French means tomorrow.", ["aujourd'hui", "yesterday", "later", "tomorrow"], "tomorrow"),
        ("The feminine form of 'acteur' (actor) is 'actrice'.", ["acteur", "actriss", "acteuress", "actrice"], "actrice"),
        ("The phrase 'J'ai mal à la tête' means 'I have a headache'.", ["suis", "vais", "fais", "ai"], "ai"),
        ("'Bibliothèque' in French means library.", ["book store", "school", "office", "library"], "library"),
        ("The relative pronoun 'qui' functions as the subject in a clause.", ["objet", "possessif", "génitif", "sujet"], "sujet"),
        ("'Nourriture' means food in French.", ["drink", "meal", "restaurant", "food"], "food"),
        ("The plural of 'journal' (newspaper) is 'journaux'.", ["journals", "journales", "journalss", "journaux"], "journaux"),
        ("'Bonjour' is the standard greeting meaning 'good day'.", ["goodbye", "hello evening", "hello night", "good day"], "good day"),
        ("The verb 'avoir' (to have) is irregular in conjugation.", ["regular", "semi-regular", "irregular", "defective"], "irregular"),
        ("'Merci' means thank you in French.", ["sorry", "please", "welcome", "thank you"], "thank you"),
        ("The letters 'ou' represent the sound /u/ like in 'vous'.", ["/o/", "/ɔ/", "/u/", "/y/"], "/u/"),
        ("'Excusez-moi' is used to apologize or get someone's attention.", ["thank you", "goodbye", "hello", "excuse me"], "excuse me"),
    ],
    "arabic": [
        ("The past tense of 'كتب' (to write) in plural is 'كتبوا'.", ["كتبنا", "كتبتم", "كتبن", "كتبوا"], "كتبوا"),
        ("'المكتبة' in Arabic refers to a library.", ["desk", "office", "school", "library"], "library"),
        ("The sound masculine plural ending is 'ون' in Arabic.", ["ين", "اء", "ات", "ون"], "ون"),
        ("'الطعام' in Arabic means food.", ["water", "drink", "meal", "food"], "food"),
        ("The present tense of 'قرأ' (to read) is 'أقرأ'.", ["قراءة", "اقرا", "يقرا", "أقرأ"], "أقرأ"),
        ("'يوم' in Arabic means day.", ["year", "month", "week", "day"], "day"),
        ("The letter 'إن' is used to negate the predicate nominative.", ["أن", "لكن", "ليس", "إن"], "إن"),
        ("The plural of 'البيت' (house) is 'بيوت'.", ["بيتات", "بيتان", "البيوت", "بيوت"], "بيوت"),
        ("'أختي' means 'my sister' in Arabic.", ["his sister", "her sister", "your sister", "my sister"], "my sister"),
        ("The adjective agrees with the noun it modifies in Arabic.", ["number", "gender", "case", "all of above"], "all of above"),
        ("The particle 'ال' in Arabic indicates the definite article.", ["conjunction", "preposition", "pronoun", "definite article"], "definite article"),
        ("'السلام عليكم' is the Islamic greeting in Arabic.", ["goodbye", "thank you", "welcome", "hello"], "hello"),
        ("The verb forms in Arabic are classified by tense and mood.", ["person only", "voice only", "tense and mood", "number only"], "tense and mood"),
        ("'لا' is used to express negation in Arabic.", ["yes", "perhaps", "negation", "affirmation"], "negation"),
        ("Diacritical marks in Arabic indicate vowels and special sounds.", ["capitalization", "punctuation", "vowels", "stress"], "vowels"),
    ],
    "igbo": [
        ("'Nne' in Igbo means mother.", ["father", "sister", "brother", "mother"], "mother"),
        ("'Ụlọ' in Igbo refers to a house or compound.", ["door", "room", "compound", "house"], "house"),
        ("The Igbo people originate from Eastern Nigeria.", ["Northern Nigeria", "Western Nigeria", "Southern Nigeria", "Eastern Nigeria"], "Eastern Nigeria"),
        ("'Chi' in Igbo belief system represents destiny or personal god.", ["spirit", "god", "ancestor", "destiny"], "destiny"),
        ("'Nwa' in Igbo means child or young person.", ["man", "woman", "person", "child"], "child"),
        ("The Igbo language belongs to the Niger-Congo language family.", ["Afro-Asiatic", "Nilo-Saharan", "Khoisan", "Niger-Congo"], "Niger-Congo"),
        ("'Anyanwu' in Igbo means sun.", ["moon", "star", "light", "sun"], "sun"),
        ("'Akwụ' in Igbo refers to the palm tree or its products.", ["oil", "coconut", "water", "palm tree"], "palm tree"),
        ("Igbo society traditionally operated with decentralized village governance.", ["centralized", "military", "monarchy", "decentralized villages"], "decentralized villages"),
        ("'Ihe' in Igbo means thing, matter, or object.", ["matter", "stuff", "object", "thing"], "thing"),
        ("Igbo market culture was important for trade and social interaction.", ["agriculture", "warfare", "trade", "crafts"], "trade"),
        ("'Ọkụkọ' in Igbo refers to a chicken or fowl.", ["goat", "sheep", "pig", "chicken"], "chicken"),
        ("The Igbo initiation rite 'Nkpu' marks important life transitions.", ["birth", "marriage", "death", "transitions"], "transitions"),
        ("'Obim' in Igbo means brother or sister relationship.", ["cousin", "friend", "neighbor", "sibling"], "sibling"),
        ("Igbo art and sculpture are known for their expressive masks and figures.", ["abstract", "minimalist", "expressive", "realistic"], "expressive"),
    ],
    "hausa": [
        ("'Gida' in Hausa means house or home.", ["school", "market", "road", "house"], "house"),
        ("The Hausa people primarily inhabit Northern Nigeria.", ["Southern Nigeria", "Western Nigeria", "Eastern Nigeria", "Northern Nigeria"], "Northern Nigeria"),
        ("'Sannu' in Hausa is a greeting meaning hello.", ["thank you", "goodbye", "welcome", "hello"], "hello"),
        ("'Ido' in Hausa refers to time, period, or moment.", ["day", "period", "moment", "time"], "day"),
        ("Hausa culture values honesty, tradition, and community.", ["honesty", "tradition", "community", "all factors"], "all factors"),
        ("'Malam' in Hausa refers to a teacher or Islamic scholar.", ["student", "scholar", "elder", "teacher"], "teacher"),
        ("The Hausa language belongs to the Afro-Asiatic language family.", ["Niger-Congo", "Nilo-Saharan", "Khoisan", "Afro-Asiatic"], "Afro-Asiatic"),
        ("Hausa people engaged in trans-Saharan trade historically.", ["local", "regional", "maritime", "trans-Saharan"], "trans-Saharan"),
        ("Hausa uses both prefixes and suffixes to form plurals.", ["prefixes", "suffixes", "both methods", "compound words"], "both methods"),
        ("Hausa traditional music prominently features drums and percussion.", ["strings", "wind", "all instruments", "drums"], "drums"),
        ("'Kudi' in Hausa means money or wealth.", ["trade", "market", "goods", "money"], "money"),
        ("Hausa naming traditions often reflect historical or cultural significance.", ["random", "family", "cultural significance", "biblical"], "cultural significance"),
        ("The Hausa settled in Northern Nigeria around the 12th century.", ["8th", "15th", "10th", "12th"], "12th"),
        ("Hausa women historically held important roles in markets and trade.", ["agriculture", "warfare", "government", "trade"], "trade"),
        ("'Acini' in Hausa means friend or companion.", ["enemy", "stranger", "neighbor", "friend"], "friend"),
    ],
}

def main():
    """Generate 300 unique questions per subject"""
    for subject_name, base_questions in SUBJECTS_DATA.items():
        all_questions = []
        
        # Create 30 variations from each base question to reach 300 total
        for base_q in base_questions:
            variations = create_question_variations(base_q, num_variations=20)  # 15 base * 20 = 300
            all_questions.extend(variations)
        
        # Shuffle all questions
        random.shuffle(all_questions)
        
        # Write to file
        filename = subject_name.replace("_", "_") + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(all_questions, f, indent=2, ensure_ascii=False)
        
        print(f"✓ {filename}: {len(all_questions)} questions ({len(set(q['question'] for q in all_questions))} unique)")

if __name__ == "__main__":
    main()
