import re


def format_receipt(items, prices, quantities):
    """Create a formatted receipt using string methods."""
    width = 40
    header = "=" * width
    lines = [header, f"{'Item':<20}{'Qty':^5}{'Price':>15}", header]

    total = 0.0
    for item, price, qty in zip(items, prices, quantities):
        subtotal = price * qty
        total += subtotal
        # price column right-aligned, show $ and aligned so cents line up
        lines.append(f"{item:<20}{str(qty):^5}{('$' + f'{subtotal:7.2f}') :>15}")

    lines.append(header)
    lines.append(f"{'TOTAL':<25}{('$' + f'{total:7.2f}') :>15}")
    lines.append(header)
    return "\n".join(lines)


def process_user_data(raw_data):

    def collapse_spaces(s):
        return re.sub(r'\s+', ' ', s.strip()) if s is not None else ''

    name = raw_data.get('name', '') or ''
    name = collapse_spaces(name)
    name_parts = [p.capitalize() for p in name.split(' ') if p != '']
    clean_name = " ".join(name_parts)

    email = raw_data.get('email', '') or ''
    email = collapse_spaces(email).lower()

    phone = raw_data.get('phone', '') or ''
    phone_digits = re.sub(r'\D', '', phone)

    address = raw_data.get('address', '') or ''
    address = collapse_spaces(address)
    address = address.title()

    username = "_".join(clean_name.split(" ")).lower() if clean_name else ""

    validation = {
        'name_valid': bool(clean_name),
        'email_valid': bool(re.match(r'^[\w\.\-+]+@[\w\.-]+\.[A-Za-z]{2,}$', email)),
        'phone_valid': len(phone_digits) >= 7,  # len >=7 as minimal
        'address_valid': bool(address)
    }

    return {
        'name': clean_name,
        'email': email,
        'phone': phone_digits,
        'address': address,
        'username': username,
        'validation': validation
    }


def analyze_text(text):
    if text is None:
        text = ""

    total_chars = len(text)
    # Split into lines
    lines = text.splitlines() if text else []
    total_lines = len(lines) if lines else 1 if text else 0

    words = re.findall(r"\b[\w']+\b", text)
    total_words = len(words)

    avg_word_length = round((sum(len(w.strip("'")) for w in words) / total_words) if total_words else 0, 2)

    words_lower = [w.lower() for w in words]
    most_common_word = None
    if words_lower:
        mc, _ = Counter(words_lower).most_common(1)[0]
        most_common_word = mc

    # Longest line by character count
    longest_line = max(lines, key=lambda l: len(l)) if lines else ""

    words_per_line = [len(re.findall(r"\b[\w']+\b", l)) for l in lines] if lines else []

    # Sentences: split by ., ?, ! including trailing punctuation
    sentence_pattern = re.compile(r'([^.!?]*[.!?])', re.M | re.S)
    sentences = [s.strip() for s in sentence_pattern.findall(text) if s.strip()]
    capitalized_sentences = sum(1 for s in sentences if s and s.strip()[0].isupper())

    questions = sum(1 for s in sentences if s.endswith('?'))
    exclamations = sum(1 for s in sentences if s.endswith('!'))

    return {
        'total_chars': total_chars,
        'total_words': total_words,
        'total_lines': len(lines),
        'avg_word_length': avg_word_length,
        'most_common_word': most_common_word,
        'longest_line': longest_line,
        'words_per_line': words_per_line,
        'capitalized_sentences': capitalized_sentences,
        'questions': questions,
        'exclamations': exclamations
    }


def find_patterns(text):
    if text is None:
        text = ""

    # decimals first
    decimals = re.findall(r'\b\d+\.\d+\b', text)
    # integers: numbers not part of decimals (exclude digits that appear within any decimal string)
    all_ints = re.findall(r'\b\d+\b', text)
    integers = [i for i in all_ints if not any(i in d for d in decimals)]

    words_with_digits = re.findall(r'\b\w*\d\w*\b', text)
    capitalized_words = re.findall(r'\b[A-Z][a-zA-Z]+\b', text)
    all_caps_words = re.findall(r'\b[A-Z]{2,}\b', text)
    repeated_chars = re.findall(r'\b\w*(\w)\1\w*\b', text)
    # repeated_chars returns only the repeated char via the capture group; find full words matching repeated chars
    repeated_words = [w for w in re.findall(r'\b\w*(\w)\1\w*\b', text) if w]

    # To list words with repeated characters (full words), run:
    repeated_full = re.findall(r'\b\w*(\w)\1\w*\b', text)
    # But that returns repeated char; instead capture full word:
    repeated_full_words = re.findall(r'\b\w*(?:([a-zA-Z0-9])\1)\w*\b', text)
    # Simpler: find words and check for double-letter sequences
    repeated_words_list = [w for w in re.findall(r'\b\w+\b', text) if re.search(r'(.)\1', w)]

    return {
        'integers': integers,
        'decimals': decimals,
        'words_with_digits': words_with_digits,
        'capitalized_words': capitalized_words,
        'all_caps_words': all_caps_words,
        'repeated_chars': repeated_words_list
    }


