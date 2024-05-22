# Matthew J Carr, Darren M Ashscroft, Evangelos Kontopantelis, David While, Yvonne Awenant, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"61455020","system":"multilex"},{"code":"61452020","system":"multilex"},{"code":"74425020","system":"multilex"},{"code":"63016020","system":"multilex"},{"code":"61167020","system":"multilex"},{"code":"69654020","system":"multilex"},{"code":"69656020","system":"multilex"},{"code":"65464020","system":"multilex"},{"code":"61616020","system":"multilex"},{"code":"61387020","system":"multilex"},{"code":"66273020","system":"multilex"},{"code":"62975020","system":"multilex"},{"code":"61420020","system":"multilex"},{"code":"61319020","system":"multilex"},{"code":"61409020","system":"multilex"},{"code":"61084020","system":"multilex"},{"code":"61439020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('selective-serotonin-reuptake-inhibitor-adds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["selective-serotonin-reuptake-inhibitor-ssri-adds-fluoxetine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["selective-serotonin-reuptake-inhibitor-ssri-adds-fluoxetine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["selective-serotonin-reuptake-inhibitor-ssri-adds-fluoxetine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
