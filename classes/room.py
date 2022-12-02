class Room:

    def __init__(self):
        self.guests_in_room = []
        self.list_of_songs = {}
        self.room_capacity = 2
        self.room_over_capacity = 0
        self.till = 100
        self.cost = 5

    def guests_check_in(self, guest):
        self.guests_in_room.append(guest)
        self.till += self.cost
        guest.wallet -= self.cost

    def guest_in_room(self):
        return len(self.guests_in_room) 

    def guests_check_out(self, guest):
        self.guests_in_room.remove(guest)

    def add_songs(self, song):
        self.list_of_songs = song
        # print(vars(self.list_of_songs))


    def guest_capacity(self):
        if len(self.guests_in_room) > 2:
            # self.room_over_capacity += 1
            return False
        else: True
    
    def sees_fav_song(self):
        for guest in self.guests_in_room:
            for song_name in self.list_of_songs["name"]:
                if guest.fav_song == song_name:
                    return "Whoo!"
                else: break