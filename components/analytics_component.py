"""
Analytics Component - Statistics and data analysis.
"""
from typing import List, Dict, Tuple
from collections import Counter

def get_general_stats(countries: List[dict]) -> Dict:
    """
    Calculate general statistics for countries.
    """
    total = len(countries)
    if total == 0:
        return {"total": 0}
        
    return {
        "total": total,
    }

def get_currency_stats(countries: List[dict]) -> List[Tuple[str, int]]:
    """
    Get top currencies.
    """
    currencies = [c.get('currency_code') for c in countries if c.get('currency_code')]
    return Counter(currencies).most_common(5)

def get_tld_stats(countries: List[dict]) -> List[Tuple[str, int]]:
    """
    Get generic TLD info (just a count of unique ones).
    """
    tlds = [c.get('tld') for c in countries if c.get('tld')]
    return Counter(tlds).most_common(5)

def get_language_stats(countries: List[dict]) -> List[Tuple[str, int]]:
    """
    Get top languages (parsing comma separated string).
    """
    all_langs = []
    for c in countries:
        langs = c.get('languages', '')
        if langs:
            # simple split by comma
            for l in langs.split(','):
                all_langs.append(l.strip())
                
    return Counter(all_langs).most_common(5)
