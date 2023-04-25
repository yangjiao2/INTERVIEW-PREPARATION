const MONTH_NAMES = [
    ['jan', 'uary'],
    ['feb', 'uary'],
    ['mar', 'ch'],
    ['apr', 'il'],
    ['may', ''],
    ['jun', 'e'],
    ['jul', 'y'],
    ['aug', 'ust'],
    ['sep', 'tember'],
    ['oct', 'ober'],
    ['nov', 'ember'],
    ['dec', 'ember'],
  ];


// Matches any month name:
const MONTH_NAME =
'(?:' +
MONTH_NAMES.map(
  ([short, rest]) => `${short}(?:${wordPrefixPattern(rest)})?`,
).join('|') +
')';

/*
  Construct a regex fragment for matching prefixes of a given string.
  wordPrefixPattern('hello') => 'h|he|hel|hell|hello'
*/
function wordPrefixPattern(word: string): string {
    return Array(word.length)
      .fill()
      .map((_, i) => word.slice(0, i + 1))
      .join('|');
  }


const DATE_SEPERATOR = '[ -/.]';
const TWO_DIGITS = '\\d\\d?';
const YEAR = '\\d\\d?\\d?\\d?';

// Matches a date without year (e.g. 12 Dec, 6/6):
const MONTH_AND_DAY =
  '(?:' +
  [
    [MONTH_NAME, DATE_SEPERATOR, TWO_DIGITS],
    [TWO_DIGITS, DATE_SEPERATOR, MONTH_NAME],
    [TWO_DIGITS, DATE_SEPERATOR, TWO_DIGITS],
  ]
    .map(a => a.join(''))
    .join(')|(?:') +
  ')';

// Matches a date with optional year at beginning or end:
const ABSOLUTE_DATE_PATTERN = new RegExp(
  `^\s*(?:${MONTH_AND_DAY}` +
    `|(?:${YEAR}${DATE_SEPERATOR}${MONTH_AND_DAY})` +
    `|(?:${MONTH_AND_DAY}${DATE_SEPERATOR}${YEAR})` +
    ')s*$',
  'i',
);
