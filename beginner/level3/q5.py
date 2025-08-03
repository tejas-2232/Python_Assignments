class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @staticmethod
    def addTime(time1, time2):
        # Add hours and minutes separately
        total_hours = time1.hours + time2.hours
        total_minutes = time1.minutes + time2.minutes
        
        # Handle minute overflow (if minutes >= 60, convert to hours)
        if total_minutes >= 60:
            extra_hours = total_minutes // 60  # How many complete hours
            total_minutes = total_minutes % 60  # Remaining minutes
            total_hours += extra_hours
        
        # Return a new Time object with the result
        return Time(total_hours, total_minutes)
    
    def displayTime(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def displayMinute(self):
        print(f"Total time in minutes: {self.hours * 60 + self.minutes} minutes")

if __name__ == "__main__":
    # Get first time from user
    print("Enter first time:")
    hours1 = int(input("Hours: "))
    minutes1 = int(input("Minutes: "))
    time1 = Time(hours1, minutes1)
    
    # Get second time from user
    print("Enter second time:")
    hours2 = int(input("Hours: "))
    minutes2 = int(input("Minutes: "))
    time2 = Time(hours2, minutes2)
    
    # Add the times and display result
    result = Time.addTime(time1, time2)
    print("\nSum of both times:")
    result.displayTime()
    result.displayMinute()