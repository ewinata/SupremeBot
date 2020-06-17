console.log('Generating Autofill...');

// Fills in personal info
document.getElementById('order_billing_name').value = 'Ermano Winata';
document.getElementById('order_email').value = 'gabrielgilbiyanto@gmail.com';
document.getElementById('order_tel').value = '206-849-9598';
document.getElementById('bo').value = '15524 Corliss Ave N';
//document.getElementById('oba3').value = '325';
document.getElementById('order_billing_zip').value = '98133';
document.getElementById('order_billing_city').value = 'Shoreline';
document.getElementById('order_billing_state').value = 'WA';

// Fills in card info
document.getElementById('nnaerb').value = '1234';
//browser.find_element_by_xpath('//*[@id="orcer"]').send_keys('');
document.getElementById('credit_card_month').value = '01';
document.getElementById('credit_card_year').value = '2021';

// Checks checkbox and checks out
document.getElementsByClassName('iCheck-helper')[1].click();
//document.getElementsByName('commit')[0].click();