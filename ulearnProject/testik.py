
def get_table_data(year=2015):
        with open(f'top20/ТОП-20 навыков по {year} году', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                header = lines[0].strip().split(',')
                rows = [line.strip().split(',') for line in lines[1:]]
                result =  {
                        'header': header,
                        'rows': rows
                }
        return result
