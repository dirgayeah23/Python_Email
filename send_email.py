import smtplib, ssl

port = 465  # Untuk SSL
smtp_server = "smtp.gmail.com"
sender_email = input ("masukkan email pengirim :")  # Masukkan email Anda
receiver_email = input ("masukkan email penerima :")  # masukkan email Penerima
password = input("Masukkan Password dan tekan enter: ")
message = """\
Subject: Halo 

Email ini di kirim melalui python script."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print('Email terkirim')