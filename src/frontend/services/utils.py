import urllib.parse

import urllib.parse

def return_mail_message_template():
    subject = "Te escribo desde tu app!"
    body = (
        "¡Hola Adam!%0D%0A%0D%0A"
        "Te escribo desde tu app porque quería comentarte algo rápido.%0D%0A"
        "Te dejo aquí algunos datos para que sepas quién soy y por qué te contacto:%0D%0A%0D%0A"
        "- Mi nombre:%0D%0A"
        "- Motivo del mensaje:%0D%0A"
        "- Algo más que deberías saber (opcional):%0D%0A%0D%0A"
        "¡Gracias por leerme! Espero que podamos conocernos pronto! 🤝"
    )

    subject_encoded = urllib.parse.quote(subject)
    body_encoded = body

    return f"{subject_encoded}&body={body_encoded}"

