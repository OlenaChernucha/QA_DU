import json
import datetime


class Event:
    def __init__(self, serial, name, event_type, time_start, time_stop, venue_serial, description, website_url, speakers, categories):
        self.serial = serial
        self.name = name
        self.event_type = event_type
        self.time_start = time_start
        self.time_stop = time_stop
        self.venue_serial = venue_serial
        self.description = description
        self.website_url = website_url
        self.speakers = speakers
        self.categories = categories

    def read_serial(self):
        return self.serial
    
    def read_name(self):
        return self.name
    
    def read_event_type(self):
        return self.event_type
    
    def read_time_start(self):
        return self.time_start
    
    def read_time_stop(self):
        return self.time_stop
    
    def read_venue_serial(self):
        return self.venue_serial
    
    def read_description(self):
        return self.description
    
    def read_website_url(self):
        return self.website_url
    
    def read_speakers(self):
        return self.speakers
    
    def read_categories(self):
        return self.categories
    

class Venue:
    def __init__(self, serial, name, category):
        self.serial = serial
        self.name = name
        self.category = category

    def read_serial(self):
        return self.serial
    
    def read_name(self):
        return self.name
    
    def read_category(self):
        return self.category
    
    def read_details(self):
        return {
            "serial": self.serial,
            "name": self.name,
            "category": self.category
        }
    
class Speaker:
    def __init__(self, serial, name, photo, url, position, affiliation, twitter, bio):
        self.serial = serial
        self.name = name
        self.photo = photo
        self.url = url
        self.position = position
        self.affiliation = affiliation
        self.twitter = twitter
        self.bio = bio

    def get_serial(self):
        return self.serial
    
    def get_name(self):
        return self.name
    
    def get_photo(self):
        return self.photo
    
    def get_url(self):
        return self.url
    
    def get_position(self):
        return self.position
    
    def get_affiliation(self):
        return self.affiliation
    
    def get_twitter(self):
        return self.twitter
    
    def get_bio(self):
        return self.bio
    
class Conference:
    def __init__(self):
        self.events = []
        self.venues = []
        self.speakers = []
    
    def add_event(self, event):
        self.events.append(event)
    
    def remove_event(self, event):
        self.events.remove(event)
    
    def add_venue(self, venue):
        self.venues.append(venue)
    
    def remove_venue(self, venue):
        self.venues.remove(venue)
    
    def add_speaker(self, speaker):
        self.speakers.append(speaker)
    
    def remove_speaker(self, speaker):
        self.speakers.remove(speaker)
    
    def filter_events_by_date(self, date):
        return [event for event in self.events if event.get_time_start().date() == date]
    
    def filter_events_by_category(self, category):
        return [event for event in self.events if category in event.get_categories()]
    
    def filter_events_by_speaker(self, speaker_name):
        return [event for event in self.events if speaker_name in event.get_speakers()]
    
    def search_events_by_keyword(self, keyword):
        return [event for event in self.events if keyword in event.get_name() or keyword in event.get_description()]
    
    def sort_events_by_time(self):
        return sorted(self.events, key=lambda event: event.get_time_start())
    
def display_menu():
    print("1. View all events")
    print("2. Filter events by date")
    print("3. Filter events by category")
    print("4. Search events by keyword")
    print("5. Exit")

def view_event_details(event):
    print("Event Name:", event.get_name())
    print("Event Type:", event.get_event_type())
    print("Start Time:", event.get_time_start())
    print("End Time:", event.get_time_stop())
    print("Venue:", event.get_venue_serial())
    print("Description:", event.get_description())
    print("Website:", event.get_website_url())
    print("Speakers:", event.get_speakers())
    print("Categories:", event.get_categories())
    print()

def main():   
    conference = Conference()
   
    with open('py_fest.json', 'r') as file:
        data = json.load(file)
    
    for event_data in data.get('events', []):
        event = Event(
            event_data['serial'],
            event_data['name'],
            event_data['event_type'],
            datetime.strptime(event_data['time_start'], '%Y-%m-%d %H:%M:%S'),
            datetime.strptime(event_data['time_stop'], '%Y-%m-%d %H:%M:%S'),
            event_data['venue_serial'],
            event_data['description'],
            event_data['website_url'],
            event_data['speakers'],
            event_data['categories']
        )
        conference.add_event(event)

    for venue_data in data.get('venues', []):
        venue = Venue(
            venue_data['serial'],
            venue_data['name'],
            venue_data['category']
        )
        conference.add_venue(venue)

    for speaker_data in data.get('speakers', []):
        speaker = Speaker(
            speaker_data['serial'],
            speaker_data['name'],
            speaker_data['photo'],
            speaker_data['url'],
            speaker_data['position'],
            speaker_data['affiliation'],
            speaker_data['twitter'],
            speaker_data['bio']
        )
        conference.add_speaker(speaker)   




    
