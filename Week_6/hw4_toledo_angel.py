import re
import time
from collections import Counter

def problem1():
    """Grouping and capturing examples."""
    # a) ISO dates
    dates_text = """
    Important dates:
    - Project due: 2024-03-15
    - Meeting on: 12/25/2024
    - Holiday: July 4, 2025
    """
    pattern_iso = r'\b(?:19|20)\d{2}-\d{2}-\d{2}\b'
    iso_dates = re.findall(pattern_iso, dates_text)

    # b) emails
    emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
    pattern_email = r'(?P<username>[\w\.\-]+)@(?P<domain>[\w\.-]+\.[A-Za-z]{2,})'
    email_parts = []
    for m in re.finditer(pattern_email, emails_text):
        email_parts.append({'username': m.group('username'), 'domain': m.group('domain')})

    # c) phones
    phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
    pattern_phone = r'\b(?:\((?P<area>\d{3})\)\s*(?P<number>\d{3}-\d{4})|(?P<area2>\d{3})-(?P<number2>\d{3}-\d{4}))\b'
    phone_numbers = []
    for m in re.finditer(pattern_phone, phones_text):
        if m.group('area'):
            phone_numbers.append((m.group('area'), m.group('number')))
        else:
            phone_numbers.append((m.group('area2'), m.group('number2')))

    # d) repeated words
    repeated_text = "The the quick brown fox jumped over the the lazy dog"
    pattern_repeated = r'\b([A-Za-z]+)\s+\1\b'
    repeated_words = [m.group(1).lower() for m in re.finditer(pattern_repeated, repeated_text, re.IGNORECASE)]

    return {
        'iso_dates': iso_dates,
        'email_parts': email_parts,
        'phone_numbers': phone_numbers,
        'repeated_words': repeated_words
    }


def problem2():
    """Alternation patterns."""
    files_text = """
    Documents: report.pdf, notes.txt, presentation.pptx
    Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
    Code: script.py, program.java, style.css
    """
    pattern_images = r'\b[\w\-]+\.(?:jpg|jpeg|png|gif)\b'
    image_files = re.findall(pattern_images, files_text, re.IGNORECASE)

    mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
    months = r'(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)'
    pattern_dates = rf'\b(?:\d{{4}}-\d{{2}}-\d{{2}}|\d{{2}}/\d{{2}}/\d{{4}}|{months}\s+\d{{1,2}},\s*\d{{4}})\b'
    all_dates = re.findall(pattern_dates, mixed_dates)

    prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
    pattern_prices = r'\b(?:\$\d+(?:\.\d+)?|USD\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?\s*dollars|€\d+(?:\.\d+)?|£\d+(?:\.\d+)?)\b'
    prices = re.findall(pattern_prices, prices_text, re.IGNORECASE)

    code_text = """
    We use Python for data science, Java for enterprise apps,
    JavaScript or JS for web development, and C++ or CPP for systems.
    """
    pattern_langs = r'\b(?:Python|JavaScript|Java|JS|C\+\+|CPP)\b'
    languages = re.findall(pattern_langs, code_text, re.IGNORECASE)
    languages = [lang if not lang.lower() == 'js' else 'JS' for lang in languages]

    return {
        'image_files': image_files,
        'all_dates': all_dates,
        'prices': prices,
        'languages': languages
    }


def problem3():
    """findall and finditer practice."""
    log_text = """
    [2024-03-15 10:30:45] INFO: Server started on port 8080
    [2024-03-15 10:31:02] ERROR: Connection failed to database
    [2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
    [2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
    [2024-03-15 10:32:30] ERROR: File not found: config.yml
    """
    pattern_timestamp = r'\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\]'
    timestamps = re.findall(pattern_timestamp, log_text)

    pattern_log = r'\]\s*([A-Z]+):\s*(.+)'
    log_entries = re.findall(pattern_log, log_text)

    pattern_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = []
    for m in re.finditer(pattern_ip, log_text):
        ip_addresses.append({'ip': m.group(0), 'start': m.start(), 'end': m.end()})

    def highlight_errors(text):
        return re.sub(r'\bERROR\b', r'**ERROR**', text)
    highlighted_log = highlight_errors(log_text)

    return {
        'timestamps': timestamps,
        'log_entries': log_entries,
        'ip_addresses': ip_addresses,
        'highlighted_log': highlighted_log
    }


