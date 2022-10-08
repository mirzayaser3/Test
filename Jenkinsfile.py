import smtplib
sender = "sender@domain.com"  
receivers = "receivers@domain.com"  
message = """
Stack Overflow! 
"""

try:
   smtp_obj = smtplib.SMTP('localhost')
   smtp_obj.sendmail(sender, receivers, message)         
   print "Done"
except SMTPException:
   print "error"
