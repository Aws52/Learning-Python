from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("keyword", type=str, help="Keyword to search for")
parser.add_argument("file", type=str, help="file to search in")
parser.add_argument("--ext", type=str, help="extention")
parser.add_argument("--context", type=int, help="how many lines to print")

args = parser.parse_args()


word = args.keyword
extention = args.ext
con = args.context
target = Path(args.file)

if target.exists():
    if target.is_file():
        lines = target.read_text().splitlines()
        for line_num, content in enumerate(lines, start=1):
            if word in content:
                idx = line_num - 1
                start_bound = max(0, idx - con)
                end_bound = idx + con + 1
                context_lines = lines[start_bound:end_bound]
                for current_no, context_content in enumerate(
                    context_lines, start=start_bound + 1
                ):
                    marker = "     <--" if current_no == line_num else ""
                    print(
                        f"""{target} : Line : {current_no} : {context_content}{marker}"""
                    )
    elif target.is_dir():
        for path_file in target.rglob("*"):
            try:
                if path_file.is_file() and (
                    not extention or path_file.suffix == extention
                ):
                    lines = path_file.read_text().splitlines()
                    for line_num, content in enumerate(lines, start=1):
                        if word in content:
                            idx = line_num - 1
                            start_bound = max(0, idx - con)
                            end_bound = idx + con + 1
                            context_lines = lines[start_bound:end_bound]
                            for current_no, context_content in enumerate(
                                context_lines, start=start_bound + 1
                            ):
                                marker = "     <--" if current_no == line_num else ""
                                print(
                                    f"""{target} : Line : {current_no} : {context_content}{marker}"""
                                )
            except (UnicodeDecodeError, PermissionError):
                pass
else:
    print("file or directory not found")