def problem4():
    """Use re.sub for transformations."""
    messy_phones = """
    Contact list:
    - John: 555.123.4567
    - Jane: (555) 234-5678
    - Bob: 555 345 6789
    - Alice: 5554567890
    """
    def standardize_phones(text):
        pattern = r'\(?(\d{3})\)?[.\s-]?(\d{3})[.\s-]?(\d{4})'
        replacement = r'(\1) \2-\3'
        return re.sub(pattern, replacement, text)
    cleaned_phones = standardize_phones(messy_phones)

    sensitive_text = """
    Customer: John Doe
    SSN: 123-45-6789
    Credit Card: 4532-1234-5678-9012
    Email: john.doe@email.com
    Phone: (555) 123-4567
    """
    def redact_sensitive(text):
        text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', 'XXX-XX-XXXX', text)
        text = re.sub(r'\b(?:\d{4}[-\s]?){3}\d{4}\b', 'XXXX-XXXX-XXXX-XXXX', text)
        text = re.sub(r'[\w\.\-+]+@[\w\.-]+\.[A-Za-z]{2,}', '[REDACTED_EMAIL]', text)
        return text
    redacted_text = redact_sensitive(sensitive_text)

    markdown_text = """
    Check out [Google](https://google.com) for search.
    Visit [GitHub](https://github.com) for code.
    Read documentation at [Python Docs](https://docs.python.org).
    """
    def markdown_to_html(text):
        pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        return re.sub(pattern, r'<a href="\2">\1</a>', text)
    html_text = markdown_to_html(markdown_text)

    template = """
    Dear {name},
    Your order #{order_id} for {product} has been shipped.
    Tracking number: {tracking}
    """
    values = {
        'name': 'John Smith',
        'order_id': '12345',
        'product': 'Python Book',
        'tracking': 'TRK789XYZ'
    }
    def fill_template(template, values):
        def repl(m):
            key = m.group(1)
            return str(values.get(key, m.group(0)))
        return re.sub(r'\{(\w+)\}', repl, template)
    filled_template = fill_template(template, values)

    return {
        'cleaned_phones': cleaned_phones,
        'redacted_text': redacted_text,
        'html_text': html_text,
        'filled_template': filled_template
    }


def problem5():
    """Compiled patterns and validation."""
    class PatternLibrary:
        EMAIL = re.compile(r'^[\w\.\-+]+@[\w\.-]+\.[A-Za-z]{2,}$', re.IGNORECASE)
        URL = re.compile(r'^(?:https?://)?(?:www\.)?[\w\.-]+\.[A-Za-z]{2,}(?:/[\w\./-]*)?$', re.IGNORECASE)
        ZIP_CODE = re.compile(r'^\d{5}(?:-\d{4})?$')
        PASSWORD = re.compile(r'^(?=.{8,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).+$')
        CREDIT_CARD = re.compile(r'^(?:\d{4}[-\s]?){3}\d{4}$')

    test_data = {
        'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
        'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
        'zips': ['12345', '12345-6789', '1234', '123456'],
        'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
        'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456', '1234567890123456']
    }
    results = {
        'emails': [bool(PatternLibrary.EMAIL.match(e)) for e in test_data['emails']],
        'urls': [bool(PatternLibrary.URL.match(u)) for u in test_data['urls']],
        'zips': [bool(PatternLibrary.ZIP_CODE.match(z)) for z in test_data['zips']],
        'passwords': [bool(PatternLibrary.PASSWORD.match(p)) for p in test_data['passwords']],
        'cards': [bool(PatternLibrary.CREDIT_CARD.match(c)) for c in test_data['cards']]
    }
    return results


def problem6():
    """Log file analyzer for Apache/Nginx like logs."""
    log_data = """
    192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 5234
    192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401 234
    192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1" 304 0
    192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1" 403 0
    192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200 1234
    192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200 15234
    192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
    """
    log_pattern = re.compile(
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \['
        r'(?P<day>\d{2})/(?P<month>[A-Za-z]{3})/(?P<year>\d{4}):(?P<hour>\d{2}):(?P<min>\d{2}):(?P<sec>\d{2})\s+(?P<tz>[+\-]\d{4})\]\s+"'
        r'(?P<method>[A-Z]+)\s+(?P<path>\S+)\s+HTTP/[0-9.]+"\s+(?P<status>\d{3})\s+(?P<size>\d+)', re.IGNORECASE)
    parsed_logs = []
    for m in log_pattern.finditer(log_data):
        timestamp = f"{m.group('day')}/{m.group('month')}/{m.group('year')}:{m.group('hour')}:{m.group('min')}:{m.group('sec')} {m.group('tz')}"
        parsed_logs.append({
            'ip': m.group('ip'),
            'timestamp': timestamp,
            'method': m.group('method'),
            'path': m.group('path'),
            'status': int(m.group('status')),
            'size': int(m.group('size'))
        })

    total_requests = len(parsed_logs)
    unique_ips = sorted({p['ip'] for p in parsed_logs})
    error_count = sum(1 for p in parsed_logs if 400 <= p['status'] < 600)
    total_bytes = sum(p['size'] for p in parsed_logs)
    path_counts = Counter(p['path'] for p in parsed_logs)
    most_requested_path = path_counts.most_common(1)[0][0] if path_counts else ''
    methods_used = sorted({p['method'] for p in parsed_logs})

    analysis = {
        'total_requests': total_requests,
        'unique_ips': unique_ips,
        'error_count': error_count,
        'total_bytes': total_bytes,
        'most_requested_path': most_requested_path,
        'methods_used': methods_used
    }

    return {
        'parsed_logs': parsed_logs,
        'analysis': analysis
    }


def run_tests_and_save():
    print("Problem 1 Results:")
    print(problem1())
    print("\nProblem 2 Results:")
    print(problem2())
    print("\nProblem 3 Results:")
    print(problem3())
    print("\nProblem 4 Results:")
    print(problem4())
    print("\nProblem 5 Results:")
    print(problem5())
    print("\nProblem 6 Results:")
    print(problem6())

if __name__ == "__main__":
    run_tests_and_save()


