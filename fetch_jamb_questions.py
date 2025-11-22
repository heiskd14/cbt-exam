import requests
import json
import time

def fetch_jamb_questions(subject, num_questions=30):
    """Fetch JAMB questions from GitHub API repository"""
    
    # Using the GitHub raw content for JAMB questions
    subject_map = {
        "english": "english",
        "mathematics": "mathematics",
        "chemistry": "chemistry",
        "physics": "physics",
        "biology": "biology"
    }
    
    questions = []
    
    try:
        # Try multiple sources for better coverage
        urls = [
            f"https://raw.githubusercontent.com/Japhethca/past-questions-api/main/data/{subject_map.get(subject, subject)}.json",
            f"https://raw.githubusercontent.com/ayshajamjam/Questionnaire-API/main/{subject_map.get(subject, subject)}.json",
        ]
        
        for url in urls:
            try:
                print(f"Trying to fetch from: {url}")
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    if isinstance(data, list):
                        questions = data[:num_questions]
                        print(f"✓ Successfully fetched {len(questions)} {subject} questions")
                        return format_questions(questions, subject)
                    elif isinstance(data, dict) and 'questions' in data:
                        questions = data['questions'][:num_questions]
                        print(f"✓ Successfully fetched {len(questions)} {subject} questions")
                        return format_questions(questions, subject)
            except Exception as e:
                print(f"  Failed: {e}")
                continue
        
    except Exception as e:
        print(f"Error fetching from API: {e}")
    
    # If API fails, return generated sample questions
    print(f"✗ Could not fetch from APIs, generating sample {subject} questions...")
    return generate_sample_questions(subject, num_questions)

def format_questions(raw_questions, subject):
    """Convert API format to our app format"""
    formatted = []
    
    for q in raw_questions:
        try:
            # Handle different API response formats
            if isinstance(q, dict):
                question_text = q.get('question') or q.get('q') or ""
                
                # Get options - handle multiple formats
                options = []
                if 'options' in q:
                    options = q['options']
                elif all(key in q for key in ['a', 'b', 'c', 'd']):
                    options = [q['a'], q['b'], q['c'], q['d']]
                elif all(key in q for key in ['option_a', 'option_b', 'option_c', 'option_d']):
                    options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
                else:
                    continue
                
                # Get answer
                answer = q.get('answer') or q.get('ans') or ""
                
                # Normalize answer format
                if isinstance(answer, str):
                    answer = answer.upper().strip()
                    if answer in ['A', 'B', 'C', 'D']:
                        answer = options[ord(answer) - ord('A')] if ord(answer) - ord('A') < len(options) else answer
                    elif answer in ['0', '1', '2', '3']:
                        idx = int(answer)
                        if idx < len(options):
                            answer = options[idx]
                
                formatted.append({
                    "question": question_text,
                    "options": options,
                    "answer": answer
                })
        except Exception as e:
            print(f"  Error formatting question: {e}")
            continue
    
    return formatted

