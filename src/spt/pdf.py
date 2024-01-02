from fpdf import FPDF

from typing import List

from src.spt import constants
from src.spt.text_generator import TextGenerator


class PDF(FPDF):
    base_text = TextGenerator().base_text
    user_text = TextGenerator().user_text

    def header(self):
        """Add a header for the PDF page. Add letter "B" to follow
        Correspondence Guideline. Excludes letterhead, please use office
        letterhead paper.
        """
        # Section: B (Arsip surat)
        self.set_xy(5, 1)
        self.set_font(family="times",
                      style="B",
                      size=constants.FONT_SIZE)
        self.cell(w=5,
                  h=5,
                  text=self.base_text[0],
                  align="L",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=constants.SHOW_BORDERS)
        self.cell(w=0,
                  h=40,
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=constants.SHOW_BORDERS)

    def section_title(self, letter_number: int):
        """Add title section. 'Surat Perintah Tugas', Letter number, and
        Office Head opening paragraph.
        """
        # Section: SURAT PERINTAH TUGAS
        self.set_font(family="times",
                      style="BU",
                      size=constants.FONT_SIZE)
        self.cell(w=0,
                  h=8,
                  text=self.base_text[2],
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=constants.SHOW_BORDERS)

        # Section: Nomor Surat
        self.set_font(family="times",
                      size=constants.FONT_SIZE)
        self.cell(w=93,
                  h=4,
                  text=self.base_text[3],
                  align="R",
                  new_x="RIGHT",
                  new_y="LAST",
                  border=constants.SHOW_BORDERS)
        self.cell(w=0,
                  h=4,
                  text=str(letter_number),
                  align="L",
                  new_x="RIGHT",
                  new_y="NEXT",
                  border=constants.SHOW_BORDERS)

        # Section: Perintah Kepala Kantor
        self.ln(8)
        self.set_font(family="times",
                      size=constants.FONT_SIZE)
        self.multi_cell(w=0,
                        h=8,
                        text=f"{self.base_text[4]} {self.user_text[0]} {self.base_text[5]}",
                        new_x="LMARGIN",
                        new_y="NEXT",
                        border=constants.SHOW_BORDERS)
        self.ln(4)

    def section_employee(self):
        """Add employee data including Nama, NIP, Pangkat/Golongan, Jabatan.
        """
        asn_value = ['ODHY PRADHANA, A.Md.Ak.',
                     '199904192021021002',
                     'Pengatur, II/c',
                     'Pengelola Gaji',
                     ]

        # Section: Data pegawai
        for i in range(6, 10):
            self.multi_cell(w=20,
                            h=6,
                            text="x",  # testing line
                            align="R",
                            new_x="RIGHT",
                            new_y="LAST",
                            border=constants.SHOW_BORDERS)
            self.multi_cell(w=40,
                            h=6,
                            text=self.base_text[i],
                            new_x="RIGHT",
                            new_y="LAST",
                            border=constants.SHOW_BORDERS)
            self.multi_cell(w=5,
                            h=6,
                            text=self.base_text[1],
                            new_x="RIGHT",
                            new_y="LAST",
                            border=constants.SHOW_BORDERS)
            self.multi_cell(w=0,
                            h=6,
                            text=asn_value[i-6],
                            new_x="RIGHT",
                            new_y="NEXT",
                            border=constants.SHOW_BORDERS)
            self.ln(1)

        self.ln(4)

    def section_assignment(self):
        """Add assignment data including Untuk, Hari/Tanggal, Tujuan Tugas.
        """
        data_value = ['Rekonsiliasi Data dan Evaluasi Pendapatan Daerah Bulan Oktober Tahun 2023',
                      'Rabu, 8 November 2023',
                      'Badan Pengelola Keuangan dan Aset DIY Badan Pengelola Keuangan dan Aset DIY Badan Pengelola Keuangan dan Aset DIY',
                      ]

        # Section: Kepentingan, hari/tanggal, tujuan tugas
        for i in range(10, 13):
            self.multi_cell(w=30,
                            h=8,
                            text=self.base_text[i],
                            new_x="RIGHT",
                            new_y="LAST",
                            border=constants.SHOW_BORDERS)
            self.multi_cell(w=5,
                            h=8,
                            text=self.base_text[1],
                            new_x="RIGHT",
                            new_y="LAST",
                            border=constants.SHOW_BORDERS)
            self.multi_cell(w=0,
                            h=8,
                            text=data_value[i-10],
                            new_x="RIGHT",
                            new_y="NEXT",
                            border=constants.SHOW_BORDERS)
            self.ln(1)

        self.ln(8)

    def section_date(self, letter_date: str):
        """Add letter date.
        """
        # Section: Tanggal surat
        self.cell(w=60,
                  h=8,
                  new_x="RIGHT",
                  new_y="LAST",
                  border=constants.SHOW_BORDERS)
        self.cell(w=0,
                  h=8,
                  text=f"{self.base_text[13]} {self.base_text[1]} {self.user_text[1]}",
                  new_x="RIGHT",
                  new_y="NEXT",
                  border=constants.SHOW_BORDERS)
        self.ln(1)

        self.cell(w=60,
                  h=8,
                  new_x="RIGHT",
                  new_y="LAST",
                  border=constants.SHOW_BORDERS)
        self.cell(w=0,
                  h=8,
                  text=f"{self.base_text[14]} {self.base_text[1]} {letter_date}",
                  new_x="RIGHT",
                  new_y="NEXT",
                  border=constants.SHOW_BORDERS)
        self.ln(1)

    def section_signature(self):
        """Add Head office status, signature area, Head office name, Head
        office NIP.
        """
        # Section: Kepala
        self.set_font(family='times',
                      style='B',
                      size=constants.FONT_SIZE)
        self.cell(w=60,
                  h=8,
                  new_x="RIGHT",
                  new_y="LAST",
                  border=constants.SHOW_BORDERS)
        self.cell(w=0,
                  h=8,
                  text=self.user_text[2],
                  align='C',
                  new_x="RIGHT",
                  new_y="NEXT",
                  border=constants.SHOW_BORDERS)

        self.ln(24)

        # Section: Data Kepala Kantor
        self.set_font(family='times',
                      size=constants.FONT_SIZE)
        self.cell(w=60,
                  h=4,
                  new_x="RIGHT",
                  new_y="LAST",
                  border=constants.SHOW_BORDERS)
        self.cell(w=0,
                  h=4,
                  text=self.user_text[3],
                  align='C',
                  new_x="RIGHT",
                  new_y="NEXT",
                  border=constants.SHOW_BORDERS)
        self.ln(1)

        self.cell(w=60,
                  h=4,
                  new_x="RIGHT",
                  new_y="LAST",
                  border=constants.SHOW_BORDERS)
        self.cell(w=0,
                  h=4,
                  text=f"{self.base_text[15]}{self.user_text[4]}",
                  align='C',
                  new_x="RIGHT",
                  new_y="NEXT",
                  border=constants.SHOW_BORDERS)
        self.ln(1)

    def print_sections(self):
        """Page setups, adding sections, and print out PDF file.
        """
        # Page settings
        self.add_page()
        self.set_title('SPT')
        self.set_author('Odhy Pradhana')
        self.set_margin(constants.PAPER_MARGINS)

        # Add sections
        self.section_title(5670)
        self.section_employee()
        self.section_employee()
        self.section_employee()
        self.section_assignment()
        self.section_date('27 November 2023')
        self.section_signature()

        # Finalize
        self.output(name='pdf_3.pdf')
