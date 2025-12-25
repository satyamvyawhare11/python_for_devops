class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

    def read_logs(self):
        try:
            with open(self.log_file, "r") as file:
                lines = file.readlines()
                if not lines:
                    print("Log file is empty.")
                    return None
                return lines
        except FileNotFoundError:
            print("Log file not found.")
            return None

    def analyze_logs(self, lines):
        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1

    def show_summary(self):
        print("\n--- Log Summary ---")
        for level, count in self.counts.items():
            print(f"{level}: {count}")

    def write_summary_to_file(self):
        try:
            with open("log_summary.txt", "w") as file:
                for level, count in self.counts.items():
                    file.write(f"{level}: {count}\n")
        except OSError as error:
            print(f"Error writing to file: {error}")

if __name__ == "__main__":
    analyzer = LogAnalyzer("app.log")

    log_lines = analyzer.read_logs()
    if log_lines:
        analyzer.analyze_logs(log_lines)
        analyzer.show_summary()
        analyzer.write_summary_to_file()
