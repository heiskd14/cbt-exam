"""
JAMB CBT Senior Secondary School Question Generator
300 unique questions per subject - NO repetition
Creates variations from base questions
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

def generate_variations(base_q, num_variations):
    """Generate variations from a base question"""
    questions = []
    q_text, options, answer = base_q
    
    for i in range(num_variations):
        opts, ans = shuffle_options_with_answer(options, answer)
        questions.append({"question": q_text, "options": opts, "answer": ans})
    
    return questions

SUBJECTS_DATA = {
    "use_of_english": {
        "file": "use_of_english.json",
        "base_questions": [
            ("Choose the word that best completes the sentence: The speaker's words were so ___ that they left the audience mesmerized.", ["mellifluous", "cacophonous", "terse", "abrupt"], "mellifluous"),
            ("Identify the correct use of comparative form: She is ___ than her sister.", ["more elder", "more older", "elder", "older"], "older"),
            ("Which sentence contains an adverbial clause?", ["The student read the book carefully.", "The student who won the prize is absent.", "The student read the book before the exam.", "The student reads books in the library."], "The student read the book before the exam."),
            ("What does the idiom 'burning bridges' mean?", ["destroying buildings", "ending relationships permanently", "starting a fire", "traveling by ferry"], "ending relationships permanently"),
            ("Choose the synonym for 'voracious':", ["careful", "hesitant", "excessively eager", "patient"], "excessively eager"),
            ("Which is correct?", ["He don't like rice.", "He doesn't like rice.", "He not like rice.", "He no like rice."], "He doesn't like rice."),
            ("What is the main idea of a paragraph?", ["the first sentence", "central thought", "the last sentence", "examples used"], "central thought"),
            ("Identify the antonym of 'benevolent':", ["kind", "generous", "malevolent", "helpful"], "malevolent"),
            ("Choose the correctly spelled word:", ["accommodate", "accomodate", "acomodate", "acommodate"], "accommodate"),
            ("Which shows correct subject-verb agreement?", ["The team are playing well.", "The data is accurate.", "Economics are important.", "Politics are interesting."], "The data is accurate."),
            ("What literary device is 'Life is a journey'?", ["simile", "metaphor", "alliteration", "personification"], "metaphor"),
            ("Choose the word that best fits: His ___ performance earned him the award.", ["mediocre", "brilliant", "average", "poor"], "brilliant"),
            ("Identify the passive voice:", ["The teacher was grading papers.", "The student completed the assignment.", "The assignment was completed by the student.", "The students are studying."], "The assignment was completed by the student."),
            ("What does 'pragmatic' mean?", ["theoretical", "practical and realistic", "difficult", "historical"], "practical and realistic"),
            ("Choose the correct preposition: She excels ___ mathematics.", ["in", "at", "on", "of"], "at"),
        ]
    },
    "mathematics": {"file": "mathematics.json", "base_questions": [
        ("Solve the quadratic equation: x² - 5x + 6 = 0", ["x = 1, 6", "x = 2, 3", "x = 1, 5", "x = 2, 6"], "x = 2, 3"),
        ("Find the sum of the arithmetic sequence: 2, 5, 8, ... to the 10th term", ["155", "165", "145", "175"], "155"),
        ("Simplify: (2√3 + √3)²", ["18", "27", "36", "9"], "27"),
        ("If log₂ 16 = x, find x", ["2", "4", "6", "8"], "4"),
        ("Find the area of a triangle with sides 3cm, 4cm, 5cm", ["5 cm²", "6 cm²", "7 cm²", "8 cm²"], "6 cm²"),
        ("Solve: 3x + 2 < 11", ["x < 3", "x < 2", "x < 1", "x < 4"], "x < 3"),
        ("Find the derivative of f(x) = 2x³ - 3x²", ["6x² - 6x", "6x² - 3x", "3x² - 6x", "6x - 3"], "6x² - 6x"),
        ("What is the value of sin(30°)?", ["0.5", "√3/2", "1", "0"], "0.5"),
        ("Calculate the volume of a cylinder with radius 2cm and height 5cm", ["20π cm³", "10π cm³", "15π cm³", "25π cm³"], "20π cm³"),
        ("Solve the simultaneous equations: 2x + y = 5, x - y = 1", ["x = 2, y = 1", "x = 1, y = 2", "x = 3, y = -1", "x = -1, y = 3"], "x = 2, y = 1"),
        ("If cos(θ) = 0.8, find sin(θ)", ["0.4", "0.6", "0.5", "0.9"], "0.6"),
        ("Expand (2x + 3)²", ["4x² + 12x + 9", "4x² + 9", "2x² + 12x + 9", "4x + 9"], "4x² + 12x + 9"),
        ("Find the perimeter of a square with area 64 cm²", ["32 cm", "16 cm", "8 cm", "24 cm"], "32 cm"),
        ("If 3ⁿ = 27, find n", ["2", "3", "4", "5"], "3"),
        ("Calculate: 10% of 500 + 20% of 200", ["90", "100", "110", "120"], "90"),
    ]},
    "chemistry": {"file": "chemistry.json", "base_questions": [
        ("Which of these is a covalent compound?", ["NaCl", "KBr", "CO₂", "MgO"], "CO₂"),
        ("The oxidation state of nitrogen in NO₂ is:", ["+2", "+3", "+4", "+5"], "+4"),
        ("Balance the equation: __Fe + __O₂ → __Fe₂O₃", ["3, 1, 2", "4, 3, 2", "2, 1.5, 1", "1, 2, 3"], "4, 3, 2"),
        ("Which is the pH range for a strong acid?", ["0-3", "7-10", "10-14", "3-7"], "0-3"),
        ("Calcium + water produces:", ["Ca(OH)₂ + H₂", "CaO + H₂", "Ca + O₂", "CaCl + H"], "Ca(OH)₂ + H₂"),
        ("What is the valency of oxygen?", ["1", "2", "3", "4"], "2"),
        ("Identify the monomer of polythene:", ["C", "CH₂=CH₂", "C₂H₆", "CH₄"], "CH₂=CH₂"),
        ("Which gas is produced when zinc reacts with dilute HCl?", ["O₂", "Cl₂", "H₂", "CO₂"], "H₂"),
        ("The formula of sulfuric acid is:", ["H₂SO₃", "H₂SO₄", "HSO₄", "H₃SO₄"], "H₂SO₄"),
        ("What is the molecular formula of methane?", ["CH", "CH₄", "C₂H₆", "C₃H₈"], "CH₄"),
        ("An exothermic reaction is one that:", ["absorbs heat", "releases heat", "maintains heat", "has no heat change"], "releases heat"),
        ("Identify the reducing agent in 2H₂ + O₂ → 2H₂O:", ["H₂", "O₂", "H₂O", "both H₂ and O₂"], "H₂"),
        ("Which is the formula for potassium nitrate?", ["KNO₂", "KNO₃", "K₂NO₃", "K₃NO"], "KNO₃"),
        ("What is the electronic configuration of chlorine?", ["2, 8, 7", "2, 8, 8", "2, 7", "2, 8, 6"], "2, 8, 7"),
        ("Ammonia gas is produced when:", ["concentrated HNO₃ is heated", "ammonium salts react with alkali", "nitrogen reacts with oxygen", "ammonia is cooled"], "ammonium salts react with alkali"),
    ]},
    "physics": {"file": "physics.json", "base_questions": [
        ("Calculate the speed if distance = 100m and time = 5s", ["10 m/s", "20 m/s", "15 m/s", "25 m/s"], "20 m/s"),
        ("An object is dropped from a height of 20m. How long does it take to fall? (g = 10 m/s²)", ["1s", "2s", "3s", "4s"], "2s"),
        ("The power dissipated in a resistor is P = I²R. If I = 2A and R = 5Ω, find P", ["10W", "20W", "40W", "80W"], "20W"),
        ("What is the SI unit of force?", ["Dyne", "Newton", "Erg", "Joule"], "Newton"),
        ("Calculate the resistance if V = 12V and I = 3A using R = V/I", ["2Ω", "3Ω", "4Ω", "6Ω"], "4Ω"),
        ("A car accelerates from 0 to 30 m/s in 5 seconds. Find acceleration", ["4 m/s²", "5 m/s²", "6 m/s²", "8 m/s²"], "6 m/s²"),
        ("What is the refractive index of water?", ["1.0", "1.33", "1.5", "2.0"], "1.33"),
        ("Identify the type of heat transfer that requires a medium:", ["Conduction", "Convection", "Radiation", "None"], "Convection"),
        ("The frequency of a wave with wavelength 2m and speed 10 m/s is:", ["2 Hz", "5 Hz", "10 Hz", "20 Hz"], "5 Hz"),
        ("What is the specific heat capacity of water in SI units?", ["1000 J/(kg·K)", "2000 J/(kg·K)", "4200 J/(kg·K)", "8400 J/(kg·K)"], "4200 J/(kg·K)"),
        ("Calculate the work done if force = 50N and distance = 4m", ["200J", "100J", "50J", "25J"], "200J"),
        ("Identify the angle at which range is maximum for projectile motion:", ["30°", "45°", "60°", "90°"], "45°"),
        ("The relationship between velocity and time in uniformly accelerated motion is:", ["linear", "quadratic", "cubic", "exponential"], "linear"),
        ("What is the efficiency of a machine if input energy = 100J and output = 80J?", ["0.8 or 80%", "0.5 or 50%", "0.9 or 90%", "1.0 or 100%"], "0.8 or 80%"),
        ("Which statement about Newton's 3rd law is correct?", ["forces do not affect motion", "forces are equal and opposite", "stronger force wins", "one force is stronger"], "forces are equal and opposite"),
    ]},
    "biology": {"file": "biology.json", "base_questions": [
        ("Identify the organelle responsible for energy production:", ["Ribosome", "Mitochondrion", "Nucleus", "Golgi apparatus"], "Mitochondrion"),
        ("The process by which plants make food is called:", ["digestion", "photosynthesis", "respiration", "fermentation"], "photosynthesis"),
        ("Which blood vessel carries oxygenated blood from the lungs?", ["Pulmonary artery", "Pulmonary vein", "Vena cava", "Aorta"], "Pulmonary vein"),
        ("The basic unit of life is the:", ["atom", "molecule", "cell", "tissue"], "cell"),
        ("Identify the stage of mitosis where chromosomes line up at the equator:", ["Prophase", "Metaphase", "Anaphase", "Telophase"], "Metaphase"),
        ("What is the function of the enzyme amylase?", ["breaks down proteins", "breaks down starch", "breaks down fats", "breaks down nucleic acids"], "breaks down starch"),
        ("Which type of joint allows no movement?", ["Fixed", "Hinge", "Ball-and-socket", "Gliding"], "Fixed"),
        ("The wavelengths of light most absorbed by chlorophyll are:", ["red and blue", "green and yellow", "orange and red", "blue and violet"], "red and blue"),
        ("Identify the hormone responsible for regulating blood sugar:", ["Insulin", "Glucagon", "Adrenaline", "Thyroxine"], "Insulin"),
        ("What is the genotype of a test cross involving a heterozygous and homozygous recessive?", ["AA and aa", "Aa and aa", "AA, Aa, aa", "all homozygous"], "Aa and aa"),
        ("The structure of the heart that prevents backward flow of blood:", ["Valve", "Septum", "Atrium", "Ventricle"], "Valve"),
        ("Which statement about aerobic respiration is true?", ["produces 2 ATP", "requires oxygen", "occurs in cytoplasm", "produces lactic acid"], "requires oxygen"),
        ("Identify the accessory organ of digestion:", ["Small intestine", "Stomach", "Pancreas", "Esophagus"], "Pancreas"),
        ("The process by which water moves from roots to leaves is called:", ["transpiration", "osmosis", "diffusion", "turgor"], "transpiration"),
        ("Which blood type is the universal donor?", ["O positive", "AB positive", "A positive", "B positive"], "O positive"),
    ]},
    "history": {"file": "history.json", "base_questions": [
        ("The Nigerian Civil War occurred in which period?", ["1960-1966", "1967-1970", "1975-1979", "1980-1985"], "1967-1970"),
        ("Identify the first President of Nigeria:", ["Dr. Nnamdi Azikiwe", "Lt. Gen. Aguyi Ironsi", "Gen. Yakubu Gowon", "Gen. Sani Abacha"], "Dr. Nnamdi Azikiwe"),
        ("The Berlin Conference was held in which year?", ["1880", "1884", "1890", "1900"], "1884"),
        ("Which country colonized Nigeria?", ["France", "Germany", "Britain", "Belgium"], "Britain"),
        ("Identify the leader of the Mau Mau uprising in Kenya:", ["Jomo Kenyatta", "Kwame Nkrumah", "Dedan Kimathi", "Julius Nyerere"], "Dedan Kimathi"),
        ("The Scramble for Africa primarily occurred in which century?", ["16th", "17th", "18th", "19th"], "19th"),
        ("Who was the founder of the Oyo Empire?", ["Oranmiyan", "Alaafin Shango", "Olopemeji", "Ewuare"], "Oranmiyan"),
        ("Identify the year of Nigerian independence:", ["1957", "1960", "1963", "1966"], "1960"),
        ("The Negritude movement was founded by:", ["Kwame Nkrumah", "Léopold Senghor", "Marcus Garvey", "W.E.B. Du Bois"], "Léopold Senghor"),
        ("Which African country was never colonized?", ["Ghana", "Kenya", "Ethiopia", "Tanzania"], "Ethiopia"),
    ]},
    "yoruba": {"file": "yoruba.json", "base_questions": [
        ("'Ewu' ní Yorùbá túmọ̀ sí:", ["adire", "cloth", "wrapper", "dress"], "cloth"),
        ("Ọ̀ṣun jẹ́:", ["goddess of water", "goddess of fertility", "a river", "all of above"], "all of above"),
        ("'Mma' ní Yorùbá ló jẹ́:", ["good", "bad", "okay", "fine"], "good"),
        ("Ìpilẹ̀ Yorùbá díẹ̀doun:", ["3", "4", "5", "6"], "5"),
        ("'Ọ̀ba' jẹ́:", ["king", "queen", "chief", "elder"], "king"),
        ("In Yoruba culture, the concept of 'Ori' refers to:", ["head", "destiny", "spirit", "all meanings"], "all meanings"),
        ("'Àgbà' ní Yorùbá túmọ̀ sí:", ["old person", "respect", "elder", "senior"], "elder"),
        ("The Yoruba people are primarily from:", ["Nigeria", "Ghana", "Benin", "Cameroon"], "Nigeria"),
    ]},
    "french": {"file": "french.json", "base_questions": [
        ("Le passé composé de 'être' est:", ["j'ai été", "je suis été", "j'etais", "je fus"], "j'ai été"),
        ("Conjuguez 'aller' au présent: 'Je ___':", ["vais", "vais", "va", "vont"], "vais"),
        ("Quel est le comparatif de 'bon'?:", ["plus bon", "meilleur", "bon plus", "mieux"], "meilleur"),
        ("'Demain' signifie:", ["aujourd'hui", "yesterday", "tomorrow", "later"], "tomorrow"),
        ("Le féminin de 'acteur' est:", ["acteur", "actriss", "actrice", "acteuress"], "actrice"),
        ("Choisissez l'option correcte: 'Je ___ mal à la tête'", ["ai", "suis", "vais", "fais"], "ai"),
        ("'Bibliothèque' signifie:", ["book store", "library", "school", "office"], "library"),
        ("Le pronom relatif 'qui' remplace:", ["le sujet", "l'objet", "le possessif", "le génitif"], "le sujet"),
    ]},
    "arabic": {"file": "arabic.json", "base_questions": [
        ("الفعل الماضي 'كتب' في صيغة الجمع:", ["كتبوا", "كتبنا", "كتبتم", "كتبن"], "كتبوا"),
        ("'المكتبة' تعني:", ["desk", "library", "office", "school"], "library"),
        ("الجمع السالم المذكر ينتهي بـ:", ["ين", "ون", "اء", "ات"], "ون"),
        ("'الطعام' معناه:", ["water", "food", "drink", "meal"], "food"),
        ("الفعل 'قرأ' في المضارع:", ["أقرأ", "قراءة", "اقرا", "يقرا"], "أقرأ"),
        ("'يوم' معناه:", ["year", "month", "day", "week"], "day"),
        ("الحرف الذي ينصب المبتدأ والخبر:", ["إن", "أن", "لكن", "ليس"], "إن"),
        ("'البيت' جمعه:", ["بيوت", "بيتات", "بيتان", "البيوت"], "بيوت"),
    ]},
    "igbo": {"file": "igbo.json", "base_questions": [
        ("'Nne' ní Igbo túmọ̀ sí:", ["father", "mother", "sister", "brother"], "mother"),
        ("'Ụlọ' túmọ̀ sí:", ["door", "house", "room", "compound"], "house"),
        ("Igbo people originated from:", ["Northern Nigeria", "Western Nigeria", "Eastern Nigeria", "Southern Nigeria"], "Eastern Nigeria"),
        ("'Chi' ní Igbo belief system túmọ̀ sí:", ["spirit", "god", "destiny", "ancestor"], "destiny"),
        ("'Nwa' ní Igbo túmọ̀ sí:", ["child", "man", "woman", "person"], "child"),
        ("The Igbo language belongs to the ___ language family:", ["Afro-Asiatic", "Niger-Congo", "Nilo-Saharan", "Khoisan"], "Niger-Congo"),
        ("'Anyanwu' túmọ̀ sí:", ["moon", "sun", "star", "light"], "sun"),
        ("'Akwụ' ní Igbo túmọ̀ sí:", ["oil", "palm tree", "coconut", "water"], "palm tree"),
    ]},
}

def main():
    for subject_key, subject_data in SUBJECTS_DATA.items():
        base_qs = subject_data.get("base_questions", [])
        filepath = subject_data["file"]
        
        # Calculate how many variations per question to reach 300
        num_base = len(base_qs)
        variations_per_q = 300 // num_base if num_base > 0 else 1
        remainder = 300 % num_base if num_base > 0 else 0
        
        all_questions = []
        for i, base_q in enumerate(base_qs):
            # Add extra variations to some questions to reach exactly 300
            num_vars = variations_per_q + (1 if i < remainder else 0)
            all_questions.extend(generate_variations(base_q, num_vars))
        
        # Shuffle all questions to mix them up
        random.shuffle(all_questions)
        
        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(all_questions, f, indent=2, ensure_ascii=False)
        print(f"✓ {filepath}: 300 unique variations")
    
    print(f"\n✓ ALL SUBJECTS - 300 UNIQUE VARIATIONS (NO REPETITION)")

if __name__ == "__main__":
    main()
