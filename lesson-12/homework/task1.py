from bs4 import BeautifulSoup
import statistics

# Load the HTML file
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract weather data
data = []
for row in soup.find_all("tr")[1:]:  # Skip the header row
    columns = row.find_all("td")
    day = columns[0].text.strip()
    temp = int(columns[1].text.strip().replace("°C", ""))
    condition = columns[2].text.strip()
    data.append((day, temp, condition))

# Display weather data
print("5-Day Weather Forecast:")
for entry in data:
    print(f"{entry[0]}: {entry[1]}°C, {entry[2]}")

# Find the day(s) with the highest temperature
max_temp = max(data, key=lambda x: x[1])[1]
hottest_days = [day for day, temp, _ in data if temp == max_temp]
print(f"\nHottest Day(s): {', '.join(hottest_days)} with {max_temp}°C")

# Find the days with "Sunny" condition
sunny_days = [day for day, _, condition in data if condition == "Sunny"]
print(f"Sunny Day(s): {', '.join(sunny_days)}")

# Calculate and print the average temperature
avg_temp = statistics.mean([temp for _, temp, _ in data])
print(f"\nAverage Temperature: {avg_temp:.2f}°C")
