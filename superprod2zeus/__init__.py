import pandas as pd
import argparse
import logging


def compute_project_parts(worklog: str, output: str):
    """
    Computes the project parts from a worklog file.

    Args:
        worklog (str): Path to the superprod worklog
        output (str): Path to save the output TSV file.
    """

    logging.basicConfig(format="%(message)s", level=logging.INFO)

    df = pd.read_csv(worklog, sep=";")
    df["Worked"] = pd.to_timedelta(df["Worked"] + ":00")

    daily_total = df.groupby("Date")["Worked"].sum().reset_index(name="Total_Worked")

    df = df.merge(daily_total, on="Date")

    df["percentage"] = round(df["Worked"] / df["Total_Worked"] * 100, 0)

    result = df.groupby(["Date", "Projects"])["percentage"].sum().reset_index()

    result.to_csv(output, sep="\t", index=False)

    logging.info(f"Output saved to {output}")


def cli():
    """
    Command line interface for the superprod2zeus module.
    """

    parser = argparse.ArgumentParser(
        description="Convert Superprod worklog file for Zeus input."
    )
    parser.add_argument("worklog", type=str, help="Path to the Superprod worklog file")
    parser.add_argument(
        "--output",
        type=str,
        help="Path to save the output TSV file",
        default="percentage_worklog.tsv",
    )

    args = parser.parse_args()
    return args


def main():
    """
    Main function to execute the script.
    """

    args = cli()
    compute_project_parts(args.worklog, args.output)


if __name__ == "__main__":

    main()
