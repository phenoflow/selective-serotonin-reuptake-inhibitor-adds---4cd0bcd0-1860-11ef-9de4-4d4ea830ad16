# Matthew J Carr, Darren M Ashscroft, Evangelos Kontopantelis, David While, Yvonne Awenant, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"63703020","system":"multilex"},{"code":"67575020","system":"multilex"},{"code":"69754020","system":"multilex"},{"code":"72933020","system":"multilex"},{"code":"66399020","system":"multilex"},{"code":"66464020","system":"multilex"},{"code":"67650020","system":"multilex"},{"code":"65578020","system":"multilex"},{"code":"72932020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('selective-serotonin-reuptake-inhibitor-adds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["selective-serotonin-reuptake-inhibitor-ssri-adds-paroxetine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["selective-serotonin-reuptake-inhibitor-ssri-adds-paroxetine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["selective-serotonin-reuptake-inhibitor-ssri-adds-paroxetine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
