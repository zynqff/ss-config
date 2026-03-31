#!/usr/bin/env python3
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

# Читаем приватный ключ
with open('private.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
    )

# Читаем конфиг
with open('config.json', 'rb') as f:
    config_data = f.read()

# Подписываем
signature = private_key.sign(config_data)

# Сохраняем в base64
with open('config.sig', 'wb') as f:
    f.write(base64.b64encode(signature))

print("✅ config.sig created")