def validate_format(input_string, format_type):

    if input_string is None:
        return (False, None)

    patterns = {
        'phone': r'^(?:\((?P<area>\d{3})\)\s*(?P<prefix>\d{3})-(?P<line>\d{4})|(?P<area2>\d{3})-(?P<prefix2>\d{3})-(?P<line2>\d{4}))$',
        'date': r'^(?P<month>0[1-9]|1[0-2])/(?P<day>0[1-9]|[12]\d|3[01])/(?P<year>(19|20)\d{2})$',
        'time': r'^(?P<hour>(0[0-9]|1[0-9]|2[0-3]|[0-9])):(?P<minute>[0-5][0-9])(?:\s*(?P<ampm>AM|PM|am|pm))?$',
        'email': r'^(?P<user>[\w\.\-+]+)@(?P<domain>[\w\.-]+\.[A-Za-z]{2,})$',
        'url': r'^(?P<scheme>https?)://(?P<host>[\w\.-]+\.[A-Za-z]{2,})(?P<path>/.*)?$',
        'ssn': r'^(?P<part1>\d{3})-(?P<part2>\d{2})-(?P<part3>\d{4})$'
    }

    pat = patterns.get(format_type)
    if not pat:
        return (False, None)
    m = re.match(pat, input_string.strip())
    if not m:
        return (False, None)

    groups = {k: v for k, v in m.groupdict().items() if v is not None}

    # Normalize phone group names
    if format_type == 'phone':
        if groups.get('area2'):
            groups = {
                'area_code': groups.get('area2'),
                'prefix': groups.get('prefix2'),
                'line': groups.get('line2')
            }
        else:
            groups = {
                'area_code': groups.get('area'),
                'prefix': groups.get('prefix'),
                'line': groups.get('line')
            }
    return (True, groups)


