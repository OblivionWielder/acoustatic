import ply.lex as lex


# ACOUSTATIC	acoustatic
# PIECE	piece
# INTENSITY	intensity
# PITCH	pitch
# DURATION	duration
# TONE	tone
# NEW	new
# SOUND	Sound
# SOUNDS	sounds
# INSTRUMENT	Instrument
# INSTRUMENTS	instruments
# CREATE	create
# LOOPS	loops
# OFF	off
# ON	on
# IF	if 
# FOR	for
# ELSE	else
# WHILE	while
# DO	do
# PLAY	play
keywords = (
	'ACOUSTATIC', 'PIECE', 'INTENSITY', 'PITCH', 'DURATION', 'TONE', 'NEW', 'SOUND', 'SOUNDS', 'INSTRUMENT', 'INSTRUMENTS', 'CREATE', 'LOOPS', 'OFF', 'ON', 'IF', 'FOR', 'ELSE', 'WHILE', 'DO', 'PLAY',	'ADD', 'FUNCTION', 'TRUE', 'FALSE', 'STRING', 'BOOLEAN', 'INT', 'FL', 'PRINT', 'VOID', 'MAIN', 'RETURN',
)
reserved = {
	'acoustatic':'ACOUSTATIC',
	'piece':'PIECE',
	'intensity':'INTENSITY',
	'pitch':'PITCH',
	'duration':'DURATION',
	'tone':'TONE',
	'new':'NEW',
	'Sound':'SOUND',
	'sounds':'SOUNDS',
	'Instrument':'INSTRUMENT',
	'instruments':'INSTRUMENTS',
	'create':'CREATE',
	'loops':'LOOPS',
	'off':'OFF',
	'if':'IF',
	'for':'FOR',
	'else':'ELSE',
	'while':'WHILE',
	'do':'DO',
	'play':'PLAY',
	'add':'ADD',
	'on':'ON',
	'track':'TRACK',
	'function':'FUNCTION',
	'true':'TRUE',
	'false':'FALSE',
	'string':'STRING',
	'boolean':'BOOLEAN',
	'int':'INT',
	'fl':'FL',
	'print':'PRINT',
	'void':'VOID',
	'main':'MAIN',
	'return':'RETURN',
}

tokens = [
	'OPENCORCH', 'CLOSECORCH', 'OPENBRACK', 'CLOSEBRACK', 'OPENPAREN', 'CLOSEPAREN', 'COMMA', 'SEMICOLON', 'COLON', 'PLUS', 'MINUS', 'MULT', 'DIV', 'REM', 'LT', 'LE', 'GT', 'GE', 'NE', 'INTEGER', 'FLOAT', 'STRINGLINE', 'ID', 'EQUALS', 'EE', 'AND', 'OR', 'NOT'
] + list(reserved.values())


t_OPENCORCH		= r'\{'
t_CLOSECORCH 	= r'\}'
t_OPENBRACK 	= r'\['
t_CLOSEBRACK	= r'\]'
t_OPENPAREN		= r'\('
t_CLOSEPAREN	= r'\)'
t_COMMA			= r','
t_SEMICOLON		= r';'
t_COLON			= r':'
t_PLUS			= r'\+'
t_MINUS			= r'-'
t_MULT			= r'\*'
t_DIV			= r'/'
t_EE   			= r'=='
t_EQUALS   		= r'='
t_REM			= r'%'
t_LT    		= r'<'
t_LE    		= r'<='
t_GT			= r'>'
t_GE			= r'>='
t_NE			= r'<>'
t_AND			= r'\&\&'
t_OR			= r'\|\|'
t_NOT			= r'\!\!'
t_INTEGER		= r'\d+'    
t_FLOAT			= r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRINGLINE		= r'\".*?\"'

# Ignored characters
t_ignore = " \t"

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
	
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r'\/\/.*'
    pass
    # No return value. Token discarded

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
	
# Build the lexer
pfile=open("busquedaArreglos.txt","r")
data = pfile.read()
pfile.close()
lex.lex()
lex.input(data)
tok = lex.token()
# while tok:
	# tok = lex.token()
	# print(tok)
	# if not tok: break