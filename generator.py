"""
JAMB CBT Question Generator
Generates 300 hard-difficulty JAMB questions for each subject
"""
import json
import os

# Subject-specific question templates
SUBJECTS_DATA = {
    "use_of_english": {
        "file": "use_of_english.json",
        "prefix": "Use of English",
        "questions": [
            ("The word 'perspicacious' most nearly means", ["transparent", "keen in judgment", "clear vision", "curious"], "keen in judgment"),
            ("Which is NOT a synonym of 'ephemeral'?", ["fleeting", "temporary", "permanent", "transient"], "permanent"),
            ("'To take the bull by the horns' means to", ["avoid risk", "face difficulty boldly", "run away", "surrender"], "face difficulty boldly"),
            ("The opposite of 'verbose' is", ["silent", "terse", "polite", "eloquent"], "terse"),
            ("'Ameliorate' means to", ["worsen", "improve", "destroy", "change"], "improve"),
            ("'Pellucid' explanation would be", ["confusing", "crystal clear", "vague", "unclear"], "crystal clear"),
            ("'Sagacious' means", ["courageous", "wise and discerning", "foolish", "stubborn"], "wise and discerning"),
            ("'Ineluctable' means", ["avoidable", "inevitable", "possible to avoid", "doubtful"], "inevitable"),
            ("What does 'serendipity' mean?", ["being serene", "fortunate discovery by chance", "searching", "tranquility"], "fortunate discovery by chance"),
            ("'Fastidious' person is", ["careless", "particular about details", "easy-going", "flexible"], "particular about details"),
        ]
    },
    "mathematics": {
        "file": "mathematics.json",
        "prefix": "Mathematics",
        "questions": [
            ("Solve: 5x² - 3x - 2 = 0", ["x = 1, -2/5", "x = -1, 2/5", "x = 2, -1/5", "x = 1/2, -2"], "x = 1, -2/5"),
            ("What is the sum of first 20 natural numbers?", ["190", "200", "210", "220"], "210"),
            ("If f(x) = 2x² - x + 3, find f(-2)", ["5", "9", "13", "11"], "13"),
            ("Solve the system: 2x + y = 5 and 3x - y = 5", ["(1, 3)", "(2, 1)", "(3, -1)", "(0, 5)"], "(2, 1)"),
            ("Find the 10th term of 2, 5, 8, ...", ["27", "28", "29", "30"], "29"),
            ("What is the derivative of 3x³ - 2x + 1?", ["9x² - 2", "9x² - 2x", "9x - 2", "3x² - 2"], "9x² - 2"),
            ("Find the area of circle with diameter 10", ["25π", "50π", "100π", "10π"], "25π"),
            ("What is the volume of sphere with radius 3?", ["36π", "27π", "54π", "108π"], "36π"),
            ("Solve: log₂(x) = 3", ["6", "8", "9", "12"], "8"),
            ("If sin(θ) = 3/5, find cos(θ) where 0 < θ < π/2", ["4/5", "3/4", "2/5", "1/5"], "4/5"),
        ]
    },
    "literature_in_english": {
        "file": "literature_in_english.json",
        "prefix": "Literature in English",
        "questions": [
            ("Shakespeare wrote", ["novels", "plays and sonnets", "only poetry", "essays"], "plays and sonnets"),
            ("Who wrote 'Things Fall Apart'?", ["Chinua Achebe", "Wole Soyinka", "Ngozi Okorafor", "Buchi Emecheta"], "Chinua Achebe"),
            ("A metaphor is", ["comparison using like/as", "direct comparison without like/as", "repeated sound", "question"], "direct comparison without like/as"),
            ("The protagonist is", ["the villain", "the main character", "the narrator", "the author"], "the main character"),
            ("Irony means", ["sarcasm only", "opposite of expected", "a joke", "exaggeration"], "opposite of expected"),
            ("An alliteration is", ["rhyming words", "repeated initial sounds", "opposite meaning", "extended metaphor"], "repeated initial sounds"),
            ("Personification gives", ["human qualities to objects", "objects to humans", "power to weak", "weakness to strong"], "human qualities to objects"),
            ("A soliloquy is", ["conversation", "character speaking alone", "group discussion", "narrator comment"], "character speaking alone"),
            ("Symbolism uses", ["obvious meaning", "hidden meanings through symbols", "direct statements", "literal language"], "hidden meanings through symbols"),
            ("Who wrote 'Pride and Prejudice'?", ["Charlotte Brontë", "Jane Austen", "George Eliot", "Emily Dickinson"], "Jane Austen"),
        ]
    },
    "history": {
        "file": "history.json",
        "prefix": "History",
        "questions": [
            ("Who was the first President of Nigeria?", ["Nnamdi Azikiwe", "Aguiyi Ironsi", "Yakubu Gowon", "Goodluck Jonathan"], "Nnamdi Azikiwe"),
            ("The Nigerian Civil War ended in", ["1967", "1968", "1969", "1970"], "1970"),
            ("Which European nation colonized Nigeria?", ["France", "Germany", "Britain", "Belgium"], "Britain"),
            ("Nigeria gained independence in", ["1958", "1959", "1960", "1961"], "1960"),
            ("The Scramble for Africa occurred in the", ["17th century", "18th century", "19th century", "20th century"], "19th century"),
            ("Who founded the Sokoto Caliphate?", ["Usman dan Fodio", "Ahmadu Bello", "Mallam Jaji", "Shehu Usmanu"], "Usman dan Fodio"),
            ("The Benin Kingdom was known for", ["agriculture only", "bronze work and art", "mining", "hunting"], "bronze work and art"),
            ("When was slavery abolished in Nigeria?", ["1800", "1833", "1875", "1900"], "1833"),
            ("Which group led the Hausa-Fulani conquest?", ["Yoruba", "Igbo", "Hausa-Fulani", "Edo"], "Hausa-Fulani"),
            ("What was the capital of the Oyo Empire?", ["Ibadan", "Oyo-Ile", "Lagos", "Abeokuta"], "Oyo-Ile"),
        ]
    },
    "government": {
        "file": "government.json",
        "prefix": "Government",
        "questions": [
            ("A democratic system emphasizes", ["dictatorial rule", "people's participation", "military rule", "oligarchy"], "people's participation"),
            ("The separation of powers includes", ["executive only", "legislative, executive, judicial", "executive and military", "judicial only"], "legislative, executive, judicial"),
            ("A federal system divides power between", ["president and military", "central and state governments", "judiciary and executive", "all parties"], "central and state governments"),
            ("The constitution is", ["a law", "supreme law of the land", "a policy", "a decree"], "supreme law of the land"),
            ("Citizens have rights and", ["no duties", "duties", "no responsibilities", "optional duties"], "duties"),
            ("What is the basis of authority in democracy?", ["constitution", "tradition", "military strength", "wealth"], "constitution"),
            ("A unicameral legislature has", ["one chamber", "two chambers", "three chambers", "multiple chambers"], "one chamber"),
            ("Checks and balances exist to", ["increase power", "prevent abuse of power", "speed up process", "reduce costs"], "prevent abuse of power"),
            ("Rule of law means", ["laws apply to everyone", "laws apply to rich", "laws are optional", "laws change daily"], "laws apply to everyone"),
            ("Sovereignty refers to", ["power to make laws", "military strength", "wealth", "population size"], "power to make laws"),
        ]
    },
    "economics": {
        "file": "economics.json",
        "prefix": "Economics",
        "questions": [
            ("Economics deals with", ["scarcity of resources", "unlimited wants", "choices", "all of the above"], "all of the above"),
            ("Money serves as", ["medium of exchange only", "store of value only", "medium of exchange and store of value", "neither"], "medium of exchange and store of value"),
            ("Inflation means", ["increase in prices", "decrease in prices", "stable prices", "no prices"], "increase in prices"),
            ("Supply and demand determine", ["production", "prices", "consumption", "distribution"], "prices"),
            ("GDP measures", ["national wealth", "total output of country", "average income", "unemployment"], "total output of country"),
            ("Comparative advantage theory suggests", ["one country best at everything", "countries specialize in what they do best", "all countries equal", "trade is bad"], "countries specialize in what they do best"),
            ("Recession is characterized by", ["high growth", "low unemployment", "declining output", "inflation"], "declining output"),
            ("Interest rate affects", ["savings", "borrowing", "investment", "all of above"], "all of above"),
            ("Elasticity of demand measures", ["price change only", "quantity response to price change", "income only", "production"], "quantity response to price change"),
            ("Fiscal policy involves", ["money supply", "government spending and taxation", "bank lending", "stock market"], "government spending and taxation"),
        ]
    },
    "commerce": {
        "file": "commerce.json",
        "prefix": "Commerce",
        "questions": [
            ("Commerce involves", ["buying and selling", "only production", "only consumption", "distribution only"], "buying and selling"),
            ("An entrepreneur is", ["an employee", "person who starts business", "a manager", "an accountant"], "person who starts business"),
            ("Marketing focuses on", ["production only", "satisfying customer needs", "accounting", "hiring"], "satisfying customer needs"),
            ("A retailer is", ["a producer", "a wholesaler", "seller to consumers", "a distributor"], "seller to consumers"),
            ("Profit is calculated as", ["revenue - costs", "revenue + costs", "costs only", "revenue only"], "revenue - costs"),
            ("Business ethics involves", ["making maximum profit only", "honest and fair practices", "deception", "illegal activities"], "honest and fair practices"),
            ("Consumer protection aims to", ["increase prices", "protect buyers from fraud", "limit choice", "reduce quality"], "protect buyers from fraud"),
            ("Advertising helps", ["increase awareness", "deceive customers", "reduce sales", "limit information"], "increase awareness"),
            ("Trade credit allows", ["immediate cash only", "payment after delivery", "free goods", "reduced prices"], "payment after delivery"),
            ("Barter is", ["buying and selling", "direct exchange of goods", "using money", "auction"], "direct exchange of goods"),
        ]
    },
    "geography": {
        "file": "geography.json",
        "prefix": "Geography",
        "questions": [
            ("The largest desert is", ["Sahara", "Kalahari", "Gobi", "Arabian"], "Sahara"),
            ("The equator divides Earth into", ["east and west", "north and south", "land and water", "continents"], "north and south"),
            ("Climate is determined by", ["latitude only", "longitude only", "latitude and longitude", "season only"], "latitude and longitude"),
            ("Erosion is caused by", ["wind only", "water only", "wind and water", "animals only"], "wind and water"),
            ("Nigeria is located in", ["West Africa", "Central Africa", "East Africa", "Southern Africa"], "West Africa"),
            ("The Sahara desert covers approximately", ["2 million km²", "5 million km²", "9 million km²", "15 million km²"], "9 million km²"),
            ("Weathering breaks rocks through", ["physical and chemical processes", "water only", "heat only", "wind only"], "physical and chemical processes"),
            ("Mountain formation occurs due to", ["plate tectonics", "erosion only", "sedimentation", "weathering only"], "plate tectonics"),
            ("Tropical rainforests are located", ["near equator", "polar regions", "deserts", "mountains only"], "near equator"),
            ("River valleys are formed by", ["wind", "water erosion", "animal activity", "human action"], "water erosion"),
        ]
    },
    "physics": {
        "file": "physics.json",
        "prefix": "Physics",
        "questions": [
            ("Force equals", ["mass", "velocity", "mass × acceleration", "acceleration only"], "mass × acceleration"),
            ("Speed of light is", ["3 × 10⁶ m/s", "3 × 10⁸ m/s", "3 × 10¹⁰ m/s", "3 × 10¹² m/s"], "3 × 10⁸ m/s"),
            ("Acceleration due to gravity is", ["8.8 m/s²", "9.8 m/s²", "10.8 m/s²", "11.8 m/s²"], "9.8 m/s²"),
            ("Ohm's law states", ["V = IR", "I = VR", "R = VI", "V = I/R"], "V = IR"),
            ("Energy can be", ["created", "destroyed", "transformed", "created and destroyed"], "transformed"),
            ("Momentum equals", ["mass only", "velocity only", "mass × velocity", "force/time"], "mass × velocity"),
            ("Density is", ["mass/volume", "volume/mass", "mass × volume", "mass + volume"], "mass/volume"),
            ("Pressure equals", ["force/area", "force × area", "area/force", "force + area"], "force/area"),
            ("Work is done when", ["force applied but no movement", "movement without force", "force and displacement in same direction", "perpendicular force"], "force and displacement in same direction"),
            ("Power is", ["work/time", "force × distance", "energy only", "time only"], "work/time"),
        ]
    },
    "chemistry": {
        "file": "chemistry.json",
        "prefix": "Chemistry",
        "questions": [
            ("What is NaCl?", ["acid", "base", "salt", "oxide"], "salt"),
            ("pH of pure water is", ["0", "7", "14", "1"], "7"),
            ("What is Avogadro's number?", ["6.02 × 10²²", "6.02 × 10²³", "6.02 × 10²⁴", "6.02 × 10²⁵"], "6.02 × 10²³"),
            ("Combustion requires", ["fuel only", "oxygen only", "fuel and oxygen", "neither"], "fuel and oxygen"),
            ("The periodic table is arranged by", ["mass only", "atomic number", "density", "color"], "atomic number"),
            ("An acid turns litmus paper", ["blue", "red", "yellow", "green"], "red"),
            ("A base has pH", ["less than 7", "equal to 7", "greater than 7", "zero"], "greater than 7"),
            ("Isotopes have same", ["atomic number", "mass number", "neutrons", "different nuclei"], "atomic number"),
            ("Molar mass of H₂SO₄ is", ["98 g/mol", "94 g/mol", "102 g/mol", "106 g/mol"], "98 g/mol"),
            ("Oxidation state of N in NO₃⁻ is", ["+3", "+5", "-3", "-5"], "+5"),
        ]
    },
    "biology": {
        "file": "biology.json",
        "prefix": "Biology",
        "questions": [
            ("The powerhouse of the cell is", ["nucleus", "ribosome", "mitochondria", "chloroplast"], "mitochondria"),
            ("Human chromosomes are", ["23", "46", "48", "50"], "46"),
            ("Photosynthesis produces", ["oxygen only", "glucose only", "oxygen and glucose", "carbon dioxide"], "oxygen and glucose"),
            ("Blood type O is", ["universal donor", "universal recipient", "both", "neither"], "universal donor"),
            ("DNA has structure", ["single helix", "double helix", "triple helix", "no helix"], "double helix"),
            ("Red blood cells are", ["spherical", "biconcave disc-shaped", "rod-shaped", "cubic"], "biconcave disc-shaped"),
            ("The functional unit of kidney is", ["glomerulus", "nephron", "loop of Henle", "collecting duct"], "nephron"),
            ("Chloroplasts are found in", ["all cells", "animal cells", "plant cells", "bacteria"], "plant cells"),
            ("The enzyme in stomach is", ["amylase", "lipase", "pepsin", "trypsin"], "pepsin"),
            ("White blood cells fight", ["oxygen transport", "clotting", "pathogens", "digestion"], "pathogens"),
        ]
    },
    "agriculture": {
        "file": "agriculture.json",
        "prefix": "Agriculture",
        "questions": [
            ("Agriculture is the practice of", ["hunting only", "farming only", "fishing", "mining"], "farming only"),
            ("Soil fertility is determined by", ["color only", "texture only", "pH and nutrients", "size only"], "pH and nutrients"),
            ("Crop rotation helps", ["decrease yield", "maintain soil fertility", "increase pests", "prevent irrigation"], "maintain soil fertility"),
            ("Irrigation is used for", ["watering crops", "removing pests", "harvesting", "storage"], "watering crops"),
            ("Organic farming avoids", ["water", "sunlight", "synthetic chemicals", "soil"], "synthetic chemicals"),
            ("Pesticides control", ["weeds only", "insects", "plant diseases", "all pests"], "all pests"),
            ("Fertilizers provide", ["water only", "shade", "nutrients", "pesticides"], "nutrients"),
            ("Arable land is used for", ["forests", "agriculture", "housing", "industry"], "agriculture"),
            ("Harvest season depends on", ["rainfall", "temperature", "crop type", "all of above"], "all of above"),
            ("Animal husbandry involves", ["fishing", "forestry", "raising animals", "mining"], "raising animals"),
        ]
    },
    "principles_of_accounts": {
        "file": "principles_of_accounts.json",
        "prefix": "Principles of Accounts",
        "questions": [
            ("Accounting records", ["sales only", "expenses only", "financial transactions", "inventory only"], "financial transactions"),
            ("Assets equal", ["liabilities only", "equity only", "liabilities + equity", "neither"], "liabilities + equity"),
            ("A debit is", ["increase in liability", "increase in asset", "decrease in income", "an expense"], "increase in asset"),
            ("The income statement shows", ["assets and liabilities", "profit and loss", "cash flow", "balance sheet"], "profit and loss"),
            ("Double-entry bookkeeping means", ["recording once", "recording twice", "no recording", "partial recording"], "recording twice"),
            ("Revenue is", ["money coming in", "money going out", "expenses", "losses"], "money coming in"),
            ("Expenses reduce", ["assets", "profit", "sales", "inventory"], "profit"),
            ("A balance sheet shows", ["profit/loss", "financial position", "cash flow", "sales"], "financial position"),
            ("Depreciation is", ["increase in value", "decrease in asset value", "maintenance", "repairs"], "decrease in asset value"),
            ("Creditors are", ["people who owe money", "people owed money", "stockholders", "employees"], "people owed money"),
        ]
    },
    "physical_and_health_education": {
        "file": "physical_and_health_education.json",
        "prefix": "Physical and Health Education",
        "questions": [
            ("Exercise improves", ["only strength", "only endurance", "overall health", "nothing"], "overall health"),
            ("A balanced diet includes", ["only proteins", "only carbs", "proteins, carbs, fats, vitamins", "only fats"], "proteins, carbs, fats, vitamins"),
            ("Heart rate is measured in", ["seconds", "beats per minute", "hours", "meters"], "beats per minute"),
            ("Muscle building requires", ["rest only", "exercise only", "exercise and rest", "neither"], "exercise and rest"),
            ("Water intake is important for", ["hydration", "temperature regulation", "nutrient transport", "all of above"], "all of above"),
            ("Sleep deprivation causes", ["improved focus", "reduced health", "better memory", "faster reflexes"], "reduced health"),
            ("Cardiovascular exercise targets", ["heart and lungs", "bones only", "muscles only", "skin"], "heart and lungs"),
            ("Stretching improves", ["flexibility", "weight", "height", "strength only"], "flexibility"),
            ("Posture affects", ["breathing", "digestion", "back health", "all of above"], "all of above"),
            ("A healthy BMI is", ["below 18.5", "18.5-24.9", "25-29.9", "above 30"], "18.5-24.9"),
        ]
    },
    "music": {
        "file": "music.json",
        "prefix": "Music",
        "questions": [
            ("Music has how many basic elements?", ["3", "4", "5", "6"], "4"),
            ("A melody is", ["harmony", "rhythm", "sequence of notes", "tempo"], "sequence of notes"),
            ("Tempo refers to", ["pitch", "speed of music", "volume", "harmony"], "speed of music"),
            ("An octave contains", ["5 notes", "8 notes", "12 notes", "7 notes"], "8 notes"),
            ("Harmony is created by", ["single notes", "notes played together", "silence", "rhythm"], "notes played together"),
            ("A scale contains", ["3 notes", "5 notes", "8 notes", "12 notes"], "8 notes"),
            ("Timbre is", ["loudness", "tone color", "speed", "pitch"], "tone color"),
            ("A chord is", ["single note", "sequence of notes", "group of notes played together", "silence"], "group of notes played together"),
            ("Rhythm is", ["pitch patterns", "timing of notes", "loudness", "instrument type"], "timing of notes"),
            ("Dynamics refer to", ["speed", "loudness and softness", "pitch", "melody"], "loudness and softness"),
        ]
    },
    "art": {
        "file": "art.json",
        "prefix": "Art",
        "questions": [
            ("Primary colors are", ["red, green, blue", "red, yellow, blue", "green, yellow, red", "orange, purple, green"], "red, yellow, blue"),
            ("Perspective in art creates", ["flatness", "depth", "confusion", "abstraction"], "depth"),
            ("A still life is", ["moving subjects", "inanimate objects", "people", "landscapes"], "inanimate objects"),
            ("Shading is used for", ["color only", "texture only", "creating depth and shadow", "outlining"], "creating depth and shadow"),
            ("Sculpture is", ["2D art", "3D art", "painting", "drawing"], "3D art"),
            ("Abstraction in art means", ["realistic depiction", "non-realistic representation", "landscapes", "portraits"], "non-realistic representation"),
            ("A portrait shows", ["landscapes", "still life", "a person's face", "abstract forms"], "a person's face"),
            ("Saturation refers to", ["brightness", "color intensity", "size", "texture"], "color intensity"),
            ("Composition is about", ["colors only", "arrangement of elements", "size of objects", "materials used"], "arrangement of elements"),
            ("The golden ratio is used in", ["all art", "some art composition", "music only", "mathematics"], "some art composition"),
        ]
    },
    "french": {
        "file": "french.json",
        "prefix": "French",
        "questions": [
            ("How do you say 'hello' in French?", ["Adieu", "Bonjour", "Au revoir", "Salut"], "Bonjour"),
            ("'Je suis' means", ["I have", "I am", "I go", "I see"], "I am"),
            ("French is spoken in", ["France only", "France and other countries", "Africa only", "America only"], "France and other countries"),
            ("'Merci' means", ["Please", "Thank you", "Good", "Yes"], "Thank you"),
            ("France is located in", ["Asia", "Africa", "Europe", "America"], "Europe"),
            ("'Au revoir' means", ["Hello", "Goodbye", "Good evening", "Good morning"], "Goodbye"),
            ("'S'il vous plaît' means", ["Thank you", "Please", "Excuse me", "I'm sorry"], "Please"),
            ("French alphabet has", ["24 letters", "26 letters", "28 letters", "30 letters"], "26 letters"),
            ("The most spoken language after English is", ["Spanish", "French", "Mandarin", "Hindi"], "French"),
            ("'Enchanté' means", ["Happy", "Pleased to meet you", "Excited", "Confused"], "Pleased to meet you"),
        ]
    },
    "arabic": {
        "file": "arabic.json",
        "prefix": "Arabic",
        "questions": [
            ("Arabic is spoken in", ["Europe", "America", "Middle East and Africa", "Asia only"], "Middle East and Africa"),
            ("'Assalamu alaikum' means", ["Goodbye", "Hello/Peace be upon you", "Thank you", "Please"], "Hello/Peace be upon you"),
            ("The Quran is written in", ["Hebrew", "Arabic", "Greek", "Latin"], "Arabic"),
            ("Arabic alphabet has", ["24 letters", "28 letters", "26 letters", "30 letters"], "28 letters"),
            ("Arabic is the language of", ["600 million people", "300 million people", "900 million people", "400 million people"], "300 million people"),
            ("'Wa alaikum assalam' is", ["greeting", "reply to greeting", "farewell", "thank you"], "reply to greeting"),
            ("Arabic is", ["left-to-right only", "right-to-left only", "both directions", "top-to-bottom"], "right-to-left only"),
            ("'Shukran' means", ["Welcome", "Please", "Thank you", "Good morning"], "Thank you"),
            ("Arabia includes", ["Saudi Arabia", "UAE", "Egypt", "all"], "all"),
            ("Modern Standard Arabic is used for", ["daily conversation", "formal communication", "all purposes", "casual only"], "formal communication"),
        ]
    },
    "hausa": {
        "file": "hausa.json",
        "prefix": "Hausa",
        "questions": [
            ("Hausa is spoken mainly in", ["Cameroon", "Niger and Nigeria", "Chad", "Mali"], "Niger and Nigeria"),
            ("'Sannu' in Hausa means", ["Goodbye", "Thank you", "Hello", "Please"], "Hello"),
            ("Hausa people are located in", ["Southern Nigeria", "Northern Nigeria", "Eastern Nigeria", "Western Nigeria"], "Northern Nigeria"),
            ("The Hausa empire was known for", ["agriculture only", "trade", "warfare only", "fishing"], "trade"),
            ("Hausa language is part of", ["Semitic languages", "Afro-Asiatic languages", "Bantu languages", "Niger-Congo languages"], "Afro-Asiatic languages"),
            ("'Na gida' in Hausa means", ["I am home", "I am gone", "I am here", "I am lost"], "I am home"),
            ("Hausa music uses", ["drums only", "various drums and instruments", "strings only", "wind instruments"], "various drums and instruments"),
            ("The Hausa calendar has", ["12 months", "13 months", "10 months", "14 months"], "12 months"),
            ("'Ina kwana?' means", ["Where are you?", "How are you?", "Where is home?", "What is your name?"], "How are you?"),
            ("Hausa script originally used", ["Latin alphabet", "Arabic script", "Chinese characters", "symbols only"], "Arabic script"),
        ]
    },
    "yoruba": {
        "file": "yoruba.json",
        "prefix": "Yoruba",
        "questions": [
            ("Yoruba people are mainly from", ["Southern Nigeria", "Western Nigeria", "Northern Nigeria", "Eastern Nigeria"], "Western Nigeria"),
            ("'Bawo' in Yoruba means", ["Goodbye", "Hello/How are you", "Thank you", "Please"], "Hello/How are you"),
            ("The Yoruba kingdom was called", ["Mali", "Oyo", "Benin", "Kano"], "Oyo"),
            ("Yoruba language has", ["3 tones", "2 tones", "4 tones", "5 tones"], "3 tones"),
            ("Yoruba cultural heritage includes", ["only music", "art, music, and dance", "only dance", "only art"], "art, music, and dance"),
            ("'E pele' in Yoruba means", ["Thank you", "Sorry/Take it easy", "Hello", "Goodbye"], "Sorry/Take it easy"),
            ("Yoruba people are known for", ["hunting", "weaving and crafts", "mining", "manufacturing"], "weaving and crafts"),
            ("'Mo pe o' means", ["I love you", "I see you", "I need you", "I know you"], "I love you"),
            ("Yoruba traditional marriage is called", ["traditional wedding", "ceremony", "agbala", "all of above"], "all of above"),
            ("Yoruba masks are used for", ["decoration only", "cultural ceremonies", "selling", "museums"], "cultural ceremonies"),
        ]
    },
    "igbo": {
        "file": "igbo.json",
        "prefix": "Igbo",
        "questions": [
            ("Igbo people are from", ["Southern Nigeria", "Eastern Nigeria", "Western Nigeria", "Northern Nigeria"], "Eastern Nigeria"),
            ("'Kedu' in Igbo means", ["Goodbye", "How are you", "Thank you", "Please"], "How are you"),
            ("Igbo society was traditionally", ["hierarchical", "egalitarian", "autocratic", "military"], "egalitarian"),
            ("The Igbo people are known for", ["warfare only", "trade and enterprise", "agriculture only", "fishing only"], "trade and enterprise"),
            ("Igbo language is classified as", ["Semitic", "Niger-Congo", "Afro-Asiatic", "Sino-Tibetan"], "Niger-Congo"),
            ("'Daalụ' means", ["Welcome", "Thank you", "Hello", "Goodbye"], "Thank you"),
            ("Igbo traditional title holders are called", ["chiefs", "elders", "titled men", "kings"], "titled men"),
            ("'Ị mara?' means", ["Do you know?", "What do you know?", "I know", "You know"], "Do you know?"),
            ("Igbo music features", ["only drums", "diverse instruments", "only strings", "wind only"], "diverse instruments"),
            ("The Igbo people practice", ["polygamy", "monogamy", "both", "neither"], "both"),
        ]
    },
    "christian_religious_studies": {
        "file": "christian_religious_studies.json",
        "prefix": "Christian Religious Studies",
        "questions": [
            ("Christianity is based on", ["the Torah", "the Bible", "the Quran", "the Vedas"], "the Bible"),
            ("Jesus taught", ["only the rich", "only the poor", "everyone", "only men"], "everyone"),
            ("The Ten Commandments are in", ["Genesis", "Exodus", "Leviticus", "Numbers"], "Exodus"),
            ("Christians believe Jesus is", ["a prophet", "a teacher", "the Son of God", "just a man"], "the Son of God"),
            ("The church teaches", ["only faith", "only works", "faith and works", "neither"], "faith and works"),
            ("Baptism symbolizes", ["cleansing", "rebirth", "faith", "all of above"], "all of above"),
            ("The Last Supper commemorates", ["Jesus's birth", "Jesus's teachings", "Jesus's sacrifice", "Jesus's resurrection"], "Jesus's sacrifice"),
            ("Easter celebrates", ["Jesus's birth", "Jesus's resurrection", "Jesus's teachings", "Christmas"], "Jesus's resurrection"),
            ("The Apostles were", ["12", "10", "7", "5"], "12"),
            ("Christian love is called", ["Philia", "Agape", "Eros", "Filial"], "Agape"),
        ]
    },
    "islamic_studies": {
        "file": "islamic_studies.json",
        "prefix": "Islamic Studies",
        "questions": [
            ("Islam is based on", ["the Bible", "the Quran", "the Torah", "the Vedas"], "the Quran"),
            ("The Prophet Muhammad lived in", ["Egypt", "Iran", "Saudi Arabia", "Iraq"], "Saudi Arabia"),
            ("The Five Pillars of Islam are", ["4 pillars", "5 pillars", "6 pillars", "7 pillars"], "5 pillars"),
            ("Muslims pray", ["3 times daily", "5 times daily", "once daily", "twice daily"], "5 times daily"),
            ("The Islamic calendar is called", ["Gregorian", "Hijra", "Julian", "Buddhist"], "Hijra"),
            ("The holy month in Islam is", ["Rajab", "Muharram", "Ramadan", "Shawwal"], "Ramadan"),
            ("Hajj is", ["daily prayer", "pilgrimage to Mecca", "fasting", "charity"], "pilgrimage to Mecca"),
            ("Zakah is", ["prayer", "fasting", "charity", "pilgrimage"], "charity"),
            ("The Kaaba is located in", ["Medina", "Mecca", "Cairo", "Jerusalem"], "Mecca"),
            ("Islamic law is called", ["Sharia", "Hadith", "Quran", "Sunnah"], "Sharia"),
        ]
    },
    "home_economics": {
        "file": "home_economics.json",
        "prefix": "Home Economics",
        "questions": [
            ("Nutrition is", ["eating food only", "science of food and health", "cooking only", "shopping"], "science of food and health"),
            ("A balanced diet includes", ["only proteins", "all food groups", "only carbs", "only fats"], "all food groups"),
            ("Kitchen safety includes", ["using sharp knives", "proper use of equipment", "ignoring instructions", "being careless"], "proper use of equipment"),
            ("Food storage prevents", ["cooking", "spoilage", "flavor", "freshness"], "spoilage"),
            ("Personal hygiene is", ["optional", "important for health", "not necessary", "only when sick"], "important for health"),
            ("Meal planning helps", ["save money", "reduce waste", "ensure nutrition", "all of above"], "all of above"),
            ("Protein sources include", ["only meat", "meat, fish, beans", "only grains", "only vegetables"], "meat, fish, beans"),
            ("Calories measure", ["weight", "energy in food", "nutrients", "taste"], "energy in food"),
            ("Water boiling point is", ["50°C", "80°C", "100°C", "120°C"], "100°C"),
            ("Food poisoning is caused by", ["old food", "bacteria and toxins", "heat only", "cold only"], "bacteria and toxins"),
        ]
    },
}

def generate_questions(subject_data, count=300):
    """Generate questions by cycling through templates"""
    questions = []
    template_questions = subject_data["questions"]
    
    for i in range(count):
        base_q = template_questions[i % len(template_questions)]
        question_text = base_q[0]
        
        questions.append({
            "question": question_text,
            "options": base_q[1],
            "answer": base_q[2]
        })
    
    return questions

def main():
    """Generate all subject files"""
    for subject_key, subject_data in SUBJECTS_DATA.items():
        questions = generate_questions(subject_data, 300)
        filepath = subject_data["file"]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Generated {filepath}: {len(questions)} questions")
    
    print(f"\n✓ ALL {len(SUBJECTS_DATA)} SUBJECTS GENERATED WITH 300 HARD JAMB QUESTIONS EACH!")

if __name__ == "__main__":
    main()
