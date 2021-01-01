from pathlib import Path

import re


def password_philosophy(password_philosophy_puzzle):
    with open(password_philosophy_puzzle, 'r', encoding='utf-8') as f:
        mytext = f.read().splitlines()
        total = 0
        for line in mytext:
            pattern = re.compile(r'(\d*)\-(\d*)\s(\w):\s(\w*)')
            match = pattern.findall(line)[0]
            resulte = re.findall(match[2], match[3])
            if int(match[0]) <= len(resulte) <= int(match[1]):
                total += 1
        return total


def passport_processing(passport_processing_puzzle):
    with open(passport_processing_puzzle, 'r', encoding='utf-8') as f:
        mytext = f.read().split('\n\n')
    pattern = re.compile(
        r'ecl'
        r'|pid'
        r'|eyr'
        r'|hcl'
        r'|byr'
        r'|iyr'
        r'|cid'
        r'|hgt')

    valid_passports = 0
    for passport in mytext:
        match = pattern.findall(passport)
        if len(match) == 8 or len(match) == 7 and 'cid' not in match:
            valid_passports += 1
    return valid_passports


if __name__ == "__main__":
    password_philosophy_puzzle = Path(Path.cwd(), 'puzzle.txt')
    passport_processing_puzzle = Path(Path.cwd(), 'puzzle2.txt')
    password_philosophy(password_philosophy_puzzle)
    passport_processing(passport_processing_puzzle)