def extract_information(text):
    """Extract prices, percentages, years, sentences, questions, quoted text."""
    if text is None:
        text = ""

    prices = re.findall(r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?', text)
    percentages = re.findall(r'\b\d+(?:\.\d+)?%', text)
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    # sentences (keep the punctuation)
    sentences = [s.strip() for s in re.findall(r'[^.!?]+[.!?]', text, re.M)]
    questions = [s for s in sentences if s.endswith('?')]
    quoted_text = re.findall(r'"(.*?)"', text, re.S)

    return {
        'prices': prices,
        'percentages': percentages,
        'years': years,
        'sentences': sentences,
        'questions': questions,
        'quoted_text': quoted_text
    }


def clean_text_pipeline(text, operations):
    """Apply series of cleaning operations and return pipeline trace."""
    if text is None:
        text = ""

    steps = []
    current = text
    steps.append(current)

    for op in operations:
        if op == 'trim':
            current = current.strip()
        elif op == 'lowercase':
            current = current.lower()
        elif op == 'remove_punctuation':
            current = re.sub(r'[^\w\s]', '', current)
        elif op == 'remove_digits':
            current = re.sub(r'\d+', '', current)
        elif op == 'remove_extra_spaces':
            current = re.sub(r'\s+', ' ', current).strip()
        elif op == 'remove_urls':
            current = re.sub(r'https?://\S+', '', current)
        elif op == 'remove_emails':
            current = re.sub(r'[\w\.\-+]+@[\w\.-]+\.[A-Za-z]{2,}', '', current)
        elif op == 'capitalize_sentences':
            # Capitalize first letter after sentence boundary
            def cap_sentences(s):
                def cap_match(m):
                    return m.group(1) + m.group(2).upper()
                # start of string
                s = re.sub(r'^(\s*)([a-zA-Z])', lambda m: m.group(1) + m.group(2).upper(), s)
                # after punctuation and space
                s = re.sub(r'([\.!\?]\s+)([a-zA-Z])', cap_match, s)
                return s
            current = cap_sentences(current)
        else:
            # unknown op -> no change
            pass
        steps.append(current)

    return {
        'original': text,
        'cleaned': current,
        'steps': steps
    }


def smart_replace(text, replacements):
    """Perform intelligent replacements based on rules dict."""
    if text is None:
        return ""

    out = text

    # Censor phone numbers
    if replacements.get('censor_phone'):
        out = re.sub(r'\(?\b\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b', 'XXX-XXX-XXXX', out)

    # Censor emails
    if replacements.get('censor_email'):
        out = re.sub(r'[\w\.\-+]+@[\w\.-]+\.[A-Za-z]{2,}', '[EMAIL]', out)

    # Fix spacing around punctuation: remove spaces before punctuation, ensure one space after punctuation
    if replacements.get('fix_spacing'):
        out = re.sub(r'\s+([,.;:!?])', r'\1', out)  # no space before punctuation
        out = re.sub(r'([,.;:!?])(?=[^\s])', r'\1 ', out)  # ensure space after punctuation
        out = re.sub(r'\s+', ' ', out).strip()

    # Expand contractions
    if replacements.get('expand_contractions'):
        contractions = {
            "don't": "do not",
            "won't": "will not",
            "can't": "cannot",
            "i'm": "I am",
            "I'm": "I am",
            "you're": "you are",
            "it's": "it is",
            "he's": "he is",
            "she's": "she is",
            "we're": "we are",
            "they're": "they are",
            "I've": "I have",
            "you've": "you have",
            "we've": "we have",
            "they've": "they have",
            "ain't": "is not",
            "I'm": "I am"
        }
        # Use regex word boundaries and do case-insensitive replacements where appropriate
        for k, v in contractions.items():
            # Keep simple: replace in a case-insensitive manner but preserve capitalization for I/I'.
            pattern = re.compile(r'\b' + re.escape(k) + r'\b', flags=re.IGNORECASE)
            out = pattern.sub(v, out)

    # Number to word for single digits
    if replacements.get('number_to_word'):
        num_map = {
            '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
            '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
        }
        out = re.sub(r'\b([0-9])\b', lambda m: num_map.get(m.group(1), m.group(1)), out)

    return out


def analyze_log_file(log_text):
    """Analyze log file entries and collect statistics."""
    if not log_text:
        return {
            'total_entries': 0,
            'error_count': 0,
            'warning_count': 0,
            'info_count': 0,
            'dates': [],
            'error_messages': [],
            'time_range': (None, None),
            'most_active_hour': None
        }

    entries = []
    pattern = re.compile(r'^\[(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\]\s*(?P<level>[A-Z]+):\s*(?P<msg>.*)$')
    for line in log_text.splitlines():
        line = line.strip()
        if not line:
            continue
        m = pattern.match(line)
        if m:
            d = m.group('date')
            t = m.group('time')
            level = m.group('level').upper()
            msg = m.group('msg').strip()
            entries.append({'date': d, 'time': t, 'level': level, 'msg': msg})

    total_entries = len(entries)
    error_count = sum(1 for e in entries if e['level'] == 'ERROR')
    warning_count = sum(1 for e in entries if e['level'] == 'WARNING')
    info_count = sum(1 for e in entries if e['level'] == 'INFO')

    dates = sorted({e['date'] for e in entries})

    error_messages = [e['msg'] for e in entries if e['level'] == 'ERROR']

    # determine earliest and latest times across entries (as datetimes)
    times = []
    for e in entries:
        try:
            dt = datetime.strptime(e['date'] + " " + e['time'], "%Y-%m-%d %H:%M:%S")
            times.append(dt)
        except Exception:
            pass
    if times:
        earliest = min(times).strftime("%Y-%m-%d %H:%M:%S")
        latest = max(times).strftime("%Y-%m-%d %H:%M:%S")
    else:
        earliest = latest = None

    # most active hour (0-23) across all entries
    hour_counts = Counter()
    for t in times:
        hour_counts[t.hour] += 1
    most_active_hour = hour_counts.most_common(1)[0][0] if hour_counts else None

    return {
        'total_entries': total_entries,
        'error_count': error_count,
        'warning_count': warning_count,
        'info_count': info_count,
        'dates': dates,
        'error_messages': error_messages,
        'time_range': (earliest, latest),
        'most_active_hour': most_active_hour
    }


def run_tests():
    """Test all functions with sample data."""
    print("="*50)
    print("Testing Part 1: String Methods")
    print("="*50)

    # Test 1.1: Receipt formatting
    items = ["Coffee", "Sandwich"]
    prices = [3.50, 8.99]
    quantities = [2, 1]
    receipt = format_receipt(items, prices, quantities)
    print("Receipt Test:")
    print(receipt)

    # Test 1.2: User data processing
    test_data = {
        'name': '  john DOE  ',
        'email': ' JOHN@EXAMPLE.COM ',
        'phone': '(555) 123-4567',
        'address': '123  main  street'
    }
    cleaned = process_user_data(test_data)
    print(f"\nCleaned name: {cleaned.get('name', 'ERROR')}")
    print(f"Cleaned email: {cleaned.get('email', 'ERROR')}")
    print(f"Cleaned phone: {cleaned.get('phone', 'ERROR')}")
    print(f"Username: {cleaned.get('username', 'ERROR')}")

    print("\n" + "="*50)
    print("Testing Part 2: Regular Expressions")
    print("="*50)

    # Test 2.1: Pattern finding
    test_text = "I have 25 apples and 3.14 pies. HELLO W0RLD!"
    patterns = find_patterns(test_text)
    print(f"Found integers: {patterns.get('integers', [])}")
    print(f"Found decimals: {patterns.get('decimals', [])}")
    print(f"Words with digits: {patterns.get('words_with_digits', [])}")
    print(f"All caps: {patterns.get('all_caps_words', [])}")

    # Test 2.2: Format validation
    phone_valid, phone_parts = validate_format("(555) 123-4567", "phone")
    print(f"\nPhone validation: {phone_valid}")
    if phone_parts:
        print(f"Extracted parts: {phone_parts}")

    date_valid, date_parts = validate_format("02/29/2024", "date")
    print(f"\nDate validation (02/29/2024): {date_valid} -> {date_parts}")

    email_valid, email_parts = validate_format("john.doe@example.com", "email")
    print(f"\nEmail valid: {email_valid} -> {email_parts}")

    # Test 2.3: Information extraction
    info_text = 'The price is $19.99 (20% off). "Great deal!" she said in 2024.'
    info = extract_information(info_text)
    print(f"\nPrices found: {info.get('prices', [])}")
    print(f"Percentages found: {info.get('percentages', [])}")
    print(f"Years found: {info.get('years', [])}")
    print(f"Quoted text: {info.get('quoted_text', [])}")

    print("\n" + "="*50)
    print("Testing Part 3: Combined Operations")
    print("="*50)

    # Test 3.1: Cleaning pipeline
    dirty_text = "  Hello   WORLD!  Visit https://example.com  "
    operations = ['trim', 'lowercase', 'remove_urls', 'remove_extra_spaces']
    cleaned_result = clean_text_pipeline(dirty_text, operations)
    print(f"Original: '{cleaned_result.get('original', '')}'")
    print(f"Cleaned: '{cleaned_result.get('cleaned', '')}'")
    print(f"Steps: {cleaned_result.get('steps', [])}")

    # Test 3.2: Smart replace
    text = "Call me at 555-123-4567. I'm busy. Email: john@example.com"
    rules = {'censor_phone': True, 'expand_contractions': True, 'censor_email': True}
    replaced = smart_replace(text, rules)
    print(f"\nSmart replaced: {replaced}")

    print("\n" + "="*50)
    print("Testing Part 4: Log Analysis")
    print("="*50)

    # Test 4.1: Log analysis
    sample_log = """[2024-01-15 10:30:45] ERROR: Connection failed
[2024-01-15 10:31:00] INFO: Retry attempt
[2024-01-15 11:00:00] WARNING: High memory usage"""
    log_analysis = analyze_log_file(sample_log)
    print(f"Total entries: {log_analysis.get('total_entries', 0)}")
    print(f"Error count: {log_analysis.get('error_count', 0)}")
    print(f"Unique dates: {log_analysis.get('dates', [])}")
    print(f"Time range: {log_analysis.get('time_range', None)}")
    print(f"Most active hour: {log_analysis.get('most_active_hour', None)}")

    print("\n" + "="*50)
    print("All tests completed!")
    print("="*50)
if __name__ == "__main__":
    run_tests()
