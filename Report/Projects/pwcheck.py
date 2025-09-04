import argparse
import math
import re
import string
from getpass import getpass
from typing import Dict, List

# 흔한 비밀번호(샘플). 필요하면 확장하세요.
COMMON_PASSWORDS = {
    "123456","123456789","12345","qwerty","password","111111","12345678",
    "abc123","password1","iloveyou","admin","welcome","monkey","dragon",
    "qwerty123","letmein","football","baseball","1q2w3e4r","asdfgh",
    "zaq12wsx","passw0rd","000000","qazwsx","sunshine","princess",
}

# 간단 사전 단어(부분일치 검사). 필요시 확장.
DICTIONARY_WORDS = {
    "love","secret","money","music","login","master","super","school",
    "student","summer","winter","spring","admin","guest","hero",
}

KEYBOARD_ROWS = ["1234567890", "qwertyuiop", "asdfghjkl", "zxcvbnm"]

def classify_chars(pw: str) -> Dict[str, int]:
    return {
        "length": len(pw),
        "lower": sum(c.islower() for c in pw),
        "upper": sum(c.isupper() for c in pw),
        "digits": sum(c.isdigit() for c in pw),
        "symbols": sum(c in string.punctuation for c in pw),
        "spaces": pw.count(" "),
    }

def charset_size(stats: Dict[str, int]) -> int:
    size = 0
    if stats["lower"] > 0:  size += 26
    if stats["upper"] > 0:  size += 26
    if stats["digits"] > 0: size += 10
    if stats["symbols"] > 0: size += len(string.punctuation)  # ~32
    if stats["spaces"] > 0:  size += 1
    return max(size, 1)

def entropy_bits(stats: Dict[str, int]) -> float:
    # 매우 러프한 엔트로피 추정
    return stats["length"] * math.log2(charset_size(stats))

def has_simple_sequence(pw: str) -> bool:
    s = pw.lower()
    for i in range(len(s) - 2):
        a, b, c = s[i], s[i+1], s[i+2]
        if a.isalpha() and b.isalpha() and c.isalpha():
            if ord(b)-ord(a) == 1 and ord(c)-ord(b) == 1: return True
            if ord(a)-ord(b) == 1 and ord(b)-ord(c) == 1: return True
        if a.isdigit() and b.isdigit() and c.isdigit():
            if int(b)-int(a) == 1 and int(c)-int(b) == 1: return True
            if int(a)-int(b) == 1 and int(b)-int(c) == 1: return True
    return False

def has_keyboard_sequence(pw: str) -> bool:
    s = pw.lower()
    for row in KEYBOARD_ROWS:
        for i in range(len(row)-2):
            if row[i:i+3] in s or row[i:i+3][::-1] in s:
                return True
    return False

def has_repetition(pw: str) -> bool:
    # 같은 문자 3연속 또는 2글자 패턴 반복
    return bool(re.search(r"(.)\1\1", pw) or re.search(r"(..)\1\1", pw))

def looks_like_year_suffix(pw: str) -> bool:
    # 끝에 1990~2099 형식 연도
    return bool(re.search(r"(19|20)\d{2}$", pw))

def contains_dictionary_word(pw: str) -> bool:
    s = pw.lower()
    for w in DICTIONARY_WORDS:
        if len(w) >= 4 and w in s:
            return True
    return False

def is_common_password(pw: str) -> bool:
    return pw.lower() in COMMON_PASSWORDS

def score_password(pw: str, show: bool=False) -> Dict:
    reasons: List[str] = []
    suggestions: List[str] = []

    stats = classify_chars(pw)
    ent = entropy_bits(stats)
    classes_used = sum(1 for k in ("lower","upper","digits","symbols","spaces") if stats[k] > 0)

    # 기본 가점
    score = 0
    score += min(40, stats["length"] * 3)                     # 길이(최대 40)
    score += max(0, (classes_used - 1) * 10)                  # 다양성(최대 40)
    score += max(0, min(20, int((ent - 28) / 2)))             # 엔트로피 보너스(최대 20)

    # 감점 요소
    if is_common_password(pw):
        reasons.append("아주 흔한 비밀번호 목록과 일치")
        score -= 40
    if has_simple_sequence(pw):
        reasons.append("연속된 문자/숫자 시퀀스 포함(예: abc, 123)")
        score -= 25
    if has_keyboard_sequence(pw):
        reasons.append("키보드 인접 패턴 포함(예: qwe, asd)")
        score -= 20
    if has_repetition(pw):
        reasons.append("반복되는 문자/패턴(aaaa, abab)")
        score -= 20
    if contains_dictionary_word(pw):
        reasons.append("일반 사전 단어 포함")
        score -= 15
    if looks_like_year_suffix(pw):
        reasons.append("연도(YYYY) 접미 사용")
        score -= 10
    if classes_used == 1:
        reasons.append("문자 종류가 한 가지뿐")
        score -= 20
    if stats["length"] < 12:
        reasons.append("길이가 12자 미만")
        score -= 15

    score = max(0, min(100, score))

    # 등급
    if score < 20:   verdict = "Very Weak"
    elif score < 40: verdict = "Weak"
    elif score < 60: verdict = "Fair"
    elif score < 80: verdict = "Strong"
    else:            verdict = "Very Strong"

    # 개선 팁
    if stats["length"] < 12:
        suggestions.append("Make your password at least 12 characters long (preferably 14–16).")
    if classes_used < 3:
        suggestions.append("Use at least three of the following: uppercase letters, lowercase letters, numbers, and symbols.")
    if has_simple_sequence(pw) or has_keyboard_sequence(pw):
        suggestions.append("Avoid consecutive or keyboard patterns (e.g., 1234, qwerty).")
    if has_repetition(pw):
        suggestions.append("Avoid repeated characters or patterns (e.g., aaaa, abab).")
    if contains_dictionary_word(pw) or is_common_password(pw):
        suggestions.append("Do not use dictionary words or common passwords; generate random ones with a password manager.")
    suggestions.append("Always enable MFA (multi-factor authentication) for important accounts.")

    if show:
        print(f"[DEBUG] stats={stats}, entropy_bits≈{ent:.1f}, classes_used={classes_used}")

    return {
        "score": score,
        "verdict": verdict,
        "reasons": reasons,
        "suggestions": suggestions
    }

def main():
    parser = argparse.ArgumentParser(description="Password Strength Checker")
    parser.add_argument("password", nargs="?", help="평가할 비밀번호")
    parser.add_argument("--show", action="store_true", help="세부 계산값 표시")
    args = parser.parse_args()

    pw = args.password or input("Enter password to check: ")
    result = score_password(pw, show=args.show)

    print("\n=== Password Strength Report ===")
    print(f"Score  : {result['score']}/100")
    print(f"Verdict: {result['verdict']}")
    if result["reasons"]:
        print("\nWeaknesses:")
        for r in result["reasons"]:
            print(f" - {r}")
    print("\nSuggestions:")
    for s in result["suggestions"]:
        print(f" - {s}")

if __name__ == "__main__":
    main()