import re

def email_ajratish(matn):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_lar = re.findall(email_pattern, matn)
    return email_lar

matn = "Mening email manzilim mena@gmail.com. Sizning email manzilingiz sizningemail@yandex.ru. Bizning email manzilimiz bizningemail@outlook.com"
print(email_ajratish(matn))
```

```python
import re

def email_ajratish(matn):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_lar = re.findall(email_pattern, matn)
    return email_lar

matn = "Mening email manzilim mena@gmail.com. Sizning email manzilingiz sizningemail@yandex.ru. Bizning email manzilimiz bizningemail@outlook.com"
print(email_ajratish(matn))
```

```python
import re

def email_ajratish(matn):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_lar = re.findall(email_pattern, matn)
    return email_lar

matn = "Mening email manzilim mena@gmail.com. Sizning email manzilingiz sizningemail@yandex.ru. Bizning email manzilimiz bizningemail@outlook.com"
print(email_ajratish(matn))
