# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"J600011","system":"readv2"},{"code":"J600.00","system":"readv2"},{"code":"J601z00","system":"readv2"},{"code":"J600000","system":"readv2"},{"code":"J600z00","system":"readv2"},{"code":"J601000","system":"readv2"},{"code":"J601.00","system":"readv2"},{"code":"J635700","system":"readv2"},{"code":"J60..00","system":"readv2"},{"code":"J60z.00","system":"readv2"},{"code":"B16.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hepatic-failure-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hepatic-failure-subacute---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hepatic-failure-subacute---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hepatic-failure-subacute---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
