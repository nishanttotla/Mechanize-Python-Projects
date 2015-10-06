import mechanize
from bs4 import BeautifulSoup
import smtplib

br = mechanize.Browser()

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

################ Fill form and submit ################

url = 'https://egov.uscis.gov/casestatus/landing.do'
form_name = 'caseStatusForm'
receipt_num = '' # enter receipt number here

response = br.open(url)
br.select_form(form_name)

# Enter info in form
br.form.set_all_readonly(False)
br['appReceiptNum'] = receipt_num
br.submit()

################ Extract info from the response ################

html_doc = br.response().read()
soup = BeautifulSoup(html_doc, 'html.parser')
case_status = soup.h1.text # first h1 is the status
case_status_description = soup.p.text # first p is the description

print '---' + case_status + '---\n' + case_status_description

################ Send email update ################

# TODO

