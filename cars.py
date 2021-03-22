class Cars:
    def __init__(self, model, color, company, speed_limit):
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
    def start (self):
        print("started")
    def stop (self):
        print("stop")
    def acclerate (self):
        print("acclerate")
    def change_gear (self):
        print("change_gear")
def main():
    truck=Cars('truck', 'blue', 'isher', 250)
    print(truck.model)
    truck.start()
    truck.acclerate()
    truck.change_gear()
    truck.stop()
main()