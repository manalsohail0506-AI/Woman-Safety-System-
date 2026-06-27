import time
import winsound
import datetime
import json
import os
import random
from abc import ABC, abstractmethod

# =========================================================
# SMART WOMEN SAFETY SYSTEM (OOP VERSION)
# Using:
# ✅ Classes
# ✅ Objects
# ✅ Encapsulation
# ✅ Inheritance
# ✅ Polymorphism
# ✅ Abstraction
# ✅ Private Methods
# =========================================================


# =========================================================
# ABSTRACT BASE CLASS
# =========================================================

class Emergency(ABC):

    @abstractmethod
    def trigger_alert(self):
        pass


# =========================================================
# CONTACT MANAGER CLASS (ENCAPSULATION)
# =========================================================

class ContactManager:

    def __init__(self):
        self.__contacts = {}
        self.__load_contacts()

    # PRIVATE METHOD
    def __load_contacts(self):
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    if "," in line:
                        name, number = line.strip().split(",", 1)
                        self.__contacts[name] = number
        except:
            pass

    def add_contact(self):
        print("\n" + "=" * 40)
        print("📞 ADD EMERGENCY CONTACT")
        print("=" * 40)

        name = input("Enter Contact Name: ")
        number = input("Enter Contact Number: ")

        self.__contacts[name] = number

        with open("contacts.txt", "a") as file:
            file.write(f"{name},{number}\n")

        print(f"\n✅ Contact '{name}' added successfully!")

    def show_contacts(self):

        if not self.__contacts:
            print("\n📭 No contacts found.")
            return

        print("\n" + "=" * 50)
        print("📞 EMERGENCY CONTACTS")
        print("=" * 50)

        for name, number in self.__contacts.items():
            print(f"👤 {name}: {number}")

        print("=" * 50)

    def get_contacts(self):
        return self.__contacts


# =========================================================
# LOCATION SERVICE CLASS
# =========================================================

class LocationService:

    def get_current_location(self):

        locations = [
            "Defence Phase 5, Karachi",
            "Gulberg III, Lahore",
            "F-10 Markaz, Islamabad",
            "Johar Town, Lahore",
            "Clifton, Karachi"
        ]

        return random.choice(locations)


# =========================================================
# INCIDENT MANAGER CLASS
# =========================================================

class IncidentManager:

    def save_incident(self, text):

        with open("incidents.txt", "a") as file:
            file.write(f"{datetime.datetime.now()} - {text}\n")

    def view_history(self):

        try:
            with open("incidents.txt", "r") as file:

                print("\n" + "=" * 60)
                print("📋 INCIDENT HISTORY")
                print("=" * 60)

                content = file.read()

                if content:
                    print(content)
                else:
                    print("No incidents found.")

                print("=" * 60)

        except:
            print("📭 No history found.")


# =========================================================
# ALERT SYSTEM CLASS
# =========================================================

class AlertSystem:

    def __init__(self, contact_manager):
        self.contact_manager = contact_manager

    # PRIVATE METHOD
    def __play_sound(self):
        winsound.Beep(1500, 500)

    def send_voice_alert(self, emergency_type, location):

        contacts = self.contact_manager.get_contacts()

        if not contacts:
            print("⚠️ No contacts available.")
            return False

        voice_message = (
            f"🚨 EMERGENCY ALERT! "
            f"{emergency_type}. "
            f"Location: {location}"
        )

        print("\n" + "=" * 50)
        print("🎙️ VOICE ALERT SYSTEM")
        print("=" * 50)

        print(f"📢 Message: {voice_message}")

        print("-" * 50)

        self.__play_sound()

        for name, number in contacts.items():

            print(f"📞 Sending to {name} ({number})...")
            time.sleep(0.5)
            print(f"✅ Delivered to {name}")

        print("-" * 50)

        print(f"✅ Alerts sent to {len(contacts)} contact(s)!")

        return True


# =========================================================
# EMOTIONAL SUPPORT CLASS
# =========================================================

class EmotionalSupport:

    def support(self):

        print("\n" + "=" * 40)
        print("💖 EMOTIONAL SUPPORT")
        print("=" * 40)

        messages = [

            "❤️ You are not alone.",
            "🛡️ Stay calm.",
            "📍 Your location has been shared.",
            "🚔 Help is on the way.",
            "💬 Breathe slowly.",

        ]

        for msg in messages:
            print(msg)
            time.sleep(0.5)


# =========================================================
# SOS EMERGENCY CLASS
# INHERITANCE + POLYMORPHISM
# =========================================================

