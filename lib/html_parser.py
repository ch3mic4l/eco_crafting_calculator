import re

from lib import receipe
from lib import html_striper
from lib import table_header
from lib import table_headers


class HTMLParser:

    def __init__(self, html: str):
        self.html = html
        self.receipes = []

    def parse_receipes(self):
        for table in self.parse_tables():
            self.parse_sub_table(table)

    def parse_sub_table(self, table: list):
        temp_column_span = 0
        headers = self.parse_headers(table)
        row_found = False
        cell_found = False
        cell_data = ''
        new_receipe = receipe.Receipe()
        row_span_found = False
        row_span_enabled = False
        for line in table[headers.line_where_headers_end:]:
            if row_found:
                if '<td' in line:
                    cell_found = True
                if cell_found:
                    cell_data += line
                if '</td' in line:
                    if 'rowspan' in cell_data:
                        row_span_found = True
                    if type(new_receipe.__getattribute__(headers.lookup[headers.headers[headers.position].name])) is dict and len(new_receipe.__getattribute__(headers.lookup[headers.headers[headers.position].name])) > 0:
                        temp_dict = new_receipe.__getattribute__(headers.lookup[headers.headers[headers.position].name])
                        temp_dict.update(self.parse_table_cell(headers.lookup[headers.headers[headers.position].name], cell_data))
                        new_receipe.__setattr__(headers.lookup[headers.headers[headers.position].name], temp_dict)
                    else:
                        new_receipe.__setattr__(headers.lookup[headers.headers[headers.position].name], self.parse_table_cell(headers.lookup[headers.headers[headers.position].name], cell_data))
                    if self.find_column_span(cell_data) == 0:
                        temp_column_span += 1
                    else:
                        temp_column_span += self.find_column_span(cell_data)
                    if temp_column_span >= headers.headers[headers.position].column_span:
                        headers.position += 1
                        temp_column_span = 0
                    cell_data = ''
                    cell_found = False
            if '<tr' in line:
                row_found = True
            if '</tr' in line:
                row_found = False
                if row_span_found and not row_span_enabled:
                    row_span_enabled = True
                    headers.position = 2
                else:
                    row_span_found = False
                    row_span_enabled = False
                    headers.position = 0
                    self.receipes.append(new_receipe)
                    new_receipe = receipe.Receipe()

    def parse_headers(self, table: list):
        headers = table_headers.TableHeaders()
        for line in table:
            headers.line_where_headers_end += 1
            if '<th' in line:
                header = table_header.TableHeader()
                header.name = self.find_header(line)
                header.column_span = self.find_column_span(line)
                headers.headers.append(header)
            if '</th></tr>' in line:
                break
        return headers

    def find_header(self, line: str):
        header = self.strip_html(line)
        if header == '':
            header = False
        if header:
            while '.png' in header:
                header = header.split('.png')[1]
        return header

    def parse_tables(self):
        tables = []
        sub_table = []
        table_found = False
        first_table = True
        for line in self.html.split("\n"):
            if self.table_begin(line):
                table_found = True
            if table_found:
                sub_table.append(line)
            if self.table_end(line):
                table_found = False
                if first_table:
                    first_table = False
                    sub_table = []
                    continue
                tables.append(sub_table)
                sub_table = []
        return tables

    def parse_table_cell(self, header: str, html_line: str):
        if header == 'crafting_station':
            results = self.strip_html(html_line)
        elif header == 'item' or header == 'materials':
            quantity_text = self.strip_html(html_line.split('</a><br />x')[1])
            quantity = int(re.search("^\d*", quantity_text)[0])
            results = {self.strip_html(html_line.split('</a><br />x')[0]): {'quantity': quantity}}
        elif header == 'level_needed':
            if self.strip_html(html_line) == 'None':
                results = {'None': {'level': 'None'}}
            else:
                level_needed = int(self.strip_html(html_line.split('</a><br /> Level')[1]))
                results = {self.strip_html(html_line.split('</a><br /> Level')[0]): {'level': level_needed}}
        elif header == 'crafting_time' or header == 'labor_cost' or header == 'xp_gained':
            try:
                results = int(self.strip_html(html_line))
            except ValueError:
                results = float(self.strip_html(html_line))
        return results

    @staticmethod
    def strip_html(html_line: str):
        stripper = html_striper.MLStripper()
        stripper.feed(html_line)
        data = stripper.get_data()
        while '.png' in data:
            data = data.split('.png')[1]
        return data

    @staticmethod
    def table_begin(line: str):
        return '<table' in line

    @staticmethod
    def table_end(line: str):
        return '</table' in line

    @staticmethod
    def find_column_span(line: str):
        column_span = 0
        if 'colspan' in line:
            column_span = int(re.search("^\d*", line.split('colspan="')[1])[0])
        return column_span
