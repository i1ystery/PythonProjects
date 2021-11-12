import re


def process_sql(nickname, text):
    if nickname is None:
        raise ValueError
    if text is None:
        raise ValueError
    assert re.search(r"('(''|[^'])*')|(;)|(\b(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})\b)", nickname, flags=re.IGNORECASE) is None
    assert re.search(r"('(''|[^'])*')|(;)|(\b(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})\b)", text, flags=re.IGNORECASE) is None
    text = re.sub(
        r"((ondra|ond[rř]ej|ondr[aá][sš]ek) mand[i|í]k)|((jaroslav|j[aá]ra|jarda) cimrman)|(alena reichlov[aá])|(mand[i|í]k)|(reichlov[aá])|(cimrman)",
        '[AUTOMATICKY CENZUROVANO]', text, flags=re.IGNORECASE)
    return f'insert into prispevek values(\'{nickname}\',\'{text}\')'


print(process_sql('\');SELECT 1;--', ' vyrobky ondrej mandik prisel do skoly'))
