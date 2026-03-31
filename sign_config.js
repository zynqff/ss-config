const fs = require('fs');
const crypto = require('crypto');

// Читаем приватный ключ (должен быть рядом)
const privateKey = fs.readFileSync('private.pem', 'utf8');

// Читаем конфиг
const config = fs.readFileSync('config.json', 'utf8');

// Создаём подпись
const sign = crypto.createSign('SHA256');
sign.update(config);
sign.end();
const signature = sign.sign(privateKey, 'base64');

// Сохраняем подпись
fs.writeFileSync('config.sig', signature);
console.log('Подпись создана: config.sig');