def generate_sample_questions(subject, count=30):
    """Generate sample questions for each subject"""
    
    sample_questions = {
        "english": [
            {"question": "Which of the following is the correct meaning of 'prudent'?", 
             "options": ["Careless", "Wise and careful", "Wasteful", "Ignorant"], 
             "answer": "Wise and careful"},
            {"question": "The phrasal verb 'put off' means?", 
             "options": ["To extinguish", "To postpone", "To annoy", "To remove"], 
             "answer": "To postpone"},
            {"question": "Identify the synonym for 'benevolent'", 
             "options": ["Cruel", "Kind", "Strict", "Silent"], 
             "answer": "Kind"},
            {"question": "In the sentence 'The student studies hard', what is the subject?", 
             "options": ["studies", "hard", "The student", "The"], 
             "answer": "The student"},
            {"question": "What is the past tense of 'begin'?", 
             "options": ["begins", "began", "beginning", "begun"], 
             "answer": "began"},
        ],
        "mathematics": [
            {"question": "What is 15 + 27?", 
             "options": ["40", "42", "41", "43"], 
             "answer": "42"},
            {"question": "If x + 5 = 12, what is x?", 
             "options": ["6", "7", "8", "9"], 
             "answer": "7"},
            {"question": "What is 20% of 150?", 
             "options": ["20", "30", "40", "50"], 
             "answer": "30"},
            {"question": "If a = 3 and b = 4, what is a² + b²?", 
             "options": ["24", "25", "26", "27"], 
             "answer": "25"},
            {"question": "What is the area of a square with side 5cm?", 
             "options": ["10 cm²", "20 cm²", "25 cm²", "30 cm²"], 
             "answer": "25 cm²"},
        ],
        "chemistry": [
            {"question": "What is the chemical formula for table salt?", 
             "options": ["NaCl", "KCl", "CaCl2", "MgCl2"], 
             "answer": "NaCl"},
            {"question": "Which gas is essential for respiration?", 
             "options": ["Nitrogen", "Oxygen", "Carbon dioxide", "Helium"], 
             "answer": "Oxygen"},
            {"question": "What is the atomic number of Carbon?", 
             "options": ["4", "6", "8", "12"], 
             "answer": "6"},
            {"question": "What type of bond exists between H and O in water?", 
             "options": ["Ionic", "Covalent", "Metallic", "Hydrogen"], 
             "answer": "Covalent"},
            {"question": "Which of the following is an element?", 
             "options": ["Water", "Salt", "Iron", "Soil"], 
             "answer": "Iron"},
        ],
        "physics": [
            {"question": "What is the SI unit of force?", 
             "options": ["Watt", "Newton", "Joule", "Pascal"], 
             "answer": "Newton"},
            {"question": "At what temperature does water boil at sea level?", 
             "options": ["90°C", "100°C", "110°C", "120°C"], 
             "answer": "100°C"},
            {"question": "What is the speed of light in vacuum?", 
             "options": ["3 × 10⁸ m/s", "3 × 10⁶ m/s", "3 × 10¹⁰ m/s", "3 × 10⁵ m/s"], 
             "answer": "3 × 10⁸ m/s"},
            {"question": "Which of the following is a scalar quantity?", 
             "options": ["Velocity", "Acceleration", "Distance", "Displacement"], 
             "answer": "Distance"},
            {"question": "What is the SI unit of energy?", 
             "options": ["Watt", "Newton", "Joule", "Pascal"], 
             "answer": "Joule"},
        ],
        "biology": [
            {"question": "What is the powerhouse of the cell?", 
             "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"], 
             "answer": "Mitochondria"},
            {"question": "How many chambers does the human heart have?", 
             "options": ["2", "3", "4", "5"], 
             "answer": "4"},
            {"question": "Which organelle is responsible for photosynthesis?", 
             "options": ["Mitochondria", "Chloroplast", "Ribosome", "Nucleolus"], 
             "answer": "Chloroplast"},
            {"question": "What is the basic unit of life?", 
             "options": ["Tissue", "Organ", "Cell", "Organism"], 
             "answer": "Cell"},
            {"question": "How many chromosomes does a human have?", 
             "options": ["23", "46", "48", "50"], 
             "answer": "46"},
        ]
    }
    
    return sample_questions.get(subject, [])[:count]

def save_to_json(filename, questions):
    """Save questions to JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved {len(questions)} questions to {filename}")
        return True
    except Exception as e:
        print(f"✗ Error saving to {filename}: {e}")
        return False

def main():
    subjects = {
        "english": "english.json",
        "mathematics": "maths.json",
        "chemistry": "chemistry.json",
        "physics": "physics.json",
        "biology": "biology.json"
    }
    
    print("=" * 50)
    print("JAMB Questions Fetcher")
    print("=" * 50)
    
    for subject, filename in subjects.items():
        print(f"\nFetching {subject.capitalize()} questions...")
        questions = fetch_jamb_questions(subject, 30)
        
        if questions:
            save_to_json(filename, questions)
        else:
            print(f"✗ Failed to get questions for {subject}")
        
        time.sleep(1)  # Be nice to the server
    
    print("\n" + "=" * 50)
    print("✓ All done! Your JSON files are updated.")
    print("=" * 50)

if __name__ == "__main__":
    main()
