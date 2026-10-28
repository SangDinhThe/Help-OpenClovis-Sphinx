from pygments.lexer import RegexLexer
from pygments.token import Keyword, Text, Name, String, Generic

class ClLogLexer(RegexLexer):
    name = 'ClLog'

    tokens = {
        'root': [
            (r'^(.{3}\s+.{3}\s+\d{1,2}\s+\d{2}[:]\d{2}[:]\d{2}([.]\d{3})?\s+\d{4})', String.Other),
            (r'[^.\()][^.\()][^.\()][^.\()][^.\()]+?[.]\d*?\s[:]', Name.Decorator),
            (r'(INFO|DEBUG|TRACE)', Keyword),
            (r'(NOTICE|WARN)', Name.Class),
            (r'(EMRGN|CRITIC|ERROR)', Name.Exception),
            (r'.', Text),
        ]
    }

class ClCliLexer(RegexLexer):
    name = 'ClCli'

    tokens = {
        'root': [
            (r'\[.*?\]', String.Other),
            (r'\b(node|su|comp|sg|si|csi)\b', Generic.Error),
            (r'\b(help|setc|list|memberList|amsEntityPrint|amsUnlock|amsLockAssignment|amsLockInstantiation|end|bye)\b', Name.Decorator),
            (r'.', Text),
        ]
    }
