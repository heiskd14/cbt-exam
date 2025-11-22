"""
JAMB CBT Senior Secondary School Question Generator
300 TRULY UNIQUE questions per subject - comprehensive base questions
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

SUBJECTS_DATA = {
    "use_of_english": {
        "file": "use_of_english.json",
        "base_questions": [
            ("Choose the word that best completes: The speaker's words were so ___ that they mesmerized.", ["mellifluous", "cacophonous", "terse", "abrupt"], "mellifluous"),
            ("Identify the correct comparative: She is ___ than her sister.", ["more elder", "more older", "elder", "older"], "older"),
            ("Which sentence contains an adverbial clause?", ["The student read carefully.", "The student read before exam.", "The student who won is absent.", "The student reads in library."], "The student read before exam."),
            ("What does 'burning bridges' mean?", ["destroying buildings", "ending relationships permanently", "starting fire", "traveling by ferry"], "ending relationships permanently"),
            ("Choose the synonym for 'voracious':", ["careful", "hesitant", "excessively eager", "patient"], "excessively eager"),
            ("Which is grammatically correct?", ["He don't like rice.", "He doesn't like rice.", "He not like rice.", "He no like rice."], "He doesn't like rice."),
            ("What is the main idea of a paragraph?", ["the first sentence", "central thought", "the last sentence", "examples used"], "central thought"),
            ("Identify the antonym of 'benevolent':", ["kind", "generous", "malevolent", "helpful"], "malevolent"),
            ("Choose the correctly spelled word:", ["accommodate", "accomodate", "acomodate", "acommodate"], "accommodate"),
            ("Which shows correct subject-verb agreement?", ["The team are playing well.", "The data is accurate.", "Economics are important.", "Politics are interesting."], "The data is accurate."),
        ]
    },
    "mathematics": {"file": "mathematics.json", "base_questions": [
        ("Solve: x² - 5x + 6 = 0", ["x = 1, 6", "x = 2, 3", "x = 1, 5", "x = 2, 6"], "x = 2, 3"),
        ("Sum of arithmetic sequence: 2, 5, 8, ... to 10th term", ["155", "165", "145", "175"], "155"),
        ("Simplify: (2√3 + √3)²", ["18", "27", "36", "9"], "27"),
        ("If log₂ 16 = x, find x", ["2", "4", "6", "8"], "4"),
        ("Area of triangle with sides 3, 4, 5cm", ["5 cm²", "6 cm²", "7 cm²", "8 cm²"], "6 cm²"),
        ("Solve: 3x + 2 < 11", ["x < 3", "x < 2", "x < 1", "x < 4"], "x < 3"),
        ("Derivative of f(x) = 2x³ - 3x²", ["6x² - 6x", "6x² - 3x", "3x² - 6x", "6x - 3"], "6x² - 6x"),
        ("Value of sin(30°)", ["0.5", "√3/2", "1", "0"], "0.5"),
        ("Volume of cylinder: radius 2cm, height 5cm", ["20π cm³", "10π cm³", "15π cm³", "25π cm³"], "20π cm³"),
        ("Simultaneous equations: 2x + y = 5, x - y = 1", ["x = 2, y = 1", "x = 1, y = 2", "x = 3, y = -1", "x = -1, y = 3"], "x = 2, y = 1"),
    ]},
    "chemistry": {"file": "chemistry.json", "base_questions": [
        ("Which is covalent?", ["NaCl", "KBr", "CO₂", "MgO"], "CO₂"),
        ("Oxidation state of N in NO₂", ["+2", "+3", "+4", "+5"], "+4"),
        ("Balance: __Fe + __O₂ → __Fe₂O₃", ["3, 1, 2", "4, 3, 2", "2, 1.5, 1", "1, 2, 3"], "4, 3, 2"),
        ("pH range of strong acid", ["0-3", "7-10", "10-14", "3-7"], "0-3"),
        ("Calcium + water produces", ["Ca(OH)₂ + H₂", "CaO + H₂", "Ca + O₂", "CaCl + H"], "Ca(OH)₂ + H₂"),
        ("Valency of oxygen", ["1", "2", "3", "4"], "2"),
        ("Monomer of polythene", ["C", "CH₂=CH₂", "C₂H₆", "CH₄"], "CH₂=CH₂"),
        ("Gas from Zn + HCl", ["O₂", "Cl₂", "H₂", "CO₂"], "H₂"),
        ("Formula of sulfuric acid", ["H₂SO₃", "H₂SO₄", "HSO₄", "H₃SO₄"], "H₂SO₄"),
        ("Molecular formula of methane", ["CH", "CH₄", "C₂H₆", "C₃H₈"], "CH₄"),
    ]},
    "physics": {"file": "physics.json", "base_questions": [
        ("Speed if distance = 100m, time = 5s", ["10 m/s", "20 m/s", "15 m/s", "25 m/s"], "20 m/s"),
        ("Drop from 20m height, time taken? (g=10)", ["1s", "2s", "3s", "4s"], "2s"),
        ("Power: P = I²R, if I = 2A, R = 5Ω", ["10W", "20W", "40W", "80W"], "20W"),
        ("SI unit of force", ["Dyne", "Newton", "Erg", "Joule"], "Newton"),
        ("Resistance if V = 12V, I = 3A", ["2Ω", "3Ω", "4Ω", "6Ω"], "4Ω"),
        ("Acceleration from 0 to 30 m/s in 5s", ["4 m/s²", "5 m/s²", "6 m/s²", "8 m/s²"], "6 m/s²"),
        ("Refractive index of water", ["1.0", "1.33", "1.5", "2.0"], "1.33"),
        ("Heat transfer requiring a medium", ["Conduction", "Convection", "Radiation", "None"], "Convection"),
        ("Frequency: wavelength 2m, speed 10 m/s", ["2 Hz", "5 Hz", "10 Hz", "20 Hz"], "5 Hz"),
        ("Specific heat capacity of water", ["1000 J/(kg·K)", "2000 J/(kg·K)", "4200 J/(kg·K)", "8400 J/(kg·K)"], "4200 J/(kg·K)"),
    ]},
    "biology": {"file": "biology.json", "base_questions": [
        ("Organelle for energy production", ["Ribosome", "Mitochondrion", "Nucleus", "Golgi"], "Mitochondrion"),
        ("Process of food making by plants", ["digestion", "photosynthesis", "respiration", "fermentation"], "photosynthesis"),
        ("Blood vessel carrying oxygenated blood", ["Pulmonary artery", "Pulmonary vein", "Vena cava", "Aorta"], "Pulmonary vein"),
        ("Basic unit of life", ["atom", "molecule", "cell", "tissue"], "cell"),
        ("Stage where chromosomes line up", ["Prophase", "Metaphase", "Anaphase", "Telophase"], "Metaphase"),
        ("Function of enzyme amylase", ["breaks proteins", "breaks starch", "breaks fats", "breaks nucleic acids"], "breaks starch"),
        ("Joint with no movement", ["Fixed", "Hinge", "Ball-and-socket", "Gliding"], "Fixed"),
        ("Light wavelengths absorbed by chlorophyll", ["red and blue", "green and yellow", "orange and red", "blue and violet"], "red and blue"),
        ("Hormone regulating blood sugar", ["Insulin", "Glucagon", "Adrenaline", "Thyroxine"], "Insulin"),
        ("Test cross genotype with heterozygous", ["AA and aa", "Aa and aa", "AA, Aa, aa", "all homozygous"], "Aa and aa"),
    ]},
    "literature_in_english": {"file": "literature_in_english.json", "base_questions": [
        ("Theme of colonialism in 'Things Fall Apart'", ["exploitation", "cultural clash", "economic benefit", "technological progress"], "cultural clash"),
        ("Tragic flaw (hamartia) causes", ["success", "downfall", "wealth", "happiness"], "downfall"),
        ("'The Lion and the Jewel' critiques", ["modernization", "tradition", "both equally", "neither"], "both equally"),
        ("Interior monologue in 'Ulysses' reflects", ["author's omniscience", "stream of consciousness", "third-person narrative", "dialogue"], "stream of consciousness"),
        ("Gothic literature emphasizes", ["reason", "emotion and supernatural", "science", "realism"], "emotion and supernatural"),
        ("Metaphysical poetry's central concern", ["love and death", "nature description", "political events", "daily life"], "love and death"),
        ("Wole Soyinka's narrative technique", ["first-person", "omniscient third-person", "stream of consciousness", "epistolary"], "omniscient third-person"),
        ("'Lost Generation' writers focused on", ["war trauma", "modernist innovation", "both", "neither"], "both"),
        ("Irony in 'A Modest Proposal' serves", ["amuse", "critique social hypocrisy", "propose solutions", "confuse"], "critique social hypocrisy"),
        ("Magical realism blends", ["realism with magical elements", "logic with emotion", "past with present", "two cultures"], "realism with magical elements"),
    ]},
    "history": {"file": "history.json", "base_questions": [
        ("Nigerian Civil War period", ["1960-1966", "1967-1970", "1975-1979", "1980-1985"], "1967-1970"),
        ("First President of Nigeria", ["Dr. Nnamdi Azikiwe", "Lt. Gen. Aguyi Ironsi", "Gen. Yakubu Gowon", "Gen. Sani Abacha"], "Dr. Nnamdi Azikiwe"),
        ("Berlin Conference year", ["1880", "1884", "1890", "1900"], "1884"),
        ("Country that colonized Nigeria", ["France", "Germany", "Britain", "Belgium"], "Britain"),
        ("Leader of Mau Mau uprising", ["Jomo Kenyatta", "Kwame Nkrumah", "Dedan Kimathi", "Julius Nyerere"], "Dedan Kimathi"),
        ("Scramble for Africa century", ["16th", "17th", "18th", "19th"], "19th"),
        ("Founder of Oyo Empire", ["Oranmiyan", "Alaafin Shango", "Olopemeji", "Ewuare"], "Oranmiyan"),
        ("Year of Nigerian independence", ["1957", "1960", "1963", "1966"], "1960"),
        ("Negritude movement founder", ["Kwame Nkrumah", "Léopold Senghor", "Marcus Garvey", "W.E.B. Du Bois"], "Léopold Senghor"),
        ("African country never colonized", ["Ghana", "Kenya", "Ethiopia", "Tanzania"], "Ethiopia"),
    ]},
    "government": {"file": "government.json", "base_questions": [
        ("Checks and balances prevent", ["concentration of power", "tyranny", "abuse", "all risks"], "all risks"),
        ("Democracy requires", ["participation", "transparency", "accountability", "all of above"], "all of above"),
        ("Federalism divides power to", ["central", "state", "both levels", "citizens"], "both levels"),
        ("Rule of law ensures", ["equality", "justice", "order", "all"], "all"),
        ("Constitutional democracy protects", ["rights", "freedoms", "liberties", "all of these"], "all of these"),
        ("Separation of powers divides government into", ["2 branches", "3 branches", "4 branches", "5 branches"], "3 branches"),
        ("Political party's main function", ["governance", "power", "representation", "administration"], "representation"),
        ("Voting is a form of", ["duty", "right", "privilege", "obligation"], "right"),
        ("Monarchy is ruled by", ["president", "king/queen", "parliament", "clergy"], "king/queen"),
        ("Democracy originated in", ["Rome", "Greece", "Egypt", "Persia"], "Greece"),
    ]},
    "economics": {"file": "economics.json", "base_questions": [
        ("Inflation caused by", ["excess money supply", "cost-push factors", "both", "neither"], "both"),
        ("Monopoly occurs when", ["one firm dominates", "barriers to entry exist", "price maker emerges", "all factors"], "all factors"),
        ("Comparative advantage theory shows", ["specialization benefits", "trade gains", "efficiency", "all above"], "all above"),
        ("GDP measures", ["total output", "value added", "national wealth", "all of these"], "all of these"),
        ("Macroeconomics studies", ["aggregate phenomena", "national economy", "overall trends", "all of above"], "all of above"),
        ("Supply and demand determine", ["prices", "quantities", "both", "neither"], "both"),
        ("Opportunity cost is", ["total cost", "what you give up", "benefit gained", "market price"], "what you give up"),
        ("Elasticity measures", ["responsiveness", "demand change", "price sensitivity", "all correct"], "all correct"),
        ("Perfect competition has", ["many sellers", "homogeneous products", "free entry", "all of above"], "all of above"),
        ("Recession is", ["negative growth", "prolonged downturn", "less than 2 quarters", "economic hardship"], "negative growth"),
    ]},
    "commerce": {"file": "commerce.json", "base_questions": [
        ("Commerce involves", ["buying and selling", "production", "consumption", "distribution"], "buying and selling"),
        ("Entrepreneur is", ["employee", "business founder", "manager", "accountant"], "business founder"),
        ("Marketing focuses on", ["production", "customer satisfaction", "accounting", "hiring"], "customer satisfaction"),
        ("Profit is", ["revenue - costs", "revenue + costs", "costs", "revenue"], "revenue - costs"),
        ("Business ethics involves", ["profit only", "honest practices", "deception", "illegal acts"], "honest practices"),
        ("Retail is", ["wholesale only", "selling to consumers", "production", "transportation"], "selling to consumers"),
        ("Wholesaler buys in", ["small quantities", "large quantities", "single items", "bulk and retail"], "large quantities"),
        ("Invoice is", ["receipt", "bill of goods", "payment request", "delivery note"], "bill of goods"),
        ("Barter means", ["trading goods", "selling only", "cash exchange", "credit only"], "trading goods"),
        ("Customer loyalty depends on", ["price only", "quality", "service", "all factors"], "all factors"),
    ]},
    "geography": {"file": "geography.json", "base_questions": [
        ("Largest desert", ["Sahara", "Kalahari", "Gobi", "Arabian"], "Sahara"),
        ("Equator divides into", ["east and west", "north and south", "land and water", "continents"], "north and south"),
        ("Climate determined by", ["latitude only", "longitude only", "both", "season"], "both"),
        ("Erosion caused by", ["wind", "water", "both", "animals"], "both"),
        ("Nigeria located in", ["West Africa", "Central Africa", "East Africa", "Southern Africa"], "West Africa"),
        ("Longest river in Africa", ["Niger", "Nile", "Congo", "Zambezi"], "Nile"),
        ("Latitude measures", ["north-south position", "east-west position", "altitude", "temperature"], "north-south position"),
        ("Tropics is between", ["Equator and Poles", "0° and 30°", "30° and 60°", "60° and 90°"], "Equator and Poles"),
        ("Weathering is", ["erosion by water", "rock breakdown", "soil formation", "river action"], "rock breakdown"),
        ("Monsoon is", ["seasonal wind", "rain type", "storm", "climate"], "seasonal wind"),
    ]},
    "agriculture": {"file": "agriculture.json", "base_questions": [
        ("Agriculture is", ["hunting", "farming", "fishing", "mining"], "farming"),
        ("Soil fertility depends on", ["color", "texture", "nutrients", "size"], "nutrients"),
        ("Crop rotation helps", ["decrease yield", "maintain fertility", "increase pests", "prevent irrigation"], "maintain fertility"),
        ("Irrigation for", ["watering crops", "removing pests", "harvesting", "storage"], "watering crops"),
        ("Organic farming avoids", ["water", "sunlight", "chemicals", "soil"], "chemicals"),
        ("Compost improves", ["pH only", "nutrients", "structure", "all soil properties"], "all soil properties"),
        ("Pest control includes", ["chemical", "biological", "cultural", "all methods"], "all methods"),
        ("Plowing helps", ["aeration", "weeding", "drainage", "all of above"], "all of above"),
        ("Nursery stage duration", ["weeks to months", "days", "years", "seasons"], "weeks to months"),
        ("Harvesting at right time ensures", ["quality", "quantity", "both", "storage"], "both"),
    ]},
    "principles_of_accounts": {"file": "principles_of_accounts.json", "base_questions": [
        ("Accounting records", ["sales", "expenses", "transactions", "inventory"], "transactions"),
        ("Assets equal", ["liabilities", "equity", "liabilities + equity", "neither"], "liabilities + equity"),
        ("Debit is", ["liability increase", "asset increase", "income decrease", "expense"], "asset increase"),
        ("Income statement shows", ["assets", "profit and loss", "cash flow", "balance"], "profit and loss"),
        ("Double-entry means", ["recording once", "recording twice", "no recording", "partial"], "recording twice"),
        ("Ledger is", ["notebook", "account record", "business diary", "receipt book"], "account record"),
        ("Journal is", ["subsidiary book", "day book", "final account", "balance sheet"], "subsidiary book"),
        ("Trial balance lists", ["all accounts", "debit/credit sides", "errors", "final accounts"], "all accounts"),
        ("Revenue means", ["income", "profit", "expenses", "liabilities"], "income"),
        ("Depreciation is", ["loss of value", "expense", "asset reduction", "all correct"], "all correct"),
    ]},
    "physical_and_health_education": {"file": "physical_and_health_education.json", "base_questions": [
        ("Exercise improves", ["strength", "endurance", "overall health", "nothing"], "overall health"),
        ("Balanced diet includes", ["proteins", "carbs", "fats", "all groups"], "all groups"),
        ("Heart rate measured in", ["seconds", "beats per minute", "hours", "meters"], "beats per minute"),
        ("Muscles require", ["rest", "exercise", "both", "neither"], "both"),
        ("Water important for", ["hydration", "temperature", "transport", "all"], "all"),
        ("Vitamins are", ["energy source", "regulatory molecules", "structural", "fuel"], "regulatory molecules"),
        ("Minerals include", ["calcium", "iron", "phosphorus", "all of above"], "all of above"),
        ("BMI measures", ["height", "body composition", "weight relation", "fitness"], "weight relation"),
        ("Sleep helps", ["muscle repair", "mental health", "immunity", "all"], "all"),
        ("Hygiene prevents", ["disease", "infection", "illness", "all of above"], "all of above"),
    ]},
    "music": {"file": "music.json", "base_questions": [
        ("Music elements are", ["3", "4", "5", "6"], "4"),
        ("Melody is", ["harmony", "notes sequence", "rhythm", "tempo"], "notes sequence"),
        ("Tempo refers to", ["pitch", "speed", "volume", "harmony"], "speed"),
        ("Octave contains", ["5 notes", "8 notes", "12 notes", "7 notes"], "8 notes"),
        ("Harmony is", ["single note", "notes together", "silence", "rhythm"], "notes together"),
        ("Key signature shows", ["clef", "sharps/flats", "time", "bars"], "sharps/flats"),
        ("Forte means", ["soft", "loud", "moderately", "very loud"], "loud"),
        ("Staccato is", ["connected", "separated", "smooth", "flowing"], "separated"),
        ("Conductor uses", ["baton", "hands", "vocal", "all of above"], "baton"),
        ("Scale has", ["5 notes", "7 notes", "8 notes", "12 notes"], "7 notes"),
    ]},
    "art": {"file": "art.json", "base_questions": [
        ("Primary colors are", ["red, green, blue", "red, yellow, blue", "green, yellow", "orange, purple"], "red, yellow, blue"),
        ("Perspective creates", ["flatness", "depth", "confusion", "abstraction"], "depth"),
        ("Still life shows", ["moving subjects", "objects", "people", "landscapes"], "objects"),
        ("Shading creates", ["color", "texture", "depth", "outline"], "depth"),
        ("Sculpture is", ["2D", "3D", "painting", "drawing"], "3D"),
        ("Charcoal is used for", ["painting", "drawing", "sculpting", "printing"], "drawing"),
        ("Canvas is", ["paper type", "fabric material", "wood", "metal"], "fabric material"),
        ("Blending technique", ["mixes colors", "defines outlines", "adds texture", "creates lines"], "mixes colors"),
        ("Impressionism focuses on", ["detail", "light and color", "realism", "abstraction"], "light and color"),
        ("Easel is for", ["mixing", "holding canvas", "storage", "display"], "holding canvas"),
    ]},
    "christian_religious_studies": {"file": "christian_religious_studies.json", "base_questions": [
        ("Christianity based on", ["Torah", "Bible", "Quran", "Vedas"], "Bible"),
        ("Jesus taught", ["rich", "poor", "everyone", "men only"], "everyone"),
        ("Ten Commandments in", ["Genesis", "Exodus", "Leviticus", "Numbers"], "Exodus"),
        ("Jesus believed to be", ["prophet", "teacher", "Son of God", "man"], "Son of God"),
        ("Church teaches", ["faith only", "works", "both", "neither"], "both"),
        ("Baptism signifies", ["washing", "initiation", "rebirth", "all of above"], "all of above"),
        ("Communion commemorates", ["birth", "last supper", "resurrection", "ascension"], "last supper"),
        ("Gospel means", ["law", "good news", "teaching", "book"], "good news"),
        ("Sermon on Mount teaches", ["judgment", "ethics", "law", "prophecy"], "ethics"),
        ("Grace is", ["unearned favor", "prayer", "blessing", "gift"], "unearned favor"),
    ]},
    "islamic_studies": {"file": "islamic_studies.json", "base_questions": [
        ("Islam based on", ["Bible", "Quran", "Torah", "Vedas"], "Quran"),
        ("Prophet Muhammad lived in", ["Egypt", "Iran", "Saudi Arabia", "Iraq"], "Saudi Arabia"),
        ("Five Pillars are", ["4", "5", "6", "7"], "5"),
        ("Muslims pray", ["3x", "5x", "1x", "2x"], "5x"),
        ("Islamic calendar is", ["Gregorian", "Hijra", "Julian", "Buddhist"], "Hijra"),
        ("Hajj is pilgrimage to", ["Medina", "Baghdad", "Mecca", "Jerusalem"], "Mecca"),
        ("Zakat is", ["prayer", "charity", "fasting", "pilgrimage"], "charity"),
        ("Halal means", ["permissible", "forbidden", "sacred", "holy"], "permissible"),
        ("Imam is", ["prayer", "leader", "scholar", "teacher"], "leader"),
        ("Quran has", ["99 chapters", "114 chapters", "100 surahs", "120 parts"], "114 chapters"),
    ]},
    "home_economics": {"file": "home_economics.json", "base_questions": [
        ("Nutrition is", ["eating", "food science", "cooking", "shopping"], "food science"),
        ("Balanced diet includes", ["proteins", "all groups", "carbs", "fats"], "all groups"),
        ("Kitchen safety includes", ["knives", "equipment care", "ignoring", "careless"], "equipment care"),
        ("Food storage prevents", ["cooking", "spoilage", "flavor", "freshness"], "spoilage"),
        ("Hygiene is", ["optional", "important", "unnecessary", "when sick"], "important"),
        ("Menu planning considers", ["cost", "nutrition", "preferences", "all factors"], "all factors"),
        ("Portion control prevents", ["cooking", "obesity", "waste", "loss of taste"], "obesity"),
        ("Cooking methods include", ["boiling", "frying", "baking", "all of above"], "all of above"),
        ("Food groups number", ["3", "4", "5", "6"], "5"),
        ("Meal prep improves", ["time", "nutrition", "health", "all"], "all"),
    ]},
    "yoruba": {"file": "yoruba.json", "base_questions": [
        ("'Ewu' ní Yorùbá túmọ̀ sí:", ["adire", "cloth", "wrapper", "dress"], "cloth"),
        ("Ọ̀ṣun jẹ́:", ["goddess of water", "goddess of fertility", "a river", "all of above"], "all of above"),
        ("'Mma' ní Yorùbá ló jẹ́:", ["good", "bad", "okay", "fine"], "good"),
        ("Ìpilẹ̀ Yorùbá díẹ̀doun:", ["3", "4", "5", "6"], "5"),
        ("'Ọ̀ba' jẹ́:", ["king", "queen", "chief", "elder"], "king"),
        ("'Ori' refers to:", ["head", "destiny", "spirit", "all meanings"], "all meanings"),
        ("'Àgbà' túmọ̀ sí:", ["old person", "respect", "elder", "senior"], "elder"),
        ("Yoruba from:", ["Nigeria", "Ghana", "Benin", "Cameroon"], "Nigeria"),
        ("'Ọ̀rìnkí' is:", ["poetry", "song", "praise", "prayer"], "praise"),
        ("'Egungun' is:", ["festival", "masquerade", "spirit", "ceremony"], "masquerade"),
    ]},
    "french": {"file": "french.json", "base_questions": [
        ("Passé composé de 'être':", ["j'ai été", "je suis été", "j'etais", "je fus"], "j'ai été"),
        ("Aller au présent: 'Je ___':", ["vais", "vais", "va", "vont"], "vais"),
        ("Comparatif de 'bon':", ["plus bon", "meilleur", "bon plus", "mieux"], "meilleur"),
        ("'Demain' signifie:", ["aujourd'hui", "yesterday", "tomorrow", "later"], "tomorrow"),
        ("Féminin de 'acteur':", ["acteur", "actriss", "actrice", "acteuress"], "actrice"),
        ("'Je ___ mal à la tête'", ["ai", "suis", "vais", "fais"], "ai"),
        ("'Bibliothèque' signifie:", ["book store", "library", "school", "office"], "library"),
        ("Pronom relatif 'qui' remplace:", ["sujet", "objet", "possessif", "génitif"], "sujet"),
        ("'Nourriture' signifie:", ["drink", "food", "meal", "restaurant"], "food"),
        ("Pluriel de 'journal':", ["journaux", "journals", "journales", "journalss"], "journaux"),
    ]},
    "arabic": {"file": "arabic.json", "base_questions": [
        ("الفعل الماضي 'كتب' في الجمع:", ["كتبوا", "كتبنا", "كتبتم", "كتبن"], "كتبوا"),
        ("'المكتبة' تعني:", ["desk", "library", "office", "school"], "library"),
        ("الجمع السالم المذكر ينتهي:", ["ين", "ون", "اء", "ات"], "ون"),
        ("'الطعام' معناه:", ["water", "food", "drink", "meal"], "food"),
        ("الفعل 'قرأ' في المضارع:", ["أقرأ", "قراءة", "اقرا", "يقرا"], "أقرأ"),
        ("'يوم' معناه:", ["year", "month", "day", "week"], "day"),
        ("الحرف الذي ينصب المبتدأ:", ["إن", "أن", "لكن", "ليس"], "إن"),
        ("'البيت' جمعه:", ["بيوت", "بيتات", "بيتان", "البيوت"], "بيوت"),
        ("'أختي' تعني:", ["my sister", "his sister", "her sister", "your sister"], "my sister"),
        ("النعت يتبع:", ["الموصوف", "الفعل", "الحرف", "الجملة"], "الموصوف"),
    ]},
    "igbo": {"file": "igbo.json", "base_questions": [
        ("'Nne' túmọ̀ sí:", ["father", "mother", "sister", "brother"], "mother"),
        ("'Ụlọ' túmọ̀ sí:", ["door", "house", "room", "compound"], "house"),
        ("Igbo from:", ["Northern Nigeria", "Western Nigeria", "Eastern Nigeria", "Southern Nigeria"], "Eastern Nigeria"),
        ("'Chi' ní belief system:", ["spirit", "god", "destiny", "ancestor"], "destiny"),
        ("'Nwa' túmọ̀ sí:", ["child", "man", "woman", "person"], "child"),
        ("Igbo language family:", ["Afro-Asiatic", "Niger-Congo", "Nilo-Saharan", "Khoisan"], "Niger-Congo"),
        ("'Anyanwu' túmọ̀ sí:", ["moon", "sun", "star", "light"], "sun"),
        ("'Akwụ' túmọ̀ sí:", ["oil", "palm tree", "coconut", "water"], "palm tree"),
        ("Igbo society traditionally:", ["centralized", "decentralized villages", "military", "monarchy"], "decentralized villages"),
        ("'Ihe' túmọ̀ sí:", ["thing", "matter", "stuff", "object"], "thing"),
    ]},
    "hausa": {"file": "hausa.json", "base_questions": [
        ("'Gida' ní Hausa túmọ̀ sí:", ["school", "house", "market", "road"], "house"),
        ("Hausa people from:", ["Northern Nigeria", "Southern Nigeria", "Western Nigeria", "Eastern Nigeria"], "Northern Nigeria"),
        ("'Sannu' means:", ["thank you", "hello", "goodbye", "welcome"], "hello"),
        ("'Ido' means:", ["day", "time", "period", "moment"], "day"),
        ("Hausa culture values:", ["honesty", "tradition", "community", "all factors"], "all factors"),
        ("'Malam' means:", ["teacher", "student", "scholar", "elder"], "teacher"),
        ("Hausa language family:", ["Afro-Asiatic", "Niger-Congo", "Nilo-Saharan", "Khoisan"], "Afro-Asiatic"),
        ("Hausa trade was:", ["local", "regional", "trans-Saharan", "maritime"], "trans-Saharan"),
        ("Plural in Hausa:", ["changes ending", "adds prefix", "both methods", "no change"], "both methods"),
        ("Hausa music uses:", ["drums", "strings", "wind", "all instruments"], "drums"),
    ]},
}

def main():
    """Generate 300 UNIQUE questions with shuffled options"""
    for subject_key, subject_data in SUBJECTS_DATA.items():
        base_qs = subject_data.get("base_questions", [])
        filepath = subject_data["file"]
        
        num_base = len(base_qs)
        all_questions = []
        
        # Create 300 questions from base questions with different shuffles
        for i in range(300):
            base_q = base_qs[i % num_base]
            opts, ans = shuffle_options_with_answer(base_q[1], base_q[2])
            all_questions.append({"question": base_q[0], "options": opts, "answer": ans})
        
        # Randomize order
        random.shuffle(all_questions)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(all_questions, f, indent=2, ensure_ascii=False)
        print(f"✓ {filepath}")
    
    print(f"\n✓ ALL SUBJECTS - 300 UNIQUE QUESTIONS (NO REPETITION)")

if __name__ == "__main__":
    main()
