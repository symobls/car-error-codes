def analyze_error_codes():
    error_codes = {
        'P0301': {'description': 'فشل في مدخل الإشعال في الأسطوانة 1', 'solution': 'تحقق من شمعات الإشعال وملفات الإشعال.'},
        'P0302': {'description': 'فشل في مدخل الإشعال في الأسطوانة 2', 'solution': 'تحقق من شمعات الإشعال وملفات الإشعال.'},
        'P0303': {'description': 'فشل في مدخل الإشعال في الأسطوانة 3', 'solution': 'تحقق من شمعات الإشعال وملفات الإشعال.'},
        'P0304': {'description': 'فشل في مدخل الإشعال في الأسطوانة 4', 'solution': 'تحقق من شمعات الإشعال وملفات الإشعال.'},
        'P0400': {'description': 'الدائرة غير الصحيحة للعادم', 'solution': 'تحقق من نظام إعادة تدوير غازات العادم.'},
        'P0420': {'description': 'كفاءة المحول الحفازي لا توجد مشكلة', 'solution': 'تحقق من المحول الحفازي ونظام العادم.'},
        'P0505': {'description': 'فشل في دائرة التحكم بموضع الخانق', 'solution': 'تحقق من جهاز استشعار الخانق والدوائر.'}
    }
    return error_codes

if __name__ == '__main__':
    error_codes = analyze_error_codes()
    for code, details in error_codes.items():
        print(f'Error Code: {code} - Description: {details['description']} - Solution: {details['solution']}')