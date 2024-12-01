import sqlite3
import matplotlib.pyplot as plt

def create_database():
    db_name = "population_GC.db"
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    conn.commit()

def insert_initial_data(conn):
    cursor = conn.cursor()
    cities = [
        ("Miami", 2023, 442241),
        ("Orlando", 2023, 309154),
        ("Tampa", 2023, 384959),
        ("Jacksonville", 2023, 954614),
        ("Tallahassee", 2023, 199223),
        ("St. Petersburg", 2023, 261338),
        ("Fort Lauderdale", 2023, 182760),
        ("Hialeah", 2023, 235185),
        ("Gainesville", 2023, 141085),
        ("Sarasota", 2023, 56103),
    ]
    cursor.executemany("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", cities)
    conn.commit()

def simulate_population_growth(conn):
    cursor = conn.cursor()
    for year in range(2024, 2044):
        cursor.execute("SELECT city, population FROM population WHERE year = ?", (year - 1,))
        rows = cursor.fetchall()
        for city, population in rows:
            new_population = int(population * 1.02)
            cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                           (city, year, new_population))
    conn.commit()

def plot_population_growth(conn, city):
    cursor = conn.cursor()
    cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (city,))
    data = cursor.fetchall()
    years = [row[0] for row in data]
    populations = [row[1] for row in data]
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, populations, marker='o', label=f"Population Growth: {city}")
    plt.title(f"Population Growth in {city} (2023-2043)")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid()
    plt.legend()
    plt.show()

def main():
    conn = create_database()
    create_table(conn)
    insert_initial_data(conn)
    simulate_population_growth(conn)

    cities = [
        "Miami", "Orlando", "Tampa", "Jacksonville", "Tallahassee",
        "St. Petersburg", "Fort Lauderdale", "Hialeah", "Gainesville", "Sarasota"
    ]

    while True:
        print("Available cities:", ", ".join(cities))
        city = input("Enter a city to see its population growth (or type 'done' to exit): ").strip()
        if city.lower() == 'done':
            print("Goodbye!")
            break
        elif city in cities:
            plot_population_growth(conn, city)
        else:
            print("Invalid city. Please choose a city from the list.")

    conn.close()

if __name__ == "__main__":
    main()
