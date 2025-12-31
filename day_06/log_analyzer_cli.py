import argparse


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
            print("Error: Log file not found.")
            return None

    def analyze_logs(self, lines, level=None):
        for line in lines:
            if level:
                if level in line:
                    self.counts[level] += 1
            else:
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

    def write_summary(self, output_file):
        try:
            with open(output_file, "w") as file:
                for level, count in self.counts.items():
                    file.write(f"{level}: {count}\n")
        except OSError as error:
            print(f"Error writing file: {error}")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")

    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--out", default="log_summary.txt", help="Output file")
    parser.add_argument(
        "--level",
        choices=["INFO", "WARNING", "ERROR"],
        help="Filter log level"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    analyzer = LogAnalyzer(args.file)
    log_lines = analyzer.read_logs()

    if not log_lines:
        return

    analyzer.analyze_logs(log_lines, args.level)
    analyzer.show_summary()
    analyzer.write_summary(args.out)


if __name__ == "__main__":
    main()