class SOSEmergency(Emergency):

    def __init__(
        self,
        alert_system,
        location_service,
        incident_manager,
        emotional_support
    ):

        self.alert_system = alert_system
        self.location_service = location_service
        self.incident_manager = incident_manager
        self.emotional_support = emotional_support

    # POLYMORPHISM
    def trigger_alert(self):

        print("\n" + "=" * 50)
        print("🚨 SOS EMERGENCY ACTIVATED 🚨")
        print("=" * 50)

        winsound.Beep(1000, 1000)

        location = self.location_service.get_current_location()

        print(f"\n📍 Location: {location}")

        self.alert_system.send_voice_alert(
            "SOS EMERGENCY",
            location
        )

        print("👮 Police Notified")
        print("🚑 Rescue Team Notified")

        self.emotional_support.support()

        print("\n⏰ HELP ARRIVAL TIMER")

        for i in range(5, 0, -1):

            print(f"{i} minutes remaining...")
            time.sleep(1)

        print("\n✅ Help is on the way!")

        self.incident_manager.save_incident(
            f"SOS Emergency at {location}"
        )


# =========================================================
# MEDICAL EMERGENCY CLASS
# INHERITANCE + POLYMORPHISM
# =========================================================

class MedicalEmergency(Emergency):

    def __init__(
        self,
        alert_system,
        location_service,
        incident_manager,
        emotional_support
    ):

        self.alert_system = alert_system
        self.location_service = location_service
        self.incident_manager = incident_manager
        self.emotional_support = emotional_support

    # POLYMORPHISM
    def trigger_alert(self):

        print("\n" + "=" * 50)
        print("🏥 MEDICAL EMERGENCY")
        print("=" * 50)

        condition = input("Enter medical condition: ").lower()

        emergency_conditions = [
            "dizziness",
            "heart attack",
            "low bp",
            "weakness",
            "faint"
        ]

        if condition in emergency_conditions:

            winsound.Beep(1200, 1000)

            location = self.location_service.get_current_location()

            print(f"\n📍 Location: {location}")

            self.alert_system.send_voice_alert(
                f"MEDICAL - {condition}",
                location
            )

            print("🚑 Ambulance Notified")

            self.emotional_support.support()

            self.incident_manager.save_incident(
                f"Medical Emergency: {condition}"
            )

        else:
            print("✅ Condition not critical.")


# =========================================================
# USER SYSTEM CLASS
# =========================================================

class UserSystem:

    def register(self):

        print("\n" + "=" * 40)
        print("📝 USER REGISTRATION")
        print("=" * 40)

        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        password = input("Enter Password: ")

        with open("users.txt", "a") as file:
            file.write(f"{name},{phone},{password}\n")

        print("✅ Registration Successful!")

    def login(self):

        print("\n" + "=" * 40)
        print("🔐 USER LOGIN")
        print("=" * 40)

        phone = input("Enter Phone: ")
        password = input("Enter Password: ")

        try:

            with open("users.txt", "r") as file:

                users = file.readlines()

                for user in users:

                    data = user.strip().split(",")

                    if data[1] == phone and data[2] == password:

                        print(f"\n✅ Welcome {data[0]}!")
                        return True

            print("❌ Invalid Credentials")
            return False

        except:
            print("❌ No users found.")
            return False


# =========================================================
# MAIN APPLICATION CLASS
# =========================================================

class SmartSafetySystem:

    def __init__(self):

        self.contact_manager = ContactManager()

        self.location_service = LocationService()

        self.incident_manager = IncidentManager()

        self.emotional_support = EmotionalSupport()

        self.alert_system = AlertSystem(
            self.contact_manager
        )

        self.user_system = UserSystem()

        self.sos = SOSEmergency(
            self.alert_system,
            self.location_service,
            self.incident_manager,
            self.emotional_support
        )

        self.medical = MedicalEmergency(
            self.alert_system,
            self.location_service,
            self.incident_manager,
            self.emotional_support
        )

    def run(self):

        while True:

            print("\n" + "=" * 60)
            print("🚨 SMART WOMEN SAFETY SYSTEM 🚨")
            print("=" * 60)

            print("1. Register")
            print("2. Login")
            print("3. SOS Emergency")
            print("4. Medical Emergency")
            print("5. Add Contact")
            print("6. Show Contacts")
            print("7. View Incident History")
            print("8. Exit")

            choice = input("\nEnter choice: ")

            if choice == "1":

                self.user_system.register()

            elif choice == "2":

                self.user_system.login()

            elif choice == "3":

                self.sos.trigger_alert()

            elif choice == "4":

                self.medical.trigger_alert()

            elif choice == "5":

                self.contact_manager.add_contact()

            elif choice == "6":

                self.contact_manager.show_contacts()

            elif choice == "7":

                self.incident_manager.view_history()

            elif choice == "8":

                print("\n✅ Exiting System...")
                print("👋 Stay Safe!")

                break

            else:

                print("❌ Invalid Choice")


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    app = SmartSafetySystem()

    app.run()