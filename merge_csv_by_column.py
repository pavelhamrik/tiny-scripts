import sys
import csv
import argparse

def merge_csv_by_column(path, col, excl):

    data = list(csv.reader(path))
    data = [data[i][:excl] for i in range(len(data))]

    # todo: now only cuts off, add real exlusion, ideally of an array of cols
    merge_column = [data[i][col:col+1] for i in range(1,len(data))]

    merge_column_flat = [c for row in merge_column for c in row]

    merge_column_set = list(set(merge_column_flat))

    for pivot in merge_column_set:
        matches = [row for row in data if pivot in row[col]]
        print ''.join(matches[0][0])

        output = list()
        for match in matches:
            del match[col]
            output.append(' - '.join(match))

        print ', '.join(output)

# argument parsing

parser = argparse.ArgumentParser(description='I expect a CSV file and a column name or number')

parser.add_argument('--f', type=file, required=True, dest='input_file',
                    help='input CSV file path')

merge_by = parser.add_mutually_exclusive_group(required=True)

# merge_by.add_argument('--c', dest='col_name',
#                     help='name of the column to merge by')

merge_by.add_argument('--n', dest='col_num', type=int,
                    help='number of the column to merge by')

parser.add_argument('--x', dest='col_exclude', type=int,
                    help='number of the column to exclude')


# run

args = parser.parse_args()
merge_csv_by_column(args.input_file, args.col_num, args.col_exclude)
