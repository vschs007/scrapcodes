class vehicle:
    def __init__(self, licence, color):
        self.licence = licence
        self.color = color

    def __repr__(self):
        return f'{self.licence},{self.color}'


class spot:
    def __init__(self, spots):
        self.vehicle_added = []
        self.spots = spots
        print(f'created parking lot with {spots} slots')
        self.vehicle_info = {}
        self.vehicle_slotsinfo = {}
        self.count = 0
        self.free = []

    def spots_available(self):
        return self.spots

    def counter(self):
        self.count += 1

    def add_vehicle(self, vehicle):
        if self.spots > 0:
            self.count += 1
            self.vehicle_added.append(str(vehicle).split(','))
            self.spots -= 1
            self.vehicle_info = {}
            for i in (self.vehicle_added):
                self.vehicle_info[i[0]] = (i[1])

            if len(self.free) > 0:
                if self.count-len(self.free) <= int(min(self.free)):
                    self.vehicle_slotsinfo[i[0]] = [self.count, i[1]]
                else:
                    k = int(min(self.free))
                    self.vehicle_slotsinfo[i[0]] = [k, i[1]]
                    print(f'Allocated slot number:{k}')
                    self.free.pop()

            else:
                self.vehicle_slotsinfo[i[0]] = [self.count, i[1]]
                print(f'Allocated slot number:{self.count}')
        else:
            print("Sorry, parking lot is full")

    def removevehicle(self, licence):
        for i in self.vehicle_info.keys():
            if i == licence:
                self.vehicle_info.pop(i, None)
                self.vehicle_slotsinfo.pop(i, None)
                self.spots += 1
                break

    def removevehicle_slot(self, slot):
        for i in list(self.vehicle_slotsinfo.keys()):
            if self.vehicle_slotsinfo[i][0] == int(slot):
                self.removevehicle(i)
                self.free.append(slot)
                sorted(self.free,reverse=True)
                print(f'Slot number {slot} is free')

    def viewvehicle(self):
        print(*['Slot No. ','Registration No.','Colour'])
        for i in self.vehicle_slotsinfo.keys():
            print(*[self.vehicle_slotsinfo[i][0] , i , self.vehicle_slotsinfo[i][1]])
            print()

    def licence_from_color(self, color):
        list_of_veh = []
        for i in range(len(self.vehicle_added)):
            if self.vehicle_added[i][1] == color:
                list_of_veh.append(self.vehicle_added[i][0])
        if len(list_of_veh) > 0:
            print(",".join(list_of_veh))
        else:
            print("Registration Number Not found with given color")

    def slot_number_from_licence(self, licence):
        for i in self.vehicle_slotsinfo.keys():
            if i == licence:
                print( self.vehicle_slotsinfo[i][0])
                break
        print("Slot Number Not Found")

    def slot_number_from_color(self, color):
        # multiple entried possible , so using list data structure
        samecolor = []

        for i in self.vehicle_slotsinfo.keys():
            if self.vehicle_slotsinfo[i][1] == color:
                samecolor.append(self.vehicle_slotsinfo[i][0])
        print(*samecolor)


rw_input = input()
# splitting the input and input the integer values only
s = int(list(rw_input.split())[-1])
spt = spot(s)
cnt = True
while (cnt):
    rw_car_input = input()
    rw_car_details = list(rw_car_input.split())
    if rw_car_details[0] == 'park':
        model = rw_car_details[1]
        color = rw_car_details[2]
        veh = vehicle(model, color)
        spt.add_vehicle(veh)
    elif rw_car_details[0] == 'leave':
        rem = rw_car_details[1]
        spt.removevehicle_slot(rem)
    elif rw_car_details[0] == 'status':
        spt.viewvehicle()
    elif rw_car_details[0] == 'registration_numbers_for_cars_with_colour':
        cor = rw_car_details[1]
        spt.licence_from_color(cor)
    elif rw_car_details[0] == 'slot_numbers_for_cars_with_colour':
        cor = rw_car_details[1]
        spt.slot_number_from_color(cor)
    elif rw_car_details[0] == 'slot_number_for_registration_number':
        rgno = rw_car_details[1]
        spt.slot_number_from_licence(rgno)
    elif rw_car_details[0] == 'exit':
        cnt = False
