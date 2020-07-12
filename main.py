class Contact:
    
    def __init__(self, first_name, last_name, phone, favourite=False, **other):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.other_info = other
        self.favourite = favourite


    def __str__(self):
        string = (f"Имя: {self.first_name}\nФамилия: {self.last_name}\nТелефон: {self.phone}\n"
        + f"В избранных: {'нет' if self.favourite == False else 'да'}\n")
        if self.other_info != {}:
            string += "Дополнительная информация:\n"
            for key, value in self.other_info.items():
                string += f"\t{key}: {value}\n"
        return string


class Phonebook:
    def __init__(self, name):
        self.name = name
        self.phone_list = []


    def print_phonebook(self):
        print(f"\n{self.name}:\n")
        for contact in self.phone_list:
            print(contact)


    def add_contact(self, Contact):
        if self.phone_list.count(Contact) != 0:
            print("Данный контакт уже существует.")
        else:
            self.phone_list.append(Contact)


    def delete_contact(self, phone_number):
        i = 0
        for contact in self.phone_list:
            if contact.phone == phone_number:
                self.phone_list.remove(contact)
                i += 1
                print("Номер успешно удалён!")
        if i == 0:
            print("Контакт не найден.")


    def show_favourites(self):
        out_list = []
        for contact in self.phone_list:
            if contact.favourite == True:
                out_list.append(contact)
        if len(out_list) != 0:
            for contact in out_list:
                print(contact)
        else:
            print("Нет номеров в избранных.")


    def find_contact(self, name):
        name = name.split(" ")
        out_list = []
        for contact in self.phone_list:
            if contact.first_name == name[0] and contact.last_name == name[1]:
                out_list.append(contact)
        if len(out_list) != 0:
            print(out_list[0])
        else:
            print("Контакт не найден.")


vasya = Contact("Вася", "Cмирнов", "8-800-555-35-35", telegram='@smirnoff', email='smirnoff@gmail.com')
igor = Contact("Игорь", "Власов", "+7-903-444-22-11", favourite=True, email="vlasov@yandex.ru", viber="@vlaasov")
john = Contact("Джон", "Доу", "+7-903-111-33-16", email="johndoe@mail.ru")
vasilisa = Contact("Василиса", "Ивановна", "+7-999-199-90-81")
putin = Contact("Влад", "Путин", "+1-111-111-11-11", favourite=True, email="putin", telegram="@putin")

# print(putin)

my_PB = Phonebook("my_phonebook")
my_PB.add_contact(vasya)
my_PB.add_contact(igor)
my_PB.add_contact(john)
my_PB.add_contact(vasilisa)
my_PB.add_contact(putin)

# my_PB.delete_contact("+7-999-199-90-81")
# my_PB.delete_contact("8-888-888-88-88")

# my_PB.print_phonebook()
# my_PB.show_favourites()

# my_PB.find_contact("Вася Смирнов")
# my_PB.find_contact("Фаррух Булсара")