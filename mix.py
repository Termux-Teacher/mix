# Encoded By : MUMIT ISLAM HIMU
# Encryption : Py3 Marshal+Zlib+B64
# Github: https://github.com/MUMIT-404-CYBER
#----------------------------------------------

import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))