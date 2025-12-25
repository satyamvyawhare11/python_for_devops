def read_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            if not lines:
                raise ValueError("Log file is empty.")

            return lines

    except FileNotFoundError:
        print("Error: Log file not found.")
        return None
    except ValueError as error:
        print(f"Error: {error}")
        return None


def analyze_logs(log_lines):
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in log_lines:
        if "INFO" in line:
            log_counts["INFO"] += 1
        elif "WARNING" in line:
            log_counts["WARNING"] += 1
        elif "ERROR" in line:
            log_counts["ERROR"] += 1

    return log_counts


def write_summary_to_file(summary, output_file):
    try:
        with open(output_file, "w") as file:
            for level, count in summary.items():
                file.write(f"{level}: {count}\n")
    except OSError as error:
        print(f"Error writing to file: {error}")


def display_summary(summary):
    print("\n--- Log Summary ---\n")
    for level, count in summary.items():
        print(f"{level}: {count}")


def main():
    log_file_path = "app.log"
    output_file_path = "log_summary.txt"

    log_lines = read_log_file(log_file_path)

    if log_lines is None:
        return

    summary = analyze_logs(log_lines)

    display_summary(summary)
    write_summary_to_file(summary, output_file_path)


if __name__ == "__main__":
    main()
