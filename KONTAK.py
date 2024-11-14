class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.phone}"


class ContactManagementSystem:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        self.contacts.append(new_contact)
        print(f"Kontak '{name}' telah ditambahkan.")

    def view_contacts(self):
        if not self.contacts:
            print("Tidak ada kontak yang tersedia.")
            return
        print("Daftar Kontak:")
        for contact in self.contacts:
            print(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Kontak '{name}' telah dihapus.")
                return
        print(f"Kontak '{name}' tidak ditemukan.")


def main():
    cms = ContactManagementSystem()

    while True:
        print("\n=== Contact Management System ===")
        print("1. Tambah Kontak")
        print("2. Lihat Kontak")
        print("3. Hapus Kontak")
        print("4. Keluar")

        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            name = input("Masukkan nama kontak: ")
            phone = input("Masukkan nomor telepon kontak: ")
            cms.add_contact(name, phone)
        elif choice == '2':
            cms.view_contacts()
        elif choice == '3':
            name = input("Masukkan nama kontak yang ingin dihapus: ")
            cms.delete_contact(name)
        elif choice == '4':
            print("Keluar dari sistem.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()