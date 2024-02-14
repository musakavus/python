"""
class method kullanarak constructor'ları manipüle edebiliriz.
"""


class Login:
    def __init__(self, username, password):
        self.arg1 = username
        self.arg2 = password

    # bir metodu constructor hale getirmek için class method kullanıyoruz ve return değeri olarak cls(params) veriyoruz
    @classmethod
    def with_mail(cls, mail, password):
        return cls(mail, password)  # neden iki parametre verdik. Çünkü init function iki parametre bekliyor
        # return cls derken aslında onu init metoduna yönlendiriyoruz. Çünkü cls sınıfı temsil ediyordu

    @classmethod
    def with_telephone(cls, telephone_number, password):
        return cls(telephone_number, password)


l1 = Login('admin', '1234')
l2 = Login.with_mail('admin@gmail.com', '165312')
l3 = Login.with_mail('545468415', 'lkshag')

print(f'Login type_text: {l1.arg2}, Password: {l1.arg2}')
print('-' * 45)
print(f'Login type_text: {l2.arg1}, Password: {l2.arg2}')
print('-' * 45)
print(f'Login type_text: {l3.arg1}, Password: {l3.arg2}')
