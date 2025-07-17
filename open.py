import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

def pomodoro():
    print("📚 Time to study! Focus for 25 minutes.")
    countdown(25)
    print("⏳ Break time! Relax for 5 minutes.")
    countdown(5)
    print("✅ One Pomodoro cycle complete!")

while True:
    start = input("Start a Pomodoro session? (yes/no): ").casefold()
    if start == "yes":
        pomodoro()
    else:
        print("Good luck with your studies!")
        break
